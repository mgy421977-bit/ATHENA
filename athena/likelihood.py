# athena/likelihood.py
"""
Likelihood and chi-squared calculations for ATHENA model fits.
"""
import numpy as np


def chi2(v_obs, v_model, err):
    """
    Compute chi-squared statistic between observed and model velocities.
    
    Args:
        v_obs (np.ndarray): Observed rotation velocities (km/s)
        v_model (np.ndarray): Model-predicted velocities (km/s)
        err (np.ndarray): Observational uncertainties (km/s)
    
    Returns:
        float: Chi-squared value
    """
    residuals = (v_obs - v_model) / err
    chi2_val = np.sum(residuals**2)
    return chi2_val


def reduced_chi2(v_obs, v_model, err, n_params):
    """
    Compute reduced chi-squared (chi²/dof).
    
    Args:
        v_obs (np.ndarray): Observed velocities
        v_model (np.ndarray): Model velocities
        err (np.ndarray): Uncertainties
        n_params (int): Number of fit parameters
    
    Returns:
        float: Reduced chi-squared
    """
    chi2_val = chi2(v_obs, v_model, err)
    dof = len(v_obs) - n_params
    if dof <= 0:
        return np.inf
    return chi2_val / dof


def log_likelihood_sparc(v_obs, v_pred, v_err):
    """
    Calculates the Gaussian log-likelihood for SPARC rotation curves.
    """
    chi2_val = chi2(v_obs, v_pred, v_err)
    return -0.5 * chi2_val
