# athena/field_solver.py
import numpy as np
from scipy.integrate import solve_ivp

def solve_phi(r, rho_b, alpha=0.36, Phi0=0.782, xi=0.1408):
    """
    Solves the radial Phi field equation for a given baryonic density profile.
    
    Args:
        r (np.ndarray): Radial coordinates (kpc).
        rho_b (np.ndarray): Baryonic density profile.
        alpha (float): Disformal coupling parameter.
        Phi0 (float): Current cosmic value of the Phi field.
        xi (float): Universal coupling constant.

    Returns:
        tuple: (phi, dphi_dr) solutions at coordinates r.
    """
    def ode(r, y):
        phi, dphi = y
        # Equation: d²phi/dr² + (2/r)*dphi/dr = xi*rho_b*phi + alpha*rho_b
        d2phi = - (2 / r) * dphi + xi * rho_b_interp(r) * phi + alpha * rho_b_interp(r)
        return [dphi, d2phi]

    # Interpolate the density profile to be callable at any r
    rho_b_interp = lambda x: np.interp(x, r, rho_b, left=0, right=0)

    r_min = max(r[0], 1e-6)  # Avoid singularity at r=0
    sol = solve_ivp(ode, (r_min, r[-1]), [Phi0, 0.0], t_eval=r, method='RK45', rtol=1e-6)
    return sol.y[0], sol.y[1]
