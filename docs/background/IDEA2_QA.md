> *Copied from the project folder (paper1/ideas/IDEA2_QA.md) on 16 Oct 2026. Links to ../lit/papers/ point to the project folder; the papers used here are in [literature/papers/](../../literature/papers/).*

# Idea 2 (challenge rights in private credit): questions and answers

*16 Oct 2026. This answers Laurence's eight questions. It updates [THREE_IDEAS.md](THREE_IDEAS.md) §2 on one point: **the 3-notch gap is not an automatic trigger** (see Q5).*

## Q1. What is the NAIC?
The National Association of Insurance Commissioners is the standard-setting body of the 50 US state insurance regulators. US insurers are regulated by states, not federally. The NAIC writes the model laws, the statutory accounting rules and the risk-based capital (RBC) formulas that the states adopt. Its committees decide investment rules; the relevant ones are the Financial Condition (E) Committee and its Valuation of Securities (E) Task Force.

## Q2. What is the SVO?
The Securities Valuation Office sits inside the NAIC's Investment Analysis Office. It assigns **NAIC Designations** (1 to 6, with 20 finer categories since 2021), and those designations set each bond's RBC charge.
- **Two routes to a designation.** The SVO produces a designation itself (the "filed" route). Alternatively, a bond rated by an approved credit rating provider (CRP) gets a designation mapped mechanically from that rating. This second route is called **filing exempt (FE)**.
- **Most bonds use FE.** Over 80% of insurers' bonds are FE (Mayer Brown, Dec 2024). Private letter ratings (PLRs) are FE ratings that are not public.
- **So the SVO is the regulator's own credit shop.** Its view (σ in the model) is what a challenge compares against.

## Q3. Is it just life insurers?
**The rule covers every insurer that files with the SVO: life, P&C, health and fraternal.** The exposure, though, is concentrated in life insurers:
- **Who holds PLRs.** Life insurers held about $478bn of PLR securities in 2025, about 8% of general-account assets (Drexler–Polacek 2026). Across all US insurers the figure was about $350bn at end-2023, about 7% of bonds (Fitch Dec 2024, citing the NAIC). Insurers affiliated with private equity or asset managers held about 17%.
- **Why life insurers.** They hold long, illiquid private credit to back annuities, and their RBC is the most sensitive to designations.

So the model's natural agent is a life insurer. P&C insurers give a low-exposure comparison group in any empirical work.

## Q4. Has anyone examined this before?
**On theory, I found no paper** that models a regulator's right to challenge individual capital-setting ratings in a market with no price. The nearest are:
- **Opp–Opp–Harris (2013):** regulatory reliance causes inflation, with no audit.
- **Stolper (2009, JBF):** the regulator approves agencies on their aggregate track record.
- **Piccolo–Shapiro (2022, RFS):** prices discipline agencies. This channel is missing in private credit.

**The empirical work is new (2026) and model-free:**
- **Li, Oh & Ricciardi (Columbia WP):** PLR bonds impair about twice as often as same-grade public bonds, implying an extra $4–4.5bn a year of capital.
- **Drexler & Polacek (Chicago Fed WP 2026-17):** PLR use jumped among insurers most exposed to a proposed capital change, with about 3 notches of inflation in investment grade.
- **Meisenzahl, Overpeck & Polacek (Chicago Fed 2025):** documents life insurers' move into private credit.
- **Policy pieces:** Fitch (Dec 2024), the KBRA rebuttal (Jun 2026), FSB (2026) and IMF GFSR notes.
- **NAIC's own 2024 study:** it found 109 PLR securities rated about 2.7 notches above the SVO view on average. It was withdrawn after industry pushback.

**Earlier NAIC reforms that are good comparators:**
- the 2009–10 replacement of ratings by regulator-procured models for RMBS/CMBS (Becker–Opp NBER w19257; Becker–Opp–Saidi 2022 RFS; Hanley–Nikolova 2021 RCFS);
- rating-based capital pricing (Murray–Nikolova 2022 JFQA).

