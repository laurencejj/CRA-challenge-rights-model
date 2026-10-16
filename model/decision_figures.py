"""Figures for docs/DECISIONS.md: whole notches vs continuous, and agency precision."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm
import core
from style import INK, MUTE, BLUE, ORANGE, RED, GREEN

OUT = '../docs/figures/'
L, tau = 2.0, 3.0
ss = np.linspace(0.15, 2.5, 60)
ints = np.arange(0, 9)

# D1. Whole notches hide the comparative statics
fig, axs = plt.subplots(1, 2, figsize=(11, 4.3))
for k0, c in [(2.5, GREEN), (4.5, BLUE), (6.0, ORANGE)]:
    b, g = 1.0, 1 / k0
    kc = [core.best_k(b, g, L, tau, s) for s in ss]
    ki = [ints[np.argmax(core.payoff(ints, b, g, L, tau, s))] for s in ss]
    axs[0].plot(ss, kc, color=c, lw=2.4, label=f'continuous, k0 = {k0}')
    axs[0].step(ss, ki, color=c, lw=1.6, ls='--', where='mid', label=f'whole notches, k0 = {k0}')
axs[0].axhline(tau, color=RED, ls=':', lw=1)
axs[0].set_xlabel('SVO noise sigma (notches)'); axs[0].set_ylabel('Chosen inflation k*')
axs[0].set_title('(a) Continuous k moves smoothly; whole notches jump', loc='left', fontsize=10.5, color=INK)
axs[0].legend(frameon=False, fontsize=8, ncol=2, loc='lower left'); axs[0].set_ylim(0, 3.4)
rng = np.random.default_rng(1)
small = rng.random(20000) < 0.86
bb = np.exp(rng.normal(0, 0.35, 20000)); gg = np.where(small, 1 / 3.0, 1 / 1.9)
eps = rng.normal(0, 0.5, 20000)
kc = np.array([core.best_k(x, y, L, tau, 0.5) for x, y in zip(bb[:2000], gg[:2000])])
ki = np.array([ints[np.argmax(core.payoff(ints, x, y, L, tau, 0.5))] for x, y in zip(bb[:2000], gg[:2000])])
gc, gi = np.round(kc - eps[:2000]), np.round(ki - eps[:2000])
gs = np.arange(-1, 6)
axs[1].bar(gs - 0.2, [(gc == v).mean() for v in gs], 0.4, color=BLUE, label='continuous model')
axs[1].bar(gs + 0.2, [(gi == v).mean() for v in gs], 0.4, color=ORANGE, label='whole-notch model')
axs[1].axvline(tau - 0.5, color=RED, ls='--')
axs[1].set_xlabel('Measured gap: rating minus SVO view (whole notches)'); axs[1].set_ylabel('Share of deals')
axs[1].set_title('(b) What the data would show is almost the same', loc='left', fontsize=10.5, color=INK)
axs[1].legend(frameon=False, fontsize=9)
fig.savefig(OUT + 'figD1_whole_notches.png'); plt.close(fig)

# D2. Agency precision: noise on the agency side
z, w = np.polynomial.hermite_e.hermegauss(60); w = w / w.sum()
K = np.linspace(0, 8, 1601)
def U_prec(k, sa, s, b=1.5, g=1 / 3, L=L, tau=tau, rule=True):
    e = k + sa * z
    P = norm.cdf((e - tau) / s) if rule else 0 * e
    return np.sum(w * (b * e * (1 - P) - L * P)) - 0.5 * g * k ** 2
sas = np.linspace(0, 2, 41)
kst, val, val0 = [], [], []
for sa in sas:
    u = np.array([U_prec(k, sa, 0.5) for k in K]); kst.append(K[u.argmax()]); val.append(u.max())
    u0 = np.array([U_prec(k, sa, 0.5, rule=False) for k in K]); val0.append(u0.max())
fig, axs = plt.subplots(1, 2, figsize=(11, 4.3))
axs[0].plot(sas, kst, color=BLUE, lw=2.5)
axs[0].fill_between(sas, np.array(kst) - sas, np.array(kst) + sas, color=BLUE, alpha=0.12, label='realised error: k* plus or minus one sd of agency noise')
axs[0].axhline(tau, color=RED, ls=':', lw=1)
axs[0].set_xlabel("Agency's own noise (sd, notches)"); axs[0].set_ylabel('Notches')
axs[0].set_title('(a) A less precise agency inflates less on purpose,\nbut its mistakes spread wider', loc='left', fontsize=10.5, color=INK)
axs[0].legend(frameon=False, fontsize=9, loc='upper right'); axs[0].set_ylim(-2, 5)
axs[1].plot(sas, val, color=BLUE, lw=2.5, label='with the challenge right')
axs[1].plot(sas, val0, color=MUTE, lw=2.5, ls='--', label='without it')
axs[1].set_xlabel("Agency's own noise (sd, notches)"); axs[1].set_ylabel("Agency's best payoff")
axs[1].set_title('(b) Accuracy only pays once the regulator can check', loc='left', fontsize=10.5, color=INK)
axs[1].legend(frameon=False, fontsize=9)
fig.savefig(OUT + 'figD2_agency_precision.png'); plt.close(fig)
print('ok')
