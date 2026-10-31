<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1565C0,100:64B5F6&height=130&section=header" alt="" width="100%">

  <h1>Reginaldo Gonçalves Leão Junior, Ph.D.</h1>

  <p>
    Thermochemistry · Combustion · Radiation Transport<br>
    Professor, Instituto Federal de Minas Gerais (IFMG) · Brazil
  </p>

  <sub><b>English</b> · <a href="README.pt-BR.md">Português</a></sub>
</div>

<div align="center">

  [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?style=flat-square&logo=google-scholar&logoColor=white)](https://scholar.google.com.br/citations?user=GcjoCaMAAAAJ&hl=en)
  [![ORCID](https://img.shields.io/badge/ORCID_0000--0002--3596--2256-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0002-3596-2256)
  [![Lattes](https://img.shields.io/badge/Lattes_CV-004488?style=flat-square)](http://lattes.cnpq.br/4370539390024098)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reginaldoleao/)
  [![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square)](mailto:reginaldo.leao@ifmg.edu.br)

</div>

---

> *"The important thing in science is not so much to obtain new facts as to discover new ways of thinking about them."*
>
> — **William Lawrence Bragg**

---

## 👨‍🏫 About

Computational scientist working on thermochemistry, combustion and radiation transport. Ph.D. in **Radiation Science** (UFMG), with degrees in Physics and Chemical Engineering. Maintainer of open-source scientific software.

Professor at the **Instituto Federal de Minas Gerais (IFMG)**, Brazil, where I work on energy systems.

## 🎓 Academic Background

| Degree | Field | Institution |
|:--|:--|:--|
| Ph.D. | Radiation Science | Universidade Federal de Minas Gerais (UFMG) |
| M.Sc. | Nuclear Sciences and Techniques | Universidade Federal de Minas Gerais (UFMG) |
| B.Eng. | Chemical Engineering | Universidade de Santo Amaro (UNISA) |
| B.Sc. | Physics | Centro Universitário de Formiga (UNIFORMG) |

## 🔬 Research

Member of **GESESC** (Study Group on Energy Systems and Computational Simulation), certified in the CNPq research group directory.

- NASA-polynomial thermochemistry and combustion modeling
- Monte Carlo radiation transport (EGSnrc / BEAMnrc / DOSXYZnrc)
- Numerical methods applied to energy systems
- Heat transfer and fluid dynamics in complex systems
- Computational modeling of nuclear reactors

[🔗 GESESC group at CNPq](http://dgp.cnpq.br/dgp/espelhogrupo/713753)

## 📚 Teaching

- Physics
- Applied Programming for Engineering
- Energy Resources
- Introduction to Nuclear Engineering
- Numerical Analysis
- Thermodynamics

---

## 📦 Software

Open-source packages for thermochemical modeling in engineering — a single NASA-polynomial core, exposed to two ecosystems.

| Package | Version | Reach | Stars | DOI |
|:--|:--|:--|:--|:--|
| **[pyglenn](https://github.com/ProfLeao/pyglenn)**<br><sub>Python · PyPI — thermodynamic properties from NASA polynomial coefficients, SQLite-backed</sub> | [![PyPI](https://img.shields.io/pypi/v/pyglenn?style=flat-square)](https://pypi.org/project/pyglenn/) | ![PyPI downloads](https://img.shields.io/pypi/dm/pyglenn?style=flat-square) | ![Stars](https://img.shields.io/github/stars/ProfLeao/pyglenn?style=flat-square) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21324586.svg)](https://doi.org/10.5281/zenodo.21324586) |
| **[Glenn.jl](https://github.com/ProfLeao/Glenn.jl)**<br><sub>Julia · General — NASA Glenn coefficients for thermodynamic properties of individual species</sub> | [![Release](https://img.shields.io/github/v/release/ProfLeao/Glenn.jl?style=flat-square)](https://github.com/ProfLeao/Glenn.jl/releases) | ![Julia requests](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FProfLeao%2FProfLeao%2Fmain%2Fassets%2Fjulia-stats.json) | ![Stars](https://img.shields.io/github/stars/ProfLeao/Glenn.jl?style=flat-square) | — |
| **[pyglenn-notebooks](https://github.com/ProfLeao/pyglenn-notebooks)**<br><sub>Jupyter — notebooks exploring thermochemical data with pyglenn</sub> | — | — | ![Stars](https://img.shields.io/github/stars/ProfLeao/pyglenn-notebooks?style=flat-square) | — |

<p align="center">
  <img src="https://api.star-history.com/svg?repos=ProfLeao/Glenn.jl,ProfLeao/pyglenn&type=Date" alt="Star history of Glenn.jl and pyglenn" width="640">
</p>

<sub>Metrics are refreshed automatically: PyPI downloads from [pypistats](https://pypistats.org/packages/pyglenn) (last 30 days, mirrors included); Julia reach from the [official package-server telemetry](https://discourse.julialang.org/t/announcing-package-download-stats/69073), aggregated over the window Julia publishes (`julialang-logs/public_outputs/current`) — no all-time figure is released.</sub>

> **Validation** — Glenn.jl is cross-validated against **NIST-JANAF** reference data for seven species (CO₂, N₂, CO, H₂O, O₂, NH₃, SO₂), with a point-by-point audit (`glenn_vs_nist.csv`) and aggregated statistics.

> **Community adoption** — Clapeyron.jl ships a `GlennJL` ideal-gas model built on the NASA coefficient database maintained by Glenn.jl ([PR #616](https://github.com/ClapeyronThermo/Clapeyron.jl/pull/616)).

## 📄 Selected Publications — Energy and Monte Carlo Radiation Transport

- Rezende, J. A. M.; **Leão Junior, R. G.**; Gomes, O. S. M. *Scientometric analysis of publications on household electricity theft and energy consumption load profiling in a smart grid context.* **Sustainability**, 2024. [10.3390/su16229921](https://doi.org/10.3390/su16229921)
- Lemos, L.; Goulart, P.; **Leão Junior, R. G.**; Carpio, R.; Fernandes, M. T. *Exergy analysis of the electricity generation process in the reuse of blast furnace gases in a steelmaking company.* Proc. 26th International Congress of Mechanical Engineering (COBEM), 2021. [10.26678/abcm.cobem2021.cob2021-1887](https://doi.org/10.26678/abcm.cobem2021.cob2021-1887)
- Leal, G.; Leal, J. M.; Gomes, A.; Carpio, R.; **Leão Junior, R. G.** *Calibration of a low-cost digital hygrometer for measuring moisture in sugarcane bagasse.* Proc. 27th International Congress of Mechanical Engineering (COBEM), 2025. [10.26678/abcm.cobem2023.cob2023-0533](https://doi.org/10.26678/abcm.cobem2023.cob2023-0533)
- Lopes, F. F.; **Leão Junior, R. G.** *Proposal for a new methodological approach to measure the concentration of methane in biogas using a low-cost sensor.* Proc. 18th Brazilian Congress of Thermal Sciences and Engineering (ENCIT), 2020. [10.26678/abcm.encit2020.cit20-0171](https://doi.org/10.26678/abcm.encit2020.cit20-0171)
- **Leão Jr, R. G.**; Sousa, R. V.; Oliveira, A. H.; Leonardo Silva, H. L.; Mourão, A. P. *Validation of a computational model of a VARIAN CLINAC 2100 linear accelerator using the EGSnrc code for small-field dosimetry*, validated against commissioning measurements. **Brazilian Journal of Radiation Sciences**, v. 6, n. 1, 2018 (in Portuguese). [10.15392/bjrs.v6i1.314](https://doi.org/10.15392/bjrs.v6i1.314)
- **Leão, R. G.**; Sousa, R. V.; Oliveira, A. H.; Silva, H. L. L.; Mourão, A. P. *Computational analysis of "Dose/Collision Kerma" relationship and lateral boundary in stereotactic circular fields using EGSnrc.* **Revista Brasileira de Física Médica**, v. 10, n. 1, 2017. [10.29384/rbfm.2016.v10.n1.p2-8](https://doi.org/10.29384/rbfm.2016.v10.n1.p2-8)

Nuclear engineering and radiation-science papers are listed on my [Google Scholar profile](https://scholar.google.com.br/citations?user=GcjoCaMAAAAJ&hl=en).

## ⚙️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Julia](https://img.shields.io/badge/Julia-9558B2?style=flat-square&logo=julia&logoColor=white) ![Fortran](https://img.shields.io/badge/Fortran-734F96?style=flat-square&logo=fortran&logoColor=white) ![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white) ![GNU Octave](https://img.shields.io/badge/GNU_Octave-0790C0?style=flat-square&logo=octave&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) ![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white) ![Overleaf](https://img.shields.io/badge/Overleaf-47A141?style=flat-square&logo=overleaf&logoColor=white)

</div>

## 📊 GitHub Activity

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=ProfLeao&theme=tokyonight" alt="Contribution summary for ProfLeao" width="640">
</div>

---

## 🤝 Collaboration

Interested in research, academic projects or computational challenges? I am open to collaborations.

- 💬 Ask me about: computational physics, nuclear engineering, numerical simulation, Python/Julia for engineering
- 🔭 Working on: advanced simulation models for energy systems and scientific libraries in Julia
- ⚡ Code is the modern laboratory of the theoretical physicist

## ☕ Support

<div align="left">
  <a href="https://www.buymeacoffee.com/reginaldoleao">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="48">
  </a>
</div>

---

<div align="center">

  *"The most incomprehensible thing about the world is that it is comprehensible."*
  <sub>— Albert Einstein</sub>

  <sub>© 2026 Prof. Reginaldo Leão · IFMG</sub>
</div>
