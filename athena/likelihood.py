# athena/likelihood.py
import numpy as np

def chi2(obs, model, err):
    """
    Calculates the chi-squared statistic.
    """
    return np.sum(((obs - model) / err)**2)

def log_likelihood_sparc(v_obs, v_pred, v_err):
    """
    Calculates the Gaussian log-likelihood for SPARC rotation curves.
    """
    chi2_val = chi2(v_obs, v_pred, v_err)
    return -0.5 * chi2_val
