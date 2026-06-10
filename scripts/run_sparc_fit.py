#!/usr/bin/env python3
# scripts/run_sparc_fit.py
"""
Minimal example: Load a SPARC galaxy, solve Phi field, compute rotation curve,
and calculate chi-squared compared to observed data.
"""
import numpy as np
import pandas as pd
import os, urllib.request, zipfile
from scipy.optimize import curve_fit
import sys

# Add parent directory to path so we can import athena modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from athena.field_solver import solve_phi
from athena.rotation_curves import rotation_curve
from athena.likelihood import chi2

# =============================================================================
# Data download helpers (same as in V17.1)
# =============================================================================
SPARC_URL = "https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1"
ZIP_PATH = "Rotmod_LTG.zip"
DATA_DIR = "Rotmod_LTG_Data"

def download_sparc():
    if not os.path.exists(ZIP_PATH):
        print("Downloading SPARC data...")
        urllib.request.urlretrieve(SPARC_URL, ZIP_PATH)
    if not os.path.exists(DATA_DIR):
        with zipfile.ZipFile(ZIP_PATH, "r") as z:
            z.extractall(DATA_DIR)
    for root, dirs, files in os.walk(DATA_DIR):
        if any(f.endswith(".dat") for f in files):
            return root
    return DATA_DIR

def load_galaxy(gal_name, data_dir):
    file_path = os.path.join(data_dir, f"{gal_name}_rotmod.dat")
    if not os.path.exists(file_path):
        return None
    data = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 6:
                try:
                    data.append([float(x) for x in parts[:6]])
                except:
                    continue
    if len(data) < 5:
        return None
    df = pd.DataFrame(data, columns=["r", "vobs", "err", "vgas", "vdisk", "vbul"])
    df = df[df["err"] > 0].copy()
    df["err"] = np.clip(df["err"], 1.0, None)
    return df if len(df) >= 5 else None

# =============================================================================
# Main fitting routine for one galaxy
# =============================================================================
def fit_galaxy(df, alpha=0.36, Phi0=0.782, xi=0.1408):
    r = df["r"].values
    vobs = df["vobs"].values
    err = df["err"].values
    vgas = df["vgas"].values
    vdisk = df["vdisk"].values
    vbul = df["vbul"].values

    # Total baryonic density (very crude approximation: mass per unit volume)
    # In a realistic model we would reconstruct rho_b from the mass profiles.
    # Here we just use a placeholder: rho_b ~ (M_baryon enclosed) / r^3
    M_baryon = np.cumsum(vgas**2 + vdisk**2 + vbul**2)  # dummy
    rho_b = M_baryon / (r**3 + 1e-6)

    # Solve Phi field
    phi, dphi = solve_phi(r, rho_b, alpha=alpha, Phi0=Phi0, xi=xi)

    # Compute rotation curve
    vpred = rotation_curve(r, phi, dphi, M_baryon)

    # Chi²
    chi2_val = chi2(vobs, vpred, err)
    return vpred, chi2_val

# =============================================================================
def main():
    print("=" * 60)
    print("  ATHENA SPARC Demo – Single Galaxy Fit")
    print("=" * 60)

    data_dir = download_sparc()
    files = [f for f in os.listdir(data_dir) if f.endswith(".dat")]
    if not files:
        print("No SPARC data found.")
        return

    # Use first galaxy as example
    gal_name = files[0].replace("_rotmod.dat", "")
    print(f"Loading galaxy: {gal_name}")
    df = load_galaxy(gal_name, data_dir)
    if df is None:
        print("Failed to load galaxy.")
        return

    vpred, chi2_val = fit_galaxy(df)
    print(f"Chi² = {chi2_val:.2f} for {len(df)} data points")
    print("Demo completed. Extend this script for full SPARC sample.")

if __name__ == "__main__":
    main()
