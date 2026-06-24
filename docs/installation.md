# docs/installation.md

# Installation Guide

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/mgy421977-bit/ATHENA.git
cd ATHENA
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

**Option A: Basic Installation**

```bash
pip install -r requirements.txt
```

**Option B: Development Installation (with testing tools)**

```bash
pip install -e .[dev]
```

**Option C: From setup.py**

```bash
pip install -e .
```

## Verify Installation

```bash
python3 -c "from athena.field_solver import solve_phi; print('✓ ATHENA imported successfully!')"
```

## System Requirements

- **Python:** 3.8 or higher
- **OS:** macOS, Linux, Windows
- **Memory:** 2GB RAM minimum (for SPARC simulations: 4GB+ recommended)
- **Disk Space:** ~500MB (including SPARC data cache)

## Dependencies

| Package    | Version  | Purpose                          |
|-----------|----------|----------------------------------|
| numpy     | ≥1.21.0  | Numerical arrays & math         |
| scipy     | ≥1.7.0   | ODE solving, interpolation      |
| pandas    | ≥1.3.0   | Data handling (SPARC galaxies)  |
| matplotlib| ≥3.4.0   | Plotting & visualization        |

### Development Dependencies

- **pytest** ≥6.0 — Unit testing
- **black** ≥21.0 — Code formatting
- **flake8** ≥3.9 — Linting

## Troubleshooting

### Issue: ModuleNotFoundError

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Reinstall the package
pip install -e .
```

### Issue: scipy.integrate.solve_ivp fails

Update scipy:
```bash
pip install --upgrade scipy
```

### Issue: Slow SPARC downloads

The SPARC data (160MB) is downloaded automatically. To pre-download:

```bash
cd simulations
python3 -c "from sparc_Z0_verification import download_sparc; download_sparc()"
```

## Uninstall

```bash
pip uninstall athena-physics
```

---

**Next:** [Quick Start Guide](quickstart.md)
