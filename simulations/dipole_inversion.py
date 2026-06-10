import numpy as np
from astropy.table import Table, vstack

def radec_to_cartesian(ra, dec):
    ra_rad = np.deg2rad(ra)
    dec_rad = np.deg2rad(dec)
    x = np.cos(dec_rad) * np.cos(ra_rad)
    y = np.cos(dec_rad) * np.sin(ra_rad)
    z = np.sin(dec_rad)
    return np.column_stack((x, y, z))

def compute_partial_sky_dipole():
    print("Evrensel veri işleniyor (Kısmi Gökyüzü Tersinir Matris)...")
    qso_ngc_path = "QSO_NGC_clustering.dat.fits"
    qso_sgc_path = "QSO_SGC_clustering.dat.fits"
    rand_ngc_path = "QSO_NGC_0_clustering.ran.fits"
    rand_sgc_path = "QSO_SGC_0_clustering.ran.fits"

    q_ngc = Table.read(qso_ngc_path, format='fits')
    q_sgc = Table.read(qso_sgc_path, format='fits')
    r_ngc = Table.read(rand_ngc_path, format='fits')
    r_sgc = Table.read(rand_sgc_path, format='fits')

    qso_cat = vstack([q_ngc, q_sgc])
    rand_cat = vstack([r_ngc, r_sgc])

    N_qso = len(qso_cat)
    N_rand = len(rand_cat)
    print(f"-> Toplam Gözlemlenen QSO Sayısı: {N_qso}")
    print(f"-> Toplam Rastgele Nokta Sayısı (Maske): {N_rand}")

    print("Kartezyen uzaya geçiş yapılıyor...")
    qso_vecs = radec_to_cartesian(qso_cat['RA'], qso_cat['DEC'])
    rand_vecs = radec_to_cartesian(rand_cat['RA'], rand_cat['DEC'])

    alpha = N_qso / N_rand
    print("Kısmi gökyüzü atalet tensörü (M_ij) hesaplanıyor...")
    M_ij = alpha * np.dot(rand_vecs.T, rand_vecs)

    print("Ham gözlem vektörü hesaplanıp, sızıntılar temizleniyor (Matrix Inversion)...")
    sum_qso = np.sum(qso_vecs, axis=0)
    sum_rand = alpha * np.sum(rand_vecs, axis=0)
    V_i = sum_qso - sum_rand

    M_inv = np.linalg.inv(M_ij)
    true_dipole_vector = np.dot(M_inv, V_i)

    amplitude = np.linalg.norm(true_dipole_vector)
    unit_dipole = true_dipole_vector / amplitude
    dipole_dec = np.rad2deg(np.arcsin(unit_dipole[2]))
    dipole_ra = np.rad2deg(np.arctan2(unit_dipole[1], unit_dipole[0]))
    if dipole_ra < 0:
        dipole_ra += 360

    print("\n" + "="*50)
    print("ANALİZ SONUÇLARI (Sızıntıdan Arındırılmış Saf Dipol)")
    print("="*50)
    print(f"Dipol Genliği (Amplitude) : {amplitude:.6f}")
    print(f"Yönelim [RA]              : {dipole_ra:.2f} derece")
    print(f"Yönelim [DEC]             : {dipole_dec:.2f} derece")
    print("="*50)

compute_partial_sky_dipole()
