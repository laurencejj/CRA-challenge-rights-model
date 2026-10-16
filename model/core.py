"""Baseline model: one rater, one bond, one SVO check.

Units: everything is in rating notches. b is the value to the rater of one
notch of inflation (normalised to 1), so L and gamma are in "notches of fee".

    rating        r = theta + k            (k >= 0 is inflation)
    SVO view      s = theta + eps,  eps ~ N(0, sigma^2)
    measured gap  g = r - s = k - eps
    challenge     if g >= tau, upheld with probability q
                  => P(k) = q * Phi((k - tau) / sigma)
    rater payoff  U(k) = b*k*(1 - P(k)) - L*P(k) - gamma/2 * k^2

Without the rule (P = 0) the rater picks k0 = b / gamma.
"""
import numpy as np
from scipy.stats import norm

GRID = np.linspace(0.0, 10.0, 5001)


def challenge_prob(k, tau=3.0, sigma=0.75, q=1.0):
    return q * norm.cdf((np.asarray(k) - tau) / sigma)


def payoff(k, b=1.0, gamma=1 / 3.0, L=2.0, tau=3.0, sigma=0.75, q=1.0):
    k = np.asarray(k)
    P = challenge_prob(k, tau, sigma, q)
    return b * k * (1 - P) - L * P - 0.5 * gamma * k ** 2


def best_k(b=1.0, gamma=1 / 3.0, L=2.0, tau=3.0, sigma=0.75, q=1.0, rule=True):
    """Optimal inflation. rule=False gives the pre-2026 benchmark k0 = b/gamma."""
    if not rule:
        return b / gamma
    u = payoff(GRID, b, gamma, L, tau, sigma, q)
    return GRID[np.argmax(u)]


def simulate_deals(n=20000, share_small=0.86, k0_small=3.0, k0_large=1.9,
                   b_sd=0.35, seed=1, **rule):
    """Many bonds, two rater tiers.

    Each deal draws its own value of inflation b_i (lognormal, median 1).
    Tier costs gamma are set so the median pre-rule inflation matches the
    NAIC 2023 sample means (about 3.0 notches small CRPs, 1.9 large).
    Returns pre-rule k0, post-rule k*, and measured gaps (rounded to notches).
    """
    rng = np.random.default_rng(seed)
    small = rng.random(n) < share_small
    b = np.exp(rng.normal(0, b_sd, n))
    gamma = np.where(small, 1 / k0_small, 1 / k0_large)
    k0 = b / gamma
    # solve on a coarse grid of b for speed, then interpolate
    sigma = rule.get('sigma', 0.75)
    eps = rng.normal(0, sigma, n)
    kstar = np.empty(n)
    for g in np.unique(gamma):
        m = gamma == g
        bs = np.linspace(b[m].min(), b[m].max(), 200)
        ks = np.array([best_k(bb, g, **rule) for bb in bs])
        kstar[m] = np.interp(b[m], bs, ks)
    gap_pre = np.round(k0 - eps)
    gap_post = np.round(kstar - eps)
    return dict(small=small, k0=k0, kstar=kstar, gap_pre=gap_pre, gap_post=gap_post)


def false_challenge_rate(tau=3.0, sigma=0.75, q=1.0):
    """Chance an honest rating (k = 0) is challenged and removed."""
    return float(challenge_prob(0.0, tau, sigma, q))
