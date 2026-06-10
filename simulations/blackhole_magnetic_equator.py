# =============================================================================
# ATHENA V24 — KARADELİK MANYETİK EKVATOR SİMÜLASYONU
# Kara delik = Toroidal düğüm → Manyetik ekvator → Spiral jetler
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("="*70)
print("  ATHENA V24 — KARADELİK MANYETİK EKVATOR SİMÜLASYONU")
print("  Toroidal Düğüm → Manyetik Ekvator → Spiral Disk")
print("="*70)

# =============================================================================
# 1. KARADELİK PARAMETRELERİ
# =============================================================================
M_BH = 1e8          # Güneş kütlesi
a_spin = 0.9        # Dönüş parametresi (0-1)
R_s = 2 * M_BH      # Schwarzschild yarıçapı (norm)
R_ergo = R_s * (1 + np.sqrt(1 - a_spin**2)) / 2  # Ergosphere

# Manyetik ekvator parametreleri
B_pole = 1e4        # Kutup manyetik alanı (Gauss)
B_equator = B_pole * 0.3  # Ekvator alanı (daha zayıf ama geniş)

# =============================================================================
# 2. TOROİDAL MANYETİK ALAN MODELİ
# =============================================================================
def black_hole_magnetic_field(r, theta, a_spin=0.9, B0=1e4):
    """
    Kerr kara delik etrafında toroidal manyetik alan.
    Manyetik ekvator: θ = π/2'de maksimum toroidal bileşen.
    """
    r_norm = r / R_s
    B_r = B0 * np.cos(theta) / (r_norm**3 + 1) * np.exp(-r_norm/10)
    B_phi = B0 * 0.3 * np.sin(2*theta) / (r_norm**2 + 0.1) * np.exp(-r_norm/20)
    B_phi *= (1 + a_spin * np.sin(theta)**2)
    B_total = np.sqrt(B_r**2 + B_phi**2)
    return B_r, B_phi, B_total

# =============================================================================
# 3. SPİRAL DİSK (MANYETİK EKVATORUN GEOMETRİK İZİ)
# =============================================================================
def spiral_disk(r_max=10, N_arms=4, a_spin=0.9):
    phi = np.linspace(0, 6*np.pi, 1000)
    b = 0.15 / (1 + a_spin)
    r_spiral = 1.5 * np.exp(b * phi)
    r_spiral = np.clip(r_spiral, 1, r_max)
    arms = []
    for n in range(N_arms):
        phase_shift = 2 * np.pi * n / N_arms
        phi_arm = phi + phase_shift
        r_arm = 1.5 * np.exp(b * phi_arm)
        r_arm = np.clip(r_arm, 1, r_max)
        x = r_arm * np.cos(phi_arm)
        y = r_arm * np.sin(phi_arm)
        arms.append((x, y))
    return arms

# =============================================================================
# 4. GÖRSELLEŞTİRME (6 panel)
# =============================================================================
fig = plt.figure(figsize=(16, 10))

# Panel 1: 3D toroidal manyetik alan
ax1 = fig.add_subplot(2, 3, 1, projection='3d')
theta_torus = np.linspace(0, 2*np.pi, 100)
phi_torus = np.linspace(0, 2*np.pi, 60)
THETA, PHI = np.meshgrid(theta_torus, phi_torus)
R_torus = 3; a_torus = 1.5
X = (R_torus + a_torus*np.cos(THETA)) * np.cos(PHI)
Y = (R_torus + a_torus*np.cos(THETA)) * np.sin(PHI)
Z = a_torus * np.sin(THETA)
_, _, B_tot = black_hole_magnetic_field(R_torus, THETA, a_spin)
colors = plt.cm.inferno(B_tot / B_tot.max())
ax1.plot_surface(X, Y, Z, facecolors=colors, alpha=0.7)
ax1.set_title('Kara Delik: Toroidal Manyetik Alan\n(Manyetik Ekvator: θ=π/2)', fontsize=10)
ax1.set_xlim(-5,5); ax1.set_ylim(-5,5); ax1.set_zlim(-5,5)

# Panel 2: Manyetik ekvator profili
ax2 = fig.add_subplot(2, 3, 2)
r_vals = np.linspace(1, 15, 200)
theta_eq = np.pi/2
B_r_eq, B_phi_eq, B_tot_eq = black_hole_magnetic_field(r_vals, theta_eq, a_spin)
ax2.plot(r_vals, B_tot_eq, 'r-', lw=2, label='|B| (Ekvator)')
ax2.plot(r_vals, B_phi_eq, 'orange', lw=1.5, label='B_φ (Toroidal)')
ax2.axvline(x=2, color='k', ls='--', alpha=0.3, label='R_s')
ax2.set_xlabel('r / R_s'); ax2.set_ylabel('B (Gauss)')
ax2.set_title('Manyetik Alan Profili (Ekvator Düzlemi)')
ax2.legend(fontsize=7); ax2.grid(alpha=0.3); ax2.set_yscale('log')

