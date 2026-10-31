<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1565C0,100:64B5F6&height=130&section=header" alt="" width="100%">

  <h1>Reginaldo Gonçalves Leão Junior, Ph.D.</h1>

  <p>
    Termoquímica · Combustão · Transporte de Radiação<br>
    Professor, Instituto Federal de Minas Gerais (IFMG) · Brasil
  </p>

  <sub><a href="README.md">English</a> · <b>Português</b></sub>
</div>

<div align="center">

  [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?style=flat-square&logo=google-scholar&logoColor=white)](https://scholar.google.com.br/citations?user=GcjoCaMAAAAJ&hl=pt-BR)
  [![ORCID](https://img.shields.io/badge/ORCID_0000--0002--3596--2256-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-3596-2256)
  [![Lattes](https://img.shields.io/badge/Curr%C3%ADculo_Lattes-004488?style=flat-square)](http://lattes.cnpq.br/4370539390024098)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reginaldoleao/)
  [![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square)](mailto:reginaldo.leao@ifmg.edu.br)

</div>

---

> *"O mais importante na ciência não é tanto obter novos fatos, mas descobrir novas formas de pensar sobre eles."*
>
> — **William Lawrence Bragg**

---

## 👨‍🏫 Perfil

Cientista computacional atuando em termoquímica, combustão e transporte de radiação. Doutor em **Ciência das Radiações** (UFMG), com formação em Física e Engenharia Química. Mantenedor de software científico de código aberto.

Professor no **Instituto Federal de Minas Gerais (IFMG)**, onde trabalho com sistemas energéticos e proteção radiológica (CNEN).

## 🎓 Formação Acadêmica

| Titulação | Área | Instituição |
|:--|:--|:--|
| Doutorado | Ciência das Radiações | Universidade Federal de Minas Gerais (UFMG) |
| Mestrado | Ciências e Técnicas Nucleares | Universidade Federal de Minas Gerais (UFMG) |
| Graduação | Engenharia Química | Universidade de Santo Amaro (UNISA) |
| Graduação | Física | Centro Universitário de Formiga (UNIFORMG) |

## 🔬 Pesquisa

Membro do **GESESC** (Grupo de Estudos em Sistemas Energéticos e Simulação Computacional), certificado no diretório de grupos de pesquisa do CNPq.

- Termoquímica por polinômios da NASA e modelagem de combustão
- Transporte de radiação via Monte Carlo (EGSnrc / BEAMnrc / DOSXYZnrc)
- Métodos numéricos aplicados a sistemas energéticos
- Transferência de calor e dinâmica de fluidos em sistemas complexos
- Modelagem computacional de reatores nucleares

[🔗 Grupo GESESC no CNPq](http://dgp.cnpq.br/dgp/espelhogrupo/713753)

## 📚 Ensino

- Física
- Programação Aplicada à Engenharia
- Recursos Energéticos
- Introdução à Engenharia Nuclear
- Análise Numérica
- Termodinâmica

---

## 📦 Software

Pacotes de código aberto para modelagem termoquímica em engenharia — um único núcleo de polinômios da NASA, exposto a dois ecossistemas.

| Pacote | Versão | Alcance | Estrelas | DOI |
|:--|:--|:--|:--|:--|
| **[pyglenn](https://github.com/ProfLeao/pyglenn)**<br><sub>Python · PyPI — propriedades termodinâmicas a partir dos coeficientes polinomiais da NASA, com banco de dados SQLite</sub> | [![PyPI](https://img.shields.io/pypi/v/pyglenn?style=flat-square)](https://pypi.org/project/pyglenn/) | ![Downloads PyPI](https://img.shields.io/pypi/dm/pyglenn?style=flat-square) | ![Estrelas](https://img.shields.io/github/stars/ProfLeao/pyglenn?style=flat-square) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21324586.svg)](https://doi.org/10.5281/zenodo.21324586) |
| **[Glenn.jl](https://github.com/ProfLeao/Glenn.jl)**<br><sub>Julia · General — coeficientes Glenn da NASA para propriedades termodinâmicas de espécies individuais</sub> | [![Release](https://img.shields.io/github/v/release/ProfLeao/Glenn.jl?style=flat-square)](https://github.com/ProfLeao/Glenn.jl/releases) | ![Requisições Julia](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FProfLeao%2FProfLeao%2Fmain%2Fassets%2Fjulia-stats.json) | ![Estrelas](https://img.shields.io/github/stars/ProfLeao/Glenn.jl?style=flat-square) | — |
| **[pyglenn-notebooks](https://github.com/ProfLeao/pyglenn-notebooks)**<br><sub>Jupyter — notebooks explorando dados termoquímicos com pyglenn</sub> | — | — | ![Estrelas](https://img.shields.io/github/stars/ProfLeao/pyglenn-notebooks?style=flat-square) | — |

<p align="center">
  <img src="https://api.star-history.com/svg?repos=ProfLeao/Glenn.jl,ProfLeao/pyglenn&type=Date" alt="Histórico de estrelas de Glenn.jl e pyglenn" width="640">
</p>

<sub>As métricas são atualizadas automaticamente: downloads do PyPI via [pypistats](https://pypistats.org/packages/pyglenn) (últimos 30 dias, incluindo mirrors); alcance no Julia a partir da [telemetria oficial dos package servers](https://discourse.julialang.org/t/announcing-package-download-stats/69073), agregada na janela publicada pelo Julia (`julialang-logs/public_outputs/current`) — não há número total histórico divulgado.</sub>

> **Validação** — o Glenn.jl é validado de forma cruzada contra dados de referência **NIST-JANAF** para sete espécies (CO₂, N₂, CO, H₂O, O₂, NH₃, SO₂), com auditoria ponto a ponto (`glenn_vs_nist.csv`) e estatísticas agregadas.

> **Adoção pela comunidade** — o Clapeyron.jl disponibiliza o modelo de gás ideal `GlennJL`, construído sobre a base de coeficientes da NASA mantida pelo Glenn.jl ([PR #616](https://github.com/ClapeyronThermo/Clapeyron.jl/pull/616)).

## ☢️ Transporte de Radiação via Monte Carlo

Modelos de feixes clínicos de fótons construídos e avaliados com **EGSnrc**, **BEAMnrc** e **DOSXYZnrc**: um cabeçote VARIAN CLINAC 2100 foi modelado e validado contra medições de comissionamento para dosimetria de pequenos campos — concordância lateral acima de 98%, concordância de dose em profundidade acima de 90% no pior caso e incerteza relativa máxima de 4% com 10⁹ histórias ([BJRS, 2018](https://doi.org/10.15392/bjrs.v6i1.314)).

## 📄 Publicações Selecionadas — Energia

- Rezende, J. A. M.; **Leão Junior, R. G.**; Gomes, O. S. M. *Scientometric analysis of publications on household electricity theft and energy consumption load profiling in a smart grid context.* **Sustainability**, 2024. [10.3390/su16229921](https://doi.org/10.3390/su16229921)
- Lemos, L.; Goulart, P.; **Leão Junior, R. G.**; Carpio, R.; Fernandes, M. T. *Exergy analysis of the electricity generation process in the reuse of blast furnace gases in a steelmaking company.* Proc. 26th International Congress of Mechanical Engineering (COBEM), 2021. [10.26678/abcm.cobem2021.cob2021-1887](https://doi.org/10.26678/abcm.cobem2021.cob2021-1887)
- Leal, G.; Leal, J. M.; Gomes, A.; Carpio, R.; **Leão Junior, R. G.** *Calibration of a low-cost digital hygrometer for measuring moisture in sugarcane bagasse.* Proc. 27th International Congress of Mechanical Engineering (COBEM), 2025. [10.26678/abcm.cobem2023.cob2023-0533](https://doi.org/10.26678/abcm.cobem2023.cob2023-0533)
- Lopes, F. F.; **Leão Junior, R. G.** *Proposal for a new methodological approach to measure the concentration of methane in biogas using a low-cost sensor.* Proc. 18th Brazilian Congress of Thermal Sciences and Engineering (ENCIT), 2020. [10.26678/abcm.encit2020.cit20-0171](https://doi.org/10.26678/abcm.encit2020.cit20-0171)

Artigos de engenharia nuclear e ciência das radiações estão no meu [perfil do Google Scholar](https://scholar.google.com.br/citations?user=GcjoCaMAAAAJ&hl=pt-BR).

## ⚙️ Stack Tecnológica

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Julia](https://img.shields.io/badge/Julia-9558B2?style=flat-square&logo=julia&logoColor=white) ![Fortran](https://img.shields.io/badge/Fortran-734F96?style=flat-square&logo=fortran&logoColor=white) ![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white) ![GNU Octave](https://img.shields.io/badge/GNU_Octave-0790C0?style=flat-square&logo=octave&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) ![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white) ![Overleaf](https://img.shields.io/badge/Overleaf-47A141?style=flat-square&logo=overleaf&logoColor=white)

</div>

## 📊 Atividade no GitHub

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=ProfLeao&theme=tokyonight" alt="Resumo de contribuições de ProfLeao" width="640">
</div>

---

## 🤝 Colaboração

Interessado em pesquisa, projetos acadêmicos ou desafios computacionais? Estou aberto a colaborações.

- 💬 Pergunte sobre: física computacional, engenharia nuclear, simulação numérica, Python/Julia para engenharia
- 🔭 Trabalhando em: modelos avançados de simulação para sistemas energéticos e bibliotecas científicas em Julia
- ⚡ Código é o laboratório moderno do físico teórico

## ☕ Apoie

<div align="left">
  <a href="https://www.buymeacoffee.com/reginaldoleao">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="48">
  </a>
</div>

---

<div align="center">

  *"O mais incompreensível do mundo é que ele seja compreensível."*
  <sub>— Albert Einstein</sub>

  <sub>© 2026 Prof. Reginaldo Leão · IFMG</sub>
</div>
