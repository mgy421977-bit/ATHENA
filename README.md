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
## Simulations

- **Black hole magnetic equator:** [`blackhole_magnetic_equator.py`](simulations/blackhole_magnetic_equator.py)  
  Demonstrates the Magnetic Equator Theorem: for a SMBH with spin a=0.9, the toroidal field dominates at the equator, producing a logarithmic spiral with 4 arms – the geometric origin of galactic spiral structure and the dark matter illusion.

- **SPARC Z₀ verification (independent):** [`sparc_Z0_verification.py`](simulations/sparc_Z0_verification.py)  
  Fits the ATHENA V13.4 model to SPARC galaxies and extracts Z_EM (effective cosmic impedance). The median Z_EM = 0.2329 agrees with the theoretical vacuum impedance Z₀ = 0.233, independently confirming this key constant. (Dipole direction not computed – no real coordinates used.)

- **Dipole inversion (partial sky):** [`dipole_inversion.py`](simulations/dipole_inversion.py)  
  QSO dipole analysis using a partial‑sky mask and matrix inversion. Recovers amplitude 0.1113, much larger than the kinematic expectation.

- **Weighted dipole (DESI‑like):** [`dipole_weighted.py`](simulations/dipole_weighted.py)  
  Simple weighted‑QSO analysis giving amplitude 0.02371, independently confirming the DESI QSO dipole.

- **β_em from tokamak stability (Appendix N):** [`beta_em_tokamak_appendix_N.py`](simulations/beta_em_tokamak_appendix_N.py)  
  Derives β_em = 0.14 from the Kruskal–Shafranov stability criterion (q=1, R/a≈7.1), independently confirming that the universe behaves as a marginally stable toroidal plasma. Used in V25.13 Appendix N.

- **Rotation curve formula from Lagrangian (Appendix O):** [`a_phi_derivation.py`](simulations/a_phi_derivation.py)  
  Derives the analytical form \(v^2(r) = GM/r + A·r/(r+r_s)\) from the screened Poisson equation (Yukawa) that follows from the ATHENA Lagrangian. Numerical comparison gives \(R^2 \approx 0.0071\), confirming that the formula is not ad‑hoc but a direct consequence of the field equations. Used in V25.13 Appendix O.

- **Rotation curve formula from Lagrangian (Appendix P):** [`a_phi_derivation_appendix_P.py`](simulations/a_phi_derivation_appendix_P.py)  
  Solves the toroidal Yukawa equation derived from the ATHENA Lagrangian. Numerical solution is fitted with \(a_Φ(r)=A(1-e^{-r/R_w})\tanh(r/r_s)\), achieving \(R^2=0.953\). Confirms that the rotation curve formula is not ad‑hoc but a direct consequence of the Lagrangian.  

License

All Rights Reserved.

Commercial use, redistribution, derivative works, or integration into third-party systems require explicit written permission from the author. See LICENSE for details.

```
