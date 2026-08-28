# ATHENA Ultimate V15.3.3

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org)
[![Status](https://img.shields.io/badge/Status-Controlled%20Research%20Release-orange)]()
[![Last Updated](https://img.shields.io/badge/Last%20Updated-August%202026-success)]()

**A Controlled Mathematical-Physics Research Monograph**  
Pure-disformal scalar–tensor framework with explicit status ledger

---

## Scope and Status (Read First)

ATHENA Ultimate V15.3.3 is a **controlled research release**, not a completed unified theory.

Its frozen lower-order core consists of:
- Einstein–Hilbert gravity
- One real compact scalar field $\Phi \sim \Phi + 2\pi f_a$ with periodic potential
- Matter coupled through a pure-disformal metric

The internal flat $T^2$ is treated as **configuration space**, not an additional spacetime dimension.

This edition explicitly separates:
- **DERIVED** algebraic and geometric results
- **CONDITIONAL** dynamics (require extra assumptions)
- **OPEN** problems
- **NO-GO** results (including the Derrick obstruction for the previous soliton mass route)

The release **does not claim**:
- Experimental validation
- A completed Standard Model derivation
- Emergent gravity as a finished theory
- A complete matter / particle-mass sector
- A solved cosmological likelihood

Unspecified sectors (neutrino, higher operators, full perturbations, lensing, growth, waveforms) remain explicitly open.

---

## Key Mathematical Results (V15.3.3)

| Item | Status |
|------|--------|
| Rank-one disformal inverse & determinant | DERIVED |
| Exact pure-disformal connection & curvature identities | DERIVED |
| ADM decomposition & hypersurface-deformation algebra | DERIVED |
| Source-free stability limits (minimal scalar + tensor) | DERIVED |
| Exact scalar backgrounds (Minkowski minima, kinetic power-law) | DERIVED |
| Derrick obstruction (static canonical soliton) | **NO-GO** |
| Particle-mass construction via soliton | **NO-GO / OPEN** |
| Full coupled stability / hyperbolicity | OPEN |
| Complete matter sector & neutrino closure | OPEN |
| Observational fits (SPARC, dipole, etc.) | Targets pending independent reproduction |

Full status tables are inside the monograph (Appendix F, Stage 5 ledgers, and Appendix K).

---

## Repository Structure (Proposed / Target)

```text
ATHENA/
├── README.md                 # This file
├── LICENSE
├── CHANGELOG.md
├── requirements.txt
├── environment.yml           # (to be added)
├── setup.py
│
├── docs/
│   ├── physics.md
│   ├── status_ledger.md      # Machine-readable status summary
│   ├── quickstart.md
│   └── falsification.md
│
├── monograph/
│   ├── V15.3.3/              # Current controlled release (PDF + LaTeX source)
│   ├── V14/                  # Archived
│   └── historical/           # Older versions
│
├── athena/                   # Core Python package (algebraic identities, FLRW, disformal utils)
├── simulations/              # Numerical experiments (source-free limits, stability checks)
├── scripts/                  # Utility & reproducibility scripts
├── tests/                    # Unit tests for algebraic identities and source-free limits
│
└── data/                     # (placeholder) SPARC catalogues, checksums, reference outputs
```

> **Note:** As of this commit the public tree still largely reflects the V14 layout.  
> The structure above is the target organisation for the V15.3.3 controlled release.

---

## Quick Start (Algebraic / Source-Free Checks)

```bash
git clone https://github.com/mgy421977-bit/ATHENA.git
cd ATHENA
pip install -r requirements.txt
pip install -e .

# Run algebraic identity and source-free limit tests (when available)
python -m pytest tests/ -q
```

Observational fitting scripts and full likelihood pipelines are **not** part of the frozen core and remain under active development / independent reproduction.

---

## Citation

Please cite the version you actually use and respect the status statements inside the monograph.

```bibtex
@software{yilmaz2026athena_v1533,
  author  = {Yılmaz, Mustafa Gökhan},
  title   = {ATHENA Ultimate V15.3.3: Controlled Mathematical-Physics Research Release},
  year    = {2026},
  url     = {https://github.com/mgy421977-bit/ATHENA},
  note    = {Controlled research release. Not a completed unified theory.}
}
```

(Previous V14 Zenodo DOI: [10.5281/zenodo.21475363](https://doi.org/10.5281/zenodo.21475363) — archival only.)

---

## Author

**Mustafa Gökhan Yılmaz**  
Independent Researcher – İzmir, Türkiye  
ORCID: [0009-0002-6591-0163](https://orcid.org/0009-0002-6591-0163)  
Email: mgy421977@gmail.com

Constructive criticism, code contributions, and scientific discussion are welcome.  
Please open an Issue or Pull Request.

---

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
