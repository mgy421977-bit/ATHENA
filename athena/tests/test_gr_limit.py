# athena/tests/test_gr_limit.py
import numpy as np
from athena.field_solver import solve_phi

def test_gr_limit():
    """
    Tests if the ATHENA model correctly reduces to GR in the limit alpha -> 0.
    """
    # Input data (radial points and an arbitrary density profile)
    r = np.linspace(0.1, 100, 100)
    rho_b = np.ones_like(r) * 1e-10
    
    # Set the coupling constant to zero
    alpha = 0.0
    
    # Solve the modified field equation
    phi, dphi = solve_phi(r, rho_b, alpha=alpha)
    
    # For alpha -> 0, the solution should be constant (Phi = Phi0) and its derivative zero.
    is_phi_constant = np.allclose(phi, phi[0], atol=1e-8)
    is_dphi_zero = np.allclose(dphi, 0.0, atol=1e-8)
    
    assert is_phi_constant and is_dphi_zero, "GR limit test failed!"
    print("GR limit test passed.")

if __name__ == "__main__":
    test_gr_limit()
