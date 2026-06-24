# athena/field_solver.py
"""
Disformal field solver for the ATHENA model.
Solves the radial field equation: d²Φ/dr² + (2/r)dΦ/dr = ξρ_b·Φ + α·ρ_b
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d


def solve_phi(r, rho_b, alpha=0.36, Phi0=0.782, xi=0.1408):
    """
    Solves the radial Phi field equation for a given baryonic density profile.
    
    The disformal field equation emerges from the toroidal vacuum geometry:
    d²Φ/dr² + (2/r)·dΦ/dr = ξ·ρ_b·Φ + α·ρ_b
    
    This ODE describes how the scalar field couples to matter.
    The singularity at r=0 is regularized by starting integration at r_min.
    
    Args:
        r (np.ndarray): Radial coordinates (kpc). Must be positive.
        rho_b (np.ndarray): Baryonic density profile. Same shape as r.
        alpha (float): Disformal coupling parameter (dimensionless).
                      Controls strength of field-to-matter coupling.
        Phi0 (float): Current cosmic value of the Phi field (~0.782).
                     Serves as boundary condition at r_min.
        xi (float): Universal coupling constant (~0.1408).
                   Scales the linear feedback term ξ·ρ_b·Φ.
    
    Returns:
        tuple: (phi, dphi_dr) solutions at coordinates r
            phi (np.ndarray): Field values Φ(r)
            dphi_dr (np.ndarray): Field derivatives dΦ/dr
    
    Raises:
        ValueError: If r contains non-positive values or rho_b has wrong shape.
    
    Notes:
        - Uses RK45 Runge-Kutta integrator with tight tolerance (rtol=1e-6)
        - Boundary condition: dΦ/dr|_min = 0 (reflecting at inner boundary)
        - Singularity at r=0 avoided by starting at r_min = max(r[0], 1e-6)
    """
    # Input validation
    if len(r) != len(rho_b):
        raise ValueError("r and rho_b must have the same length")
    
    if np.any(r <= 0):
        raise ValueError("All radial coordinates must be positive")
    
    # Create interpolation function for density
    # Use extrapolation: zero density outside data range
    rho_b_interp = interp1d(
        r, rho_b, kind='cubic', bounds_error=False,
        fill_value=0.0
    )
    
    # Regularize singularity at r=0 by starting integration at r_min
    # Physical justification: the toroidal geometry has finite size
    r_min = max(r[0], 1e-6)
    
    def ode_system(r_current, y):
        """
        ODE system for scipy.integrate.solve_ivp
        y = [Φ, dΦ/dr]
        Returns: [dΦ/dr, d²Φ/dr²]
        """
        phi_val, dphi_val = y
        
        # Evaluate density at current radius
        rho_val = rho_b_interp(r_current)
        
        # Second derivative from the field equation:
        # d²Φ/dr² = -(2/r)·dΦ/dr + ξ·ρ_b·Φ + α·ρ_b
        d2phi = (
            -(2.0 / (r_current + 1e-10)) * dphi_val +
            xi * rho_val * phi_val +
            alpha * rho_val
        )
        
        return [dphi_val, d2phi]
    
    # Boundary conditions at r_min:
    # Φ(r_min) = Φ_0 (cosmic value)
    # dΦ/dr|_min = 0 (reflecting boundary / regularity condition)
    y0 = [Phi0, 0.0]
    
    # Solve ODE from r_min to r_max
    sol = solve_ivp(
        ode_system,
        (r_min, r[-1]),
        y0,
        t_eval=r,
        method='RK45',
        rtol=1e-6,
        atol=1e-9,
        dense_output=False
    )
    
    if not sol.success:
        raise RuntimeError(f"ODE solver failed: {sol.message}")
    
    return sol.y[0], sol.y[1]
