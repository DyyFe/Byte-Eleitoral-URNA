from pathlib import Path

import pandas as pd

PASTA = Path(__file__).resolve().parent
ARQ_COMP = PASTA / "perfil_comparecimento_abstencao_2018" / "perfil_comparecimento_abstencao_2018_BRASIL.csv"
ARQ_ELEI = PASTA / "perfil_eleitorado_2018" / "perfil_eleitorado_2018.csv"
SAIDA = PASTA / "saida_powerbi"

ENCODING = "latin-1"
SEP = ";"
DESCARTAR = ["DT_GERACAO", "HH_GERACAO"]
COLS_MUN = ["SG_UF", "CD_MUNICIPIO", "NM_MUNICIPIO", "CD_MUN_SIT_BIOMETRICA", "DS_MUN_SIT_BIOMETRICA"]
GERAR_UNIFICADA = True
GERAR_CSV = True


def tipo_coluna(nome):
    n = nome.strip().upper()
    if n.startswith(("SG_", "DS_", "NM_")):
        return "category"
    if n.startswith(("CD_", "NR_", "QT_", "ANO_")):
        return "int32"
    return None


def ler(caminho):
    cab = pd.read_csv(caminho, sep=SEP, encoding=ENCODING, nrows=0).columns
    cols = [c for c in cab if c.strip().upper() not in DESCARTAR]
    tipos = {c: t for c in cols if (t := tipo_coluna(c))}
    try:
        df = pd.read_csv(caminho, sep=SEP, encoding=ENCODING, usecols=cols, dtype=tipos)
    except (ValueError, TypeError):
        tipos = {c: t for c, t in tipos.items() if t == "category"}
        df = pd.read_csv(caminho, sep=SEP, encoding=ENCODING, usecols=cols, dtype=tipos, low_memory=False)
    df.columns = df.columns.str.strip().str.upper()
    print(f"{caminho.name}: {len(df):,} linhas, {df.shape[1]} colunas")
    return df


def separar_municipio(df):
    cols = [c for c in COLS_MUN if c in df.columns]
    mun = df[cols].drop_duplicates("CD_MUNICIPIO")
    fato = df.drop(columns=[c for c in cols if c not in ("SG_UF", "CD_MUNICIPIO")])
    return fato, mun


def preparar(df, dims):
    for cd in [c for c in df.columns if c.startswith("CD_")]:
        valores = df[cd].unique()
        if len(valores) == 1 and valores[0] == -1:
            ds = "DS_" + cd[3:]
            df = df.drop(columns=[c for c in (cd, ds) if c in df.columns])
            print(f"coluna removida (sem informacao): {cd}")

    for cd in [c for c in df.columns if c.startswith("CD_")]:
        ds = "DS_" + cd[3:]
        if ds in df.columns:
            dims.setdefault(cd, []).append(df[[cd, ds]].drop_duplicates())
            df = df.drop(columns=ds)
    return df


def chave_unica(df):
    medidas = [c for c in df.columns if c.startswith("QT_")]
    chaves = [c for c in df.columns if c not in medidas]
    if df.duplicated(chaves).any():
        df = df.groupby(chaves, observed=True, as_index=False)[medidas].sum()
        df[medidas] = df[medidas].astype("int32")
    return df


def montar_dimensoes(dims, mun_ele, mun_comp):
    tabelas = {}
    mun = pd.concat([mun_ele, mun_comp], ignore_index=True).drop_duplicates("CD_MUNICIPIO")
    if "CD_MUN_SIT_BIOMETRICA" in mun.columns:
        mun["CD_MUN_SIT_BIOMETRICA"] = mun["CD_MUN_SIT_BIOMETRICA"].astype("Int64")
    tabelas["dim_municipio"] = mun.sort_values("CD_MUNICIPIO").reset_index(drop=True)

    for cd, partes in dims.items():
        ds = "DS_" + cd[3:]
        d = pd.concat(partes, ignore_index=True)
        d[ds] = d[ds].astype(str)
        d = d.drop_duplicates().drop_duplicates(cd)
        tabelas["dim_" + cd[3:].lower()] = d.sort_values(cd).reset_index(drop=True)
    return tabelas


def unificar(comp, ele, tabelas):
    extras = [c for c in comp.columns
              if c not in ele.columns and not c.startswith("QT_") and c != "NR_TURNO"]
    if extras:
        print(f"base unificada nao gerada, quebras so no comparecimento: {extras}")
        return None

    chaves = [c for c in comp.columns if c in ele.columns and not c.startswith("QT_")]
    uni = comp.merge(ele, on=chaves, how="left", validate="many_to_one")

    primeiro = uni["NR_TURNO"] == uni["NR_TURNO"].min()
    for c in [c for c in ele.columns if c.startswith("QT_")]:
        uni[c] = uni[c].astype("Int32")
        uni.loc[~primeiro, c] = pd.NA

    for nome, dim in tabelas.items():
        chave = "CD_MUNICIPIO" if nome == "dim_municipio" else dim.columns[0]
        if chave not in uni.columns:
            continue
        for col in dim.columns:
            if col == chave or col in uni.columns:
                continue
            nova = uni[chave].map(dim.set_index(chave)[col])
            uni[col] = nova.astype("category") if col.startswith(("DS_", "NM_", "SG_")) else nova
    return uni


def salvar(df, nome):
    SAIDA.mkdir(exist_ok=True)
    df.to_parquet(SAIDA / f"{nome}.parquet", index=False, compression="snappy")
    if GERAR_CSV:
        df.to_csv(SAIDA / f"{nome}.csv", index=False, sep=";", encoding="utf-8-sig")
    print(f"{nome}: {len(df):,} linhas, {df.shape[1]} colunas")


def main():
    for arq in (ARQ_COMP, ARQ_ELEI):
        if not arq.exists():
            raise SystemExit(f"Arquivo nao encontrado: {arq}")

    comp = ler(ARQ_COMP)
    ele = ler(ARQ_ELEI)

    tot_comp = comp.filter(like="QT_").sum()
    tot_ele = ele.filter(like="QT_").sum()

    comp, mun_comp = separar_municipio(comp)
    ele, mun_ele = separar_municipio(ele)

    dims = {}
    comp = chave_unica(preparar(comp, dims))
    ele = chave_unica(preparar(ele, dims))

    assert (comp.filter(like="QT_").sum() == tot_comp).all()
    assert (ele.filter(like="QT_").sum() == tot_ele).all()

    tabelas = montar_dimensoes(dims, mun_ele, mun_comp)

    salvar(comp, "fato_comparecimento")
    salvar(ele, "fato_eleitorado")
    for nome, tab in tabelas.items():
        salvar(tab, nome)

    if GERAR_UNIFICADA:
        uni = unificar(comp, ele, tabelas)
        if uni is not None:
            salvar(uni, "base_unificada")


if __name__ == "__main__":
    main()
