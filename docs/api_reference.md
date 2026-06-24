# API Reference

## athena.field_solver

### `solve_phi(r, rho_b, alpha=0.36, Phi0=0.782, xi=0.1408)`

Solves the radial disformal field equation.

**Equation:**
```
d²Φ/dr² + (2/r)·dΦ/dr = ξ·ρ_b·Φ + α·ρ_b
```

**Parameters:**
- `r` (np.ndarray): Radial coordinates in kpc. Must be > 0, shape (N,)
- `rho_b` (np.ndarray): Baryonic density profile in M☉/kpc³. Shape (N,), same as r
- `alpha` (float, optional): Disformal coupling parameter. Default: 0.36
- `Phi0` (float, optional): Cosmic field value today. Default: 0.782
- `xi` (float, optional): Universal coupling constant. Default: 0.1408

**Returns:**
- `phi` (np.ndarray): Field values Φ(r), shape (N,)
- `dphi_dr` (np.ndarray): Field derivatives dΦ/dr, shape (N,)

**Raises:**
- `ValueError`: If r and rho_b have different lengths or r contains non-positive values
- `RuntimeError`: If ODE solver fails to converge

**Example:**
```python
import numpy as np
from athena.field_solver import solve_phi

r = np.linspace(0.1, 100, 100)
rho_b = np.exp(-r / 20)
phi, dphi = solve_phi(r, rho_b)
```

**Notes:**
- Uses RK45 integrator from scipy with tight tolerance (rtol=1e-6)
- Singularity at r=0 is regularized by starting at r_min = max(r[0], 1e-6)
- Boundary condition: dΦ/dr|_min = 0 (reflecting/regular solution)

---

## athena.rotation_curves

### `rotation_curve(r, phi, dphi, M_baryon, v_esc=420.0, r_s=5.0, v_crit=50.0, alpha=0.36)`

Computes the total observable rotation curve from field solution.

**Formula:**
```
v_total² = v_baryon² + v_field²
```

**Parameters:**
- `r` (np.ndarray): Radial coordinates (kpc)
- `phi` (np.ndarray): Disformal field values from solve_phi()
- `dphi` (np.ndarray): Field derivatives from solve_phi()
- `M_baryon` (np.ndarray): Enclosed baryonic mass (M☉)
- `v_esc` (float): Escape velocity amplitude (km/s). Default: 420.0
- `r_s` (float): Scale radius (kpc). Default: 5.0
- `v_crit` (float): Critical velocity (km/s). Default: 50.0
- `alpha` (float): Disformal coupling. Default: 0.36

**Returns:**
- `v_total` (np.ndarray): Rotation velocity at each radius (km/s), shape same as r

**Example:**
```python
M_baryon = np.cumsum(rho_b)  # Enclosed mass
v_rot = rotation_curve(r, phi, dphi, M_baryon)
```

---

## athena.likelihood

### `chi2(v_obs, v_model, err)`

Computes chi-squared statistic.

**Formula:**
```
χ² = Σ [(v_obs - v_model) / err]²
```

**Parameters:**
- `v_obs` (np.ndarray): Observed velocities (km/s)
- `v_model` (np.ndarray): Model predictions (km/s)
- `err` (np.ndarray): Observational uncertainties (km/s)

**Returns:**
- `chi2_value` (float): Chi-squared statistic

**Example:**
```python
from athena.likelihood import chi2

chi2_val = chi2(v_obs, v_predicted, v_errors)
print(f"χ² = {chi2_val:.2f}")
```

### `reduced_chi2(v_obs, v_model, err, n_params)`

Computes reduced chi-squared (chi²/dof).

**Formula:**
```
χ²_red = χ² / (N - n_params)
```

**Parameters:**
- `v_obs`, `v_model`, `err`: Same as chi2()
- `n_params` (int): Number of fitted parameters

**Returns:**
- `reduced_chi2` (float): Chi²/dof

**Example:**
```python
red_chi2 = reduced_chi2(v_obs, v_predicted, v_errors, n_params=5)
print(f"χ²/dof = {red_chi2:.3f}")
```

**Good Fit Criterion:** χ²/dof ≈ 1.0 (indicates data are well-described by model)

### `log_likelihood_sparc(v_obs, v_pred, v_err)`

Gaussian log-likelihood for SPARC fits.

**Formula:**
```
ln(L) = -0.5 · χ²
```

**Parameters:** Same as chi2()

**Returns:**
- `log_likelihood` (float): Log probability of data given model

---

## Module Imports

```python
# Import entire module
import athena

# Or import specific functions
from athena.field_solver import solve_phi
from athena.rotation_curves import rotation_curve
from athena.likelihood import chi2, reduced_chi2, log_likelihood_sparc
```

---

## Data Structures

All functions expect **NumPy arrays**:
```python
import numpy as np

# ✅ Correct
r = np.linspace(0.1, 100, 100)

# ❌ Wrong
r = list(range(100))  # Use np.array() to convert
```

---

## Performance Tips

1. **Vectorize:** Always pass arrays to functions, not loops
2. **Memory:** SPARC simulations load 160MB data cache (one-time)
3. **Speed:** ODE solving ~100ms for 100 radial points

---

## Error Handling

```python
try:
    phi, dphi = solve_phi(r, rho_b)
except ValueError as e:
    print(f"Input error: {e}")
except RuntimeError as e:
    print(f"ODE solver failed: {e}")
```

---

**For questions:** See [physics.md](physics.md) or contact mgy421977@gmail.com
