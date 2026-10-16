"""
Baseline model: one rater, one bond, one SVO check (Julia port of core.py).

    rating        r = θ + k                 (k ≥ 0 is inflation, in notches)
    SVO view      s = θ + ε,  ε ~ N(0, σ²)
    challenge     P(k) = q Φ((k - τ)/σ)
    rater payoff  U(k) = b k (1 - P(k)) - L P(k) - γ/2 k²
"""
module ChallengeModel

using SpecialFunctions: erfc
export Φ, challenge_prob, payoff, best_k, false_challenge_rate

Φ(z) = 0.5 * erfc(-z / sqrt(2))

challenge_prob(k; τ=3.0, σ=0.75, q=1.0) = q * Φ((k - τ) / σ)

function payoff(k; b=1.0, γ=1/3, L=2.0, τ=3.0, σ=0.75, q=1.0)
    P = challenge_prob(k; τ, σ, q)
    return b * k * (1 - P) - L * P - 0.5 * γ * k^2
end

"""
Optimal inflation: grid search on [0, 10] for the global maximum (U can have two
local maxima), then golden-section refinement around it. `rule=false` gives k₀ = b/γ.
"""
function best_k(; b=1.0, γ=1/3, L=2.0, τ=3.0, σ=0.75, q=1.0, rule=true, grid=0:0.002:10)
    rule || return b / γ
    f(k) = payoff(k; b, γ, L, τ, σ, q)
    best, kbest = -Inf, 0.0
    for k in grid
        u = f(k)
        if u > best
            best, kbest = u, k
        end
    end
    lo, hi = max(0.0, kbest - step(grid)), kbest + step(grid)
    g = (sqrt(5) - 1) / 2
    for _ in 1:60
        a, c = hi - g * (hi - lo), lo + g * (hi - lo)
        f(a) > f(c) ? (hi = c) : (lo = a)
    end
    return (lo + hi) / 2
end

false_challenge_rate(; τ=3.0, σ=0.75, q=1.0) = challenge_prob(0.0; τ, σ, q)

end
