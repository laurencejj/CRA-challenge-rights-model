# Same cases as the Python prototype; values should match to the grid step.
include("ChallengeModel.jl"); using .ChallengeModel
for (b, σ, expected) in [(1.5, 0.5, 2.082), (1.0, 0.25, 2.342), (2.5, 1.0, 1.918)]
    k = best_k(; b, γ=1/3, L=2.0, σ)
    println("b=$b σ=$σ  k*=$(round(k, digits=2))  (python ≈ $expected)")
end
