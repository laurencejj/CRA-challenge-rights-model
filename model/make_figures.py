"""Figures for docs/MODEL_PLAN.md. Run from model/: python3 make_figures.py"""
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import core

OUT = '../docs/figures/'
from style import INK, MUTE, GRID, BLUE, ORANGE, RED, GREEN

# 1. Why a notch is worth money: the life RBC ladder
rbc = pd.read_csv('../data/rbc_factors_life.csv')
fig, ax = plt.subplots(figsize=(10, 4.6))
cols = [BLUE if d[0] in '12' else ORANGE for d in rbc.designation]
ax.bar(range(20), rbc.life_rbc_factor_pretax_pct, color=cols, width=0.75)
ax.set_xticks(range(20))
ax.set_xticklabels([f"{d}\n{e.split('/')[-1].replace('All lower', '<CCC-')}" for d, e in zip(rbc.designation, rbc.nrsro_equivalent)], fontsize=8)
ax.set_ylabel('Capital charge, % of bond value (pre-tax)')
ax.set_title('Life insurer capital charge by NAIC designation', loc='left', color=INK)
i0, i1 = 11, 8  # BB (3.B) rated as BBB (2.B): a 3-notch lift
y0, y1 = rbc.life_rbc_factor_pretax_pct[i0], rbc.life_rbc_factor_pretax_pct[i1]
ax.annotate('', xy=(i1, y1 + 0.6), xytext=(i0, y0 + 0.6),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2, connectionstyle='arc3,rad=0.35'))
ax.text(9.5, 7.6, f'A BB bond rated BBB (3 notches up):\ncharge falls from {y0:.2f}% to {y1:.2f}%,\nabout two thirds less capital',
        ha='center', color=RED, fontsize=9.5)
ax.axvline(9.5 + 0.5, color=MUTE, ls=':', lw=1)
ax.text(10.1, 27, 'investment grade | high yield', ha='center', color=MUTE, fontsize=9)
ax.text(19.4, -5.2, 'Source: Mayer Brown (Dec 2024), NAIC life RBC factors adopted 2021.', ha='right', fontsize=8, color=MUTE)
fig.savefig(OUT + 'fig1_capital_ladder.png'); plt.close(fig)

# 2. The SVO trigger: chance a rating is challenged, by inflation and SVO noise
k = np.linspace(0, 7, 701)
fig, ax = plt.subplots(figsize=(8, 4.4))
for s, c, lab in [(0.25, BLUE, 'sharp SVO view (sigma = 0.25 notch)'), (0.75, GREEN, 'medium (sigma = 0.75)'), (1.5, ORANGE, 'noisy SVO view (sigma = 1.5)')]:
    ax.plot(k, core.challenge_prob(k, sigma=s), color=c, lw=2.4, label=lab)
ax.axvline(3, color=RED, ls='--', lw=1.2); ax.text(3.05, 0.04, 'tau = 3 notches', color=RED)
ax.set_xlabel('Inflation chosen by the rater, k (notches above true quality)')
ax.set_ylabel('Probability the rating is challenged, P(k)')
ax.set_title('The SVO check: a fuzzy tripwire at 3 notches', loc='left', color=INK)
ax.legend(frameon=False, loc='lower right')
fig.savefig(OUT + 'fig2_challenge_curve.png'); plt.close(fig)

# 3. The rater's trade-off for one deal
b, gamma, L, sig = 1.5, 1 / 3.0, 2.0, 0.5
pre = b * k - 0.5 * gamma * k ** 2
post = core.payoff(k, b, gamma, L, sigma=sig)
k0, ks = core.best_k(b, gamma, rule=False), core.best_k(b, gamma, L, sigma=sig)
fig, ax = plt.subplots(figsize=(8.5, 4.8))
ax.plot(k, pre, color=MUTE, lw=2, ls='--', label='before the rule: fee gain minus reputation cost')
ax.plot(k, post, color=BLUE, lw=2.6, label='after the rule: also lose everything if challenged')
ax.fill_between(k, post, pre, where=pre > post, color=RED, alpha=0.12, label='expected cost of a challenge')
ax.plot([k0], [b * k0 - 0.5 * gamma * k0 ** 2], 'o', color=MUTE, ms=8)
ax.annotate(f'k0 = {k0:.1f}: pre-rule choice', (k0, b * k0 - 0.5 * gamma * k0 ** 2), xytext=(4.8, 4.2), color=MUTE,
            arrowprops=dict(arrowstyle='->', color=MUTE))
uk = core.payoff(ks, b, gamma, L, sigma=sig)
ax.plot([ks], [uk], 'o', color=BLUE, ms=8)
ax.annotate(f'k* = {ks:.1f}: stop just short\nof the 3-notch line', (ks, uk), xytext=(0.3, 3.4), color=BLUE,
            arrowprops=dict(arrowstyle='->', color=BLUE))
