> *Copied from the project folder (paper1/ideas/LIT_REVIEW.md) on 16 Oct 2026. Links to ../lit/papers/ point to the project folder; the papers used here are in [literature/papers/](../../literature/papers/).*

# Literature review for the new paper ideas

*15 Oct 2026. It builds on three earlier sources: your literature map (44 core sources plus 6 EFA/AFA papers, `literature-map/` on your device), [../lit/LIT_SCOPING.md](../lit/LIT_SCOPING.md), and the 39 papers in the repo, now catalogued in `reference/CATALOGUE.csv`. About 90 further papers were screened for this review.*

**Tags.**
- **[FT]**: the full text was read, at least the relevant sections.
- **[AB]**: only the abstract or a publisher, RePEc, NBER or SSRN record was seen.
- **[WP]**: working paper.

Every citation below was checked against a publisher, Crossref, RePEc, NBER, SSRN or author page. No DOI was guessed. Items whose details are still uncertain are marked as such.

PDFs downloaded in this round are in [../lit/papers/](../lit/papers/), in three folders. That location is the shared project folder, not the repo, for copyright reasons.

| Folder | What it holds |
|---|---|
| `verification_testing_and_cycle/` (18) | Backtesting, low-default portfolios, testing experts, procyclicality, crisis-era rating behaviour |
| `private_credit_and_outlooks/` (16) | NAIC private letter ratings, insurer capital arbitrage, outlooks and watchlists |
| `recent_theory_2019_2026/` (10) | Recent theory: ESG ratings, stress-test secrecy, rating design, man plus machine |

---

## 1. The organising map: how the literature has moved

The literature advances by making one more object endogenous (your atlas makes the same point). Here is where each object stands in October 2026.

| Object | Made endogenous by | Still exogenous or open |
|---|---|---|
| Rating bias (inflation) | BFS 2012, Mathis et al. 2009, OOH 2013, Skreta–Veldkamp 2009 | – |
| Rating precision / effort | OOH 2013, Kashyap–Kovrijnykh 2016, Bizzotto–Vigier 2021, Kartasheva–Yilmaz WP | how cheap AI precision changes incentives |
| Coarseness / rating scale | Goel–Thakor 2015, Yang 2026 WP, Saeedi–Shourideh WP | how scale interacts with verifiability |
| Market discipline from prices | Piccolo–Shapiro 2022 | markets with no price (private credit) |
| Issuer response / manipulation | Cohn–Rajan–Strobl 2024, Guo et al. 2025 | – |
| **Verification of ratings (who can tell a rating was wrong, and when)** | **reputation by default only (BFS; Bar-Isaac–Shapiro 2013; Chen–Gu–Yao 2017)** | **statistical verification, its power, and who runs it: open** |
| Regulator as active auditor | Stolper 2009 (approval on track record) | **a per-rating challenge right: open** |
| Communication tiers | Boot–Milbourn–Schmeits 2006 (watch as implicit contract) | **regulated vs soft tier under liability: open for CRAs** |

All three ideas sit in the bold rows. That is deliberate. Our own work found that the effective verification d (not the statute χ) is what moves agencies, and that d arrives with the crisis.

---

## 2. Verification as a statistical test (Idea 1)

**Verdict.** I found no CRA, certifier or forecaster model that derives the verification probability as the power of a default backtest. Such a power would depend on bucket size, PD, default correlation and horizon. I also found no model that derives the cross-section "inflation lives where backtests are weak". The time dimension is partly taken (Bar-Isaac–Shapiro; Chen–Gu–Yao), so the paper must lead with the cross-section and the one-sided-test result.

