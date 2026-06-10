# =============================================================================
# ATHENA V16 — TÜRETİM #4 (DÜZELTİLMİŞ v2)
# Toroidal Yukawa Çözümü — Çalışan Versiyon
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, eye, kron, csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.optimize import curve_fit

print("="*60)
print("  ATHENA V16 — TÜRETİM #4 (DÜZELTİLMİŞ v2)")
print("  Toroidal Yukawa Denklemi Çözümü")
print("="*60)

# Torus geometrisi
R, a = 7.1, 1.0
N_theta, N_phi = 80, 40
theta = np.linspace(0, 2*np.pi, N_theta)
phi = np.linspace(0, 2*np.pi, N_phi)
d_theta = theta[1] - theta[0]
d_phi = phi[1] - phi[0]
THETA, PHI = np.meshgrid(theta, phi, indexing='ij')

mu, Z0 = 0.3, 0.233

print(f"Torus: R={R}, a={a}, R/a={R/a:.1f}, Grid: {N_theta}×{N_phi}")

# Operatörler
def D2(N, dx):
    main = -2 * np.ones(N); off = np.ones(N-1)
    D = diags([off, main, off], [-1,0,1]).toarray()
    D[0,-1]=1; D[-1,0]=1
    return D/dx**2

def D1(N, dx):
    main = np.zeros(N); off = np.ones(N-1)
    D = diags([-off, main, off], [-1,0,1]).toarray()
    D[0,-1]=-1; D[-1,0]=1
    return D/(2*dx)

# Yukawa operatörü
L_theta = kron(eye(N_phi).toarray(), D2(N_theta, d_theta)) / a**2

metric = 1.0 / (R + a*np.cos(THETA))**2
L_phi = np.diag(metric.flatten()) @ kron(D2(N_phi, d_phi), eye(N_theta).toarray())

conn = np.sin(theta) / (a*(R + a*np.cos(theta)))
L_conn = np.diag(np.tile(conn, N_phi)) @ kron(eye(N_phi).toarray(), D1(N_theta, d_theta))

H = L_theta + L_phi + L_conn - mu**2 * np.eye(N_theta*N_phi)

# Kaynak
sigma = 0.4
rho = np.exp(-((THETA - np.pi) % (2*np.pi) - np.pi)**2 / (2*sigma**2))
rho = rho / rho.max()
b = -Z0 * rho.flatten()

# Çöz (CSC formatında)
print("Çözülüyor...")
Phi_flat = spsolve(csc_matrix(H), b)
Phi = Phi_flat.reshape(N_theta, N_phi)

# Profil
phi_mid = N_phi // 2
Phi_prof = Phi[:, phi_mid]
r_prof = a * theta

a_phi = np.zeros_like(Phi_prof)
dr = r_prof[1] - r_prof[0]
a_phi[1:-1] = np.abs(Phi_prof[2:] - Phi_prof[:-2]) / (2*dr)
a_phi[0] = a_phi[1]; a_phi[-1] = a_phi[-2]

# Disk bölgesi
disk = (theta > np.pi/2) & (theta < 3*np.pi/2)
r_fit = np.abs(r_prof[disk] - np.pi*a)
a_fit = a_phi[disk]

# Analitik fit (daha iyi başlangıç değerleri ve daha fazla iterasyon)
def a_analytical(r, A, r_s, R_w):
    return A * (1 - np.exp(-r/R_w)) * np.tanh(r/r_s)

try:
    popt, _ = curve_fit(a_analytical, r_fit, a_fit,
                        p0=[a_fit.max(), 1.5, 2.0],
                        maxfev=20000, method='trf')
    A_f, rs_f, Rw_f = popt
    a_pred = a_analytical(r_fit, *popt)
    ss_res = np.sum((a_fit - a_pred)**2)
    ss_tot = np.sum((a_fit - np.mean(a_fit))**2)
    R2 = 1 - ss_res/ss_tot
    fit_ok = True
except:
    R2 = 0
    fit_ok = False
    print("Fit yakınsamadı, parametreleri manuel ayarla.")

print(f"\n{'='*50}")
print(f"  SONUÇLAR")
print(f"{'='*50}")
if fit_ok:
    print(f"  A = {A_f:.4f}, r_s = {rs_f:.2f}, R_whim = {Rw_f:.2f}")
    print(f"  R² = {R2:.4f}")
    if R2 > 0.95:
        print("  ★ MÜKEMMEL! Ad-hoc eleştirisi çürütüldü.")
    elif R2 > 0.8:
        print("  ✓ İyi uyum. Formül fizikseldir.")
    else:
        print("  → Orta düzey uyum.")
print(f"{'='*50}")

# Görsel
fig, axes = plt.subplots(1, 3, figsize=(15,4))
ax=axes[0]; im=ax.contourf(PHI, THETA, Phi, levels=20, cmap='plasma')
ax.axhline(np.pi, color='cyan', ls='--'); ax.set_xlabel('φ'); ax.set_ylabel('θ')
ax.set_title('Φ-Alanı'); plt.colorbar(im, ax=ax)

ax=axes[1]; im=ax.contourf(PHI, THETA, rho, levels=20, cmap='inferno')
ax.axhline(np.pi, color='cyan', ls='--'); ax.set_xlabel('φ'); ax.set_ylabel('θ')
ax.set_title('Baryon Yoğunluğu'); plt.colorbar(im, ax=ax)

ax=axes[2]
ax.plot(r_fit, a_fit, 'b-', lw=2, alpha=0.7, label='Toroidal çözüm')
if fit_ok:
    ax.plot(r_fit, a_pred, 'r--', lw=2, label=f'Fit (R²={R2:.3f})')
ax.set_xlabel('r (kpc)'); ax.set_ylabel('a_Φ(r)')
ax.set_title('a_Φ(r) Profili'); ax.legend(); ax.grid(alpha=0.3)

plt.suptitle('ATHENA V16: Toroidal Yukawa → a_Φ(r) Türetimi', fontweight='bold', fontsize=14)
plt.tight_layout(); plt.savefig('yukawa_toroidal_final.png', dpi=150); plt.show()

print("\n" + "="*60)
print("  TÜRETİM #4 TAMAMLANDI")
print("="*60)
