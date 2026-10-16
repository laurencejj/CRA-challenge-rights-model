# Stage 1: numerical checks of the propositions in docs/STAGE1.md, and the
# data behind the Stage 1 figures (written to ../output/stage1_*.csv).
# Run: julia --project=. stage1.jl
include("ChallengeModel.jl"); using .ChallengeModel
using Printf

const τ = 3.0
outdir = joinpath(@__DIR__, "..", "output"); mkpath(outdir)

# all local maxima of U on a fine grid (to see the "two hills")
function local_maxima(; b, γ, L, σ, q, grid=0:0.002:12)
    u = [payoff(k; b, γ, L, τ, σ, q) for k in grid]
    [(grid[i], u[i]) for i in 2:length(u)-1 if u[i] > u[i-1] && u[i] >= u[i+1]]
end

# Prop 3: approximate safety margin for small σ (comply regime, k0 > τ)
margin_approx(; b, γ, L, σ, q) = σ * sqrt(2 * log(q * (b * τ + L) / (sqrt(2π) * σ * (b - γ * τ))))

# Prop 4: enforcement level below which the agency jumps the threshold (σ → 0 limit)
function q_defy(; k0, L)
    b, γ = 1.0, 1 / k0
    A, C = b^2 / (2γ), b * τ - γ * τ^2 / 2
    B2 = 2A + L
    return (B2 - sqrt(B2^2 - 4A * (A - C))) / (2A)
end

kstar(; k0, L=2.0, σ=0.5, q=1.0) = best_k(; b=1.0, γ=1 / k0, L, τ, σ, q)

println("== Prop 2: k* < k0 on a grid of parameter values")
cases = [(k0, L, σ, q) for k0 in 0.5:0.5:8, L in (0.0, 1.0, 2.0, 4.0), σ in (0.2, 0.5, 1.0, 2.0), q in (0.1, 0.5, 1.0)]
viol = count(c -> kstar(; k0=c[1], L=c[2], σ=c[3], q=c[4]) > c[1] + 1e-6, cases)
maxgap = maximum(c -> kstar(; k0=c[1], L=c[2], σ=c[3], q=c[4]) - c[1], cases)
println("cases: $(length(cases)), violations (k* > k0 + 1e-6): $viol, largest k* - k0: $(round(maxgap, sigdigits=3))")

println("\n== Prop 3: safety margin, exact vs approximation (k0 = 4.5, L = 2, q = 1)")
open(joinpath(outdir, "stage1_margin.csv"), "w") do io
    println(io, "sigma,margin_exact,margin_approx")
    for σ in 0.05:0.05:1.5
        me = τ - kstar(; k0=4.5, σ)
        ma = margin_approx(; b=1.0, γ=1 / 4.5, L=2.0, σ, q=1.0)
        println(io, "$σ,$me,$ma")
        σ in (0.1, 0.25, 0.5, 1.0) && @printf("σ=%.2f exact %.3f approx %.3f\n", σ, me, ma)
    end
end

println("\n== Prop 4: defy threshold q̂(k0), σ → 0 formula vs numerical boundary at σ = 0.25")
open(joinpath(outdir, "stage1_regimes.csv"), "w") do io
    println(io, "k0,q_hat_limit,q_hat_sigma025")
    for k0 in 3.1:0.1:9.0
        qh = q_defy(; k0, L=2.0)
        # numerical: largest q on a grid for which k* > τ
        qs = 0.0:0.0025:0.6
        defy = [q for q in qs if q > 0 && kstar(; k0, L=2.0, σ=0.25, q) > τ]
        qn = isempty(defy) ? 0.0 : maximum(defy)
        println(io, "$k0,$qh,$qn")
        k0 in (4.5, 6.0, 7.5) && @printf("k0=%.1f  q̂ limit %.3f  numerical(σ=.25) %.3f\n", k0, qh, qn)
    end
end

println("\n== Two hills example (k0 = 7.5, σ = 0.25)")
for q in (0.05, 0.10, 0.20, 0.50)
    lm = local_maxima(; b=1.0, γ=1 / 7.5, L=2.0, σ=0.25, q)
    @printf("q=%.2f  local maxima: %s  global k* = %.2f\n", q,
        join([@sprintf("k=%.2f U=%.2f", k, u) for (k, u) in lm], "; "), kstar(; k0=7.5, σ=0.25, q))
end
open(joinpath(outdir, "stage1_two_hills.csv"), "w") do io
    println(io, "k,U_q05,U_q10,U_q50,U_norule")
    for k in 0:0.02:9
        us = [payoff(k; b=1.0, γ=1 / 7.5, L=2.0, τ, σ=0.25, q) for q in (0.05, 0.10, 0.50)]
        println(io, "$k,$(us[1]),$(us[2]),$(us[3]),$(k - k^2 / 15)")
    end
end

println("\n== Prop 5: signs of comparative statics (comply regime, finite differences)")
function sign_check(param; base=(k0=4.5, L=2.0, σ=0.5, q=1.0), h=0.01)
    up = merge(base, NamedTuple{(param,)}((getfield(base, param) + h,)))
    dn = merge(base, NamedTuple{(param,)}((getfield(base, param) - h,)))
    (kstar(; up...) - kstar(; dn...)) / (2h)
end
for p in (:L, :q, :σ, :k0)
    @printf("dk*/d%s = %+.3f\n", p, sign_check(p))
end
# τ separately (it is a constant above)
dτ = (best_k(; b=1.0, γ=1 / 4.5, L=2.0, τ=3.01, σ=0.5, q=1.0) - best_k(; b=1.0, γ=1 / 4.5, L=2.0, τ=2.99, σ=0.5, q=1.0)) / 0.02
@printf("dk*/dτ = %+.3f\n", dτ)

open(joinpath(outdir, "stage1_statics.csv"), "w") do io
    println(io, "x,param,kstar")
    for L in 0:0.1:6; println(io, "$L,L,$(kstar(; k0=4.5, L))"); end
    for q in 0.05:0.025:1; println(io, "$q,q,$(kstar(; k0=4.5, q))"); end
    for σ in 0.1:0.05:2.5; println(io, "$σ,sigma,$(kstar(; k0=4.5, σ))"); end
    for t in 1.5:0.1:5; println(io, "$t,tau,$(best_k(; b=1.0, γ=1/4.5, L=2.0, τ=t, σ=0.5, q=1.0))"); end
end
println("\nCSV files written to model/output/")