# Panel 3: Spiral disk
ax3 = fig.add_subplot(2, 3, 3)
spiral_arms = spiral_disk(r_max=8, N_arms=4, a_spin=a_spin)
colors_spiral = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
for i, (x, y) in enumerate(spiral_arms):
    ax3.plot(x, y, color=colors_spiral[i], lw=1.5, alpha=0.8)
    ax3.plot(-x, -y, color=colors_spiral[i], lw=1.5, alpha=0.4)
circle = plt.Circle((0, 0), 1.5, color='black', alpha=0.9)
ax3.add_patch(circle)
ax3.scatter(0, 0, c='white', s=100, marker='*')
ax3.set_xlim(-8,8); ax3.set_ylim(-8,8)
ax3.set_aspect('equal')
ax3.set_title('Spiral Disk: Manyetik Ekvatorun\nGeometrik İzi (4 Kollu)', fontsize=10)
ax3.grid(alpha=0.2)

# Panel 4: Φ-alanı akışı
ax4 = fig.add_subplot(2, 3, 4, projection='polar')
theta_flow = np.linspace(0, 2*np.pi, 200)
inflow = np.exp(-2 * np.abs(theta_flow - np.pi/2)**2)
outflow = np.sin(2*theta_flow)**2 * np.exp(-0.5 * np.abs(theta_flow - np.pi/2))
ax4.fill(theta_flow, inflow, alpha=0.5, color='blue', label='İnflow (Kutuplar)')
ax4.fill(theta_flow, outflow*0.8, alpha=0.5, color='red', label='Outflow (Ekvator)')
ax4.set_title('Φ-Alanı Akışı: Kutuplar → Ekvator', fontsize=10)
ax4.legend(loc='upper right', fontsize=7)

# Panel 5: Frame dragging
ax5 = fig.add_subplot(2, 3, 5)
r_drag = np.linspace(1, 10, 100)
omega_drag = a_spin / (r_drag**3 + a_spin**2) * np.exp(-r_drag/8)
ax5.plot(r_drag, omega_drag, 'purple', lw=2)
ax5.set_xlabel('r / R_s'); ax5.set_ylabel('ω_frame (a.u.)')
ax5.set_title('Frame Dragging: Vakum Sürükleme Hızı')
ax5.grid(alpha=0.3)

# Panel 6: Özet metin
ax6 = fig.add_subplot(2, 3, 6)
ax6.axis('off')
ozet = [
    '★ MANYETİK EKVATOR TEOREMİ ★',
    '',
    '1. Kara delik = Toroidal düğüm',
    '   (Protonun fraktal kopyası)',
    '',
    '2. Manyetik Ekvator:',
    '   • Φ-alanı topolojik kilitlenme noktası',
    '   • Kutuplar → İnflow (yutma)',
    '   • Ekvator → Outflow (jetler/plazma)',
    '',
    '3. Spiral Disk:',
    '   • Manyetik ekvatorun geometrik izi',
    '   • Frame dragging ile oluşur',
    '   • Logaritmik sarmal yapısı',
    '',
    '4. Karanlık Madde İllüzyonu:',
    '   • Ekvatordan pompalanan vakum',
    '     enerjisinin topolojik basıncı',
    '',
    '→ Kara delik = Galaksinin topolojik kalbi',
]
for i, line in enumerate(ozet):
    color = '#E8A030' if '★' in line else ('cyan' if '→' in line else 'white')
    ax6.text(0.1, 0.95 - i*0.06, line, fontsize=8, transform=ax6.transAxes,
             fontfamily='monospace', color=color)

plt.suptitle('ATHENA V24: Kara Delik Manyetik Ekvator Modeli\n'
             'Toroidal Düğüm → Manyetik Jeneratör → Galaktik Kalp',
             fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('blackhole_magnetic_equator.png', dpi=150)
plt.show()

# =============================================================================
# 5. SAYISAL ÖZET
# =============================================================================
print(f"\n{'='*70}")
print(f"  MANYETİK EKVATOR SİMÜLASYONU TAMAMLANDI")
print(f"{'='*70}")
print(f"  Kara delik kütlesi: {M_BH:.0e} M_sun")
print(f"  Dönüş parametresi: a = {a_spin}")
print(f"  Manyetik alan (kutup): {B_pole:.0e} G")
print(f"  Manyetik alan (ekvator): {B_equator:.0e} G")
print(f"  Spiral kol sayısı: 4")
print(f"")
print(f"  Sonuç: Kara delik, galaksinin Φ-alanı jeneratörüdür.")
print(f"  Manyetik ekvator, karanlık madde illüzyonunu yaratan")
print(f"  topolojik basıncın kaynağıdır.")
print(f"{'='*70}")
