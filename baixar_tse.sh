#!/bin/bash
# Baixa todas as bases do TSE 2018 (Eleitorado + Comparecimento/Abstenção)
# Uso: bash baixar_tse.sh

set -e

PASTA_DESTINO="dados_tse_2018"
mkdir -p "$PASTA_DESTINO"
cd "$PASTA_DESTINO"

echo "Baixando arquivos em: $(pwd)"
echo ""

# --- Comparecimento e Abstenção ---
curl -L -C - -o comparecimento_abstencao_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_comparecimento_abstencao/perfil_comparecimento_abstencao_2018.zip"

curl -L -C - -o comparecimento_abstencao_pcd_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_comparecimento_abstencao_eleitor_deficiente/perfil_comparecimento_abstencao_eleitor_deficiente_2018.zip"

curl -L -C - -o comparecimento_abstencao_tte_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_comparecimento_abstencao_eleitor_tte/perfil_comparecimento_abstencao_eleitor_tte_2018.zip"

# --- Eleitorado (bases nacionais) ---
curl -L -C - -o eleitorado_perfil_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_eleitorado/perfil_eleitorado_2018.zip"

curl -L -C - -o eleitorado_pcd_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_eleitor_deficiente/perfil_eleitor_deficiencia_2018.zip"

curl -L -C - -o eleitorado_local_votacao_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/eleitorado_locais_votacao/eleitorado_local_votacao_2018.zip"

curl -L -C - -o eleitorado_transferencia_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_eleitor_tte/transferencia_temporaria_2018.zip"

curl -L -C - -o eleitorado_transferencia_secao_2018.zip \
  "https://cdn.tse.jus.br/estatistica/sead/odsele/perfil_eleitor_tte/transf_temporaria_secao_2018.zip"

echo ""
echo "Concluído! Todos os arquivos nacionais foram baixados em: $(pwd)"
echo ""
echo "Para testar a integridade de cada zip, rode:"
echo "  for f in *.zip; do unzip -t \"\$f\" > /dev/null && echo \"OK: \$f\" || echo \"ERRO: \$f\"; done"
