import pytest
import numpy as np
from athena.field_solver import solve_phi
from athena.rotation_curves import rotation_curve
from athena.likelihood import chi2, reduced_chi2


class TestFieldSolver:
    """Test suite for the disformal field solver."""
    
    def test_solve_phi_basic(self):
        """Test basic field solver execution."""
        r = np.linspace(0.1, 100, 50)
        rho_b = np.exp(-r / 10)
        
        phi, dphi = solve_phi(r, rho_b)
        
        assert len(phi) == len(r)
        assert len(dphi) == len(r)
        assert np.all(np.isfinite(phi))
        assert np.all(np.isfinite(dphi))
    
    def test_solve_phi_boundary_conditions(self):
        """Test that boundary conditions are satisfied."""
        r = np.linspace(0.1, 50, 100)
        rho_b = np.ones_like(r) * 0.1
        Phi0 = 0.782
        
        phi, dphi = solve_phi(r, rho_b, Phi0=Phi0)
        
        # Check initial condition
        assert np.isclose(phi[0], Phi0, rtol=0.1)
        # Check derivative at boundary
        assert np.isclose(dphi[0], 0.0, atol=0.1)
    
    def test_solve_phi_parameter_variation(self):
        """Test solver with different coupling parameters."""
        r = np.linspace(0.1, 50, 50)
        rho_b = np.exp(-r / 10)
        
        phi1, _ = solve_phi(r, rho_b, alpha=0.36)
        phi2, _ = solve_phi(r, rho_b, alpha=0.50)
        
        # Different alpha should produce different fields
        assert not np.allclose(phi1, phi2)
    
    def test_solve_phi_invalid_input(self):
        """Test error handling for invalid inputs."""
        r = np.linspace(0.1, 50, 50)
        rho_b = np.linspace(0.1, 1, 60)  # Wrong size
        
        with pytest.raises(ValueError):
            solve_phi(r, rho_b)
    
    def test_solve_phi_negative_radius(self):
        """Test error handling for negative radii."""
        r = np.linspace(-10, 50, 50)
        rho_b = np.exp(-r / 10)
        
        with pytest.raises(ValueError):
            solve_phi(r, rho_b)


class TestRotationCurves:
    """Test suite for rotation curve calculations."""
    
    def test_rotation_curve_basic(self):
        """Test basic rotation curve computation."""
        r = np.linspace(1, 100, 50)
        phi = np.ones_like(r) * 0.782
        dphi = np.zeros_like(r)
        M_baryon = r**2
        
        v = rotation_curve(r, phi, dphi, M_baryon)
        
        assert len(v) == len(r)
        assert np.all(np.isfinite(v))
        assert np.all(v >= 0)
    
    def test_rotation_curve_increasing_mass(self):
        """Test that velocity increases with enclosed mass."""
        r = np.linspace(1, 100, 50)
        phi = np.ones_like(r) * 0.782
        dphi = np.zeros_like(r)
        
        M1 = r**2
        M2 = r**2 * 2  # Double mass
        
        v1 = rotation_curve(r, phi, dphi, M1)
        v2 = rotation_curve(r, phi, dphi, M2)
        
        # Velocity should generally increase with mass
        assert np.mean(v2) > np.mean(v1)
    
    def test_rotation_curve_field_contribution(self):
        """Test that field derivatives affect rotation curve."""
        r = np.linspace(1, 100, 50)
        phi = np.ones_like(r) * 0.782
        M_baryon = r**2
        
        dphi1 = np.zeros_like(r)
        dphi2 = np.ones_like(r) * 0.01
        
        v1 = rotation_curve(r, phi, dphi1, M_baryon)
        v2 = rotation_curve(r, phi, dphi2, M_baryon)
        
        # Different field derivatives should affect velocity
        assert not np.allclose(v1, v2)


class TestLikelihood:
    """Test suite for chi-squared and likelihood calculations."""
    
    def test_chi2_perfect_fit(self):
        """Test chi2 for perfect model-data agreement."""
        v_obs = np.array([100, 150, 200, 250, 300])
        v_model = v_obs.copy()
        err = np.ones_like(v_obs) * 10
        
        chi2_val = chi2(v_obs, v_model, err)
        
        assert np.isclose(chi2_val, 0.0)
    
    def test_chi2_known_value(self):
        """Test chi2 with known values."""
        v_obs = np.array([100, 150, 200])
        v_model = np.array([105, 145, 195])
        err = np.array([10, 10, 10])
        
        chi2_val = chi2(v_obs, v_model, err)
        expected = (5/10)**2 + (-5/10)**2 + (-5/10)**2
        
        assert np.isclose(chi2_val, expected)
    
    def test_reduced_chi2(self):
        """Test reduced chi2 calculation."""
        v_obs = np.linspace(100, 300, 50)
        v_model = v_obs + np.random.normal(0, 5, 50)
        err = np.ones_like(v_obs) * 5
        n_params = 3
        
        chi2_val = chi2(v_obs, v_model, err)
        red_chi2_val = reduced_chi2(v_obs, v_model, err, n_params)
        
        dof = len(v_obs) - n_params
        assert np.isclose(red_chi2_val, chi2_val / dof)
    
    def test_chi2_array_inputs(self):
        """Test chi2 with array inputs."""
        n = 100
        v_obs = np.random.normal(150, 30, n)
        v_model = np.random.normal(150, 30, n)
        err = np.ones(n) * 10
        
        chi2_val = chi2(v_obs, v_model, err)
        
        assert chi2_val > 0
        assert np.isfinite(chi2_val)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
