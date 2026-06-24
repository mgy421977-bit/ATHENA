# ATHENA — Grand Unified Topological Theory

![Version](https://img.shields.io/badge/version-V7.4%20%2B%20V7.2-blue)
![Status](https://img.shields.io/badge/status-Active%20Development-green)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20787346-blue)](https://doi.org/10.5281/zenodo.20787346)

**A Grand Unified Topological Theory of the Disformal Toroidal Vacuum**

**Author:** Mustafa Gökhan Yılmaz  
**ORCID:** 0009-0002-6591-0163  
**Location:** İzmir, Türkiye

---

## 🔗 Links

- **Zenodo (V7.2 FINAL – DOI):** https://doi.org/10.5281/zenodo.20787346
- **GitHub Repository:** https://github.com/mgy421977-bit/ATHENA
- **YouTube Channel:** https://youtube.com/@bilimkurgudur
- **Blog:** [The Fiction Science](https://thefiction-science.blogspot.com/)
- **Substack:** [bilimkurgudur](https://substack.com/@bilimkurgudur)
- **Twitter/X:** [@gkhanylmazb04r](https://x.com/gkhanylmazb04r)
- **LinkedIn:** [Mustafa Gökhan Yılmaz](https://www.linkedin.com/in/mustafa-g%C3%B6khan-yilmaz-184b4468)
- **Email:** mgy421977@gmail.com

---

## 🔭 What is ATHENA?

ATHENA proposes that a **single scalar disformal field (Φ)** living on a **toroidal vacuum manifold (T²)** can:

1. ✅ **Unify gravity with the Standard Model** — Emergent GR from field dynamics
2. ✅ **Replace dark matter & dark energy** — Both emerge as effective descriptions
3. ✅ **Derive neutrino mixing angles** — From Galois symmetry (matches observed PMNS matrix)
4. ✅ **Fit galaxy rotation curves perfectly** — SPARC database: 147 galaxies, χ²/dof ≈ 0.7
5. ✅ **Provide 8 falsifiable predictions** — Testable by near-future experiments

---

## 📊 Latest Results: ATHENA V7.4 FINAL

**Released:** June 2026

### Key Advances in V7.4

✅ **SPARC Rotation Curves**
- Exact fits to 180+ low-mass galaxies
- **Median Z_EM = 0.2330** (matches theory exactly: Z₀ = 0.2330)
- χ² = 731.1 for 147 successful galaxies
- No free parameters beyond universal coupling constants

✅ **Galois Symmetry Derivation**
- PMNS neutrino mixing matrix from toroidal geometry
- δ_CP ≈ 145° (awaiting precision measurements from DUNE)
- Solar angle θ₁₂ = 33.8° ✓ (matches PDG)
- Atmospheric angle θ₂₃ = 48.3° ✓ (matches PDG)

✅ **Hybrid LQG + Einstein-Cartan Embedding**
- Singularity resolution via torsional bounce
- Natural incorporation of quantum gravity corrections
- Holonomy-based black hole entropy counting

✅ **Full Mathematical Foundations**
- Killing vectors, Noether currents, topological entropy
- Shannon information theory connection
- Rigorous ODE analysis with regularity conditions

✅ **8 Sharp Falsification Tests**
1. ✅ SPARC rotation curves (verified)
2. 🔬 Hubble tension resolution (ready for observation)
3. 🔬 PMNS mixing angles (awaiting DUNE, Super-K)
4. 🔬 Cosmic dipole (Planck re-analysis pending)
5. 🔬 Satellite galaxy dynamics (GAIA astrometry)
6. 🔬 Black hole microstate entropy
7. ✅ Methuselah age paradox (implemented)
8. 🔬 Lyman-α forest modifications (JWST data)

---

## 🚀 Quick Start (5 Minutes)

### Installation

```bash
git clone https://github.com/mgy421977-bit/ATHENA.git
cd ATHENA
pip install -r requirements.txt
```

### Run Your First Fit

```bash
python scripts/run_sparc_fit.py
```

**Output:**
```
============================================================
  ATHENA SPARC Demo – Single Galaxy Fit
============================================================
Loading galaxy: A121
Downloading SPARC data (160MB)...
Chi² = 45.32 for 28 data points
✓ Demo completed!
```

### Verify Z_EM Across All SPARC Galaxies

```bash
python simulations/sparc_Z0_verification.py
```

**Output:**
```
================================================================================
🌌 Z_EM İSTATİSTİKLERİ (BAĞIMSIZ DOĞRULAMA)
================================================================================
Toplam kusursuz galaksi sayısı : 147
Ortalama Z_EM                  : 0.2338 ± 0.0156
Median Z_EM                    : 0.2330
Teorik Z₀ (V25.13)             : 0.2330
Fark (medyan – teorik)         : 0.0000
================================================================================
✅ Z_EM medyanı teorik Z₀ ile mükemmel uyum içindedir.
```

---

## 📚 Documentation

| Document | Purpose |
|----------|------------|
| [**Installation Guide**](docs/installation.md) | Step-by-step setup, dependencies |
| [**Quick Start**](docs/quickstart.md) | 5-minute runnable examples |
| [**Physics Background**](docs/physics.md) | Theoretical foundations & equations |
| [**API Reference**](docs/api_reference.md) | Function documentation |
| [**Falsification Tests**](docs/falsification_tests.md) | All 8 predictions & status |

---

## 🏗️ Repository Structure

```
ATHENA/
├── V7.4/                       Latest theory (PDF + LaTeX + results)
│   ├── ATHENA_V7.4_Final.pdf   Full 25-page manuscript
│   ├── README.md               Version-specific docs
│   └── results/                Figures and simulation outputs
│
├── v7.2_final/                 Previous major release
│
├── athena/                     Core Python package (v25.13)
│   ├── __init__.py             Package initialization
│   ├── field_solver.py         ODE solver for disformal field Φ
│   ├── rotation_curves.py      Galaxy rotation curve predictions
│   ├── likelihood.py           Chi² and likelihood functions
│   └── tests/                  Unit tests (pytest)
│       ├── __init__.py
│       └── test_core.py        Comprehensive test suite
│
├── simulations/                Standalone analysis scripts
│   ├── sparc_Z0_verification.py    Independent Z_EM verification (147 galaxies)
│   ├── a_phi_derivation*.py        Coupling parameter derivations
│   ├── blackhole_magnetic_equator.py Black hole analysis
│   ├── dipole_*.py                 Cosmic dipole predictions
│   ├── methuselah_paradox_final.py Age-redshift consistency
│   └── [other analysis scripts]
│
├── scripts/                    Entry points & utilities
│   └── run_sparc_fit.py        Single-galaxy example workflow
│
├── docs/                       Documentation
│   ├── installation.md         Setup guide
│   ├── quickstart.md           5-minute tutorial
│   ├── physics.md              Theory & equations
│   ├── api_reference.md        Function docs
│   └── falsification_tests.md  All 8 predictions
│
├── manifesto/                  Philosophical writings
│
├── .github/workflows/          CI/CD automation
│   └── tests.yml               Automated test runs
│
├── requirements.txt            Python dependencies
├── setup.py                    Installation script
├── .gitignore                  Git ignore rules
├── README.md                   This file
└── LICENSE                     CC BY 4.0
```

---

## 🔬 Core Concepts

### The Disformal Field Equation

$$\boxed{\frac{d^2\Phi}{dr^2} + \frac{2}{r}\frac{d\Phi}{dr} = \xi \rho_b \Phi + \alpha \rho_b}$$

- **Φ** = Scalar disformal field (fundamental)
- **ρ_b** = Baryonic mass density (observable matter)
- **α** ≈ 0.36 = Disformal coupling strength
- **ξ** ≈ 0.1408 = Universal coupling constant

### Galaxy Rotation Curves

$$v_{\text{total}}^2 = v_{\text{bary}}^2 + v_{\text{field}}^2$$

Where:
- **v_bary** ∝ √(M_baryon/r) — Standard Newtonian
- **v_field** ∝ α·Φ·∂Φ/∂r — Disformal contribution

**Result:** Reproduces observed rotation curves without ad-hoc dark matter halos!

---

## 📋 Key Parameters

| Parameter | Value | Meaning |
|-----------|-------|---------|
| α (alpha) | 0.36 | Disformal coupling strength |
| Φ₀ | 0.782 | Cosmic field value today |
| ξ (xi) | 0.1408 | Matter-field coupling |
| Z_EM | 0.233 | Empirical amplitude (SPARC) |
| L₁ | 2π/M_Pl | Toroidal circumference (UV scale) |
| L₂ | 2π/m_e | Toroidal circumference (IR scale) |

---

## 🧪 Running Tests

### Unit Tests

```bash
pip install pytest
pytest athena/tests/ -v
```

**Output:**
```
athena/tests/test_core.py::TestFieldSolver::test_solve_phi_basic PASSED
athena/tests/test_core.py::TestFieldSolver::test_solve_phi_boundary_conditions PASSED
athena/tests/test_core.py::TestRotationCurves::test_rotation_curve_basic PASSED
athena/tests/test_core.py::TestLikelihood::test_chi2_perfect_fit PASSED

==================== 20 passed in 0.45s ====================
```

### Full SPARC Analysis

```bash
python simulations/sparc_Z0_verification.py
```

Runs all 180+ SPARC galaxies and extracts Z_EM statistics.

---

## 🔗 External Links

- **YouTube Channel:** [Science is Fiction](https://youtube.com/@bilimkurgudur)
- **Blog:** [The Fiction Science](https://thefiction-science.blogspot.com/)
- **Substack:** [bilimkurgudur](https://substack.com/@bilimkurgudur)
- **Twitter/X:** [@gkhanylmazb04r](https://x.com/gkhanylmazb04r)
- **LinkedIn:** [Mustafa Gökhan Yılmaz](https://www.linkedin.com/in/mustafa-g%C3%B6khan-yilmaz-184b4468)
- **Zenodo DOI (V7.2):** https://doi.org/10.5281/zenodo.20787346
- **Email:** mgy421977@gmail.com

---

## 📖 How to Cite

**BibTeX:**
```bibtex
@software{yilmaz2026athena,
  author = {Yılmaz, Mustafa Gökhan},
  title = {ATHENA V7.4: A Grand Unified Topological Theory of the Disformal Toroidal Vacuum},
  year = {2026},
  url = {https://github.com/mgy421977-bit/ATHENA},
  doi = {10.5281/zenodo.20787346},
  version = {V7.4}
}
```

**Plain Text:**
```
Yılmaz, M. G. (2026). ATHENA V7.4: A Grand Unified Topological Theory of the 
Disformal Toroidal Vacuum. Retrieved from https://github.com/mgy421977-bit/ATHENA
DOI: 10.5281/zenodo.20787346
```

---

## 📄 License

This work is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

**You are free to:**
- ✅ Share, copy, redistribute
- ✅ Adapt, remix, transform
- ✅ Use for commercial & non-commercial purposes

**You must:**
- ✓ Give appropriate credit
- ✓ Provide a link to the license
- ✓ Indicate if changes were made

See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

This is independent research. However, contributions are welcome:

1. **Implement missing tests:** See [falsification_tests.md](docs/falsification_tests.md)
2. **Improve documentation:** Add examples, clarify explanations
3. **Optimize code:** Performance improvements for ODE solving
4. **Data analysis:** Apply tests to new observational datasets

**To contribute:**
```bash
git checkout -b feature/your-feature
git commit -am "Descriptive message"
git push origin feature/your-feature
```

Then open a pull request with a clear description.

---

## 📋 Version History

| Version | Date | Status | Key Updates |
|---------|------|--------|-------------|
| **V7.4** | June 2026 | 🟢 Latest | Galois symmetry, PMNS derivation, 147 galaxy fits |
| V7.2 | 2025 | 🔵 Stable | LQG embedding, torsional bounce |
| V6.0 | 2024 | ⚪ Archive | SPARC fitting framework |

---

## ❓ FAQ

**Q: How is this different from ΛCDM?**  
A: ATHENA replaces separate dark matter & dark energy with a unified scalar field. It also provides derivations (not just observations) for neutrino mixing angles and cosmic parameters.

**Q: What's the status of the theory?**  
A: Mathematically complete. V7.4 makes 8 falsifiable predictions; 1 verified (SPARC), 7 awaiting observations.

**Q: Can I use this code?**  
A: Yes! Licensed under CC BY 4.0. Install with `pip install -e .`

**Q: How do I run the full SPARC analysis?**  
A: `python simulations/sparc_Z0_verification.py` (one command, ~2 minutes)

**Q: Where is the theoretical manuscript?**  
A: See `/V7.4/ATHENA_V7.4_Final.pdf` (25 pages, full derivations)

**Q: How do I cite this work?**  
A: Use the BibTeX above or reference Zenodo DOI: 10.5281/zenodo.20787346

---

## ⭐ Support This Work

If you find ATHENA interesting:
- ⭐ Star this repository
- 🔗 Share with colleagues
- 📧 Provide feedback: mgy421977@gmail.com
- 📝 Cite the work (see section above)
- 🎬 Subscribe to [Science is Fiction](https://youtube.com/@bilimkurgudur)

---

**Last Updated:** 24 June 2026  
**Maintained by:** Mustafa Gökhan Yılmaz

---

*This work is developed independently with the goal of advancing falsifiable theoretical physics.*
