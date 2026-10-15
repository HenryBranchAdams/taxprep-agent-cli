# Coverage and limitations

## Implemented content

35 modules; 466 explicit questions; 264 activation rules; 234 support templates; 19 cross-topic routes; 122 distinct form/schedule/obligation candidate labels; 60 official references.

The structural DAG has 1,280 nodes and 1,784 edges. Those totals include screening, questions, rules, support units, form candidates and route tasks—not just taxpayer questions.

| Topic | Questions | Rules | Scope |
|---|---:|---:|---|
| CORE — Scope, baseline and permissions | 13 | 9 | detailed_intake |
| PERSON — People and dependency | 23 | 11 | detailed_intake |
| STATUS — Filing status and household tests | 12 | 6 | detailed_intake |
| STATE — Residence, work locations and state/local obligations | 12 | 3 | intake_plus_required_jurisdiction_adapter |
| WAGE — Employment, tips, overtime and equity pay | 17 | 11 | detailed_intake |
| INVEST — Interest, dividends and investment accounts | 13 | 8 | detailed_intake |
| DISPOSE — Sales, exchanges and adjusted basis | 16 | 14 | detailed_intake |
| DIGITAL — Digital assets and wallet reconciliation | 13 | 7 | detailed_intake |
| RETIRE — Retirement contributions, distributions and conversions | 25 | 17 | detailed_intake |
| BUSINESS — Self-employment and closely held business | 22 | 22 | detailed_intake |
| RENTAL — Rental real estate and royalties | 21 | 11 | detailed_intake |
| PASS — Pass-through interests and K-1s | 15 | 9 | detailed_intake |
| OTHER — Other income and nontaxable receipts | 12 | 10 | detailed_intake |
| HOME — Sale of a principal residence | 10 | 3 | detailed_intake |
| ADJUST — Adjustments and special deductions | 9 | 7 | detailed_intake |
| ITEMIZE — Standard versus itemized deductions | 13 | 6 | detailed_intake |
| CHARITY — Charitable contributions and appraisals | 11 | 6 | detailed_intake |
| EDUCATION — Education, scholarships and 529 coordination | 15 | 6 | detailed_intake |
| CARE — Dependent care and adoption | 14 | 4 | detailed_intake |
| HEALTH — Marketplace health coverage | 11 | 4 | detailed_intake |
| HSA — HSAs, MSAs, FSAs and ABLE accounts | 12 | 8 | detailed_intake |
| ENERGY — Home energy improvements | 8 | 3 | detailed_intake |
| VEHICLE — Vehicle credits and loan-interest deduction | 15 | 4 | detailed_intake |
| FOREIGN — International status, income, accounts and entities | 23 | 16 | detailed_intake_plus_specialist |
| DEBT — Canceled debt, foreclosure and bankruptcy | 10 | 7 | detailed_intake |
| DISASTER — Casualty, theft and disaster relief | 8 | 3 | detailed_intake |
| GIFT — Gifts, inheritances and estate-related obligations | 12 | 4 | detailed_intake |
| HOUSEHOLD — Household workers and payroll | 9 | 2 | detailed_intake |
| FARM — Farming, fishing and natural resources | 10 | 4 | detailed_intake_plus_specialist |
| CARRY — Prior-year attributes and carryovers | 13 | 13 | detailed_intake |
| CREDITS — Household credit eligibility screening | 10 | 7 | detailed_intake |
| TAX — Additional taxes and calculation handoffs | 10 | 7 | detailed_intake |
| PAY — Withholding, payments, refunds and notices | 11 | 6 | detailed_intake |
| SPECIAL — Military, clergy and uncommon situations | 6 | 5 | screening_plus_specialist |
| CLOSE — Completeness, exceptions and preparer handoff | 12 | 1 | detailed_intake |

## What the code actually does

Evaluates three-valued predicates, reveals conditional questions, instantiates repeatable tracks, creates specific support requirements and candidate forms, tracks manual evidence verification and reviewed decisions, invalidates changed-context work, preserves inactive evidence, produces open-item reports, and validates structural DAG integrity. It does not search external accounts.

## What still requires a preparer or an implemented adapter

Numeric tax computations; legal filing-status eligibility; income and deduction thresholds; modified AGI; coordinated credits and limitations; loss ordering; contribution eligibility/limits; tax basis calculations; precise return line values; state/local law; foreign/nonresident full return preparation; entity returns; independent filing deadlines; actual form rendering; e-filing; signatures; payments; professional review and legal sufficiency. Some catalog questions deliberately ask whether a specialized test may apply; that opens support/review work rather than pretending the test has already been computed.

