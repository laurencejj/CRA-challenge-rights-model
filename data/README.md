# Data

## In this folder
| File | What it is | Source |
|---|---|---|
| `rbc_factors_life.csv` | Life insurer capital charge (pre-tax %) for each of the 20 NAIC designations, with rating equivalents | Mayer Brown, *NAIC investment-related developments*, Dec 2024, slide 10 (factors adopted for year-end 2021) |
| `calibration_targets.csv` | Published numbers the model should match: pre-rule gaps by agency tier, share above 3 notches, PLR holdings, spread premium | Fitch (Dec 2024, citing the withdrawn NAIC 2023 sample), Drexler–Polacek 2026, Li–Oh–Ricciardi 2026, Morgan Lewis (Aug 2024) |

The NAIC 2023 sample (109 securities) was later withdrawn by the NAIC as too limited. We use it as a calibration target only, and say so in the paper.

## What we would need to test the predictions
| Need | Source | Cost |
|---|---|---|
| Bond-by-bond holdings with NAIC designation and the "PL" / "FE" symbol (Schedule D Part 1; trades in Parts 3–4) | NAIC statutory filings via S&P Capital IQ Pro (insurance statutory module), as in Drexler–Polacek 2026 and Becker–Opp–Saidi 2022. Notch-level designations start at year-end 2020 | Paid. Check that the university licence covers the statutory module; the NAIC also licenses data directly (price not checked) |
| Public ratings and bond details to compare with | Mergent FISD via WRDS; TRACE via WRDS (public bonds only) | Paid (WRDS) |
| Aggregate exposure, agency shares | NAIC Capital Markets Bureau reports; SEC annual NRSRO staff report | Free |
| Rule texts and any challenge summaries | NAIC VOSTF and Credit Rating Provider (E) Working Group meeting materials | Free |

Post-rule filings (year-end 2026) arrive around March 2027.

## What is deliberately not here
- Laurence's PhD bank panel and any results derived from it. Those stay on his device and in the private project folder.
- Licensed S&P Capital IQ extracts.