| Paper | Venue | Tag | What it does | How Idea 1 differs |
|---|---|---|---|---|
| Chen, Gu & Yao 2017, "Rating deflation versus inflation" | PBFJ 41:46–64 | FT | Reputation loss from lying scales with default probability p, so ratings inflate in booms and deflate in busts | Detection depends on p only: no N, no ρ, no test, no cross-section. **Closest paper.** |
| Bar-Isaac & Shapiro 2013 | JFE 108:62–78 | FT | Rating quality is countercyclical; monitoring is weaker when defaults are rare | Time dimension only, with exogenous detection |
| Bolton, Freixas & Shapiro 2012 | JF 67:85–111 | FT | CRA caught iff it lied and the project defaults; detection rises with precision | Detection is a single default event, not a test on a bucket |
| Pérez-Richet & Skreta 2022, "Test design under falsification" | Ecta 90:1109–42 | FT | Optimal tests when the tested party can falsify | The test designer is the principal; here the test is fixed by regulation and the CRA best-responds to its power |
| DeMarzo, Kremer & Skrzypacz 2019 | AER 109 | AB | Pass/fail minimum standards are optimal certification | Certification design, not ex-post audit of a rater |
| Asseyer & Weksler 2024 | Ecta 92(3) | AB | A transparency-maximising regulator prefers a less precise test | Bridge only |
| Olszewski & Sandroni 2009; Olszewski 2015 | AoS; Handbook GT | FT/AB | Calibration tests can be gamed by uninformed experts asymptotically | Asymptotic manipulability, not finite-sample power with rare events |
| Deb, Pai & Said 2018 | AER 108:3057–3103 | AB | Optimal evaluation of strategic forecasters | No rare events, no buckets |
| Lerch et al. 2017, "Forecaster's dilemma" | Stat. Sci. 32:106–27 | FT | Evaluating only on extreme outcomes rewards exaggeration | Statistical bridge to the crisis-timing corollary |
| Pollanen 2026, "When AAA satisfies nothing" | arXiv / SSRN WP | FT | A structured-finance AAA claim needs about 10,000:1 discrimination: AAA is statistically unverifiable at those base rates | Information limit, with no incentives. Supports the premise. |
| Pluto & Tasche 2005; Coppens et al. 2007, 2016; EBA staff paper 2026 | stats / ECB / EBA | FT | Low-default PD estimation; one-sided traffic-light and correlation-adjusted binomial tests | **The verification technology**; none models rater incentives |
| Leitner & Williams 2023, "Model secrecy and stress tests" | JF 78:1055–95 | FT (WP) | Disclosing the regulator's model invites gaming | Bridge for "should the backtest rule be public?" |
| Cornaggia, Cornaggia & Hund 2017 | RoF 21:465–509 | AB | The same letter grade carries very different default rates across asset classes | Empirical anchor for cross-class predictions |
| Griffin & Nickerson 2023 | RFS 36:2319–60 | AB | In 2020 CLO collateral was cut about 25% but tranches only about 2% | Anchor: top tranches protected where tests have no power |

**Crisis timing, a corollary of Idea 1.** On its own this idea is **not novel**:
- Ferri, Liu & Stiglitz (1999, *Economic Notes*) argue informally that agencies missed the Asian crisis, then over-downgraded to repair their reputation.
- Chen–Gu–Yao derive deflation in recessions.
- Manso (2013), Goldstein–Huang (2020), Holden–Natvik–Vigier (2018, IER) and Kiff–Kisser–Schumacher (2013, IMF WP) cover feedback and cliff effects.
- Ellul–Jotikasthira–Lundblad (2011, JFE) cover the fire sales.

It becomes new when it is derived from power. In a bust the conditional PD rises, so test power jumps for every grade at once. The predictions follow: synchronised catch-up downgrades, and statutes that bite only when the next bust arrives. That is exactly our data pattern.

Empirical anchors in your target journal:
- Ballis–Ioannidis–Sifodaskalakis (2024, JFS 73): all three agencies tightened bank ratings in 2008.
- Huang–Shen–Lin (2022, RQFA): bank issuer-rating standards were not tighter after 2008, but standalone ratings were.

---

## 3. Private credit and the regulator's challenge right (Idea 2)

**Verdict.** The core mechanism looks new. Theory has either reliance without an audit, or a regulator approving agencies on aggregate records. Nobody models a costly, threshold-triggered challenge of individual capital-setting ratings in a market with no price. The empirical papers are brand new (2026) and contain no model.