All emitted forms are candidates. Broad candidate groups can contain alternatives that will be ruled out later. The agent should narrow them using evidence and authoritative instructions, not present them as forms the filer definitely must submit. Many uncommon fact patterns are recognized only as specialist handoffs. A reviewed handoff must attach a sufficiently detailed external questionnaire/support/decision record.

## Exhaustiveness and maintenance

No finite handwritten catalog here is certified to encode every statutory exception, historical year, jurisdiction, election or litigation-driven fact pattern. The claim is broad detailed intake coverage with mandatory uncertainty/exception handling. A generic Other/Unresolved selection activates an extension review instead of silently clearing the branch. Production coverage requires independent subject-matter review, law-version tests and a maintained jurisdiction/exception registry.

2025 is pinned as the reference tax year. Another answered year creates a non-waivable version issue. References were checked on October 14, 2026, but official pages can change. Several specialized instructions retain older published revision dates. A source link and edition label do not constitute a frozen content snapshot; archive approved source versions and review later corrections before production use.

## Security and technical boundaries

The HTML is self-contained and local-only, with no automatic persistent storage, external scripts, analytics or network calls. Exported JSON is unencrypted. It is not a secure document vault. There is no authenticated reviewer role enforcement, encrypted backend, permission broker, conflict-safe multi-user database, automatic document hashing or immutable audit service. The audit list and FNV content fingerprint are useful prototype safeguards but not tamper-proof records.

Only current fact-context changes are detected by the fingerprint; replacing a source file without changing answers requires explicit re-verification. Identical facts restored to an earlier context can restore its matching verification. Human attestations are not independently verified by software. The final state is READY_FOR_PREPARER_REVIEW, never READY_TO_FILE.

## Validation scope

Python unit tests and browser tests cover branching behavior, unknowns, owner/instance separation, verification gates, stale decisions, exclusions, import/export and browser/Python parity. They do not establish the correctness of tax results or exhaustive legal coverage. Consult the exact checked-in test results.

## Official source register