## Q5. Any cases of the SVO challenging ratings?
**None publicly reported, as far as I could find (searched 16 Oct 2026).**
- **Timeline.**
  - The amendment was adopted in 2024 with effect from 1 Jan 2026.
  - It was not operational at the December 2025 meeting (Mayer Brown).
  - At the Summer 2026 National Meeting it was reported "now operational" once the systems work was done (Willkie, Aug 2026).
  - KBRA (Jun 2026) described implementation as delayed.
- **Why we may not see challenges anyway.** The SVO would publish only an anonymised summary of a removal, and only where insurers can access it. Capstone expects the power to be used rarely.

**Correction to the earlier write-up.** Under the procedure (Morgan Lewis, Aug 2024):
- The SVO, or a state regulator, can question any FE rating it thinks is "not a reasonable assessment of investment risk". It weighs peer CRP ratings, yields and the rater's methodology.
- If the SVO's own view is **3 or more notches** away, a meeting of regulators and interested parties **may** be convened.
- The SVO credit committee and a task-force subcommittee then decide whether to remove the security from filing exemption. The insurer can ask for reinstatement in a later year.

So τ = 3 is the gap at which escalation becomes *possible*, not an automatic trigger. In the model this is better: d(k) is a smooth probability that rises steeply around τ, and the decision itself is a choice for the regulator. Separately, the new Credit Rating Provider (E) Working Group (from Jan 2026, with PwC) is building a due-diligence framework that could de-admit whole CRPs, with a 36-month provisional acceptance period. That gives a second lever: **rating-level challenges vs agency-level eligibility.**

## Q6. Any post-regime data? What counterfactuals can we run?
**There are no clean post-regime data yet.** The process only became operational in mid-2026, and year-end 2026 statutory filings arrive around March 2027. The pre-period and anticipation window are well covered, though:
- **Statutory Schedule D filings**, bond by bond, with the NAIC designation and the administrative symbols "FE" and "PL". These are available through S&P Capital IQ Pro, which you already use.
- **Event dates.** The 2023 SVO proposal, the 2024 adoption, the 2021 move to 20 designation categories (used by Li–Oh–Ricciardi), the PLR rationale-report requirement, and the 2026 start.
- **Anticipation tests now.** Do gaps bunch below 3 notches? Do insurers move from small to large CRPs? Do PLR filings fall after 2024?

Counterfactuals the model can run once it is calibrated to the pre-period gap distribution:
1. **Threshold rule vs a graduated haircut** (capital rising with the gap), and different values of τ.
2. **Better SVO information** (lower σ), and whether to publish the SVO's view.
3. **Regulator-produced designations** for PLR securities, as was done for RMBS in 2009–10.
4. **De-admitting a CRP tier** (the CRP Working Group lever) against rating-level challenges.
5. **A capital and stability scenario:** aggregate RBC shortfall and the scale of forced sales if many ratings are removed at once in a downturn.

## Q7. What does a structural model add?
1. **An ex-ante evaluation before the data exist.** Reduced-form work cannot say anything about the challenge right until 2027–28. The model gives out-of-sample predictions now: bunching at τ−1, migration across CRA tiers, and capital effects. Those predictions can be tested when the filings arrive, which makes a clean pre-registered-style contribution.
2. **Equilibrium responses that reduced form cannot net out.** Shopping, the choice of agency tier, and the decision to use a PLR at all respond together. The net effect on capital adequacy can be the opposite of the gross effect.
3. **Unobservables.** The bunching shape of the gap distribution identifies the SVO's precision and the strength of the deterrent. Neither is observed directly.
4. **Welfare and design.** Policy here is a choice of τ, haircut shape, disclosure and eligibility, which is a design question that needs a model. The trade-off is insurer capital adequacy against access to private credit and the cost of false challenges.
5. **Generality.** The same structure covers Basel ECAI mapping, ECB collateral eligibility and private-credit funds, which takes the paper beyond a US insurance niche.