| Paper | Venue | Tag | What it does | How Idea 2 differs |
|---|---|---|---|---|
| Opp, Opp & Harris 2013 | JFE 108:46–61 | FT | Regulatory value of a high rating crowds out information acquisition | No audit or challenge |
| Ozerturk 2014, "Ratings as regulatory stamps" | JEBO 105:17–29 | AB | Regulatory reliance lowers quality, more so for complex products | No regulator verification |
| Stolper 2009 | JBF 33:1266–73 | AB | Regulator approves CRAs on track records; common shocks hide collusion | **Nearest "regulator disciplines certifier"**; approval is aggregate and ex post, not a per-rating challenge |
| Piccolo & Shapiro 2022 | RFS 35:4425–73 | AB | Prices after a rating expose errors and discipline the CRA | Private credit has no price, so the challenge right has to *replace* this channel |
| Sangiorgi & Spatt 2017 | MS 63:4016–36 | FT | Hidden shopping biases disclosed ratings | Adds capital use and a challenge right |
| Josephson & Shapiro 2020 | JFI 41 | FT | Tighter investor minimum-quality constraints raise inflation | Constraint without verification |
| Kashyap & Kovrijnykh 2016 | RFS 29:420–56 | FT | Who orders the rating shapes effort and errors | Benchmark for "regulator-ordered" ratings |
| Becker & Opp 2013/14; Becker, Opp & Saidi 2022 | NBER w19257; RFS 35(12) | FT | NAIC replaced ratings with regulator-procured models for RMBS/CMBS; capital fell about 80% | **Empirical counterpart of "regulator-produced ratings"**; no theory of the choice; welfare "beyond scope" |
| Hanley & Nikolova 2021 | RCFS 10:347–401 | AB | Same reform: fewer fire sales, more low-rated MBS | Same |
| Murray & Nikolova 2022 | JFQA 57 | AB | Rating-based capital distorts prices near the IG boundary | Pricing side |
| Li, Oh & Ricciardi 2026, "Rating without market discipline" | Columbia WP | AB | PLR bonds impair about 2× as often as same-grade public bonds; about $4.5bn/yr capital shortfall | Empirical only |
| Drexler & Polacek 2026, "Market knows best" | Chicago Fed WP 2026-17 | FT (intro) | Insurers most exposed to a capital change raised PLR use most; about 3 notches of inflation in IG | Empirical only |
| Leitner & Williams 2023 | JF 78 | FT (WP) | Secrecy vs gaming of the regulator's model | Should the SVO's methodology be public? |

**Institutional facts to calibrate with.** Sources: Fitch Dec 2024 white paper (citing NAIC CMB June 2024); Drexler–Polacek 2026; Akin Gump client note; KBRA rebuttal.
- US insurers held about $350bn of PLR securities at end-2023, about 7% of bonds. Life insurers held $478bn in 2025, 8% of general-account assets.
- Small CRAs issued about 86% of PLRs at end-2023, up from 69% in 2019.
- NAIC 2023 sample:
  - 106 of 109 PLRs were rated above the SVO's view.
  - The average gap was about 3.0 notches for small CRAs and 1.9 for large ones.
  - 36% were more than 3 notches above, and 17 crossed from HY to IG.
  - The NAIC later withdrew this sample as "limited".
- The rule:
  - The SVO may challenge a PLR that is at least 3 notches above its own view.
  - If the challenge is upheld, the SVO designation or another CRA's rating applies.
  - Effective around 1 Jan 2026, with a Credit Rating Provider (E) Working Group overseeing it. **I could not confirm final adoption or that any challenge has been made.**

---

## 4. Two-tier signals: ratings vs outlooks and watches (Idea 3)

**Verdict.** The idea is partly anticipated in general form but new for CRAs.
- The abstract mechanism is Bertomeu & Marinovic (2016, TAR), "A theory of hard and soft information": mandating hard disclosure degrades soft information. It has no liability, no posture choice and no rating-contingent contracts.
- For CRAs, the theory is Boot–Milbourn–Schmeits (2006, RFS), where the watch is an implicit contract that induces issuer effort.
- Nobody asks how penalties on rating errors, or hard-wiring outlooks into contracts and rules, move information between the tiers.

