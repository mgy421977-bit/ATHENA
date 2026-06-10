import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from athena.field_solver import solve_phi

def test_gr_limit():
    r = np.linspace(0.1, 100, 100)
    rho_b = np.ones_like(r) * 1e-10
    alpha = 0.0
    phi, dphi = solve_phi(r, rho_b, alpha=alpha)
    is_phi_constant = np.allclose(phi, phi[0], atol=1e-8)
    is_dphi_zero = np.allclose(dphi, 0.0, atol=1e-8)
    assert is_phi_constant and is_dphi_zero, "GR limit test failed!"
    print("GR limit test passed.")

if __name__ == "__main__":
    test_gr_limit()
