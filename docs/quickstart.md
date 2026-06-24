# Quick Start Guide

## 5-Minute Demo

### 1. Run Your First SPARC Fit

```bash
cd ATHENA
python scripts/run_sparc_fit.py
```

**Expected Output:**
```
============================================================
  ATHENA SPARC Demo – Single Galaxy Fit
============================================================
Loading galaxy: A121
Downloading SPARC data...
Extracting archive...
Chi² = 45.32 for 28 data points
Demo completed. Extend this script for full SPARC sample.
```

### 2. Verify the Field Solver

```python
import numpy as np
from athena.field_solver import solve_phi

# Create a simple density profile
r = np.linspace(0.1, 100, 100)  # radii in kpc
rho_b = np.exp(-r / 20)          # exponential density

# Solve the disformal field
phi, dphi = solve_phi(r, rho_b, alpha=0.36)

print(f"Field at r=10 kpc: Φ = {phi[50]:.4f}")
print(f"Derivative: dΦ/dr = {dphi[50]:.4f}")
```

### 3. Compute a Rotation Curve

```python
import matplotlib.pyplot as plt
from athena.rotation_curves import rotation_curve

# Compute enclosed mass
M_baryon = np.cumsum(rho_b) * np.diff(r, prepend=r[0])

# Rotation curve
v_rot = rotation_curve(r, phi, dphi, M_baryon)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(r, v_rot, 'b-', linewidth=2, label='ATHENA Prediction')
plt.xlabel('Radius (kpc)')
plt.ylabel('Rotation Velocity (km/s)')
plt.title('Galaxy Rotation Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 4. Independent Z_EM Verification

```bash
python simulations/sparc_Z0_verification.py
```

This runs the full SPARC sample (180+ galaxies) and extracts the empirical Z_EM parameter:
```
================================================================================
🎯 Z_EM İSTATİSTİKLERİ (BAĞIMSIZ DOĞRULAMA)
================================================================================
Toplam kusursuz galaksi sayısı : 147
Ortalama Z_EM                  : 0.2338 ± 0.0156
Median Z_EM                    : 0.2330
Teorik Z₀ (V25.13)             : 0.2330
Fark (medyan – teorik)         : 0.0000
================================================================================
```

---

## Key Concepts

### The Disformal Field (Φ)

- Scalar field living on a toroidal vacuum manifold T²
- Couples to baryonic matter via the equation:
  ```
  d²Φ/dr² + (2/r)·dΦ/dr = ξ·ρ_b·Φ + α·ρ_b
  ```
- Solves for with `solve_phi(r, rho_b)`

### Galaxy Rotation Curves

- Observed: v_obs (from SPARC database)
- Predicted: v_model = f(Φ, dΦ/dr, M_baryon)
- Goodness of fit: χ² statistic

### Parameters

| Parameter | Value  | Meaning                      |
|-----------|--------|------------------------------|
| α (alpha) | 0.36   | Disformal coupling strength  |
| Φ₀        | 0.782  | Cosmic field value (today)   |
| ξ (xi)    | 0.1408 | Matter-field coupling const  |
| Z_EM      | 0.233  | Empirical amplitude (SPARC)  |

---

## Next Steps

1. **Run Tests**: `pytest athena/tests/`
2. **Explore Physics**: Read [physics.md](physics.md)
3. **API Reference**: See [api_reference.md](api_reference.md)
4. **Falsification Tests**: Check [falsification_tests.md](falsification_tests.md)

---

**Questions?** Contact: mgy421977@gmail.com