| Paper | Venue | Tag | What it does | How Idea 3 differs |
|---|---|---|---|---|
| Boot, Milbourn & Schmeits 2006 | RFS 19:81–118 | AB | Watch as an implicit contract for issuer recovery effort | No error penalties, no regulated/unregulated split |
| Bertomeu & Marinovic 2016 | TAR | AB | Hard vs soft channels; mandatory hard disclosure crowds out soft | Not a CRA model, no liability, no hard-wiring |
| Goel & Thakor 2015 | JFE 115:541–57 | FT | Coarse ratings limit inflation in cheap talk | The finer information could live in outlooks; not modelled |
| Herpfer & Maturana 2026, "Who prices credit rating inflation?" | JFQA 61 | FT | CRAs delay downgrades when performance-sensitive debt makes them costly; banks price this | Soft-tier forbearance evidence |
| Acharya et al. 2022, "Exorbitant privilege?" | NY Fed SR 1004 | FT | Sluggish downgrades of prospective fallen angels at BBB− in 2020 | The systemic-shock case of Idea 3 |
| Bannier & Hirsch 2010 | JBF 34:3037–49 | FT (WP) | The watch carries information for strong issuers and works as a monitoring contract for weak ones | Empirical baseline |
| Poon & Shen 2020 | RQFA 55:1063–91 | FT | Outlooks and watches predict EDF; negative outlooks induce recovery effort | Empirical baseline |
| Kiesel & Riehl 2024 | BAR | AB | Reviews for downgrade make acquirers 42.8% more likely to withdraw deals | Soft tier has real effects |
| Saeedi & Shourideh WP 2026; Yang WP 2026 | WP | FT/AB | Optimal censorship / grade count under moral hazard | Single-tier design |

**Institutional facts.**
- The EU regulates outlooks and watches (CRA III, Reg. 462/2013, including the sovereign calendar); the US does not in the same way. That gives a natural EU vs US contrast.
- Moody's CLO methodology notched negative outlooks −1 and reviews for downgrade −2. That is hard-wiring in practice (2020 request for comment).

---

## 5. Other recent theory a referee will expect to see cited

- **Rating design and certification:** Bizzotto–Vigier 2021 AEJ:Micro (contingent fees); Weksler–Zik 2023 AEJ:Micro (voluntary vs mandatory disclosure of ratings); Celik–Strausz 2026 ReStud; Vellodi 2026 TE; Hörner–Lambert 2021 ReStud; Choi–Mukherjee 2020 RAND; Parlour–Rajan 2020 RFS (contracting on ratings and prices).
- **Markets and structure:** Chu–Rysman 2019 AER (structural CMBS rating auctions); Daley–Green–Vanasco 2020 JF; Azarmsa–Shapiro 2026 JF (ESG raters specialise or generalise).
- **Regulator testing:** Shapiro–Zeng 2024 RFS (stress-test toughness as a signal).
- **Empirical:** Bernstein–Frydman–Hilt 2026 JPE (ratings had value before any regulatory use); Kim–Park–Wilson 2026 JFQA (credibility of mandated CRA disclosure); Cole–Cooley 2023 RED; Cao–Jiang–Wang–Yang 2024 JFE (man plus machine); Kempf–Tsoutsoura 2021 JF.
- **New versions of papers you already have:** Bayona–Peia–Vlahu is now in MS (2026); Cohn–Rajan–Strobl in RoF (2024).

## 6. Still to check before claiming novelty in a manuscript
- Full texts of Chen–Gu–Yao 2017 (Idea 1), Stolper 2009 (Idea 2) and Bertomeu–Marinovic 2016 (Idea 3). These are the three closest papers.
- Feng, Keppo & Li 2025 SSRN, "Credit rating design under adverse selection". I saw the title only.
- Whether the NAIC's challenge rule was finally adopted, and whether any challenge has been made.
- Cornaggia–Cornaggia–Hund published table values. The cross-class numbers quoted in the notes come from the WP.
