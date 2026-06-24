# athena/rotation_curves.py
"""
Rotation curve predictions for the ATHENA model.
Computes observable velocities from the disformal field solution.
"""
import numpy as np


def rotation_curve(r, phi, dphi, M_baryon, v_esc=420.0, r_s=5.0, v_crit=50.0, alpha=0.36):
    """
    Compute the total rotation curve from the disformal field.
    
    Args:
        r (np.ndarray): Radial coordinates (kpc)
        phi (np.ndarray): Disformal field values
        dphi (np.ndarray): Disformal field derivatives
        M_baryon (np.ndarray): Enclosed baryonic mass
        v_esc (float): Escape velocity parameter (km/s)
        r_s (float): Scale radius (kpc)
        v_crit (float): Critical velocity (km/s)
        alpha (float): Disformal coupling parameter
    
    Returns:
        np.ndarray: Total rotation velocity at each radius
    """
    # Baryonic contribution
    v_bary = np.sqrt(np.maximum(M_baryon / r, 0) + 1e-6)
    
    # Disformal field contribution (simplified)
    v_extra = alpha * phi * dphi * np.tanh(r / r_s) * (v_esc / 100.0)
    
    # Total velocity
    v_total = np.sqrt(v_bary**2 + v_extra**2)
    
    return v_total
