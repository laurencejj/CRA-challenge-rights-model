"""Figures for docs/STAGE1.md, drawn from the CSVs written by julia/stage1.jl."""
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from style import INK, MUTE, BLUE, ORANGE, RED, GREEN

OUT, D = '../docs/figures/', 'output/'
TAU = 3.0

# S1. Two hills: comply or defy
h = pd.read_csv(D + 'stage1_two_hills.csv')
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(h.k, h.U_norule, color=MUTE, ls='--', lw=1.8, label='no rule')
for col, q, c in [('U_q50', 0.50, BLUE), ('U_q10', 0.10, ORANGE), ('U_q05', 0.05, RED)]:
    ax.plot(h.k, h[col], color=c, lw=2.4, label=f'enforcement q = {q:.2f}')
    i = h[col].idxmax(); ax.plot(h.k[i], h[col][i], 'o', color=c, ms=8)
ax.axvline(TAU, color=RED, ls=':', lw=1.2)
ax.annotate('comply hill:\nstop just below 3', (2.6, 2.1), xytext=(0.3, 3.6), color=BLUE, fontsize=9.5,
            arrowprops=dict(arrowstyle='->', color=BLUE))
ax.annotate('defy hill:\ngo far above and\nhope not to be removed', (6.9, 2.9), xytext=(7.3, 0.6), color=ORANGE, fontsize=9.5,
            arrowprops=dict(arrowstyle='->', color=ORANGE))
ax.set_ylim(-2, 4.5); ax.set_xlabel('Inflation k (notches)'); ax.set_ylabel("Agency's payoff")
ax.set_title('A high-value deal (k0 = 7.5): weak enforcement opens a second hill', loc='left', color=INK)
ax.legend(frameon=False, fontsize=9, loc='lower left')
fig.savefig(OUT + 'figS1_two_hills.png'); plt.close(fig)

# S2. Regime map
r = pd.read_csv(D + 'stage1_regimes.csv')
fig, ax = plt.subplots(figsize=(8.5, 4.6))
ax.fill_between(r.k0, 0, r.q_hat_limit, color=ORANGE, alpha=0.18)
ax.fill_between(r.k0, r.q_hat_limit, 0.5, color=BLUE, alpha=0.10)
ax.plot(r.k0, r.q_hat_limit, color=INK, lw=2.4, label='boundary q-hat(k0), exact as SVO noise goes to 0')
ax.plot(r.k0, r.q_hat_sigma025, color=INK, lw=1.4, ls='--', label='boundary computed with SVO noise 0.25')
ax.text(4.0, 0.33, 'COMPLY\nbunch just below 3 notches', color=BLUE, fontsize=11, fontweight='bold')
ax.text(7.2, 0.04, 'DEFY\ninflate far above 3', color=ORANGE, fontsize=11, fontweight='bold')
ax.set_xlim(3.1, 9); ax.set_ylim(0, 0.5)
ax.set_xlabel('Pre-rule inflation k0 (how much the deal is worth inflating)')
ax.set_ylabel('Enforcement q (chance a challenge is upheld)')
ax.set_title('Who complies and who defies', loc='left', color=INK)
ax.legend(frameon=False, fontsize=9, loc='upper right', bbox_to_anchor=(1, 0.86))
fig.savefig(OUT + 'figS2_regimes.png'); plt.close(fig)

# S3. Safety margin
m = pd.read_csv(D + 'stage1_margin.csv')
fig, ax = plt.subplots(figsize=(8, 4.3))
ax.plot(m.sigma, m.margin_exact, color=BLUE, lw=2.6, label='exact (numerical)')
ax.plot(m.sigma, m.margin_approx, color=ORANGE, lw=2, ls='--', label='formula in Result 3')
ax.plot(m.sigma, m.sigma, color=MUTE, lw=1, ls=':', label='one sigma, for scale')
ax.set_xlabel('SVO noise sigma (notches)'); ax.set_ylabel('Safety margin: tau minus k* (notches)')
ax.set_title('How far below the line the agency stops', loc='left', color=INK)
ax.legend(frameon=False, fontsize=9)
fig.savefig(OUT + 'figS3_margin.png'); plt.close(fig)

# S4. Comparative statics
s = pd.read_csv(D + 'stage1_statics.csv')
fig, axs = plt.subplots(1, 4, figsize=(13, 3.6), sharey=True)
spec = [('L', 'penalty L', 'k* falls a little'), ('q', 'enforcement q', 'k* falls; jumps at the defy boundary'),
        ('sigma', 'SVO noise sigma', 'k* falls while margin > sigma'), ('tau', 'threshold tau', 'k* rises almost one for one')]
for ax, (p, lab, note) in zip(axs, spec):
    d = s[s.param == p]
    ax.plot(d.x, d.kstar, color=BLUE, lw=2.4)
    ax.set_xlabel(lab); ax.set_title(note, loc='left', fontsize=9.5, color=INK)
axs[0].set_ylabel('chosen inflation k*'); axs[0].set_ylim(0, 5)
fig.suptitle('What moves the agency (deal with k0 = 4.5; base L = 2, q = 1, sigma = 0.5, tau = 3)', x=0.01, y=1.04, ha='left', color=INK, fontsize=11)
fig.savefig(OUT + 'figS4_statics.png'); plt.close(fig)

# S5. The limit prediction: three-part distribution
rng = np.random.default_rng(1)
k0 = 3.0 * np.exp(rng.normal(0, 0.35, 200000))
q = 0.10
A = k0 / 2; C = TAU - TAU ** 2 / (2 * k0); B2 = 2 * A + 2.0
qhat = np.where(k0 > TAU, (B2 - np.sqrt(B2 ** 2 - 4 * A * (A - C))) / (2 * A), 0)
post = np.where(k0 <= TAU, k0, np.where(q < qhat, (1 - q) * k0, TAU - 0.03))
fig, ax = plt.subplots(figsize=(9, 4.4))
bins = np.linspace(0, 9, 91)
ax.hist(k0, bins, color=MUTE, alpha=0.5, density=True, label='before the rule')
ax.hist(post, bins, color=BLUE, alpha=0.7, density=True, label=f'after (SVO noise near 0, q = {q})')
ax.axvline(TAU, color=RED, ls='--')
ax.annotate('1. below 3: unchanged', (2.0, 0.45), xytext=(0.2, 0.9), fontsize=9.5, color=INK, arrowprops=dict(arrowstyle='->', color=MUTE))
ax.annotate(f'2. spike just below 3:\n{100*np.mean((k0 > TAU) & (q >= qhat)):.0f}% of deals', (2.95, 1.5), xytext=(3.8, 1.1), fontsize=9.5, color=BLUE,
            arrowprops=dict(arrowstyle='->', color=BLUE))
ax.annotate(f'3. defiers far above:\n{100*np.mean(q < qhat):.1f}% of deals', (5.8, 0.03), xytext=(6.2, 0.5), fontsize=9.5, color=ORANGE,
            arrowprops=dict(arrowstyle='->', color=ORANGE))
ax.set_ylim(0, 2.0); ax.set_xlabel('Inflation k (notches)'); ax.set_ylabel('Density')
ax.set_title('The three-part prediction', loc='left', color=INK); ax.legend(frameon=False, loc='upper right')
fig.savefig(OUT + 'figS5_three_parts.png'); plt.close(fig)
print('defiers %.3f, bunch %.3f' % (np.mean(q < qhat), np.mean((k0 > TAU) & (q >= qhat))))
