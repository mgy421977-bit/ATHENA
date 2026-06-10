# ATHENA

ATHENA V25.13 — Scalar–Disformal Vacuum Field Theory

![Version](https://img.shields.io/badge/version-V25.13-blue)
![Status](https://img.shields.io/badge/status-preprint-orange)
![Research](https://img.shields.io/badge/type-research-green)

**A research framework investigating whether galaxy dynamics, gravitational lensing, and cosmological phenomena can emerge from vacuum-field geometry without invoking particle dark matter.**

**Author:** Mustafa Gökhan Yılmaz  
**ORCID:** 0009-0002-6591-0163  
**Location:** İzmir, Türkiye

---

## Project Status

| Area | Status |
|------|--------|
| Mathematical Model | ✅ Active |
| Numerical Tests | ✅ Active |
| Repository Development | ✅ Active |
| Independent Review | ⏳ Ongoing |
| Preprint Submission | ⏳ Pending (ID: 217942) |

---

## Core Hypothesis

ATHENA investigates the possibility that part of the phenomena commonly attributed to dark matter and dark energy may emerge from vacuum geometry and information structure rather than additional matter components.

This hypothesis remains under active investigation and should be considered exploratory until independently validated.

---

## Repository Structure

```

ATHENA/
├── preprints/          (V25.13 PDF - to be added)
├── manifesto/          (V26.md – ontological manifesto)
├── athena/             (Python modules: field_solver, rotation_curves, likelihood)
├── scripts/            (run_sparc_fit.py)
├── tests/              (test_gr_limit.py)
└── README.md

```

---

## Getting Started

```bash
git clone https://github.com/mgy421977-bit/ATHENA.git
cd ATHENA
pip install numpy scipy pandas matplotlib
python scripts/run_sparc_fit.py
python -m athena.tests.test_gr_limit
```

---

Documentation

· Preprint: ATHENA V25.13 (link will be added when online)
· - **Ontological Manifesto:** [ATHENA V26 – Işık Neden Dönüyor?](./manifesto/V26.md)  
  DOI: [10.5281/zenodo.20627859](https://doi.org/10.5281/zenodo.20627859)

---

Citation

```bibtex
@misc{Yilmaz2026ATHENA,
  author = {Mustafa Gökhan Yılmaz},
  title = {ATHENA V25.13: Scalar–Disformal Vacuum Field Theory},
  year = {2026},
  note = {Research Repository},
  howpublished = {\url{https://github.com/mgy421977-bit/ATHENA}}
}
```

---

License

All Rights Reserved.

Commercial use, redistribution, derivative works, or integration into third-party systems require explicit written permission from the author. See LICENSE for details.

```
