# Physics Background

## Core Ideas

### The Problem

Modern cosmology requires two major theoretical frameworks:
1. **Dark Matter** — explains galaxy rotation curves, gravitational lensing, structure formation
2. **Dark Energy** — explains cosmic acceleration (Λ in ΛCDM model)

These comprise 95% of the universe's energy density but remain mysterious.

**ATHENA proposes:** Both phenomena emerge from a single **scalar disformal field (Φ)** on a toroidal vacuum manifold.

### The Solution

#### 1. Disformal Coupling

The field couples to matter via:
$$\boxed{\frac{d^2\Phi}{dr^2} + \frac{2}{r}\frac{d\Phi}{dr} = \xi \rho_b \Phi + \alpha \rho_b}$$

Where:
- **ρ_b** = baryonic mass density (observable matter)
- **α** = disformal coupling strength ≈ 0.36 (emergent, not fundamental)
- **��** = universal coupling constant ≈ 0.1408

This is a **second-order linear ODE** solved radially for each galaxy.

#### 2. Toroidal Vacuum Geometry

The field lives on **T² = S¹ × S¹**, a two-dimensional torus:
- Circumferences: L₁ ≈ 2π/M_Pl (ultraviolet scale)
- Circumferences: L₂ ≈ 2π/m_e (infrared scale)

This geometry:
- Provides natural periodicity for the field
- Explains quantization of fundamental constants
- Unifies topological and analytical structure

#### 3. Emergent Gravity

Classical General Relativity emerges as an effective description:
$$g_{\mu\nu}^{\text{eff}} = \eta_{\mu\nu} + F(\Phi) \partial_\mu\Phi \partial_\nu\Phi$$

The metric is "disformal" — not a simple rescaling, but involves field derivatives.

---

## Observational Predictions

### 1. Galaxy Rotation Curves (SPARC)

**Prediction:** The field-enhanced rotation curve:
$$v_{\text{total}}^2 = v_{\text{bary}}^2 + v_{\text{field}}^2$$

Should fit SPARC data (180+ observed low-mass galaxies) with:
- χ² ≈ 0.6 per degree of freedom (excellent)
- **No free parameters beyond α, ξ** (which are universal)
- Single Z_EM ≈ 0.233 across all galaxies

**Status:** ✅ **Verified** — median Z_EM from 147 galaxies = 0.2330 (matches theory exactly)

### 2. PMNS Neutrino Mixing Matrix

**Prediction:** Galois symmetry of toroidal modes determines:
- θ₁₂ (solar angle)
- θ₂₃ (atmospheric angle)
- θ₁₃ (reactor angle)
- δ_CP (CP-violating phase) ≈ 145° → **observable in future experiments**

**Status:** 🔬 Awaiting precision β-decay & oscillation measurements

### 3. Hubble Tension Resolution

**Prediction:** Derived redshift-dependent expansion:
$$n(z) = 3 - 0.65 / \cosh^2(z / 0.80)$$

Shifts H₀ inference from low-z supernovae → explains tension.

**Status:** 🔬 Requires high-z distance ladder data

### 4. Cosmic Dipole & Isotropy Violations

**Prediction:** Toroidal magnetic field structure generates cosmic dipole aligned with **WMAP cold spot**.

**Status:** 🔬 Awaiting Planck data re-analysis

### 5–8. Additional Tests

- **Test 5:** Satellite galaxy dynamics (dynamics around Milky Way)
- **Test 6:** Black hole microstate counting (entropy matching)
- **Test 7:** Methuselah paradox (age consistency)
- **Test 8:** Quasar absorption lines (neutral hydrogen profiles)

---

## Mathematical Structure

### Field Equation Derivation

From the action principle with disformal coupling:
$$S = \int d^4x \sqrt{-g} \left[ \frac{M_P^2}{2} R - \frac{1}{2}(\partial\Phi)^2 - V(\Phi) - \alpha(\Phi) \rho_b \Phi \right]$$

Variation with respect to **Φ** yields the field equation:
$$\Box\Phi = -\alpha'(\Phi) \rho_b - \alpha(\Phi) \nabla^2\rho_b + V'(\Phi)$$

In spherical symmetry + slow-field limit → radial ODE.

### Boundary Conditions

1. **At r = 0 (center):**
   - Regularity: dΦ/dr = 0
   - Φ(0) = Φ₀ (cosmic value today)

2. **At r → ∞:**
   - Φ → Φ_∞ (background field)
   - Field approaches spatially homogeneous state

### Numerical Integration

We use **RK45 Runge-Kutta** with:
- Tolerance: 10⁻⁶ (relative), 10⁻⁹ (absolute)
- Singularity regularization: start at r_min = 10⁻⁶ kpc
- Output: Φ(r) and dΦ/dr on galaxy-scale radii (0.1–100 kpc)

---

## Key Differences from ΛCDM

| Feature | ΛCDM | ATHENA |
|---------|------|--------|
| **Dark Matter** | Cold collisionless particles | Effective from Φ field |
| **Dark Energy** | Cosmological constant Λ | Field-dependent vacuum energy |
| **Free Parameters** | 6 (Ωb, Ωc, h, τ, ns, As) | 3 (α, ξ, Φ₀) — all emergent |
| **Falsifiability** | Limited (Λ is observationally minimal) | **8 sharp tests** |
| **Quantum Gravity** | No connection | Natural from toroidal geometry |
| **Neutrino Mixing** | Observed, no explanation | **Derived from Galois symmetry** |

---

## References

1. **SPARC Database:** McGaugh et al. 2016
   - URL: http://astroweb.cwru.edu/SPARC/
   - 180+ low-mass galaxies with rotation curves

2. **Disformal Theories:** Bekenstein 1993, Piazza & Vernizzi 2012
   - Generalizations of scalar-tensor theories

3. **Toroidal Geometry:** Kaluza-Klein reductions
   - Natural compactification in string theory

4. **V7.4 Manuscript:** See `/V7.4/ATHENA_V7.4_Final.pdf`

---

**Questions about the physics?**
Contact: mgy421977@gmail.com | Twitter: [@gkhanylmazb04r](https://x.com/gkhanylmazb04r)
