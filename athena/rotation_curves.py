# athena/rotation_curves.py
import numpy as np

def rotation_curve(r, phi, dphi, M_baryon):
    """
    Calculates the total circular velocity from baryonic matter and the Phi field.

    Args:
        r (np.ndarray): Radial coordinates (kpc).
        phi (np.ndarray): Solution of the Phi field.
        dphi (np.ndarray): First derivative of the Phi field.
        M_baryon (np.ndarray): Cumulative enclosed baryonic mass (solar masses).

    Returns:
        np.ndarray: Total circular velocity (km/s).
    """
    G = 4.302e-3  # Gravitational constant in (km/s)^2 * kpc / Msun
    v_baryon_sq = G * M_baryon / r
    v_phi_sq = - r * dphi
    return np.sqrt(v_baryon_sq + v_phi_sq)