## Q8. How do we stand apart?
- **The object is new.** This is the first model of *delegated certification with an audit right*: a regulator outsources risk measurement to private raters but keeps a costly, noisy override. The literature has delegation without audit (OOH) or approval on aggregate records (Stolper).
- **The regulator's information is explicit.** The SVO's noise σ is a primitive, which yields the result that **a threshold beats a graduated haircut when the regulator is noisy, and the reverse when it is precise**.
- **Unpriced assets.** The model sits exactly where Piccolo–Shapiro's market discipline is absent, and asks what the substitute is worth.
- **Two levers.** Rating-level challenges against agency-level eligibility, which the CRP Working Group is now designing.
- **Timing.** Predictions are made before the data arrive, then tested on 2026–27 filings in a follow-up or a final section.

## Sources
- Willkie, [NAIC Report: 2026 Summer National Meeting](https://www.willkie.com/publications/2026/08/naic-report-2026-summer-national-meeting) (process "now operational"; CRP Working Group)
- Morgan Lewis, [Update on NAIC proposals to challenge credit ratings](https://www.morganlewis.com/pubs/2024/08/update-on-naic-proposals-to-challenge-credit-ratings-for-structured-securities) (procedure and the 3-notch meeting rule)
- Mayer Brown, [NAIC Fall 2025 highlights](https://www.mayerbrown.com/en/insights/publications/2026/01/us-naic-fall-2025-national-meeting-highlights-investment-related-highlights) (not yet operational in Dec 2025)
- Capstone, [Insurers' increasing exposure to private credit](https://capstonedc.com/insights/insurers-increasing-exposure-to-private-credit-attracts-regulators-scrutiny/)
- KBRA, [A more balanced review of the NAIC PLR review process](https://www.kbra.com/publications/NqqwYmxw) (Jun 2026)
- fi-desk, [Ratings agencies spar in private ratings legitimacy debacle](https://www.fi-desk.com/rules-ratings-ratings-agencies-spar-in-private-ratings-legitimacy-debacle/) (withdrawn NAIC study)
- NAIC, [letter of 24 Sep 2026 on private credit](https://content.naic.org/sites/default/files/government-affairs-letter-20260924-warren-exposure-private-credit-equity-funds.pdf)
- PDFs of the papers cited are in `../lit/papers/private_credit_and_outlooks/`.

## Q9. What data can test this, and what is free? (added 16 Oct 2026)
| Need | Source | Cost |
|---|---|---|
| Bond-by-bond insurer holdings, with NAIC designation and the "PL"/"FE" symbol that flags a PLR (Schedule D Part 1; trades in Parts 3–4) | NAIC statutory filings via S&P Capital IQ Pro (insurance/SNL statutory module), as in Drexler–Polacek 2026 and Becker–Opp–Saidi 2022. Notch-level designations start at year-end 2020. | Paid. Check that the university licence covers the statutory module; NAIC also licenses the data directly (price not checked) |
| Public ratings to compare with PLRs, issuer/bond details | Mergent FISD via WRDS; TRACE via WRDS for public bonds only | Paid (WRDS) |
| Aggregate PLR exposure, gaps and agency shares | NAIC Capital Markets Bureau special reports; Fitch (Dec 2024), KBRA (Jun 2026), Chicago Fed, FSB and IMF pieces; the withdrawn 2024 NAIC study figures (109 securities, ~2.7 notches) | Free |
| Rule texts, timeline, any challenge summaries | NAIC VOSTF and CRP Working Group meeting materials | Free |
| Agency market shares | SEC annual NRSRO staff report | Free |
| Public rating histories | SEC 17g-7 files (already in paper1/data/17g7/). PLRs are generally not in them (inferred from the rule's scope, not checked file by file) | Free |

Free data are enough to calibrate the model lightly (gap mean, PLR share, capital charges). The bunching and tier-migration tests need Schedule D, and post-rule filings arrive around March 2027.
