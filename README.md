<div align="center">

<!-- ===== BANNER PRINCIPAL COM EFEITO DE BOOT ===== -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0f1a,50:1a4dad,100:0f1a3d&height=220&section=header&text=URNA.SYS%20INITIALIZING&fontSize=42&fontColor=4FA3FF&animation=fadeIn&fontAlignY=38&desc=Eleitorado%20e%20Absten%C3%A7%C3%A3o%20Nacional%20%E2%80%A2%20TSE%202018&descAlignY=58&descAlign=50" width="100%"/>

<br/>

<!-- TYPING ANIMATION -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&duration=3000&pause=800&color=4FA3FF&center=true&vCenter=true&width=650&lines=%3E+Booting+Urna.exe...;%3E+Carregando+base+TSE+2018...;%3E+Eleitorado+%3A+ONLINE;%3E+Comparecimento+%2F+Absten%C3%A7%C3%A3o+%3A+ONLINE;%3E+Bem-vindo+ao+Byte+Eleitoral+%F0%9F%97%B3%EF%B8%8F)](https://git.io/typing-svg)

<img src="https://raw.githubusercontent.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/main/e0e29a37-eb0f-4c9d-9737-3d327d2fe74b.gif" width="100%" height="3px"/>

</div>

<!-- ===== SOBRE O PROJETO ===== -->
## `<SobreProjeto />`

```yaml
sistema:
  nome: "URNA.SYS"
  equipe: "Byte Eleitoral"
  tipo: "Projeto Acadêmico - Análise de Dados Eleitorais"
  status: "🟢 em desenvolvimento"
  escopo: "Nacional"
  ano_referencia: 2018
  fonte_dados: "Portal de Dados Abertos do TSE"
  missao: >
    Investigar o perfil do eleitorado brasileiro e os padrões de
    comparecimento e abstenção nas eleições de 2018, transformando
    bases de dados públicas do TSE em insights claros sobre
    participação eleitoral em todo o território nacional.
```

> "Entender quem vota — e quem não vota — é o primeiro passo pra entender a democracia."

---

<!-- ===== SOBRE OS DADOS ===== -->
## `<FonteDeDados />`

<div align="center">

| 📦 Dataset | 📝 Conteúdo | 🔗 Fonte |
|:---|:---|:---|
| **Eleitorado - 2018** | Perfil do eleitorado, eleitorado por local de votação, perfil do eleitorado com deficiência, perfil por seção eleitoral | [Portal TSE](https://dadosabertos.tse.jus.br/dataset/eleitorado-2018) |
| **Comparecimento e Abstenção - 2018** | Comparecimento e abstenção, pessoas com deficiência, transferência temporária de eleitor | [Portal TSE](https://dadosabertos.tse.jus.br/dataset/comparecimento-e-abstencao-2018) |

</div>

Todos os dados são públicos, oficiais e distribuídos sob licença **Creative Commons Atribuição (CC-BY)** pelo Tribunal Superior Eleitoral.

---

<!-- ===== PIPELINE ===== -->
## `<Pipeline />`

```bash
byte-eleitoral@urna:~$ cat pipeline_tse_2018.ipynb

[✓] Importação das bases (eleitorado + comparecimento/abstenção)
[✓] Leitura com encoding latin-1 e separador ";"
[✓] Padronização de colunas e sufixos (_eleitorado, _comparecimento)
[✓] Merge das bases por chave comum (seção eleitoral / município / UF)
[✓] Tratamento de valores nulos (NaN)
[✓] Consolidação da base nacional 2018

byte-eleitoral@urna:~$ echo "Status: base unificada pronta para análise 📊"
```

---

<!-- ===== TECH STACK ===== -->
## `<TechStack />`

<div align="center">

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=4FA3FF)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=4FA3FF)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

<div align="center">
<img src="https://skillicons.dev/icons?i=python,git,github,vscode,linux&theme=dark" />
</div>

---

<!-- ===== OBJETIVOS ===== -->
## `<ObjetivosDoProjeto />`

```bash
byte-eleitoral@urna:~$ cat objetivos.txt

[■■■■■■■■■■■■■■■□□□□□] 75%  Consolidar base nacional de eleitorado 2018
[■■■■■■■■■■■■□□□□□□□□] 60%  Analisar padrões de abstenção por região/UF
[■■■■■■■■■■□□□□□□□□□□] 50%  Cruzar perfil do eleitorado com deficiência x comparecimento
[■■■■■■■□□□□□□□□□□□□□] 35%  Construir dashboard/visualizações finais
[■■■■■□□□□□□□□□□□□□□□] 25%  Documentar conclusões e apresentar resultados

byte-eleitoral@urna:~$ echo "Status: pipeline rodando, análises em andamento 🗳️"
```

---

<!-- ===== EQUIPE ===== -->
## `<Equipe />`

<div align="center">

**Byte Eleitoral**

| Integrante | Função |
|:---|:---|
| Cindy Larissa Cardoso Fernandes | Engenheiro(a) de Dados (T-SQL / AWS) |
| Vinicius Mello de Cavalho | Project Manager / Scrum Master |
| Kauã da Silva Santos | Analista de BI (Power BI) · Analista de Dados / ETL |

</div>

---

<!-- ===== RODAPÉ ===== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f1a3d,50:1a4dad,100:0f0f1a&height=120&section=footer"/>

**Projeto Inovation Lab - Faculdade**

</div>