### P17 — Publication 17: Federal income tax
- URL: https://www.irs.gov/publications/p17
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P501 — Publication 501: Dependents and filing status
- URL: https://www.irs.gov/publications/p501
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P519 — Publication 519: U.S. tax guide for aliens
- URL: https://www.irs.gov/publications/p519
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P550 — Publication 550: Investment income
- URL: https://www.irs.gov/publications/p550
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P590B — Publication 590B: IRA distributions
- URL: https://www.irs.gov/publications/p590b
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P590A — Publication 590A: IRA contributions
- URL: https://www.irs.gov/publications/p590a
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P970 — Publication 970: Education benefits
- URL: https://www.irs.gov/publications/p970
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P527 — Publication 527: Residential rental property
- URL: https://www.irs.gov/publications/p527
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P334 — Publication 334: Small business
- URL: https://www.irs.gov/publications/p334
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P502 — Publication 502: Medical expenses
- URL: https://www.irs.gov/publications/p502
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P503 — Publication 503: Dependent care
- URL: https://www.irs.gov/publications/p503
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P523 — Publication 523: Selling a home
- URL: https://www.irs.gov/publications/p523
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P525 — Publication 525: Taxable and nontaxable income
- URL: https://www.irs.gov/publications/p525
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P526 — Publication 526: Charitable contributions
- URL: https://www.irs.gov/publications/p526
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P559 — Publication 559: Survivors and estates
- URL: https://www.irs.gov/publications/p559
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P596 — Publication 596: Earned income credit
- URL: https://www.irs.gov/publications/p596
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P969 — Publication 969: HSA and other health plans
- URL: https://www.irs.gov/publications/p969
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P504 — Publication 504: Divorce and separation
- URL: https://www.irs.gov/publications/p504
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P541 — Publication 541: Partnerships
- URL: https://www.irs.gov/publications/p541
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P925 — Publication 925: Passive activity and at-risk rules
- URL: https://www.irs.gov/publications/p925
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P547 — Publication 547: Casualties and disasters
- URL: https://www.irs.gov/publications/p547
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P4681 — Publication 4681: Canceled debt
- URL: https://www.irs.gov/publications/p4681
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P936 — Publication 936: Mortgage interest
- URL: https://www.irs.gov/publications/p936
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P561 — Publication 561: Donated property valuation
- URL: https://www.irs.gov/publications/p561
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P54 — Publication 54: Citizens and residents abroad
- URL: https://www.irs.gov/publications/p54
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P463 — Publication 463: Travel and vehicle expenses
- URL: https://www.irs.gov/publications/p463
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P587 — Publication 587: Home office
- URL: https://www.irs.gov/publications/p587
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P225 — Publication 225: Farming
- URL: https://www.irs.gov/publications/p225
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P570 — Publication 570: Territories
- URL: https://www.irs.gov/publications/p570
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P544 — Publication 544: Property dispositions
- URL: https://www.irs.gov/publications/p544
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### P551 — Publication 551: Property basis
- URL: https://www.irs.gov/publications/p551
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I1040GI — Instructions: 1040 and Schedules 1, 1-A, 2, 3
- URL: https://www.irs.gov/instructions/i1040gi
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8962 — Instructions: Premium tax credit
- URL: https://www.irs.gov/instructions/i8962
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8606 — Instructions: Nondeductible IRAs
- URL: https://www.irs.gov/instructions/i8606
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8949 — Instructions: Capital dispositions
- URL: https://www.irs.gov/instructions/i8949
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I5695 — Instructions: Residential energy credits
- URL: https://www.irs.gov/instructions/i5695
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8936 — Instructions: Clean vehicle credits
- URL: https://www.irs.gov/instructions/i8936
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I1040SCA — Instructions: Itemized deductions
- URL: https://www.irs.gov/instructions/i1040sca
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8283 — Instructions: Noncash charitable contributions
- URL: https://www.irs.gov/instructions/i8283
- Edition: 12/2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8839 — Instructions: Adoption
- URL: https://www.irs.gov/instructions/i8839
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I4547 — Instructions: Trump account elections
- URL: https://www.irs.gov/instructions/i4547
- Edition: 12/2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8938 — Instructions: Specified foreign financial assets
- URL: https://www.irs.gov/instructions/i8938
- Edition: 11/2021
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I3520 — Instructions: Foreign trusts and gifts
- URL: https://www.irs.gov/instructions/i3520
- Edition: 12/2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8621 — Instructions: PFIC reporting
- URL: https://www.irs.gov/instructions/i8621
- Edition: 12/2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I5471 — Instructions: Foreign corporations
- URL: https://www.irs.gov/instructions/i5471
- Edition: 12/2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8865 — Instructions: Foreign partnerships
- URL: https://www.irs.gov/instructions/i8865
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8858 — Instructions: Foreign disregarded entities and branches
- URL: https://www.irs.gov/instructions/i8858
- Edition: 12/2024
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I709 — Instructions: Gift and GST tax
- URL: https://www.irs.gov/instructions/i709
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I1040SH — Instructions: Household employment
- URL: https://www.irs.gov/instructions/i1040sh
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I1040NR — Instructions: Nonresident individual returns
- URL: https://www.irs.gov/instructions/i1040nr
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I5329 — Instructions: Retirement and savings account additional taxes
- URL: https://www.irs.gov/instructions/i5329
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I7203 — Instructions: S corporation shareholder basis
- URL: https://www.irs.gov/instructions/i7203
- Edition: 12/2022
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8995 — Instructions: Qualified business income
- URL: https://www.irs.gov/instructions/i8995
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8960 — Instructions: Net investment income tax
- URL: https://www.irs.gov/instructions/i8960
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I8959 — Instructions: Additional Medicare tax
- URL: https://www.irs.gov/instructions/i8959
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I6251 — Instructions: Alternative minimum tax
- URL: https://www.irs.gov/instructions/i6251
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### I1116 — Instructions: Foreign tax credit
- URL: https://www.irs.gov/instructions/i1116
- Edition: 2025
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### DIGITAL — IRS digital assets guidance
- URL: https://www.irs.gov/filing/digital-assets
- Edition: Current guidance
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### FBAR — FinCEN foreign account reporting
- URL: https://www.fincen.gov/report-foreign-bank-and-financial-accounts
- Edition: Current guidance
- Checked: 2026-10-14
- Note: Routing and evidence reference; verify relevant section before a legal conclusion.

### INTAKE — IRS intake and interview process
- URL: https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp
- Edition: Current process guidance
- Checked: 2026-10-14
- Note: Design reference only, not a declaration that this organizer is VITA in-scope.

