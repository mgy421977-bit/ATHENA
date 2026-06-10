import numpy as np
from astropy.table import Table, vstack

def radec_to_cartesian(ra, dec):
    ra_rad = np.deg2rad(ra)
    dec_rad = np.deg2rad(dec)
    x = np.cos(dec_rad) * np.cos(ra_rad)
    y = np.cos(dec_rad) * np.sin(ra_rad)
    z = np.sin(dec_rad)
    return np.column_stack((x, y, z))

qso_cat = vstack([Table.read("QSO_NGC_clustering.dat.fits"), Table.read("QSO_SGC_clustering.dat.fits")])
rand_cat = vstack([Table.read("QSO_NGC_0_clustering.ran.fits"), Table.read("QSO_SGC_0_clustering.ran.fits")])

weights = np.ones(len(qso_cat))  # Basit ağırlık (LSS Weighting geliştirilebilir)

qso_vecs = radec_to_cartesian(qso_cat['RA'], qso_cat['DEC'])
rand_vecs = radec_to_cartesian(rand_cat['RA'], rand_cat['DEC'])

V_i = np.sum(qso_vecs, axis=0) - (len(qso_cat)/len(rand_cat)) * np.sum(rand_vecs, axis=0)
amplitude = np.linalg.norm(V_i) / len(qso_cat)

print(f"MASKEDEN ARINDIRILMIŞ DİPOL GENLİĞİ: {amplitude:.6f}")
# Çıktı: 0.023712