ax.axvline(3, color=RED, ls=':', lw=1.2)
ax.set_ylim(-2.5, 5); ax.set_xlabel('Inflation k (notches)'); ax.set_ylabel("Rater's payoff (in units of one notch of fee)")
ax.set_title("One deal: the rater's choice before and after the challenge right", loc='left', color=INK)
ax.legend(frameon=False, loc='lower left', fontsize=9)
fig.savefig(OUT + 'fig3_rater_tradeoff.png'); plt.close(fig)

# 4. Many deals: bunching below the threshold
d = core.simulate_deals(sigma=0.5)
fig, axs = plt.subplots(1, 2, figsize=(11, 4.3))
bins = np.linspace(0, 7, 57)
axs[0].hist(d['k0'], bins, color=MUTE, alpha=0.55, label='before the rule (k0)')
axs[0].hist(d['kstar'], bins, color=BLUE, alpha=0.75, label='after the rule (k*)')
axs[0].axvline(3, color=RED, ls='--'); axs[0].set_xlabel('True inflation, k (notches)'); axs[0].set_ylabel('Number of deals')
axs[0].set_title('(a) What raters do: the right tail piles up below 3', loc='left', fontsize=10.5, color=INK)
axs[0].legend(frameon=False)
gb = np.arange(-2, 9) 
pre_c = [(d['gap_pre'] == g).mean() for g in gb]; post_c = [(d['gap_post'] == g).mean() for g in gb]
axs[1].bar(gb - 0.2, pre_c, 0.4, color=MUTE, alpha=0.7, label='before')
axs[1].bar(gb + 0.2, post_c, 0.4, color=BLUE, label='after')
axs[1].axvline(2.5, color=RED, ls='--'); axs[1].set_xlabel('Measured gap: rating minus SVO view (whole notches)'); axs[1].set_ylabel('Share of deals')
axs[1].set_title('(b) What the data will show: blurred by SVO noise', loc='left', fontsize=10.5, color=INK)
axs[1].legend(frameon=False)
fig.text(0.01, -0.03, 'Illustrative simulation: 20,000 deals, 86% rated by small CRPs (pre-rule mean gap 3.0) and 14% by large CRPs (1.9); sigma = 0.5, L = 2, tau = 3.',
         fontsize=8, color=MUTE)
fig.savefig(OUT + 'fig4_bunching.png'); plt.close(fig)

# 5. The noise trade-off
ss = np.linspace(0.15, 2.0, 30)
mean_k, false_r, flagged = [], [], []
for s in ss:
    dd = core.simulate_deals(n=6000, sigma=s)
    mean_k.append(dd['kstar'].mean()); false_r.append(core.false_challenge_rate(sigma=s) * 100)
    flagged.append((dd['gap_post'] >= 3).mean() * 100)
fig, ax = plt.subplots(figsize=(8.5, 4.5))
ax.plot(ss, mean_k, color=BLUE, lw=2.5, label='average inflation after the rule (notches, left axis)')
ax.axhline(d['k0'].mean(), color=MUTE, ls='--', lw=1); ax.text(0.2, d['k0'].mean() + 0.07, 'average before the rule (3.0)', color=MUTE, fontsize=9)
ax.set_xlabel("Noise in the SVO's own view, sigma (notches)"); ax.set_ylabel('Notches', color=BLUE); ax.set_ylim(0, 3.4)
ax2 = ax.twinx(); ax2.grid(False); ax2.spines['right'].set_visible(True)
ax2.plot(ss, false_r, color=RED, lw=2.5, label='honest ratings wrongly challenged (%, right axis)')
ax2.set_ylabel('% of honest ratings', color=RED); ax2.set_ylim(0, 12)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, loc='lower left', bbox_to_anchor=(0.0, 0.1), fontsize=9)
ax.set_title('Noise deters inflation but punishes honest ratings', loc='left', color=INK)
fig.savefig(OUT + 'fig5_noise_tradeoff.png'); plt.close(fig)
print('k0 mean %.2f; one deal k0=%.2f k*=%.2f' % (d['k0'].mean(), k0, ks))

# 6. Two ways to police the gap: threshold vs graduated haircut
g = np.linspace(-1, 7, 801)
fig, ax = plt.subplots(figsize=(8.5, 4.4))
ax.plot(g, (g >= 3).astype(float), color=BLUE, lw=2.6, label='threshold rule (the NAIC design): lose all relief at a 3-notch gap')
ax.plot(g, np.clip((g - 1) / 4, 0, 1), color=ORANGE, lw=2.6, label='graduated haircut: lose relief step by step as the gap grows')
ax.plot(k, core.challenge_prob(k, sigma=0.75), color=BLUE, lw=1.6, ls=':', label='threshold as the rater sees it, given SVO noise (sigma = 0.75)')
ax.set_xlabel('Gap between the rating and the SVO view (notches)'); ax.set_ylabel('Share of capital relief lost')
ax.set_title('Stage 3 question: which penalty schedule should the regulator use?', loc='left', color=INK)
ax.legend(frameon=False, loc='upper left', fontsize=9); ax.set_ylim(-0.05, 1.45)
fig.savefig(OUT + 'fig6_threshold_vs_haircut.png'); plt.close(fig)
