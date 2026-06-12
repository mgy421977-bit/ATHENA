# =============================================================================
# methuselah_paradox_final.py
# ATHENA vs ΛCDM – Methuselah Star (HD 140283) Age Paradox
# Balanced H0 = 70.0 (mid‑point between Planck 67.4 and SH0ES 73.0)
# Effective dimension transition n(z) slows down early expansion.
# =============================================================================

import numpy as np
from scipy.integrate import quad

print("=" * 85)
print("   Methuselah Yıldızı – Son Dengeli ATHENA Karşılaştırması (H0=70)")
print("=" * 85)

# ====================== SABİT YILDIZ VERİSİ ======================
star_age = 14.2
star_unc = 0.4

print(f"Methuselah Yıldızı (standart izokron) : {star_age:.2f} ± {star_unc} Gyr\n")

# ====================== EVREN YAŞI HESAP FONKSİYONU ======================
def universe_age(H0, Om, n_func=None):
    def integrand(z):
        if n_func is None:   # ΛCDM
            E = np.sqrt(Om * (1 + z)**3 + (1 - Om))
        else:
            nz = n_func(z)
            E = np.sqrt(Om * (1 + z)**nz + (1 - Om))
        return 1.0 / ((1 + z) * E)
    integral, _ = quad(integrand, 0, 1000)
    return integral * (977.8 / H0)   # Gyr

# ====================== 1. ΛCDM (Planck) ======================
age_lcdm = universe_age(67.4, 0.315)
print(f"ΛCDM (Planck H0=67.4) Evren Yaşı     : {age_lcdm:.2f} Gyr")

# ====================== 2. ATHENA (H0=70, Dengeli EDT) ======================
H0_ath = 70.0
Om_ath = 0.32
zt = 1.35
k = 2.7

def n_z(z):
    # Erken evren yavaş (n≈2.35), geç evren hızlanma (n≈3)
    return 2.35 + 0.65 / (1.0 + (z / zt)**k)

age_athena = universe_age(H0_ath, Om_ath, n_z)
print(f"ATHENA (H0={H0_ath:.1f}, EDT) Evren Yaşı : {age_athena:.2f} Gyr")

# ====================== KARŞILAŞTIRMA ======================
print("\n" + "=" * 85)
print("                          SONUÇ TABLOSU")
print("=" * 85)
print(f"Model                          | Evren Yaşı | Yıldız ile Fark")
print("-" * 85)
print(f"ΛCDM (Planck H0=67.4)          | {age_lcdm:.2f}     | +{star_age - age_lcdm:.2f} Gyr")
print(f"ATHENA (H0={H0_ath:.1f}, EDT)          | {age_athena:.2f}     | +{star_age - age_athena:.2f} Gyr")
print("=" * 85)

print(f"\nHubble Gerilimi Oranı (73/67.4) : 1.083 (%8.31)")
print("ATHENA, bu gerilimi n(z) geçişiyle dengeleyerek paradoksu çözme potansiyeli gösteriyor.")
