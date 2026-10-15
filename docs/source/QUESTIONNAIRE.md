# Complete conditional tax questionnaire

U.S. federal individual preparation organization · Tax year 2025 · 466 questions · 264 activation rules · 234 support templates

**Read this as a conditional rulebook, not as 466 questions everyone must answer.** A topic can apply alongside many others. Repeat every active instance-based track for each identified person, source, account, property or activity. Unknown answers remain open. No/false closes only the condition it actually answers.

Every form below is a candidate pending a supported applicability decision. Evidence requests identify source records/workpapers, not automatic return attachments. This is extensive intake coverage—not an exhaustive legal or tax-calculation engine. State/local, nonresident, entity and specialized modules require reviewed adapters. See AGENT_RUNBOOK.md and COVERAGE_AND_LIMITS.md.

## Topics

- [CORE — Scope, baseline and permissions](#core) · 13 questions / 9 rules
- [PERSON — People and dependency](#person) · 23 questions / 11 rules
- [STATUS — Filing status and household tests](#status) · 12 questions / 6 rules
- [STATE — Residence, work locations and state/local obligations](#state) · 12 questions / 3 rules
- [WAGE — Employment, tips, overtime and equity pay](#wage) · 17 questions / 11 rules
- [INVEST — Interest, dividends and investment accounts](#invest) · 13 questions / 8 rules
- [DISPOSE — Sales, exchanges and adjusted basis](#dispose) · 16 questions / 14 rules
- [DIGITAL — Digital assets and wallet reconciliation](#digital) · 13 questions / 7 rules
- [RETIRE — Retirement contributions, distributions and conversions](#retire) · 25 questions / 17 rules
- [BUSINESS — Self-employment and closely held business](#business) · 22 questions / 22 rules
- [RENTAL — Rental real estate and royalties](#rental) · 21 questions / 11 rules
- [PASS — Pass-through interests and K-1s](#pass) · 15 questions / 9 rules
- [OTHER — Other income and nontaxable receipts](#other) · 12 questions / 10 rules
- [HOME — Sale of a principal residence](#home) · 10 questions / 3 rules
- [ADJUST — Adjustments and special deductions](#adjust) · 9 questions / 7 rules
- [ITEMIZE — Standard versus itemized deductions](#itemize) · 13 questions / 6 rules
- [CHARITY — Charitable contributions and appraisals](#charity) · 11 questions / 6 rules
- [EDUCATION — Education, scholarships and 529 coordination](#education) · 15 questions / 6 rules
- [CARE — Dependent care and adoption](#care) · 14 questions / 4 rules
- [HEALTH — Marketplace health coverage](#health) · 11 questions / 4 rules
- [HSA — HSAs, MSAs, FSAs and ABLE accounts](#hsa) · 12 questions / 8 rules
- [ENERGY — Home energy improvements](#energy) · 8 questions / 3 rules
- [VEHICLE — Vehicle credits and loan-interest deduction](#vehicle) · 15 questions / 4 rules
- [FOREIGN — International status, income, accounts and entities](#foreign) · 23 questions / 16 rules
- [DEBT — Canceled debt, foreclosure and bankruptcy](#debt) · 10 questions / 7 rules
- [DISASTER — Casualty, theft and disaster relief](#disaster) · 8 questions / 3 rules
- [GIFT — Gifts, inheritances and estate-related obligations](#gift) · 12 questions / 4 rules
- [HOUSEHOLD — Household workers and payroll](#household) · 9 questions / 2 rules
- [FARM — Farming, fishing and natural resources](#farm) · 10 questions / 4 rules
- [CARRY — Prior-year attributes and carryovers](#carry) · 13 questions / 13 rules
- [CREDITS — Household credit eligibility screening](#credits) · 10 questions / 7 rules
- [TAX — Additional taxes and calculation handoffs](#tax) · 10 questions / 7 rules
- [PAY — Withholding, payments, refunds and notices](#pay) · 11 questions / 6 rules
- [SPECIAL — Military, clergy and uncommon situations](#special) · 6 questions / 5 rules
- [CLOSE — Completeness, exceptions and preparer handoff](#close) · 12 questions / 1 rules

<a id="core"></a>
## CORE — Scope, baseline and permissions

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CORE.year — Which tax year is being organized?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.
This rule pack is for 2025. Any other year creates a blocking rule-version exception.

#### CORE.return_kind — Is this an original return, an amendment, or an unfiled prior-year return?

**IF:** `Always within this active topic`
**Answer:** enum · Original / Amended / Unfiled prior year. Unknown/conflict does not become false.

#### CORE.person_type — Is the filer an individual rather than a trust, estate or business entity?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.calendar — Does the individual use a calendar tax year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.prior — Was a federal or state return filed for the preceding year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.prior_missing — Is any prior return, basis history, election or carryover workpaper unavailable?

**IF:** `CORE.prior = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.notices — Were any IRS/state notices, examination adjustments or credit disallowances received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.identity_issue — Is there identity theft, a duplicate return, a name/TIN mismatch or an IP PIN issue?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.extension — Was an extension already submitted or an extension payment made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.special_deadline — Could disaster relief, overseas status, military service, death or another event change a deadline?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.authorized_sources — List the repositories the agent is authorized to search.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.
Read-only source access is separate from filing, contacting people, requesting transcripts, or making payments.

#### CORE.unusual — Is there any transaction, document code, court case, election or situation not covered elsewhere?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CORE.unusual_detail — Describe the uncovered issue and name the records that may explain it.

**IF:** `CORE.unusual = true`
**Answer:** text. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CORE.prior_packet — Recover previous-year starting balances

**IF:** `CORE.prior = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Prior filed federal and state returns, all schedules and carryover workpapers** (`PRIOR`; support)
  - Extract/match: tax year; filing status; dependents; AGI; elections; carryovers; filed version
  - Look in: Taxpayer tax folder; prior preparer portal; authorized IRS transcript access
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: IRS return transcripts can help reconstruct a missing filed return but do not replace all basis, election, state, or carryover workpapers.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.wrong_year — Unsupported tax-year rule pack

**IF:** `CORE.year != 2025`
**THEN, form candidates:** None implied by this rule alone.
**Review gate:** BLOCK: load and validate a rule pack for the actual year before determining forms, eligibility or deadlines.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.nonindividual — Nonindividual return scope

**IF:** `CORE.person_type = false`
**THEN, form candidates:** None implied by this rule alone.
**Review gate:** BLOCK: create a separate entity/estate/trust return workflow. This organizer is not its return engine.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.amend — Originally filed return and amendment change log

**IF:** `CORE.return_kind = "Amended"`
**THEN, form candidates:** 1040-X (individual_return_or_workpaper)
- **Support: Originally filed return and amendment change log** (`CORE.doc_amend`; support)
  - Extract/match: original return; all amendments; changed documents; original payments; refund timing; explanation; state effects
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review amendment deadlines, affected years and linked state amendments; do not overwrite the original filing.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.notices — Full IRS and state notice packet

**IF:** `CORE.notices = true`
**THEN, form candidates:** 8862 (individual_return_or_workpaper)
- **Support: Full IRS and state notice packet** (`CORE.doc_notices`; support)
  - Extract/match: notice number; tax year; issue date; response deadline; adjusted items; prior responses
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Determine whether a disallowance, ban, audit adjustment or response deadline affects this return.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.identity — Identity issue and IP PIN resolution evidence

**IF:** `CORE.identity_issue = true`
**THEN, form candidates:** 14039 (separate_obligation_or_procedure)
- **Support: Identity issue and IP PIN resolution evidence** (`CORE.doc_identity`; support)
  - Extract/match: secure identity reference; mismatch; affected returns; current IP PIN availability; prior rejection
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not submit a duplicate return or put an IP PIN in ordinary notes.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.extension — Extension acknowledgement and separately identified extension payments

**IF:** `CORE.extension = true`
**THEN, form candidates:** 4868 (individual_return_or_workpaper)
- **Support: Extension acknowledgement and separately identified extension payments** (`CORE.doc_extension`; support)
  - Extract/match: form or payment extension method; tax year; acceptance; date; payment designation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.deadline — Deadline relief support

**IF:** `CORE.special_deadline = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Deadline relief support** (`CORE.doc_deadline`; support)
  - Extract/match: event; jurisdiction; dates; residence; applicable IRS notice; affected obligations
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify the actual deadline for each obligation. An extension to file is not automatically an extension to pay.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### CORE.special_scope — Resolve special scope

**IF:** `(CORE.calendar = false OR CORE.prior_missing = true OR CORE.unusual = true)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not force an unsupported case through a standard branch. Preserve a named owner, next action and blocker.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="person"></a>
## PERSON — People and dependency

**Opening screen:** Mandatory: always review.
**Unit:** Repeat for each person. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### PERSON.role — What is this person’s role?

**IF:** `Always within this active topic`
**Answer:** enum · Taxpayer / Spouse / Potential dependent or supported person. Unknown/conflict does not become false.

#### PERSON.identity — Has this person’s legal name, birth date and tax ID been verified against secure records?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.citizenship — What was this person’s U.S. tax-residency situation?

**IF:** `Always within this active topic`
**Answer:** enum · U.S. citizen all year / Resident alien all year / Nonresident or dual status / Unresolved. Unknown/conflict does not become false.

#### PERSON.age — What was this person’s age on December 31, 2025?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.
Exact birth date remains in secure source records; January 1 birthdays and individual benefit rules still need review.

#### PERSON.blind — Was this person legally blind?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.disabled — Was this person permanently and totally disabled, or unable to care for themselves?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.student — Was this person a full-time student for any part of five calendar months?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.death — Did this person die during the tax year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.claimed_elsewhere — Could another taxpayer claim this person as a dependent, even if that taxpayer will not claim them?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.relationship — Describe the relationship, including adoption, foster placement or unrelated household member.

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** text. Unknown/conflict does not become false.

#### PERSON.nights — How many nights did this person live with the taxpayer, accounting for temporary absences?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** number. Unknown/conflict does not become false.

#### PERSON.absences — Were there temporary absences, a birth/death, kidnapping, placement change or another residency exception?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.own_support — Did this person provide more than half of their own total support?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.taxpayer_support — Did the taxpayer provide more than half of this person’s total support?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.gross_income — What was this person’s gross income for the qualifying-relative test?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** number. Unknown/conflict does not become false.
Retain a separate gross-income calculation; not every receipt is included in this test.

#### PERSON.joint_return — Did this person file, or plan to file, a joint return with a spouse?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.refund_only — Was that joint return filed only to recover withheld or estimated tax, with no tax liability?

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.joint_return = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.other_qualifying — Could this person be another taxpayer’s qualifying child?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.custody — Are parents divorced, separated, living apart, or disputing who claims the child?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.release — Was a Form 8332 release or revocation signed for this tax year?

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.custody = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.multiple_support — Did several people collectively provide support under a possible multiple-support agreement?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.child_income — Does a minor/student dependent have investment income or a separate filing obligation?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.

#### PERSON.trump_account — Should eligibility for the optional Form 4547 child-account election be reviewed?

**IF:** `PERSON.role = "Potential dependent or supported person"`
**Answer:** boolean. Unknown/conflict does not become false.
This is an optional account/pilot election, not automatic consent to establish an account.

### Then: required support, form candidates and review gates

#### PERSON.id_check — Verify identity for this person

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Identity and tax identification verification record** (`ID`; verification)
  - Extract/match: legal name; date of birth; taxpayer role; SSN/ITIN verification; identity document reference
  - Look in: Taxpayer secure vault
  - Accept only when: Record a secure reference and verification result. Do not put full SSNs, IP PINs, IDs, passwords or account credentials into this organizer.
  - Fallback: Use an appropriately approved identity verification method; unresolved identity discrepancies remain open.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.dependency — Person-specific dependency and support worksheet

**IF:** `PERSON.role = "Potential dependent or supported person"`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); Schedule 8812 (individual_return_or_workpaper); Schedule EIC (individual_return_or_workpaper)
- **Support: Person-specific dependency and support worksheet** (`PERSON.doc_dependency`; support)
  - Extract/match: relationship; birth date; citizenship/residency; nights; temporary absences; own support; household support; gross income; other claimants
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Test qualifying child and qualifying relative separately; then test each benefit. Dependency, EIC, head-of-household and care-credit eligibility are not interchangeable.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.custody — Custody calendar and release/revocation records

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.custody = true)`
**THEN, form candidates:** 8332 (individual_return_or_workpaper)
- **Support: Custody calendar and release/revocation records** (`PERSON.doc_custody`; support)
  - Extract/match: overnight calendar; parents addresses; decree; actual support; current Form 8332; revocations
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** A release does not transfer head-of-household status, EIC or dependent-care benefits. Resolve tie-breakers and each benefit separately.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.multiple_support — Multiple-support agreement

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.multiple_support = true)`
**THEN, form candidates:** 2120 (individual_return_or_workpaper)
- **Support: Multiple-support agreement** (`PERSON.doc_multiple_support`; support)
  - Extract/match: contributors; total support; each share; eligible claimant; signed releases
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.child_return — Child’s income and parent-return coordination

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.child_income = true)`
**THEN, form candidates:** 8615 (individual_return_or_workpaper); 8814 (individual_return_or_workpaper)
- **Support: Child’s income and parent-return coordination** (`PERSON.doc_child_return`; support)
  - Extract/match: unearned/earned income; birth date; student status; support; parent income; parent filing status
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review kiddie-tax rules and the optional parent election separately; do not combine a child’s income by default.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.new_account — Optional child-account election support

**IF:** `(PERSON.role = "Potential dependent or supported person" AND PERSON.trump_account = true)`
**THEN, form candidates:** 4547 (individual_return_or_workpaper)
- **Support: Optional child-account election support** (`PERSON.doc_new_account`; support)
  - Extract/match: child birth date; citizenship; valid SSN verification; authorized individual; prior election/account; pilot eligibility; explicit election consent
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Trump account elections](https://www.irs.gov/instructions/i4547)

#### PERSON.disability — Benefit-specific blindness or disability support

**IF:** `(PERSON.blind = true OR PERSON.disabled = true)`
**THEN, form candidates:** Schedule R (individual_return_or_workpaper)
- **Support: Benefit-specific blindness or disability support** (`PERSON.doc_disability`; support)
  - Extract/match: medical certification if required; condition; effective date; benefit sought
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not request unnecessary medical detail; collect only proof required for the affected benefit.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.foreign_person — Foreign residency classification review

**IF:** `PERSON.citizenship is one of ["Nonresident or dual status", "Unresolved"]`
**THEN, form candidates:** 1040-NR (individual_return_or_workpaper); 8843 (individual_return_or_workpaper); 8840 (individual_return_or_workpaper)
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Open the international module; apply day-count, exempt-day, treaty and residency-election rules before determining the return family.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.deceased — Death and representative authority

**IF:** `PERSON.death = true`
**THEN, form candidates:** 1310 (individual_return_or_workpaper); 56 (individual_return_or_workpaper)
- **Support: Death and representative authority** (`PERSON.doc_deceased`; support)
  - Extract/match: date of death; representative appointment; surviving spouse; income before/after death; refund claimant
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate the final individual return from estate/trust income and independent estate obligations.
**Authority:** [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559)

#### PERSON.identity_unresolved — Person identity remains unverified

**IF:** `PERSON.identity = false`
**THEN, form candidates:** None implied by this rule alone.
**Review gate:** Resolve identity/TIN verification through the secure process before handoff.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PERSON.unmodeled_citizenship — Resolve unmodeled selection: PERSON.citizenship

**IF:** `PERSON.citizenship is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="status"></a>
## STATUS — Filing status and household tests

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### STATUS.marital — What was the legal marital status on December 31?

**IF:** `Always within this active topic`
**Answer:** enum · Never married / Married / Divorced or legally separated under qualifying decree / Widowed. Unknown/conflict does not become false.

#### STATUS.marriage_change — Was there a marriage, divorce, separation, annulment or spouse’s death during the year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.apart — Did spouses live apart throughout the last six months of the year?

**IF:** `STATUS.marital = "Married"`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.joint_consent — Are both spouses considering a joint return with informed consent?

**IF:** `STATUS.marital = "Married"`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.spouse_itemizes — Would the spouse itemize on a separate return?

**IF:** `STATUS.marital = "Married"`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.community — Did either spouse live in a community-property jurisdiction or have community income?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.house_cost — Did the taxpayer pay more than half the cost of keeping up a home?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.qualifying_person — Could a qualifying person support head-of-household or surviving-spouse status?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.widow_year — In which year did the spouse die?

**IF:** `STATUS.marital = "Widowed"`
**Answer:** number. Unknown/conflict does not become false.

#### STATUS.remarried — Did the taxpayer remarry before year-end?

**IF:** `STATUS.marital = "Widowed"`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.spouse_debt — Could joint liability, refund offset, abuse, abandonment or a spouse’s past tax debt affect filing choices?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATUS.status_selected — Which filing status has the preparer tentatively selected?

**IF:** `Always within this active topic`
**Answer:** enum · Single / Married filing jointly / Married filing separately / Head of household / Qualifying surviving spouse / Decision pending. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### STATUS.status_workpaper — Filing-status and household-cost workpaper

**IF:** `Always within this active topic`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Filing-status and household-cost workpaper** (`STATUS.doc_status_workpaper`; support)
  - Extract/match: year-end marital status; qualifying-person determination; household costs; amount taxpayer paid; legally available statuses; comparison rationale
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review all legally available statuses. Do not select a status based only on whichever refund looks largest.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### STATUS.marital_records — Marriage, divorce or separation records

**IF:** `STATUS.marriage_change = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Marriage, divorce or separation records** (`STATUS.doc_marital_records`; support)
  - Extract/match: legal effective dates; decree; support provisions; prior agreements; property division
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### STATUS.community — Community/separate income and withholding allocation

**IF:** `STATUS.community = true`
**THEN, form candidates:** 8958 (individual_return_or_workpaper)
- **Support: Community/separate income and withholding allocation** (`STATUS.doc_community`; support)
  - Extract/match: domicile; marital period; income ownership; withholding; community agreement; state law
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply jurisdiction-specific community-property rules; federal joint/separate status alone is insufficient.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### STATUS.spouse_relief — Spouse-liability or offset fact packet

**IF:** `STATUS.spouse_debt = true`
**THEN, form candidates:** 8379 (individual_return_or_workpaper); 8857 (separate_obligation_or_procedure)
- **Support: Spouse-liability or offset fact packet** (`STATUS.doc_spouse_relief`; support)
  - Extract/match: debt ownership; filing history; payment allocation; liability facts; safety-sensitive contact limits
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Injured-spouse allocation and innocent-spouse relief are different proceedings; route to qualified review and avoid unsafe contact.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### STATUS.status_pending — Filing status remains unresolved

**IF:** `STATUS.status_selected = "Decision pending"`
**THEN, form candidates:** None implied by this rule alone.
**Review gate:** Determine the eligible status using the household facts and record the selected candidate.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### STATUS.unmodeled_status_selected — Resolve unmodeled selection: STATUS.status_selected

**IF:** `STATUS.status_selected is one of ["Decision pending"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="state"></a>
## STATE — Residence, work locations and state/local obligations

**Opening screen:** Mandatory: always review.
**Unit:** Repeat for each jurisdiction. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### STATE.name — Which state, locality, U.S. territory or foreign jurisdiction is this?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### STATE.resident — Was the taxpayer domiciled or resident here at any time?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.dates — List residence dates and workdays in this jurisdiction.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### STATE.source_income — Was there income sourced here, including remote work, property, business or pass-through income?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.withholding — Was tax withheld or paid here, even if no return seems required?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.move — Did domicile change, or is residency disputed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.remote — Did the taxpayer work remotely for an employer in a different state?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.military — Could military-spouse or service-member residency relief apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.ptet — Are pass-through entity tax credits, nonresident withholding or composite payments involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.local — Could city, county, school-district, local business, use-tax or health-coverage rules apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.adjustments — Are there federal/state differences in depreciation, basis, deductions, exclusions or carryovers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### STATE.adapter — Has a tax-year-specific official jurisdiction checklist been completed and recorded?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### STATE.jurisdiction — Jurisdiction-specific filing determination

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Jurisdiction-specific filing determination** (`STATE.doc_jurisdiction`; workpaper)
  - Extract/match: domicile; days; work locations; source income; credits for other taxes; withholding; carryovers; official forms and thresholds; reviewer
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** REQUIRED ADAPTER: name exact state/local forms, official sources and filing/no-filing rationale. Federal completion cannot close this jurisdiction.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 570: Territories](https://www.irs.gov/publications/p570)

#### STATE.location — Residence and work-location evidence

**IF:** `(STATE.resident = true OR STATE.source_income = true OR STATE.move = true OR STATE.remote = true)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Residence and work-location evidence** (`STATE.doc_location`; support)
  - Extract/match: leases/deeds; move dates; workday calendar; payroll state boxes; source-income allocations
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 570: Territories](https://www.irs.gov/publications/p570)

#### STATE.state_payments — State/local payments and entity-tax credits

**IF:** `(STATE.withholding = true OR STATE.ptet = true)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: State/local payments and entity-tax credits** (`STATE.doc_state_payments`; support)
  - Extract/match: jurisdiction; year; amount; payer; tax type; entity statement; account posting
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 570: Territories](https://www.irs.gov/publications/p570)


<a id="wage"></a>
## WAGE — Employment, tips, overtime and equity pay

**Opening screen:** Did the taxpayer or spouse have employee compensation, tips, benefits or employer equity activity?
**Unit:** Repeat for each employer. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### WAGE.owner — Whose employment is this? Use the person ID or name alias.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### WAGE.w2_issued — Was a W-2 or W-2c issued?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.w2_correct — Does the final W-2 match payroll and the actual employer/employee?

**IF:** `WAGE.w2_issued = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.tips — Were cash, card or other tips received, including tips not reported to the employer?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.unreported_tips — Were any tips unreported, allocated, or missing from the W-2?

**IF:** `WAGE.tips = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.tip_occupation — What tipped occupation was performed and are tips separately documented?

**IF:** `WAGE.tips = true`
**Answer:** text. Unknown/conflict does not become false.

#### WAGE.overtime — Was overtime paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.flsa — Was any overtime premium required by the federal Fair Labor Standards Act?

**IF:** `WAGE.overtime = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.overtime_detail — Can regular wages be separated from the FLSA-required overtime premium?

**IF:** `(WAGE.overtime = true AND WAGE.flsa = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.equity — Were RSUs, stock options, ESPP shares, restricted stock or deferred compensation involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.equity_type — Describe grants, vesting, exercises, releases, sales and any 83(b) election.

**IF:** `WAGE.equity = true`
**Answer:** text. Unknown/conflict does not become false.

#### WAGE.iso — Were incentive stock options exercised or sold?

**IF:** `WAGE.equity = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.statutory — Is the W-2 statutory-employee box checked?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.misclassified — Was compensation reported on a 1099 even though employee treatment may apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.benefits — Were dependent-care, adoption, moving, disability, educational or other unusual benefits provided?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.foreign — Was work performed abroad, for a foreign employer, or in a U.S. territory?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### WAGE.deferral_excess — Could combined retirement deferrals across employers exceed the applicable limit?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### WAGE.w2 — Locate and reconcile this employer’s W-2

**IF:** `Always within this active topic`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Complete current-year W-2 or W-2c** (`W2`; source_form)
  - Extract/match: employer; employee; EIN; boxes 1 through 20; corrected version; state and local allocation
  - Look in: Employer payroll portal; authorized email attachments; tax folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: Last pay statement plus documented employer/IRS recovery efforts may support a preparer-approved Form 4852 workflow; not an automatic replacement for a missing W-2.
- **Support: Year-end payroll and earnings detail** (`PAYROLL`; support)
  - Extract/match: regular wages; tips; overtime premium; pretax deductions; employer benefits; withholding; year-to-date totals
  - Look in: Employer payroll portal; pay-statement folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.replacement — W-2 recovery/correction workflow

**IF:** `(WAGE.w2_issued = false OR WAGE.w2_correct = false)`
**THEN, form candidates:** 4852 (individual_return_or_workpaper)
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Attempt authorized recovery and correction before considering a substitute form. Do not infer missing compensation is zero.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.tips — Tip records and qualifying-tip deduction workpaper

**IF:** `WAGE.tips = true`
**THEN, form candidates:** Schedule 1-A (individual_return_or_workpaper)
- **Support: Tip records and qualifying-tip deduction workpaper** (`WAGE.doc_tips`; support)
  - Extract/match: tip diary; employer-reported tips; allocated tips; occupation; employer information; eligible reported tips; qualifying SSN; MAGI; filing status
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate gross-income reporting from deduction eligibility; not all service charges or occupations qualify.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.unreported_tips — Unreported-tip reconciliation

**IF:** `(WAGE.tips = true AND WAGE.unreported_tips = true)`
**THEN, form candidates:** 4137 (individual_return_or_workpaper)
- **Support: Unreported-tip reconciliation** (`WAGE.doc_unreported_tips`; support)
  - Extract/match: cash and noncash tips; employer reports; allocated tips; W-2 amounts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.overtime — Overtime hours and premium substantiation

**IF:** `WAGE.overtime = true`
**THEN, form candidates:** Schedule 1-A (individual_return_or_workpaper)
- **Support: Overtime hours and premium substantiation** (`WAGE.doc_overtime`; support)
  - Extract/match: pay periods; hours; regular rate; overtime rate; FLSA status; qualified premium; qualifying SSN; MAGI; filing status
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** The full overtime paycheck is not the qualified premium. Contractual or state-law overtime is not automatically FLSA-qualified.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.equity — Equity compensation lifecycle packet

**IF:** `WAGE.equity = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Equity compensation lifecycle packet** (`WAGE.doc_equity`; support)
  - Extract/match: grant agreement; grant date; vest/exercise date; FMV; strike price; shares; W-2 income; sell-to-cover; 1099-B basis; 83(b) proof
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Reconcile compensation included in wages to adjusted stock basis; do not double-tax W-2 income.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.iso — ISO exercise and disposition records

**IF:** `(WAGE.equity = true AND WAGE.iso = true)`
**THEN, form candidates:** 6251 (individual_return_or_workpaper); 8801 (individual_return_or_workpaper)
- **Support: ISO exercise and disposition records** (`WAGE.doc_iso`; support)
  - Extract/match: Form 3921; exercise spread; shares held at year-end; dispositions; prior AMT basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.statutory — Statutory-employee expense routing

**IF:** `WAGE.statutory = true`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper)
- **Support: Business income and expense ledger with reconciliations** (`BUS_BOOKS`; support)
  - Extract/match: gross receipts; cash receipts; platform gross sales; refunds; expenses; owner transfers; bank ties; accounting method
  - Look in: Bookkeeping records; business bank statements; platform exports
  - Accept only when: Reconcile information returns and cash/platform receipts to the ledger; remove duplicates, loans and owner transfers with evidence.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate statutory-employee reporting from ordinary self-employment and Schedule SE treatment.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.classification — Worker-classification facts

**IF:** `WAGE.misclassified = true`
**THEN, form candidates:** 8919 (individual_return_or_workpaper); SS-8 (separate_obligation_or_procedure)
- **Support: Worker-classification facts** (`WAGE.doc_classification`; support)
  - Extract/match: contract; actual control; employer determinations; SS-8 status; payments
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Classification review is required; do not simply treat every 1099 as a business.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.benefits — Employer benefit details

**IF:** `WAGE.benefits = true`
**THEN, form candidates:** 2441 (individual_return_or_workpaper); 8839 (individual_return_or_workpaper)
- **Support: Employer benefit details** (`WAGE.doc_benefits`; support)
  - Extract/match: benefit type; W-2 box/code; reimbursement; plan limits; recipient; payroll treatment
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Allocate each benefit to its dedicated module; do not deduct reimbursed amounts again.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

#### WAGE.deferrals — All-employer elective-deferral reconciliation

**IF:** `WAGE.deferral_excess = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: All-employer elective-deferral reconciliation** (`WAGE.doc_deferrals`; support)
  - Extract/match: each employer and plan; deferral type; age; total contributions; corrective distributions; dates
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Distinguish different plan aggregation rules and catch-up eligibility.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

**Linked track:** IF `WAGE.foreign = true` → FOREIGN. Review overseas work and international status; also review each state in STATE. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `WAGE.statutory = true` → BUSINESS. Statutory employee business-expense track. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="invest"></a>
## INVEST — Interest, dividends and investment accounts

**Opening screen:** Were there taxable bank, brokerage, bond or other investment accounts or investment income?
**Unit:** Repeat for each account. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### INVEST.owner — Whose account is this and is it jointly owned or held as nominee?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### INVEST.taxable — Is this outside a tax-deferred or tax-exempt retirement account?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.interest — Was interest earned, including amounts below information-reporting thresholds?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.dividends — Were dividends, capital-gain distributions or return-of-capital payments received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.sales — Were securities or other assets sold, exchanged, redeemed or otherwise disposed of?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.foreign_tax — Was foreign tax withheld or paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.nominee — Were amounts reported under this taxpayer’s ID that belong to somebody else?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.bond — Were OID, market discount, bond premium, accrued interest or savings bonds involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.municipal — Was tax-exempt interest or a private-activity bond amount reported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.margin — Was investment interest paid or is there an investment-interest carryforward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.k1 — Did this investment issue or expect a K-1 rather than only a 1099?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.foreign_account — Was the account maintained outside the U.S. or invested in foreign pooled funds?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### INVEST.closed — Was the account closed, transferred or consolidated during the year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### INVEST.tax_package — Collect this account’s complete tax package

**IF:** `INVEST.taxable = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); Schedule B (individual_return_or_workpaper)
- **Support: Complete consolidated brokerage tax package** (`BROKER`; source_form)
  - Extract/match: 1099-INT; 1099-DIV; 1099-OID; 1099-B sections as issued; transaction supplements; corrections; account owner
  - Look in: Broker tax center; authorized email tax notices; tax folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Determine Schedule B thresholds and special filing triggers; a tax package alone does not make every listed schedule necessary.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.sales — Open asset-disposition inventory

**IF:** `INVEST.sales = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Acquisition and adjusted-basis history** (`BASIS`; support)
  - Extract/match: acquisition dates; cost; fees; lot identification; transfers; reinvestment; basis adjustments; original owner
  - Look in: Broker history; transfer statements; trade confirmations; prior tax files
  - Accept only when: Trace basis and holding period to records. Missing or blank broker basis must not be replaced with zero.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Create or reconcile asset-sale records in DISPOSE; retirement-account trades are not taxable brokerage sales by default.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.nominee — Nominee income allocation

**IF:** `INVEST.nominee = true`
**THEN, form candidates:** Schedule B (individual_return_or_workpaper); 1099 series (separate_obligation_or_procedure)
- **Support: Nominee income allocation** (`INVEST.doc_nominee`; support)
  - Extract/match: beneficial owners; gross reported amount; ownership agreement; income allocation; recipient reporting
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Assess nominee reporting and deadlines as a separate information-return task.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.bond — Bond and savings-bond detail

**IF:** `INVEST.bond = true`
**THEN, form candidates:** Schedule B (individual_return_or_workpaper); 8815 (individual_return_or_workpaper)
- **Support: Bond and savings-bond detail** (`INVEST.doc_bond`; support)
  - Extract/match: CUSIP; purchase/sale dates; price; OID; discount; premium; elections; redemption; interest previously recognized
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review bond adjustments and any education savings-bond exclusion using actual eligibility facts.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.foreign_tax — Investment foreign-tax detail

**IF:** `INVEST.foreign_tax = true`
**THEN, form candidates:** 1116 (individual_return_or_workpaper)
- **Support: Investment foreign-tax detail** (`INVEST.doc_foreign_tax`; support)
  - Extract/match: country; income category; gross income; foreign tax; qualified dividends; K-3; foreign tax carryovers
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review direct-credit exception versus Form 1116; link all categories and foreign-tax carryovers.
**Authority:** [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### INVEST.margin — Investment-interest allocation

**IF:** `INVEST.margin = true`
**THEN, form candidates:** 4952 (individual_return_or_workpaper)
- **Support: Investment-interest allocation** (`INVEST.doc_margin`; support)
  - Extract/match: loan proceeds tracing; interest paid; investment income; prior disallowed interest; qualified-dividend election
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.muni — Tax-exempt and private-activity bond detail

**IF:** `INVEST.municipal = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); 6251 (individual_return_or_workpaper)
- **Support: Tax-exempt and private-activity bond detail** (`INVEST.doc_muni`; support)
  - Extract/match: tax-exempt interest; private-activity portion; issuer state; premium adjustments
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### INVEST.closed — Closed-account continuity

**IF:** `INVEST.closed = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Closed-account continuity** (`INVEST.doc_closed`; support)
  - Extract/match: closing statement; destination account; transferred basis; final tax documents; transfer dates
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

**Linked track:** IF `INVEST.sales = true` → DISPOSE. Create sale records and reconcile all lots. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `INVEST.k1 = true` → PASS. Create the pass-through interest and expected K-1 package. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `INVEST.foreign_account = true` → FOREIGN. Assess foreign accounts/PFIC holdings. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="dispose"></a>
## DISPOSE — Sales, exchanges and adjusted basis

**Opening screen:** Were capital assets, securities, personal property or business assets sold, exchanged, redeemed or disposed of?
**Unit:** Repeat for each sale or homogeneous lot group. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### DISPOSE.asset_type — What asset was disposed of?

**IF:** `Always within this active topic`
**Answer:** enum · Public security / Digital asset / Personal-use property / Investment real estate / Business asset / Private company interest / Other. Unknown/conflict does not become false.

#### DISPOSE.dates — What are the acquisition and disposition dates?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### DISPOSE.proceeds — What were gross proceeds, in U.S. dollars?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### DISPOSE.basis_known — Are acquisition cost and all basis adjustments supported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.acquired — How was the asset acquired?

**IF:** `Always within this active topic`
**Answer:** enum · Purchase / Gift / Inheritance / Compensation / Exchange or reorganization / Other. Unknown/conflict does not become false.

#### DISPOSE.info_return — Was a 1099-B, 1099-DA or 1099-S issued?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.basis_reported — Was basis reported to the IRS, and is it correct?

**IF:** `DISPOSE.info_return = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.adjustment — Are there basis, proceeds, holding-period or other reporting adjustments?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.wash — Were substantially identical securities bought in the 30 days before or after a loss sale, including other accounts or a spouse’s account?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.special — Were options, short sales, straddles, futures, section 1256 contracts or trader elections involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.installment — Will any sale proceeds be collected after the year of sale?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.related — Was the buyer or counterparty related to the taxpayer?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.qsbs — Could qualified-small-business-stock, opportunity-zone or another deferral/exclusion provision apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.business_use — Was the asset depreciated, used in a business, or converted between personal and business use?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.like_kind — Was a real-property like-kind exchange attempted?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISPOSE.worthless — Is a claimed loss due to worthlessness, abandonment, bad debt, fraud or inaccessible assets rather than an ordinary sale?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### DISPOSE.sales_packet — Sale ledger and basis reconciliation

**IF:** `Always within this active topic`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Acquisition and adjusted-basis history** (`BASIS`; support)
  - Extract/match: acquisition dates; cost; fees; lot identification; transfers; reinvestment; basis adjustments; original owner
  - Look in: Broker history; transfer statements; trade confirmations; prior tax files
  - Accept only when: Trace basis and holding period to records. Missing or blank broker basis must not be replaced with zero.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Confirm return routing for the asset type; Form 8949 may be bypassed only if its reporting exception is actually satisfied.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.settlement — Disposition confirmation and proceeds support

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Disposition confirmation and proceeds support** (`DISPOSE.doc_settlement`; support)
  - Extract/match: asset; quantity; date; gross proceeds; fees; withholding; information-return category; USD conversion
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.gift_basis — Gift-basis history

**IF:** `DISPOSE.acquired = "Gift"`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Gift-basis history** (`DISPOSE.doc_gift_basis`; support)
  - Extract/match: donor basis; date of gift; gift-date FMV; gift tax basis adjustment; donor holding period
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Gift loss basis and gain basis can differ; do not automatically substitute gift-date FMV.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.inheritance — Inherited-asset basis support

**IF:** `DISPOSE.acquired = "Inheritance"`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Inherited-asset basis support** (`DISPOSE.doc_inheritance`; support)
  - Extract/match: decedent; date of death; valuation; alternate valuation if elected; Form 8971/Schedule A if applicable; later adjustments
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.wash — Cross-account wash-sale workpaper

**IF:** `DISPOSE.wash = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper)
- **Support: Cross-account wash-sale workpaper** (`DISPOSE.doc_wash`; support)
  - Extract/match: loss lots; replacement lots; dates; spouse accounts; IRA acquisitions; basis and holding-period adjustments
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.special — Complex securities workpaper

**IF:** `DISPOSE.special = true`
**THEN, form candidates:** 6781 (individual_return_or_workpaper); 4797 (individual_return_or_workpaper)
- **Support: Complex securities workpaper** (`DISPOSE.doc_special`; support)
  - Extract/match: instrument terms; transactions; elections and dates; broker reporting; straddle links
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Specialist review of character, mark-to-market, straddles and election validity.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.installment — Installment sale agreement and amortization

**IF:** `DISPOSE.installment = true`
**THEN, form candidates:** 6252 (individual_return_or_workpaper)
- **Support: Installment sale agreement and amortization** (`DISPOSE.doc_installment`; support)
  - Extract/match: contract; down payment; selling price; gross profit; assumed debt; interest; later receipts; security
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review eligibility, related-party rules and depreciation recapture before installment treatment.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.business_asset — Business-asset disposition workpaper

**IF:** `DISPOSE.business_use = true`
**THEN, form candidates:** 4797 (individual_return_or_workpaper); 4562 (individual_return_or_workpaper)
- **Support: Business-asset disposition workpaper** (`DISPOSE.doc_business_asset`; support)
  - Extract/match: depreciation history; business use; adjusted basis; recapture; proceeds allocation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.exchange — Like-kind exchange closing packet

**IF:** `DISPOSE.like_kind = true`
**THEN, form candidates:** 8824 (individual_return_or_workpaper)
- **Support: Like-kind exchange closing packet** (`DISPOSE.doc_exchange`; support)
  - Extract/match: relinquished/replacement property; qualified intermediary; identification and receipt dates; boot; debt; basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify real-property eligibility, timing and related-party limits.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.exclusion — Special asset exclusion/deferral support

**IF:** `DISPOSE.qsbs = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); 8997 (individual_return_or_workpaper)
- **Support: Special asset exclusion/deferral support** (`DISPOSE.doc_exclusion`; support)
  - Extract/match: stock issuance date; issuer qualifications; holding period; prior exclusions; investment dates; elections
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review exact statutory conditions; do not infer QSBS status from a company being small.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.loss_event — Worthlessness or loss-event substantiation

**IF:** `DISPOSE.worthless = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); 4684 (individual_return_or_workpaper)
- **Support: Worthlessness or loss-event substantiation** (`DISPOSE.doc_loss_event`; support)
  - Extract/match: rights retained; recovery claims; bankruptcy status; identifiable event; debt instrument; basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** An exchange freeze, price collapse or missing wallet key does not alone establish a deductible loss.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.basis_block — Unresolved basis blocks affected sale

**IF:** `DISPOSE.basis_known = false`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: recover or reconstruct supported basis. Do not use zero as a convenience default.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.unmodeled_asset_type — Resolve unmodeled selection: DISPOSE.asset_type

**IF:** `DISPOSE.asset_type is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

#### DISPOSE.unmodeled_acquired — Resolve unmodeled selection: DISPOSE.acquired

**IF:** `DISPOSE.acquired is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)


<a id="digital"></a>
## DIGITAL — Digital assets and wallet reconciliation

**Opening screen:** Did the taxpayer or spouse own, buy, transfer, receive or dispose of any digital assets, including stablecoins and NFTs?
**Unit:** Repeat for each wallet or platform. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### DIGITAL.owner — Who owns this wallet/account, and is any activity for an employer or another person?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### DIGITAL.inventory — Have all addresses, chains, exchange subaccounts and closed accounts for this source been identified?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.fiat_only — Were activities limited to buying with fiat currency and holding?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.transfer — Were there transfers between wallets/accounts owned by the same person?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.fee_crypto — Were transaction or network fees paid in digital assets?

**IF:** `(DIGITAL.transfer = true OR DIGITAL.fiat_only = false)`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.disposal — Were assets sold, swapped, spent or otherwise disposed of?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.rewards — Were staking, mining, airdrop, referral, lending or other rewards received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.services — Were digital assets received as pay for services or business sales?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.defi — Were liquidity pools, lending, wrapping, bridges, rebases, derivatives or other complex DeFi involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.gift — Were digital assets given to another person, donated, or inherited?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.unavailable — Are any records missing or assets frozen, hacked, stolen or inaccessible?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.basis — Are beginning lots and wallet/account-specific basis supported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DIGITAL.broker_form — Was a 1099-DA, 1099-B, 1099-MISC or other digital-asset statement issued?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### DIGITAL.ledger — Full wallet/platform transaction export

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Full wallet/platform transaction export** (`DIGITAL.doc_ledger`; support)
  - Extract/match: wallet addresses; chain; timestamp; transaction hash; event type; asset; units; counterparty; USD value; fees; source record
  - Look in: Exchange tax and activity exports; blockchain explorers; taxpayer wallet inventory
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.opening — Beginning and ending digital-asset inventory

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Beginning and ending digital-asset inventory** (`DIGITAL.doc_opening`; support)
  - Extract/match: opening units and basis; closing units; account/wallet allocation; transfers; source of historical lots; reconciliation differences
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Reconcile holdings and explain gaps. Never request seed phrases or private keys.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.transfer — Matched self-transfer and fee workpaper

**IF:** `DIGITAL.transfer = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Matched self-transfer and fee workpaper** (`DIGITAL.doc_transfer`; support)
  - Extract/match: sending and receiving ownership; hashes; timestamps; quantities; fees; carried basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not treat the transfer principal as a sale by default; separately classify crypto-denominated fees.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.taxable_disposal — Digital-asset disposition ledger

**IF:** `(DIGITAL.disposal = true OR DIGITAL.fee_crypto = true)`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Digital-asset disposition ledger** (`DIGITAL.doc_taxable_disposal`; support)
  - Extract/match: acquisition lots; disposal timestamp; proceeds; fees; USD price source; basis; holding period
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.income — Digital-asset income valuation records

**IF:** `(DIGITAL.rewards = true OR DIGITAL.services = true)`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); Schedule C (individual_return_or_workpaper); Schedule SE (individual_return_or_workpaper)
- **Support: Digital-asset income valuation records** (`DIGITAL.doc_income`; support)
  - Extract/match: receipt timestamp; control/availability; units; USD FMV; activity character; later asset basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Classify activity and ordinary income separately from any later disposal.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.complex — DeFi or disputed digital-asset treatment memo

**IF:** `(DIGITAL.defi = true OR DIGITAL.unavailable = true)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: DeFi or disputed digital-asset treatment memo** (`DIGITAL.doc_complex`; support)
  - Extract/match: protocol mechanics; legal rights; relevant events; transaction evidence; recoveries; supported tax characterization
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: determine treatment from facts and authority. Do not manufacture certainty from generic transaction labels.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DIGITAL.basis_block — Digital-asset history incomplete

**IF:** `(DIGITAL.basis = false OR DIGITAL.inventory = false)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: incomplete wallet coverage or beginning basis prevents a complete digital-asset reconciliation.
**Authority:** [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

**Linked track:** IF `DIGITAL.disposal = true` → DISPOSE. Create digital-asset disposal workpapers. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `DIGITAL.services = true` → BUSINESS. Classify service/business receipt activity. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="retire"></a>
## RETIRE — Retirement contributions, distributions and conversions

**Opening screen:** Were there retirement contributions, distributions, rollovers, Roth conversions, inherited accounts or unresolved retirement-account issues?
**Unit:** Repeat for each retirement account. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### RETIRE.owner — Whose account is this? Identify the individual, not just the joint return.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### RETIRE.type — What type of account or payment is involved?

**IF:** `Always within this active topic`
**Answer:** enum · Traditional IRA / Roth IRA / SEP IRA / SIMPLE IRA / Employer plan / 401(k) / 403(b) / 457 / Pension or annuity / Inherited IRA or plan / Other. Unknown/conflict does not become false.

#### RETIRE.contribution — Were contributions designated for this tax year made, including after year-end?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.contribution_details — List contribution dates, amounts, designation years and direct/employer/rollover classifications.

**IF:** `RETIRE.contribution = true`
**Answer:** text. Unknown/conflict does not become false.

#### RETIRE.covered_plan — Was the contributor or spouse covered by a workplace retirement plan?

**IF:** `RETIRE.contribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.compensation — Does the contributor have qualifying compensation or qualify for a spousal IRA contribution?

**IF:** `RETIRE.contribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.nondeductible — Was a traditional IRA contribution nondeductible or is there prior after-tax IRA basis?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.distribution — Was any distribution, including a direct rollover or conversion, made from the account?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.rollover — Was any distribution rolled over or intended to be rolled over?

**IF:** `RETIRE.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.rollover_kind — Was it direct, a 60-day rollover, or a transfer that was not a distribution?

**IF:** `(RETIRE.distribution = true AND RETIRE.rollover = true)`
**Answer:** enum · Direct rollover / 60-day rollover / Trustee-to-trustee transfer / Unresolved. Unknown/conflict does not become false.

#### RETIRE.rollover_date — What are the distribution and redeposit dates, gross amount, withholding and redeposited amount?

**IF:** `(RETIRE.distribution = true AND RETIRE.rollover = true)`
**Answer:** text. Unknown/conflict does not become false.

#### RETIRE.late_rollover — Was a rollover late, incomplete, an RMD, or potentially barred by the one-per-year rule?

**IF:** `(RETIRE.distribution = true AND RETIRE.rollover = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.conversion — Was money converted to Roth, including a backdoor Roth transaction?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.roth_distribution — Was money withdrawn from a Roth IRA?

**IF:** `RETIRE.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.roth_history — Are first Roth contribution, conversion-by-year and withdrawal histories available?

**IF:** `(RETIRE.distribution = true AND RETIRE.roth_distribution = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.early — Could a distribution be subject to additional tax because of age, account type or an early-withdrawal rule?

**IF:** `RETIRE.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.exception — Could an early-distribution exception apply, including disability, education, medical, first home, birth/adoption, emergency or other permitted events?

**IF:** `(RETIRE.distribution = true AND RETIRE.early = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.inherited — Is this an inherited account or a survivor payment?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.inherited_details — Identify decedent, death date, relationship, beneficiary category, original owner’s RMD status and elections.

**IF:** `RETIRE.inherited = true`
**Answer:** text. Unknown/conflict does not become false.

#### RETIRE.rmd — Was an RMD due, potentially due, or missed for this owner/account?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.rmd_shortfall — Was a required distribution missed, short, or taken in a later year?

**IF:** `RETIRE.rmd = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.qcd — Was an IRA distribution sent directly to a charity as a possible QCD?

**IF:** `RETIRE.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.excess — Were there excess contributions, recharacterizations, corrective distributions or returned deferrals?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.disaster — Was a special disaster-related distribution, repayment or prior-year election involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RETIRE.aftertax_plan — Did an employer-plan/pension distribution include after-tax basis, employer stock or a lump-sum special method?

**IF:** `RETIRE.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### RETIRE.contributions — Retirement contribution designation and eligibility

**IF:** `RETIRE.contribution = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Retirement contribution designation and eligibility** (`RETIRE.doc_contributions`; support)
  - Extract/match: custodian; owner; account type; amount; date; tax year; compensation; employer-plan coverage; correction; 5498 if issued
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: Custodian contribution confirmations and account statements may substitute for a not-yet-issued Form 5498; reconcile the later form when available.
**Review gate:** Check annual limits, compensation, age, MAGI and filing-status rules; no deduction is automatic.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.distribution — Classify retirement distributions

**IF:** `RETIRE.distribution = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Complete 1099-R and corrections** (`R1099`; source_form)
  - Extract/match: recipient; payer; account; boxes 1, 2a, 2b, 4, 5, 7; IRA checkbox; state withholding
  - Look in: Custodian tax portal; pension administrator; tax folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.ira_basis — IRA after-tax basis and pro-rata workpaper

**IF:** `(RETIRE.nondeductible = true OR RETIRE.conversion = true)`
**THEN, form candidates:** 8606 (individual_return_or_workpaper)
- **Support: Prior Forms 8606 and IRA basis rollforward** (`IRA_HISTORY`; support)
  - Extract/match: owner; nondeductible contributions; prior distributions and conversions; remaining basis; missing years
  - Look in: Prior returns; former preparer; custodian contribution records
  - Accept only when: Reconcile by individual, across all relevant traditional/SEP/SIMPLE IRAs. A missing prior 8606 does not establish zero basis. Keep inherited IRA basis separate by decedent where required; do not merge it indiscriminately with the beneficiary’s own IRAs.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
- **Support: December 31 values of every relevant traditional, SEP and SIMPLE IRA for the same individual** (`IRA_DEC31`; support)
  - Extract/match: owner; all custodians; year-end balances; outstanding rollovers; account type
  - Look in: All IRA custodian year-end statements
  - Accept only when: Confirm the account inventory is complete across custodians; do not use only the converted account. Determine exactly which own or inherited accounts belong in the applicable Form 8606 aggregation; do not pool different reporting units.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Compute at the individual level across relevant IRAs, not only the converted account. Prior basis is not assumed to be zero.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.rollover — Rollover source-to-destination reconciliation

**IF:** `(RETIRE.distribution = true AND RETIRE.rollover = true)`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Rollover source-to-destination reconciliation** (`RETIRE.doc_rollover`; support)
  - Extract/match: 1099-R; distribution amount/date; withholding; receiving account; deposit date; rollover classification; one-per-year history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify eligibility and gross-versus-net rollover amount. Withholding can leave a taxable shortfall.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.rollover_exception — Late or restricted rollover support

**IF:** `RETIRE.late_rollover = true`
**THEN, form candidates:** 5329 (individual_return_or_workpaper)
- **Support: Late or restricted rollover support** (`RETIRE.doc_rollover_exception`; support)
  - Extract/match: deadline; reason; redeposit; self-certification or waiver evidence; distribution eligibility
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Preparer review required; do not relabel a late deposit as a valid rollover.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.roth_basis — Roth contribution/conversion ordering history

**IF:** `(RETIRE.distribution = true AND RETIRE.roth_distribution = true)`
**THEN, form candidates:** 8606 (individual_return_or_workpaper); 5329 (individual_return_or_workpaper)
- **Support: Roth contribution/conversion ordering history** (`RETIRE.doc_roth_basis`; support)
  - Extract/match: regular Roth contributions; conversion amounts by year; taxable/nontaxable conversion portions; first Roth year; prior withdrawals; age
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.early — Early-distribution exception evidence

**IF:** `(RETIRE.distribution = true AND RETIRE.early = true)`
**THEN, form candidates:** 5329 (individual_return_or_workpaper)
- **Support: Early-distribution exception evidence** (`RETIRE.doc_early`; support)
  - Extract/match: birth date; distribution code; account type; exception type; event date; eligible costs; reimbursements; amount assigned
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** A distribution code or hardship approval does not establish every tax exception; exceptions differ between IRAs and employer plans.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.inherited — Inherited-account beneficiary and distribution workpaper

**IF:** `RETIRE.inherited = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); 5329 (individual_return_or_workpaper)
- **Support: Inherited-account beneficiary and distribution workpaper** (`RETIRE.doc_inherited`; support)
  - Extract/match: death certificate; beneficiary designation; owner death year; required beginning date; beneficiary class; prior RMDs; elections; custodian history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: verify applicable inherited-account distribution regime and relief for the relevant year.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.rmd — Required-minimum-distribution calculation and payment proof

**IF:** `RETIRE.rmd = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Required-minimum-distribution calculation and payment proof** (`RETIRE.doc_rmd`; support)
  - Extract/match: owner birth date; prior December 31 balance; account type; beneficiary factors; calculated RMD; distributions; aggregation eligibility
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Check each account type; not every RMD can be aggregated across accounts.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.shortfall — RMD correction and reasonable-error relief packet

**IF:** `(RETIRE.rmd = true AND RETIRE.rmd_shortfall = true)`
**THEN, form candidates:** 5329 (individual_return_or_workpaper)
- **Support: RMD correction and reasonable-error relief packet** (`RETIRE.doc_shortfall`; support)
  - Extract/match: required amount; actual amount; correction date; shortfall; cause; correction steps; relief statement
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.qcd — Qualified charitable distribution evidence

**IF:** `(RETIRE.distribution = true AND RETIRE.qcd = true)`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Qualified charitable distribution evidence** (`RETIRE.doc_qcd`; support)
  - Extract/match: donor age at distribution; direct custodian-to-charity transfer; charity eligibility; acknowledgement; deductible IRA contributions; amount
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not also deduct the same QCD as an itemized charitable contribution.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.correction — Retirement correction/recharacterization packet

**IF:** `RETIRE.excess = true`
**THEN, form candidates:** 5329 (individual_return_or_workpaper); 8606 (individual_return_or_workpaper)
- **Support: Retirement correction/recharacterization packet** (`RETIRE.doc_correction`; support)
  - Extract/match: contribution year; excess amount; earnings; correction date; 1099-R codes; custodian letter; amended prior years
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Distinguish a recharacterization from a Roth conversion; verify permitted timing.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.disaster — Retirement disaster distribution and repayment history

**IF:** `RETIRE.disaster = true`
**THEN, form candidates:** 8915-F (individual_return_or_workpaper)
- **Support: Retirement disaster distribution and repayment history** (`RETIRE.doc_disaster`; support)
  - Extract/match: disaster; eligibility; distribution date; prior elections; income spread; repayments by year
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.plan_basis — Pension or plan after-tax/stock basis

**IF:** `(RETIRE.distribution = true AND RETIRE.aftertax_plan = true)`
**THEN, form candidates:** 4972 (individual_return_or_workpaper); 1040 (individual_return_or_workpaper)
- **Support: Pension or plan after-tax/stock basis** (`RETIRE.doc_plan_basis`; support)
  - Extract/match: employee contributions; annuity start; prior recoveries; employer securities; net unrealized appreciation; lump-sum eligibility
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Special pension, annuity and employer-stock methods require separate review.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.deduction_candidate — Potential IRA / self-employed retirement deduction

**IF:** `(RETIRE.contribution = true AND RETIRE.type is one of ["Traditional IRA", "SEP IRA", "SIMPLE IRA"])`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
**Review gate:** Apply account type, compensation, workplace coverage, income limits and owner/business contribution rules before claiming a deduction; nondeductible contributions remain a separate basis track.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.unmodeled_type — Resolve unmodeled selection: RETIRE.type

**IF:** `RETIRE.type is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

#### RETIRE.unmodeled_rollover_kind — Resolve unmodeled selection: RETIRE.rollover_kind

**IF:** `RETIRE.rollover_kind is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)


<a id="business"></a>
## BUSINESS — Self-employment and closely held business

**Opening screen:** Was there a trade, business, freelancing, consulting, gig work, personal-property rental business or ownership of a disregarded entity?
**Unit:** Repeat for each business. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### BUSINESS.owner — Who owns the business, and what are the ownership percentages?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### BUSINESS.structure — What is the federal tax classification?

**IF:** `Always within this active topic`
**Answer:** enum · Sole proprietor / disregarded single-member LLC / Qualified joint venture candidate / Partnership / S corporation / C corporation / Unresolved. Unknown/conflict does not become false.

#### BUSINESS.activity — Describe the activity, business start/stop dates, and accounting method.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### BUSINESS.receipts — Were there gross receipts, including cash, barter, reimbursements or platform payments?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.information — Were any 1099-NEC, 1099-K, 1099-MISC or other income statements issued?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.overlap — Could platform and payer reports describe the same income, personal reimbursements, sales tax or nonbusiness transfers?

**IF:** `BUSINESS.information = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.inventory — Were products produced or held for sale, or were materials/inventory purchased?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.expenses — Were any business expenses incurred?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.vehicle — Was a vehicle used for business?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.expenses = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.home_office — Was part of a home used regularly for the business?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.expenses = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.assets — Were equipment, software, improvements or other longer-lived assets acquired, sold or converted?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.travel_meals — Were travel, meals, gifts or entertainment costs incurred?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.expenses = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.workers — Were employees or contractors paid?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.retirement — Were self-employed retirement contributions made or a plan maintained?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.insurance — Were health insurance premiums paid for the owner or family?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.loss — Is there a loss, prior suspended loss, large interest expense or significant debt?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.qbi — Could income or loss be qualified business income?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.startup — Was the business started, acquired, sold, abandoned or closed this year?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.foreign — Were there foreign operations, owners, accounts, services or withholding?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.special — Were research costs, accounting-method changes, credits, excise taxes, litigation or unusual elections involved?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.hobby — Is profit motive or trade/business status uncertain?

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND Always within this active topic)`
**Answer:** boolean. Unknown/conflict does not become false.

#### BUSINESS.farm — Is this a farm, fishing operation, mineral/royalty interest or agricultural rental?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### BUSINESS.books — Reconcile business gross income and expenses

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Business income and expense ledger with reconciliations** (`BUS_BOOKS`; support)
  - Extract/match: gross receipts; cash receipts; platform gross sales; refunds; expenses; owner transfers; bank ties; accounting method
  - Look in: Bookkeeping records; business bank statements; platform exports
  - Accept only when: Reconcile information returns and cash/platform receipts to the ledger; remove duplicates, loans and owner transfers with evidence.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Confirm federal entity classification first; corporate and partnership operations require their own entity-return workflow.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.entity — Entity classification and elections

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Entity classification and elections** (`BUSINESS.doc_entity`; support)
  - Extract/match: formation documents; owners; EIN; accepted S/corporate elections; activity; tax year; accounting method
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Entity returns are separate obligations; these are candidate handoffs, not attachments to a 1040.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.income_forms — Business information statements and duplicate reconciliation

**IF:** `BUSINESS.information = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Business information statements and duplicate reconciliation** (`BUSINESS.doc_income_forms`; support)
  - Extract/match: all issued 1099s; payer; gross receipts; fees; refunds; overlap; nonbusiness amounts; corrected forms
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.inventory — Inventory and cost-of-goods-sold workpaper

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.inventory = true)`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper)
- **Support: Inventory and cost-of-goods-sold workpaper** (`BUSINESS.doc_inventory`; support)
  - Extract/match: beginning inventory; purchases; production; withdrawals; closing count; valuation method; cash/accrual treatment
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.expenses — Business expense substantiation

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.expenses = true)`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper)
- **Support: Business expense substantiation** (`BUSINESS.doc_expenses`; support)
  - Extract/match: date; payee; amount; category; business purpose; payment proof; personal-use allocation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.vehicle — Business vehicle log and method history

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.vehicle = true))`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper); 4562 (individual_return_or_workpaper)
- **Support: Business vehicle log and method history** (`BUSINESS.doc_vehicle`; support)
  - Extract/match: vehicle; dates; total/business/commuting miles; trip purpose; lease or ownership; actual costs; prior method; prior depreciation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** A standard-mileage amount cannot be created from an unsupported estimate of annual miles.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.home — Home-office qualification and expense workpaper

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.home_office = true))`
**THEN, form candidates:** 8829 (individual_return_or_workpaper)
- **Support: Home-office qualification and expense workpaper** (`BUSINESS.doc_home`; support)
  - Extract/match: exclusive/regular use; exceptions; business area; total home area; use dates; indirect/direct costs; prior carryovers
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review eligibility and actual-versus-simplified method. Employee home office treatment is different.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.assets — Fixed-asset additions and dispositions

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.assets = true)`
**THEN, form candidates:** 4562 (individual_return_or_workpaper); 4797 (individual_return_or_workpaper)
- **Support: Historical fixed-asset and depreciation schedule** (`DEPR`; support)
  - Extract/match: asset identity; cost; land allocation; placed-in-service date; method; life; prior depreciation; section 179; bonus; dispositions
  - Look in: Prior returns and depreciation workpapers; asset ledger
  - Accept only when: Carry forward allowed or allowable depreciation and reconcile acquisitions, improvements and disposals.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify effective dates, eligibility, business-use percentages and annual elections before bonus/section 179 treatment.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.travel — Travel/meals/gifts detail

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.travel_meals = true))`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Travel/meals/gifts detail** (`BUSINESS.doc_travel`; support)
  - Extract/match: date; location; attendees; business purpose; overnight tax-home facts; receipt; reimbursement; entertainment separation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.workers — Worker payments and employer reporting packet

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.workers = true)`
**THEN, form candidates:** W-2 / W-3 (separate_obligation_or_procedure); 1099 series (separate_obligation_or_procedure)
- **Support: Worker payments and employer reporting packet** (`BUSINESS.doc_workers`; support)
  - Extract/match: worker identity secure reference; employee/contractor determination; W-9; payroll; payments by method; filed information returns
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Open separate payroll/information-return obligations and verify who already filed them.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.retirement — Self-employed plan and contribution workpaper

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.retirement = true)`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); 5500-EZ (separate_obligation_or_procedure)
- **Support: Self-employed plan and contribution workpaper** (`BUSINESS.doc_retirement`; support)
  - Extract/match: plan type; establishment date; employees; compensation; contributions; deadlines; plan assets; filing history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.insurance — Self-employed health insurance allocation

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.insurance = true)`
**THEN, form candidates:** 7206 (individual_return_or_workpaper)
- **Support: Self-employed health insurance allocation** (`BUSINESS.doc_insurance`; support)
  - Extract/match: insured people; premiums by month; employer-plan eligibility; Marketplace subsidies; business earned income; payroll treatment
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Coordinate with Form 8962 and other deductions; do not deduct employer-ineligible months or double-count premiums.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.limits — Business loss, interest and participation limits

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.loss = true)`
**THEN, form candidates:** 6198 (individual_return_or_workpaper); 8582 (individual_return_or_workpaper); 461 (individual_return_or_workpaper); 8990 (individual_return_or_workpaper)
- **Support: Business loss, interest and participation limits** (`BUSINESS.doc_limits`; support)
  - Extract/match: basis; debt; at-risk amounts; participation; prior losses; business interest; aggregate business results
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply ordering and aggregation rules; a book loss is not automatically currently deductible.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.qbi — Business QBI information

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.qbi = true)`
**THEN, form candidates:** 8995 (individual_return_or_workpaper); 8995-A (individual_return_or_workpaper)
- **Support: Business QBI information** (`BUSINESS.doc_qbi`; support)
  - Extract/match: qualified income; specified-service status; W-2 wages; qualified-property basis; carryovers; aggregation elections
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.startup — Business start/acquisition/closure packet

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.startup = true)`
**THEN, form candidates:** 8594 (individual_return_or_workpaper); 4797 (individual_return_or_workpaper)
- **Support: Business start/acquisition/closure packet** (`BUSINESS.doc_startup`; support)
  - Extract/match: closing agreement; asset purchase allocation; startup/organizational costs; abandoned assets; sale date; final payroll
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.special — Special business tax issues

**IF:** `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.special = true OR BUSINESS.hobby = true))`
**THEN, form candidates:** 3115 (individual_return_or_workpaper); 3800 (individual_return_or_workpaper)
- **Support: Special business tax issues** (`BUSINESS.doc_special`; support)
  - Extract/match: exact activity; affected years; profit-motive evidence; research costs; method changes; credits; election history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: extend the rule pack; do not invent an eligibility conclusion for an uncovered business provision.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.sole_forms — Sole proprietor / qualified joint venture form review

**IF:** `BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"]`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper); Schedule SE (individual_return_or_workpaper)
**Review gate:** Confirm actual sole proprietor or qualified-joint-venture treatment, and evaluate Schedule SE thresholds/exceptions.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.entity_1065 — Separate Partnership return handoff

**IF:** `BUSINESS.structure = "Partnership"`
**THEN, form candidates:** 1065 (separate_obligation_or_procedure)
**Review gate:** Track this entity return independently; its completed results may feed the individual return.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.entity_1120-S — Separate S corporation return handoff

**IF:** `BUSINESS.structure = "S corporation"`
**THEN, form candidates:** 1120-S (separate_obligation_or_procedure)
**Review gate:** Track this entity return independently; its completed results may feed the individual return.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.entity_1120 — Separate C corporation return handoff

**IF:** `BUSINESS.structure = "C corporation"`
**THEN, form candidates:** 1120 (separate_obligation_or_procedure)
**Review gate:** Track this entity return independently; its completed results may feed the individual return.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.unknown_class — Federal entity classification unresolved

**IF:** `BUSINESS.structure = "Unresolved"`
**THEN, form candidates:** None implied by this rule alone.
**Review gate:** BLOCK: obtain accepted elections and determine federal tax classification.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### BUSINESS.unmodeled_structure — Resolve unmodeled selection: BUSINESS.structure

**IF:** `BUSINESS.structure is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

**Linked track:** IF `BUSINESS.farm = true` → FARM. Open the farming/resource-specific branch. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `BUSINESS.foreign = true` → FOREIGN. Open international activity review. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="rental"></a>
## RENTAL — Rental real estate and royalties

**Opening screen:** Was property rented, available for rent, converted to/from rental use, or held with suspended rental losses?
**Unit:** Repeat for each property. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### RENTAL.owner — Identify owners, ownership percentages and property address alias.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### RENTAL.type — What kind of rental is this?

**IF:** `Always within this active topic`
**Answer:** enum · Residential real estate / Commercial real estate / Short-term/vacation home / Personal property / Royalty interest / Other. Unknown/conflict does not become false.

#### RENTAL.available — Was it placed in service and available for rent during the year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.start_date — What was its placed-in-service date?

**IF:** `RENTAL.available = true`
**Answer:** date. Unknown/conflict does not become false.

#### RENTAL.rental_days — How many days was it rented at fair rental value?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### RENTAL.personal_days — How many personal-use days were there, including applicable related-party use?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### RENTAL.below_market — Was any use by relatives or anyone paying below-market rent?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.residence — Was the dwelling used as a personal residence under the tax use tests?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.fewer15 — Was a residence rented for fewer than 15 days?

**IF:** `RENTAL.residence = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.shortstay — Were stays short or substantial guest services provided?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.services — Describe services and average stay length.

**IF:** `RENTAL.shortstay = true`
**Answer:** text. Unknown/conflict does not become false.

#### RENTAL.manager — Was a property manager or booking platform used?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.repairs_assets — Were repairs, improvements, furnishings or other assets acquired?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.convert — Was the property converted between personal and rental use?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.sold — Was the property sold, exchanged, foreclosed on, or otherwise disposed of?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.participation — Did the owner actively or materially participate, or claim real-estate-professional status?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.participation_hours — What participation hours were documented for each activity and person?

**IF:** `RENTAL.participation = true`
**Answer:** text. Unknown/conflict does not become false.

#### RENTAL.losses — Are there current losses or prior passive/at-risk/depreciation carryovers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.self_rental — Was property rented to the owner’s business or under a related-party/grouping arrangement?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.qbi — Could a rental trade/business or safe harbor support a QBI deduction?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### RENTAL.debt_event — Was debt refinanced, canceled or modified, or did a disaster occur?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### RENTAL.rental_packet — Property income, costs and depreciation

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule E (individual_return_or_workpaper)
- **Support: Property-specific rental income and expense ledger** (`RENT_BOOKS`; support)
  - Extract/match: rent; deposits retained; refunds; platform gross receipts; interest; taxes; repairs; management; utilities; insurance; reimbursements
  - Look in: Property manager portal; rental platforms; bank records; property folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
- **Support: Historical fixed-asset and depreciation schedule** (`DEPR`; support)
  - Extract/match: asset identity; cost; land allocation; placed-in-service date; method; life; prior depreciation; section 179; bonus; dispositions
  - Look in: Prior returns and depreciation workpapers; asset ledger
  - Accept only when: Carry forward allowed or allowable depreciation and reconcile acquisitions, improvements and disposals.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review Schedule E versus Schedule C or other reporting using property/service facts; do not treat every short-term rental identically.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.use — Rental and personal-use calendar

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule E (individual_return_or_workpaper)
- **Support: Rental and personal-use calendar** (`RENTAL.doc_use`; support)
  - Extract/match: fair-rental days; personal days; related-party use; repair days; available days; bookings; household use
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply vacation-home and expense-allocation rules using actual day counts.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.under15 — Residence rented fewer than 15 days workpaper

**IF:** `(RENTAL.residence = true AND RENTAL.fewer15 = true)`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Residence rented fewer than 15 days workpaper** (`RENTAL.doc_under15`; support)
  - Extract/match: residence qualification; rental days; gross rents; related information returns; otherwise allowable personal deductions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review the special rule and any information-return reconciliation; do not automatically claim rental expenses.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.services — Short-stay and substantial-services classification

**IF:** `RENTAL.shortstay = true`
**THEN, form candidates:** Schedule C (individual_return_or_workpaper); Schedule SE (individual_return_or_workpaper); 8582 (individual_return_or_workpaper)
- **Support: Short-stay and substantial-services classification** (`RENTAL.doc_services`; support)
  - Extract/match: average stay calculation; cleaning/maid/meal/concierge services; occupancy; owner participation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate self-employment classification from passive-activity classification.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.improvements — Repairs versus improvements and asset additions

**IF:** `RENTAL.repairs_assets = true`
**THEN, form candidates:** 4562 (individual_return_or_workpaper)
- **Support: Repairs versus improvements and asset additions** (`RENTAL.doc_improvements`; support)
  - Extract/match: invoices; project description; replaced components; cost; placed-in-service date; elections
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.conversion — Conversion-date valuation and basis

**IF:** `RENTAL.convert = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Conversion-date valuation and basis** (`RENTAL.doc_conversion`; support)
  - Extract/match: original cost; accumulated improvements; FMV at conversion; land; depreciation; use dates
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.sale — Rental property closing and disposition packet

**IF:** `RENTAL.sold = true`
**THEN, form candidates:** 4797 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper); 8582 (individual_return_or_workpaper)
- **Support: Rental property closing and disposition packet** (`RENTAL.doc_sale`; support)
  - Extract/match: purchase and sale closings; selling costs; depreciation; suspended losses; buyer relationship; installment/exchange facts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.participation — Rental participation and grouping workpaper

**IF:** `RENTAL.participation = true`
**THEN, form candidates:** 8582 (individual_return_or_workpaper)
- **Support: Rental participation and grouping workpaper** (`RENTAL.doc_participation`; support)
  - Extract/match: hours by person and property; other work hours; contemporaneous logs; grouping election; active participation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not infer real-estate-professional status solely from an occupation or owner statement.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.carry — Property-specific suspended-loss history

**IF:** `RENTAL.losses = true`
**THEN, form candidates:** 8582 (individual_return_or_workpaper); 6198 (individual_return_or_workpaper)
- **Support: Property-specific suspended-loss history** (`RENTAL.doc_carry`; support)
  - Extract/match: prior passive loss; at-risk loss; basis limitation; vacation-home carryovers; current usage; disposition releases
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.qbi — Rental QBI qualification file

**IF:** `RENTAL.qbi = true`
**THEN, form candidates:** 8995 (individual_return_or_workpaper); 8995-A (individual_return_or_workpaper)
- **Support: Rental QBI qualification file** (`RENTAL.doc_qbi`; support)
  - Extract/match: trade/business facts; service hours; records; safe-harbor statement if relied on; exclusions; aggregation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### RENTAL.unmodeled_type — Resolve unmodeled selection: RENTAL.type

**IF:** `RENTAL.type is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

**Linked track:** IF `RENTAL.sold = true` → DISPOSE. Create the property disposition. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `RENTAL.debt_event = true` → DEBT. Determine whether debt cancellation exists; an ordinary refinance can resolve as not applicable with rationale. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="pass"></a>
## PASS — Pass-through interests and K-1s

**Opening screen:** Was there any partnership, S corporation, trust, estate, fund, PTP or other interest that issued or could issue a K-1?
**Unit:** Repeat for each entity interest. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### PASS.owner — Who owns the interest or is the beneficiary?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### PASS.kind — Which return family issues the K-1?

**IF:** `Always within this active topic`
**Answer:** enum · 1065 partnership / 1120-S S corporation / 1041 trust/estate / Unresolved. Unknown/conflict does not become false.

#### PASS.received — Has a complete final or corrected K-1 package arrived?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.acquired — Was the interest acquired, gifted, inherited or transferred this year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.contributed — Were capital contributions, shareholder loans or debt changes made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.distributions — Were cash or property distributions received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.loss — Were losses, deductions, credits or suspended amounts reported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.participates — Did the taxpayer work in or materially participate in the activity?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.ptp — Is this a publicly traded partnership?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.sale — Was any part of the interest sold, redeemed, abandoned or liquidated?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.final — Is this the final K-1 or final year of the entity?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.foreign — Was a K-3 issued or foreign income/taxes/entities disclosed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.state — Are state K-1s, withholding, composite returns or PTET credits involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.qbi — Were section 199A/QBI amounts, wages, property or loss carryovers reported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PASS.special — Were carried interest, section 751/743, PTE basis adjustments, recapture, credits or special disclosures reported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### PASS.k1_packet — Complete pass-through reporting package

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule E (individual_return_or_workpaper)
- **Support: Final Schedule K-1 package and all attachments** (`K1`; source_form)
  - Extract/match: entity EIN; tax period; beneficiary/partner/shareholder; form family; all boxes; footnotes; state schedules; K-3 status; corrected or final flags
  - Look in: Entity administrator portal; tax-package email; prior preparer
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** A prior-year interest creates an expected current package until closure is supported. Missing K-1 is not zero income.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.basis — Outside basis, debt basis and at-risk rollforward

**IF:** `Always within this active topic`
**THEN, form candidates:** 6198 (individual_return_or_workpaper)
- **Support: Outside basis, debt basis and at-risk rollforward** (`PASS.doc_basis`; support)
  - Extract/match: opening basis; contributions; allocated income/loss; distributions; liabilities; owner loans; adjustments; prior suspended amounts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Partnership tax-basis capital is not automatically outside basis. S corporation stock and debt basis are separate.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.limits — Pass-through limitation and activity workpaper

**IF:** `PASS.loss = true`
**THEN, form candidates:** 8582 (individual_return_or_workpaper); 6198 (individual_return_or_workpaper); 461 (individual_return_or_workpaper)
- **Support: Pass-through limitation and activity workpaper** (`PASS.doc_limits`; support)
  - Extract/match: basis-allowed loss; at-risk; passive grouping; participation; PTP isolation; carryovers; excess business loss
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply basis, at-risk and passive limits in the correct order; keep separate activity and PTP ledgers.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.sale — Interest disposition and ordinary-income reconciliation

**IF:** `PASS.sale = true`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); 4797 (individual_return_or_workpaper); 6252 (individual_return_or_workpaper)
- **Support: Interest disposition and ordinary-income reconciliation** (`PASS.doc_sale`; support)
  - Extract/match: sale agreement; proceeds; selling costs; debt relief; outside basis; partnership sales schedule; section 751 amounts; installment terms
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Broker-reported gain on a PTP sale may not reflect correct outside basis or ordinary-income components.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.foreign — K-3 and foreign allocations

**IF:** `PASS.foreign = true`
**THEN, form candidates:** 1116 (individual_return_or_workpaper); 8938 (individual_return_or_workpaper)
- **Support: K-3 and foreign allocations** (`PASS.doc_foreign`; support)
  - Extract/match: K-3; income categories; countries; taxes; foreign entities; prior carryovers
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Assess additional international forms from the attached disclosures, not only the K-1 face.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.qbi — Pass-through QBI supplement

**IF:** `PASS.qbi = true`
**THEN, form candidates:** 8995 (individual_return_or_workpaper); 8995-A (individual_return_or_workpaper)
- **Support: Pass-through QBI supplement** (`PASS.doc_qbi`; support)
  - Extract/match: 199A statement; qualified income; SSTB; W-2 wages; UBIA; REIT/PTP components; prior losses
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.special — Pass-through special allocations and disclosures

**IF:** `(PASS.special = true OR PASS.final = true)`
**THEN, form candidates:** 3800 (individual_return_or_workpaper); 1040 (individual_return_or_workpaper)
- **Support: Pass-through special allocations and disclosures** (`PASS.doc_special`; support)
  - Extract/match: full footnotes; carry/holding period; basis elections; final deductions; capital loss/NOL carryouts; recapture
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: map each disclosed code to a supported return/workpaper rule; unknown codes stay open.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.s_basis_form — S corporation shareholder-basis form test

**IF:** `(PASS.kind = "1120-S S corporation" AND (PASS.loss = true OR PASS.distributions = true OR PASS.sale = true OR PASS.contributed = true))`
**THEN, form candidates:** 7203 (individual_return_or_workpaper)
**Review gate:** Apply the actual shareholder filing triggers, including losses, distributions, stock disposal or loan repayment, not merely entity ownership.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### PASS.unmodeled_kind — Resolve unmodeled selection: PASS.kind

**IF:** `PASS.kind is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

**Linked track:** IF `PASS.foreign = true` → FOREIGN. Review the K-3 and ownership chain. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `PASS.sale = true` → DISPOSE. Create the pass-through interest disposition. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="other"></a>
## OTHER — Other income and nontaxable receipts

**Opening screen:** Were there benefits, unemployment, Social Security, alimony, winnings, awards, canceled payments, settlements or any other receipts not yet categorized?
**Unit:** Repeat for each income or receipt source. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### OTHER.kind — Which receipt type is involved?

**IF:** `Always within this active topic`
**Answer:** enum · Social Security / railroad retirement / Unemployment / State/local tax refund / Alimony / Gambling / Prize / award / jury / other compensation / Disability / workers compensation / Medicaid waiver / Lawsuit settlement / insurance / Gift / inheritance / life insurance / Scholarship / Personal payment / reimbursement / 1099-K / Other. Unknown/conflict does not become false.

#### OTHER.owner — Who received the payment, from whom, and when?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### OTHER.amount — What was the gross amount before withholding or fees?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### OTHER.form — Was an information statement issued, and is it accurate?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.repaid — Was any amount repaid, reversed or recovered, including a prior-year receipt?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.social_lump — Did benefits include a lump-sum payment for earlier years?

**IF:** `OTHER.kind = "Social Security / railroad retirement"`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.prior_itemized — Did the taxpayer itemize and receive a tax benefit for taxes later refunded?

**IF:** `OTHER.kind = "State/local tax refund"`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.alimony_date — When was the divorce/separation instrument executed and materially modified?

**IF:** `OTHER.kind = "Alimony"`
**Answer:** text. Unknown/conflict does not become false.

#### OTHER.losses — Were gambling losses or expenses incurred?

**IF:** `OTHER.kind = "Gambling"`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.professional — Was gambling carried on as a trade or business?

**IF:** `OTHER.kind = "Gambling"`
**Answer:** boolean. Unknown/conflict does not become false.

#### OTHER.settlement_terms — What claims, damages, attorney fees and payment allocations appear in the settlement?

**IF:** `OTHER.kind = "Lawsuit settlement / insurance"`
**Answer:** text. Unknown/conflict does not become false.

#### OTHER.foreign — Did the receipt come from a foreign payer, trust, estate or person?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### OTHER.receipt — Receipt classification and gross-payment record

**IF:** `Always within this active topic`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); Schedule 1 (individual_return_or_workpaper)
- **Support: Receipt classification and gross-payment record** (`OTHER.doc_receipt`; support)
  - Extract/match: payer; recipient; type; tax year; date; gross amount; withholding; information forms; classification rationale
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Receipt classification is not determined solely by whether a 1099 was issued.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.ssa — Social Security or railroad retirement statement

**IF:** `OTHER.kind = "Social Security / railroad retirement"`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Social Security or railroad retirement statement** (`OTHER.doc_ssa`; support)
  - Extract/match: SSA-1099/RRB-1099; gross benefits; repayments; withholding; earlier-year allocation; spouse benefits
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply the taxable-benefit worksheet and separately assess lump-sum election support.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.refund — Prior-year tax-benefit recovery workpaper

**IF:** `OTHER.kind = "State/local tax refund"`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Prior-year tax-benefit recovery workpaper** (`OTHER.doc_refund`; support)
  - Extract/match: 1099-G; prior Schedule A; actual tax deduction; SALT limit; state refund; prior AMT
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.alimony — Alimony agreement and payment history

**IF:** `OTHER.kind = "Alimony"`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Alimony agreement and payment history** (`OTHER.doc_alimony`; support)
  - Extract/match: execution date; modifications; payer/payee secure tax-ID reference; payment amounts; child support separation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.gambling — Gambling winnings and session/loss records

**IF:** `OTHER.kind = "Gambling"`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); Schedule A (individual_return_or_workpaper); Schedule C (individual_return_or_workpaper)
- **Support: Gambling winnings and session/loss records** (`OTHER.doc_gambling`; support)
  - Extract/match: W-2G; session diary; all winnings; losses; tickets/statements; professional facts; withholding
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply 2025 rules. Do not net losses against winnings without the correct reporting and substantiation.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.disability — Benefit taxability and premium history

**IF:** `OTHER.kind = "Disability / workers compensation / Medicaid waiver"`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); Schedule 1 (individual_return_or_workpaper)
- **Support: Benefit taxability and premium history** (`OTHER.doc_disability`; support)
  - Extract/match: benefit type; payer; disability onset; premiums paid pretax/after-tax; living arrangement; qualifying waiver program
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Determine taxability and any earned-income election from the program facts.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.settlement — Settlement agreement and gross legal proceeds

**IF:** `OTHER.kind = "Lawsuit settlement / insurance"`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Settlement agreement and gross legal proceeds** (`OTHER.doc_settlement`; support)
  - Extract/match: signed agreement; nature of underlying claims; damages categories; attorney fees; fee payment; 1099s; interest
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: taxability and deductibility depend on the underlying claim, not the label on the settlement.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.repayment — Repayment and claim-of-right evidence

**IF:** `OTHER.repaid = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper); Schedule 3 (individual_return_or_workpaper)
- **Support: Repayment and claim-of-right evidence** (`OTHER.doc_repayment`; support)
  - Extract/match: original inclusion year; original tax return; repayment date; legal obligation; amount; corrected forms
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review deduction versus credit and amendment implications; do not simply offset unrelated income.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.personal1099 — Personal payments and erroneous information-return reconciliation

**IF:** `OTHER.kind = "Personal payment / reimbursement / 1099-K"`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); 8949 (individual_return_or_workpaper)
- **Support: Personal payments and erroneous information-return reconciliation** (`OTHER.doc_personal1099`; support)
  - Extract/match: gross reported amount; sale/reimbursement/gift breakdown; original cost; payer correction attempts; duplicates
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Personal-item gains, nondeductible personal losses and reimbursements require different paths.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### OTHER.unmodeled_kind — Resolve unmodeled selection: OTHER.kind

**IF:** `OTHER.kind is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

**Linked track:** IF `OTHER.foreign = true` → FOREIGN. Classify foreign income/gift/trust source. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="home"></a>
## HOME — Sale of a principal residence

**Opening screen:** Did the taxpayer or spouse sell or otherwise dispose of a home, or receive Form 1099-S for one?
**Unit:** Repeat for each home sale. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### HOME.owners — Who owned the property, during which dates, and in what proportions?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HOME.dates — What were the purchase, occupancy, move-out and sale dates?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HOME.owned2 — Did the relevant owner satisfy the two-year ownership test during the five-year lookback?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.used2 — Did each relevant spouse satisfy the two-year use test during the five-year lookback?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.prior_exclusion — Was another home-sale exclusion claimed in the preceding two years?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.reduced — Could work, health, unforeseen circumstances or a special service rule affect eligibility?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.rental — Was any part used for rental/business, or was there nonqualified use?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.depreciation — Was depreciation allowed or allowable on the home?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.1099s — Was Form 1099-S issued?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOME.special — Were divorce, death, an installment sale, a gift/inheritance, foreclosure or a like-kind exchange involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### HOME.home_sale — Home sale proceeds and exclusion packet

**IF:** `Always within this active topic`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Home sale proceeds and exclusion packet** (`HOME.doc_home_sale`; support)
  - Extract/match: purchase and sale closing disclosures; title; selling costs; improvements; occupancy calendar; prior exclusions; 1099-S
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review gain reporting even when exclusion is available. A personal loss is not automatically deductible.
**Authority:** [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### HOME.home_use — Home-sale special use and depreciation

**IF:** `(HOME.rental = true OR HOME.depreciation = true)`
**THEN, form candidates:** 4797 (individual_return_or_workpaper); Schedule D (individual_return_or_workpaper)
- **Support: Home-sale special use and depreciation** (`HOME.doc_home_use`; support)
  - Extract/match: rental/business dates; nonqualified-use periods; depreciation; office boundaries; adjusted basis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### HOME.exception — Reduced-exclusion or special home-sale support

**IF:** `(HOME.reduced = true OR HOME.special = true)`
**THEN, form candidates:** 8949 (individual_return_or_workpaper); 6252 (individual_return_or_workpaper)
- **Support: Reduced-exclusion or special home-sale support** (`HOME.doc_exception`; support)
  - Extract/match: qualifying event; dates; employer/medical/event proof; relevant ownership history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Document the specific exception rather than assuming the full exclusion.
**Authority:** [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

**Linked track:** IF `HOME.rental = true` → RENTAL. Reconcile rental use and depreciation for the home sale. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="adjust"></a>
## ADJUST — Adjustments and special deductions

**Opening screen:** Were there student-loan interest, educator expenses, alimony paid, qualifying moving costs, early-savings penalties or other income adjustments?
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### ADJUST.student_loan — Was interest paid on a qualified student loan?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.loan_owner — Who is legally obligated on the loan, who paid it, and can the borrower be claimed as a dependent?

**IF:** `ADJUST.student_loan = true`
**Answer:** text. Unknown/conflict does not become false.

#### ADJUST.educator — Was the taxpayer/spouse an eligible educator with unreimbursed classroom expenses?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.alimony — Was alimony paid under a divorce or separation instrument?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.moving — Were moving expenses connected to a qualifying active-duty military move?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.reservist — Were qualifying reservist, performing-artist or fee-basis-government employee expenses incurred?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.penalty — Was there a penalty on early withdrawal of savings?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.legal — Were legal fees, whistleblower expenses, reforestation, 501(c)(18), or another uncommon adjustment involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ADJUST.other_adjustment — Describe any adjustment not already captured. Enter none if none.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### ADJUST.student — Student-loan interest support

**IF:** `ADJUST.student_loan = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Student-loan interest support** (`ADJUST.doc_student`; support)
  - Extract/match: 1098-E; lender statement; qualified loan; borrower; payments; dependency; filing status; MAGI
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.educator — Educator qualification and expenses

**IF:** `ADJUST.educator = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Educator qualification and expenses** (`ADJUST.doc_educator`; support)
  - Extract/match: school; role; hours; qualifying supplies; reimbursements; grant amounts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.alimony — Alimony paid agreement and support

**IF:** `ADJUST.alimony = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Alimony paid agreement and support** (`ADJUST.doc_alimony`; support)
  - Extract/match: instrument execution/modification dates; payer/payee; payments; child-support distinction
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.moving — Qualified military move packet

**IF:** `ADJUST.moving = true`
**THEN, form candidates:** 3903 (individual_return_or_workpaper)
- **Support: Qualified military move packet** (`ADJUST.doc_moving`; support)
  - Extract/match: orders; active-duty status; permanent change of station; moving/storage costs; reimbursement
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.employee — Special employee expense packet

**IF:** `ADJUST.reservist = true`
**THEN, form candidates:** 2106 (individual_return_or_workpaper)
- **Support: Special employee expense packet** (`ADJUST.doc_employee`; support)
  - Extract/match: qualifying role; travel distance; orders/contracts; receipts; reimbursements
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.penalty — Savings early-withdrawal penalty statement

**IF:** `ADJUST.penalty = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Savings early-withdrawal penalty statement** (`ADJUST.doc_penalty`; support)
  - Extract/match: 1099-INT/OID; penalty amount; owner; institution
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

#### ADJUST.special — Other adjustment legal basis and support

**IF:** `ADJUST.legal = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Other adjustment legal basis and support** (`ADJUST.doc_special`; support)
  - Extract/match: exact adjustment; qualifying statute; amount; payment date; reimbursement; income nexus
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: identify the actual provision and limitations rather than using an unspecified miscellaneous deduction.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)


<a id="itemize"></a>
## ITEMIZE — Standard versus itemized deductions

**Opening screen:** Were there medical costs, taxes, mortgage/investment interest, gifts, casualty losses or other potentially itemized deductions?
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### ITEMIZE.medical — Were unreimbursed medical, dental, vision, premiums, long-term-care or related costs paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.medical_people — Identify patients, payment dates, reimbursements and whether HSA/FSA or insurance funds were used.

**IF:** `ITEMIZE.medical = true`
**Answer:** text. Unknown/conflict does not become false.

#### ITEMIZE.taxes — Were state/local income, sales, real estate or personal-property taxes paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.tax_choice — Are both state/local income-tax and sales-tax amounts available for comparison?

**IF:** `ITEMIZE.taxes = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.mortgage — Was interest paid on debt secured by a main or second home?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.refinance — Were there refinancings, home-equity loans, points or cash-out proceeds?

**IF:** `ITEMIZE.mortgage = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.loan_use — What were the origination dates, balances and actual uses of each mortgage/HELOC advance?

**IF:** `ITEMIZE.mortgage = true`
**Answer:** text. Unknown/conflict does not become false.

#### ITEMIZE.gifts — Were charitable contributions made, including payroll giving or property donations?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.disaster — Was there a casualty/theft/disaster loss potentially deductible?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.investment — Was investment interest paid or carried forward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.other — Were gambling losses, estate tax on income in respect of a decedent, impairment-related work expenses, or another surviving special deduction involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.forced — Could separate-spouse itemizing, nonresident/dual status or another rule restrict the standard deduction?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ITEMIZE.comparison — Has the preparer compared allowed itemized deductions with the correct standard deduction and state effects?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### ITEMIZE.medical — Medical expense and reimbursement ledger

**IF:** `ITEMIZE.medical = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Medical expense and reimbursement ledger** (`ITEMIZE.doc_medical`; support)
  - Extract/match: patient; qualifying relationship; provider; service; payment date; amount; reimbursements; insurance; HSA/FSA; long-term-care age limits
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Only qualifying unreimbursed amounts enter the medical deduction calculation; retain the AGI-floor workpaper.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

#### ITEMIZE.taxes — Tax payments eligible for itemized deductions

**IF:** `ITEMIZE.taxes = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Tax payments eligible for itemized deductions** (`ITEMIZE.doc_taxes`; support)
  - Extract/match: tax type; jurisdiction; actual payment; refund; escrow disbursement; value-based assessment; income-versus-sales election
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply 2025 SALT limitations and phase-down rules; escrow deposits are not themselves property-tax payments.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

#### ITEMIZE.mortgage — All home mortgage statements and acquisition-debt tracing

**IF:** `ITEMIZE.mortgage = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: All home mortgage statements and acquisition-debt tracing** (`ITEMIZE.doc_mortgage`; support)
  - Extract/match: 1098; lender; secured property; origination dates; average balances; proceeds use; refinancings; points; ownership
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Deductibility depends on qualifying debt and proceeds use, not simply interest appearing on Form 1098.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

#### ITEMIZE.refinance — Refinance, cash-out and points history

**IF:** `(ITEMIZE.mortgage = true AND ITEMIZE.refinance = true)`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Refinance, cash-out and points history** (`ITEMIZE.doc_refinance`; support)
  - Extract/match: closing disclosures; old/new debt; cash-out tracing; home improvements; points; remaining unamortized points
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

#### ITEMIZE.other — Other itemized deduction substantiation

**IF:** `ITEMIZE.other = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Other itemized deduction substantiation** (`ITEMIZE.doc_other`; support)
  - Extract/match: deduction category; payment; income linkage; statutory rule; limitations; duplicate-use check
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify that the deduction is permitted for 2025 rather than assuming all unreimbursed expenses are deductible.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

#### ITEMIZE.compare — Standard/itemized comparison and restrictions

**IF:** `Always within this active topic`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); Schedule A (individual_return_or_workpaper)
- **Support: Standard/itemized comparison and restrictions** (`ITEMIZE.doc_compare`; workpaper)
  - Extract/match: age/blindness; dependency; marital status; spouse itemization; residency; allowable deductions; federal/state comparison
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Collection of deduction records does not automatically elect itemizing.
**Authority:** [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

**Linked track:** IF `ITEMIZE.gifts = true` → CHARITY. Enumerate charitable gifts and carryovers. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.

**Linked track:** IF `ITEMIZE.disaster = true` → DISASTER. Create the casualty/disaster event. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="charity"></a>
## CHARITY — Charitable contributions and appraisals

**Opening screen:** Were cash or noncash charitable gifts made, or are charitable carryovers available?
**Unit:** Repeat for each donation or similar-property group. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CHARITY.kind — What was donated?

**IF:** `Always within this active topic`
**Answer:** enum · Cash / check / card / payroll / Publicly traded securities / Household goods / clothing / Vehicle / boat / aircraft / Real estate / conservation interest / Digital assets / private stock / other property / Carryover only. Unknown/conflict does not become false.

#### CHARITY.organization — Identify the donee and evidence it is a qualifying organization.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### CHARITY.value — What amount is claimed for this gift or similar-property group?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### CHARITY.benefit — Did the donor receive goods, services, tickets or another benefit?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.ack — Was a contemporaneous written acknowledgement obtained when required?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.noncash — Is this a noncash contribution?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.noncash_total — What is the aggregate claimed noncash deduction across the return?

**IF:** `CHARITY.noncash = true`
**Answer:** number. Unknown/conflict does not become false.

#### CHARITY.appraisal — Could appraisal, appraiser signature, donee acknowledgement or special attachment rules apply?

**IF:** `CHARITY.noncash = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.basis — Are acquisition date, basis, holding period, condition and valuation method supported?

**IF:** `CHARITY.noncash = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.carryover — Is there a prior charitable contribution carryforward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CHARITY.qcd — Was this paid directly from an IRA as a QCD?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CHARITY.cash — Charitable payment and eligibility records

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Charitable payment and eligibility records** (`CHARITY.doc_cash`; support)
  - Extract/match: donee; date; amount; payment proof; charitable status; restrictions; goods/services value
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review substantiation deadlines, organization eligibility and percentage limits; not every payment to a nonprofit qualifies.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

#### CHARITY.noncash — Noncash donation inventory and valuation

**IF:** `CHARITY.noncash = true`
**THEN, form candidates:** 8283 (individual_return_or_workpaper)
- **Support: Noncash donation inventory and valuation** (`CHARITY.doc_noncash`; support)
  - Extract/match: item/group description; acquisition date; donor basis; holding period; condition; donation date; FMV; method; donee
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply aggregate and similar-property rules, including the over-$500 noncash reporting test; exceptions still need review.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

#### CHARITY.appraisal — Required appraisal and signed donation acknowledgements

**IF:** `(CHARITY.noncash = true AND CHARITY.appraisal = true)`
**THEN, form candidates:** 8283 (individual_return_or_workpaper)
- **Support: Required appraisal and signed donation acknowledgements** (`CHARITY.doc_appraisal`; support)
  - Extract/match: qualified appraisal; appraiser qualifications; valuation date; donor basis; required signatures; attachment threshold
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** The general over-$5,000 appraisal framework has property-specific exceptions; public securities, vehicles and digital assets are not interchangeable.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

#### CHARITY.vehicle — Donated vehicle special documentation

**IF:** `CHARITY.kind = "Vehicle / boat / aircraft"`
**THEN, form candidates:** 8283 (individual_return_or_workpaper)
- **Support: Donated vehicle special documentation** (`CHARITY.doc_vehicle`; support)
  - Extract/match: 1098-C; VIN; sale proceeds or significant-use certification; contemporaneous acknowledgement; valuation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

#### CHARITY.carryover — Charitable carryforward schedule

**IF:** `CHARITY.carryover = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Charitable carryforward schedule** (`CHARITY.doc_carryover`; support)
  - Extract/match: origin year; contribution type; percentage limitation category; used amounts; expiration; remaining balance
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

#### CHARITY.qcd_duplicate — Prevent QCD double deduction

**IF:** `CHARITY.qcd = true`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Route to the IRA/QCD workpaper and do not also use the same amount as an itemized contribution.
**Authority:** [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)


<a id="education"></a>
## EDUCATION — Education, scholarships and 529 coordination

**Opening screen:** Did anyone in the tax household attend school, receive scholarships, use a 529/Coverdell account, or claim education benefits?
**Unit:** Repeat for each student. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### EDUCATION.student — Identify the student and the taxpayer who may claim them.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### EDUCATION.postsecondary — Was the institution an eligible postsecondary institution?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.half_time — Was the student at least half-time for an academic period?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.degree — Was the student pursuing a degree or recognized credential?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.first4 — Had the student completed the first four years of postsecondary education before this year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.aotc_years — For how many earlier tax years was AOTC/Hope claimed for this student?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### EDUCATION.drug_felony — Was there a disqualifying felony drug conviction before year-end?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.expenses — Were tuition, required fees, books, supplies or equipment paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.scholarships — Were scholarships, grants, fellowships, veterans benefits or employer reimbursements received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.restrictions — Which aid amounts were restricted to tuition and which could pay living costs?

**IF:** `EDUCATION.scholarships = true`
**Answer:** text. Unknown/conflict does not become false.

#### EDUCATION.529 — Was there a 529/Coverdell distribution, rollover or refund?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.529_type — Describe higher education, K-12, apprenticeship, credentials, student loans or Roth-rollover use.

**IF:** `EDUCATION.529 = true`
**Answer:** text. Unknown/conflict does not become false.

#### EDUCATION.refund — Were tuition or other qualifying costs refunded or reimbursed after being used for a credit?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.support — Could age, full-time study, parents living, or self-support affect refundable AOTC eligibility?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### EDUCATION.disallowed — Was an education credit disallowed or restricted in an earlier year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### EDUCATION.tuition — Education source documents

**IF:** `Always within this active topic`
**THEN, form candidates:** 8863 (individual_return_or_workpaper)
- **Support: 1098-T plus detailed school account and payment records** (`TUITION`; source_form)
  - Extract/match: student; school EIN; billed and paid dates; tuition; fees; enrollment; refunds; scholarships; employer assistance
  - Look in: School bursar portal; tax folder; payment statements
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: A 1098-T exception may apply; retain school account, payment records and documented preparer determination rather than silently skipping the credit.
**Review gate:** Evaluate AOTC and lifetime learning credit separately; the 1098-T boxes alone do not establish eligible expenses.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

#### EDUCATION.allocation — Student-level education expense allocation

**IF:** `Always within this active topic`
**THEN, form candidates:** 8863 (individual_return_or_workpaper); 5329 (individual_return_or_workpaper)
- **Support: Student-level education expense allocation** (`EDUCATION.doc_allocation`; workpaper)
  - Extract/match: each expense; date paid; aid; 529/Coverdell use; employer benefits; credit allocation; taxable scholarship allocation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** No expense can support multiple incompatible tax benefits. Preserve a shared allocation ledger across the student and parents.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

#### EDUCATION.scholarships — Scholarship and grant terms

**IF:** `EDUCATION.scholarships = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper)
- **Support: Scholarship and grant terms** (`EDUCATION.doc_scholarships`; support)
  - Extract/match: award agreements; tuition restrictions; living costs; service requirements; disbursement; taxable amounts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Any election to treat unrestricted aid as taxable needs coordinated household calculations and approval.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

#### EDUCATION.529 — 529/Coverdell distributions and eligibility

**IF:** `EDUCATION.529 = true`
**THEN, form candidates:** 5329 (individual_return_or_workpaper); Schedule 1 (individual_return_or_workpaper)
- **Support: 529/Coverdell distributions and eligibility** (`EDUCATION.doc_529`; support)
  - Extract/match: 1099-Q; recipient; beneficiary; basis/earnings; dates; eligible expenses; refunds; rollovers; prior use
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review federal and state qualification and recapture; do not assume every withdrawal for a student is qualified.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

#### EDUCATION.refund — Education refund and credit recapture

**IF:** `EDUCATION.refund = true`
**THEN, form candidates:** 8863 (individual_return_or_workpaper)
- **Support: Education refund and credit recapture** (`EDUCATION.doc_refund`; support)
  - Extract/match: original credit year; allocated expenses; refund date; amount; benefit recovery
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

#### EDUCATION.prior_credit — Prior AOTC claims and disallowances

**IF:** `(EDUCATION.aotc_years > 0 OR EDUCATION.disallowed = true)`
**THEN, form candidates:** 8862 (individual_return_or_workpaper); 8863 (individual_return_or_workpaper)
- **Support: Prior AOTC claims and disallowances** (`EDUCATION.doc_prior_credit`; support)
  - Extract/match: student prior credit years; preparer workpapers; disallowance notices; ban period
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 970: Education benefits](https://www.irs.gov/publications/p970)


<a id="care"></a>
## CARE — Dependent care and adoption

**Opening screen:** Were there care expenses, dependent-care employer benefits, adoption costs or adoption benefits?
**Unit:** Repeat for each qualifying person or adoption. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CARE.kind — Is this dependent care or adoption?

**IF:** `Always within this active topic`
**Answer:** enum · Dependent care / Adoption. Unknown/conflict does not become false.

#### CARE.person — Identify the cared-for person/child and relationship.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### CARE.age — What was the person’s age when care was provided?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** number. Unknown/conflict does not become false.

#### CARE.unable — Was a spouse or dependent physically or mentally unable to care for themselves?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.work — Was care needed so the taxpayer and, if relevant, spouse could work or look for work?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.student_spouse — Was a spouse a full-time student or unable to care for themselves?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.provider — Identify each provider, secure TIN reference, payment and service period.

**IF:** `CARE.kind = "Dependent care"`
**Answer:** text. Unknown/conflict does not become false.

#### CARE.related_provider — Was the provider a spouse, parent of the child, dependent, or the taxpayer’s child under 19?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.benefits — Were dependent-care FSA/employer benefits used or forfeited?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.custody — Is the qualifying person subject to separated-parent custody rules?

**IF:** `CARE.kind = "Dependent care"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.adoption_type — Is the adoption domestic, foreign, or U.S. special needs?

**IF:** `CARE.kind = "Adoption"`
**Answer:** enum · Domestic / Foreign / U.S. special needs / Unresolved. Unknown/conflict does not become false.

#### CARE.final — Was the adoption finalized this year or in a previous year?

**IF:** `CARE.kind = "Adoption"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.employer — Were employer adoption benefits or reimbursements provided?

**IF:** `CARE.kind = "Adoption"`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARE.prior — Were adoption costs or credits claimed or carried forward previously?

**IF:** `CARE.kind = "Adoption"`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CARE.care — Dependent-care qualification and payments

**IF:** `CARE.kind = "Dependent care"`
**THEN, form candidates:** 2441 (individual_return_or_workpaper)
- **Support: Dependent-care qualification and payments** (`CARE.doc_care`; support)
  - Extract/match: qualifying person; nights; age/disability; provider TIN reference; service dates; amounts; work purpose; earned income
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply provider exclusions and separated-parent rules; a dependency release does not necessarily transfer care benefits.
**Authority:** [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CARE.fsa — Dependent-care benefit allocation

**IF:** `(CARE.kind = "Dependent care" AND CARE.benefits = true)`
**THEN, form candidates:** 2441 (individual_return_or_workpaper)
- **Support: Dependent-care benefit allocation** (`CARE.doc_fsa`; support)
  - Extract/match: W-2 box 10; benefits received; expenses incurred; carryover/grace period; forfeitures; spouse benefits
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Coordinate employer exclusion and credit; do not use the same expenses twice.
**Authority:** [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CARE.adoption — Adoption costs, finalization and benefits packet

**IF:** `CARE.kind = "Adoption"`
**THEN, form candidates:** 8839 (individual_return_or_workpaper)
- **Support: Adoption costs, finalization and benefits packet** (`CARE.doc_adoption`; support)
  - Extract/match: child secure ID reference; domestic/foreign status; decree; special-needs determination; qualified costs by year; employer benefits; reimbursements; carryovers
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Timing, eligibility and refundability depend on the tax year and adoption facts.
**Authority:** [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CARE.unmodeled_adoption_type — Resolve unmodeled selection: CARE.adoption_type

**IF:** `CARE.adoption_type is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)


<a id="health"></a>
## HEALTH — Marketplace health coverage

**Opening screen:** Did anyone in the tax household have Marketplace coverage, receive advance premium tax credits, or expect a 1095-A?
**Unit:** Repeat for each policy. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### HEALTH.people — Who was covered, including anyone not on this return?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HEALTH.months — Which months were covered and who belonged to each tax household?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HEALTH.advance — Were any advance premium tax credit payments made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.corrected — Is a 1095-A missing, incorrect, voided or corrected?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.shared — Was the policy shared between different tax returns?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.allocation — Have policy allocation percentages and counterparties been established?

**IF:** `HEALTH.shared = true`
**Answer:** text. Unknown/conflict does not become false.

#### HEALTH.marriage — Was there a marriage, divorce, separation or other household change during the year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.other_coverage — Was employer, Medicare, Medicaid or other potentially disqualifying coverage available?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.hra — Was an ICHRA, QSEHRA or other employer reimbursement arrangement involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.dependent_income — Did a dependent with a filing requirement have income affecting household MAGI?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HEALTH.mfs_relief — Could abuse, abandonment or another married-separate exception apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### HEALTH.policy — Marketplace reporting and reconciliation

**IF:** `Always within this active topic`
**THEN, form candidates:** 8962 (individual_return_or_workpaper)
- **Support: Final Form 1095-A for every Marketplace policy** (`HEALTH_A`; source_form)
  - Extract/match: policy ID; covered persons; months; columns A, B and C; correction or void status
  - Look in: Marketplace account; authorized email; taxpayer records
  - Accept only when: Use final corrected records and a month-by-month household reconciliation. 1095-B and 1095-C are not substitutes for 1095-A.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
- **Support: Marketplace coverage and household reconciliation** (`ACA_MONTHS`; support)
  - Extract/match: covered individuals by month; tax households; other coverage offers; employer affordability data; dependents income; marriage/divorce dates; SLCSP amounts
  - Look in: Marketplace records; employer benefits; household records
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Form 8962 may be required to reconcile advance payments even if a normal income filing threshold is not met.
**Authority:** [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

#### HEALTH.shared — Shared-policy allocation agreement/workpaper

**IF:** `HEALTH.shared = true`
**THEN, form candidates:** 8962 (individual_return_or_workpaper)
- **Support: Shared-policy allocation agreement/workpaper** (`HEALTH.doc_shared`; support)
  - Extract/match: policy amounts by month; allocation percentages; counterpart taxpayer secure ID reference; allocation rule; signatures/confirmations
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

#### HEALTH.coverage — Other-coverage and employer-offer eligibility

**IF:** `(HEALTH.other_coverage = true OR HEALTH.hra = true)`
**THEN, form candidates:** 8962 (individual_return_or_workpaper)
- **Support: Other-coverage and employer-offer eligibility** (`HEALTH.doc_coverage`; support)
  - Extract/match: monthly offers; affordability; minimum value; family cost; actual enrollment; Medicare dates; HRA amounts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

#### HEALTH.exception — Marketplace household-change or exception support

**IF:** `(HEALTH.marriage = true OR HEALTH.mfs_relief = true)`
**THEN, form candidates:** 8962 (individual_return_or_workpaper)
- **Support: Marketplace household-change or exception support** (`HEALTH.doc_exception`; support)
  - Extract/match: effective dates; prior household; new household; legal status; applicable exception; safety-preserving evidence
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Sensitive abuse/abandonment facts must be handled privately; do not contact the spouse without express authority.
**Authority:** [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)


<a id="hsa"></a>
## HSA — HSAs, MSAs, FSAs and ABLE accounts

**Opening screen:** Did anyone hold or use an HSA, MSA, FSA or ABLE account, or have unresolved contribution/distribution issues?
**Unit:** Repeat for each account. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### HSA.owner — Identify the account owner and plan/custodian.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HSA.type — What type of account is involved?

**IF:** `Always within this active topic`
**Answer:** enum · HSA / Archer or Medicare Advantage MSA / Health FSA / HRA / ABLE. Unknown/conflict does not become false.

#### HSA.contribution — Were any employer or personal contributions made or designated for this tax year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.distribution — Were any distributions made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.coverage — List each month’s HDHP category and other health coverage.

**IF:** `(HSA.type = "HSA" AND HSA.contribution = true)`
**Answer:** text. Unknown/conflict does not become false.

#### HSA.medicare — Was there Medicare enrollment, including retroactive coverage?

**IF:** `(HSA.type = "HSA" AND HSA.contribution = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.disqualifying — Could a general-purpose FSA, other coverage or dependency make any contribution month ineligible?

**IF:** `(HSA.type = "HSA" AND HSA.contribution = true)`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.lastmonth — Was the HSA last-month rule used this year or is a prior testing period still open?

**IF:** `HSA.type = "HSA"`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.qualified — Are all distributions tied to eligible unreimbursed expenses?

**IF:** `HSA.distribution = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.excess — Were there excess contributions, mistaken distributions or corrections?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.transfer — Were there trustee transfers, rollovers, IRA-to-HSA funding or death transfers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HSA.carry_issue — Is a prior testing-period failure or unresolved additional-tax issue present?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### HSA.hsa_forms — HSA activity reporting

**IF:** `(HSA.type = "HSA" AND (HSA.contribution = true OR HSA.distribution = true OR HSA.lastmonth = true OR HSA.carry_issue = true))`
**THEN, form candidates:** 8889 (individual_return_or_workpaper)
- **Support: HSA contribution and distribution statements** (`HSA_DOCS`; source_form)
  - Extract/match: account owner; 1099-SA; 5498-SA if available; employer W-2 code W; direct contributions; rollovers; corrections
  - Look in: HSA custodian; payroll; tax folder
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: Contribution transaction statements can establish amounts when Form 5498-SA is not yet issued. Preserve the expected later form as a reconciliation task.
**Review gate:** A separate HSA reporting workpaper is needed for each spouse with reportable activity; do not aggregate owners.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.medical — Substantiate HSA distributions

**IF:** `(HSA.type = "HSA" AND HSA.distribution = true)`
**THEN, form candidates:** 8889 (individual_return_or_workpaper)
- **Support: Unreimbursed qualified medical expense allocation for HSA distributions** (`HSA_MED`; support)
  - Extract/match: service date; patient; amount; HSA establishment date; distribution used; insurance or FSA reimbursement; prior-year use
  - Look in: Medical invoices; insurer EOBs; HSA receipts vault
  - Accept only when: Avoid reuse across HSA, FSA, insurance, Schedule A and other benefits; older expenses require proof that they were not previously reimbursed or deducted.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.eligibility — HSA month-by-month eligibility and contribution limit

**IF:** `(HSA.type = "HSA" AND HSA.contribution = true)`
**THEN, form candidates:** 8889 (individual_return_or_workpaper)
- **Support: HSA month-by-month eligibility and contribution limit** (`HSA.doc_eligibility`; support)
  - Extract/match: HDHP coverage; self/family category; Medicare; other coverage; FSA; dependency; age; spouse allocation; employer/personal contributions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.testing — HSA last-month and testing-period history

**IF:** `(HSA.lastmonth = true OR HSA.carry_issue = true)`
**THEN, form candidates:** 8889 (individual_return_or_workpaper)
- **Support: HSA last-month and testing-period history** (`HSA.doc_testing`; support)
  - Extract/match: prior December eligibility; testing period; months lost eligibility; death/disability exception; prior contributions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.correction — Savings-account excess/correction packet

**IF:** `HSA.excess = true`
**THEN, form candidates:** 5329 (individual_return_or_workpaper)
- **Support: Savings-account excess/correction packet** (`HSA.doc_correction`; support)
  - Extract/match: account type; limit; excess; earnings; correction date; custodian confirmation; affected years
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.msa — MSA reporting support

**IF:** `HSA.type = "Archer or Medicare Advantage MSA"`
**THEN, form candidates:** 8853 (individual_return_or_workpaper)
- **Support: MSA reporting support** (`HSA.doc_msa`; support)
  - Extract/match: 1099-SA; 5498-SA; eligibility; contributions; qualified expenses; distributions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.able — ABLE eligibility and expense allocation

**IF:** `HSA.type = "ABLE"`
**THEN, form candidates:** 5329 (individual_return_or_workpaper); Schedule 1 (individual_return_or_workpaper)
- **Support: ABLE eligibility and expense allocation** (`HSA.doc_able`; support)
  - Extract/match: beneficiary; disability eligibility; contribution sources; distributions; qualified disability expenses; rollovers; 1099-QA
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply the eligibility age and other rules for the actual tax year, not a later-year expansion.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### HSA.fsa — FSA/HRA benefits and duplicate-use control

**IF:** `HSA.type = "Health FSA / HRA"`
**THEN, form candidates:** None implied by this rule alone.
- **Support: FSA/HRA benefits and duplicate-use control** (`HSA.doc_fsa`; support)
  - Extract/match: plan; claims; reimbursements; forfeitures; carryover/grace period; employer contributions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Coordinate with medical deductions, care credits and HSA eligibility; holding a health FSA alone does not create Form 8889.
**Authority:** [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="energy"></a>
## ENERGY — Home energy improvements

**Opening screen:** Were energy-efficiency improvements, solar/battery/other clean-energy systems or prior energy-credit carryovers involved?
**Unit:** Repeat for each project. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### ENERGY.type — What type of project or carryover is this?

**IF:** `Always within this active topic`
**Answer:** enum · Home efficiency improvement / Solar / wind / geothermal / battery / fuel cell / Prior residential clean energy carryover / Other. Unknown/conflict does not become false.

#### ENERGY.property — Identify the property, owner, occupant and business-use percentage.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### ENERGY.dates — Record purchase, installation-completion and placed-in-service dates.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### ENERGY.costs — Separate equipment, labor, rebates, utility subsidies and reimbursements.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### ENERGY.standards — Are manufacturer certifications, eligible standards and required product identification numbers available?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ENERGY.main_home — Was it installed in an existing main home, another residence, a rental or new construction?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### ENERGY.shared — Did multiple owners/occupants pay or claim expenses for the project?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### ENERGY.carry — Is a prior residential clean energy credit carryforward available?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### ENERGY.energy — Energy credit installation and eligibility packet

**IF:** `Always within this active topic`
**THEN, form candidates:** 5695 (individual_return_or_workpaper)
- **Support: Energy credit installation and eligibility packet** (`ENERGY.doc_energy`; support)
  - Extract/match: itemized invoices; installation date; qualifying property; manufacturer certification; PIN if required; receipts; labor split; rebates; business use
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify 2025 eligibility, category caps and effective/termination dates; a product marketed as energy efficient is not sufficient.
**Authority:** [Instructions: Residential energy credits](https://www.irs.gov/instructions/i5695)

#### ENERGY.carry — Prior residential clean energy credit carryforward

**IF:** `ENERGY.carry = true`
**THEN, form candidates:** 5695 (individual_return_or_workpaper)
- **Support: Prior residential clean energy credit carryforward** (`ENERGY.doc_carry`; support)
  - Extract/match: prior Form 5695; origin year; credit allowed; carryforward remaining
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Residential energy credits](https://www.irs.gov/instructions/i5695)

#### ENERGY.unmodeled_type — Resolve unmodeled selection: ENERGY.type

**IF:** `ENERGY.type is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Instructions: Residential energy credits](https://www.irs.gov/instructions/i5695)


<a id="vehicle"></a>
## VEHICLE — Vehicle credits and loan-interest deduction

**Opening screen:** Was a vehicle purchased, a vehicle tax credit transferred/claimed, eligible loan interest paid, or charging equipment installed?
**Unit:** Repeat for each vehicle or charging installation. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### VEHICLE.kind — What transaction is involved?

**IF:** `Always within this active topic`
**Answer:** enum · New vehicle purchase / Used vehicle purchase / Lease / Charging equipment / Prior credit issue or recapture. Unknown/conflict does not become false.

#### VEHICLE.dates — Record binding contract, payment, acquisition and delivery/placed-in-service dates.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### VEHICLE.vin — Record a secure source reference for VIN, model, model year and assembly information.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### VEHICLE.ev — Is this a clean vehicle potentially eligible for a federal vehicle credit?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.transfer — Was a credit transferred to the dealer at the point of sale?

**IF:** `VEHICLE.ev = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.seller — Is an accepted seller/time-of-sale report available?

**IF:** `VEHICLE.ev = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.income — Are current and prior-year MAGI and filing status available for the credit test?

**IF:** `VEHICLE.ev = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.business — Was there business use or a commercial clean vehicle claim?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.loan — Was interest paid on a loan used to buy a vehicle?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.loan_date — Was the loan originated after December 31, 2024, and what vehicle purchase did it finance?

**IF:** `VEHICLE.loan = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.new_original — Was original use of the vehicle with the taxpayer?

**IF:** `VEHICLE.loan = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.us_assembly — Was final assembly in the United States?

**IF:** `VEHICLE.loan = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.secured — Was the loan secured by a first lien and the vehicle purchased for personal use?

**IF:** `VEHICLE.loan = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.refinance — Was the loan refinanced or partly used for something other than the original qualifying vehicle?

**IF:** `VEHICLE.loan = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### VEHICLE.disposed — Was the vehicle returned, resold quickly, leased to others or converted in use?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### VEHICLE.credit — Clean vehicle eligibility and seller report

**IF:** `VEHICLE.ev = true`
**THEN, form candidates:** 8936 (individual_return_or_workpaper); Schedule A (Form 8936) (individual_return_or_workpaper)
- **Support: Clean vehicle eligibility and seller report** (`VEHICLE.doc_credit`; support)
  - Extract/match: VIN; accepted seller report; buyer; new/used status; acquisition and service dates; price/MSRP; prior sales; battery/assembly eligibility; MAGI; credit transfer
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Use the actual acquisition and transition-date rules. A dealer discount is not proof the filer qualifies for the credit.
**Authority:** [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### VEHICLE.loan — Vehicle-loan interest qualification and payments

**IF:** `VEHICLE.loan = true`
**THEN, form candidates:** Schedule 1-A (individual_return_or_workpaper)
- **Support: Vehicle-loan interest qualification and payments** (`VEHICLE.doc_loan`; support)
  - Extract/match: origination date; signed loan; first lien; original use; personal use; U.S. final assembly; VIN; interest statement; refinance tracing; business interest allocation; MAGI
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not equate all car interest with qualified interest. Used vehicles, leases and business-deducted interest require separate treatment.
**Authority:** [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### VEHICLE.charger — Charging equipment credit facts

**IF:** `VEHICLE.kind = "Charging equipment"`
**THEN, form candidates:** 8911 (individual_return_or_workpaper)
- **Support: Charging equipment credit facts** (`VEHICLE.doc_charger`; support)
  - Extract/match: property location; census tract qualification; installation date; equipment/labor cost; business use; subsidies
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify location and effective-date conditions before credit selection.
**Authority:** [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### VEHICLE.recapture — Vehicle credit change/recapture facts

**IF:** `VEHICLE.disposed = true`
**THEN, form candidates:** 8936 (individual_return_or_workpaper); 4255 (individual_return_or_workpaper)
- **Support: Vehicle credit change/recapture facts** (`VEHICLE.doc_recapture`; support)
  - Extract/match: return/resale date; original credit; transfer; use changes; ownership history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Determine the relevant disallowance or recapture rule rather than applying a generic recapture assumption.
**Authority:** [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="foreign"></a>
## FOREIGN — International status, income, accounts and entities

**Opening screen:** Was there foreign residence, work, income, tax, an account/signature authority, foreign assets/entities/trusts/gifts, or expatriation?
**Unit:** Repeat for each foreign relationship or jurisdiction. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### FOREIGN.owner — Which person has the relationship, in which country, and in what capacity?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### FOREIGN.residency — Was the person nonresident, dual-status, on a visa, or changing U.S. residency?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.day_counts — Record U.S. presence for current/prior two years, exempt days, green-card dates and treaty residence.

**IF:** `FOREIGN.residency = true`
**Answer:** text. Unknown/conflict does not become false.

#### FOREIGN.spouse_election — Is a nonresident-spouse resident election or treaty-residency claim being considered?

**IF:** `FOREIGN.residency = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.earned — Was employment or self-employment income earned while abroad?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.tax_home — Identify tax home, foreign residence, physical-presence dates and housing costs.

**IF:** `FOREIGN.earned = true`
**Answer:** text. Unknown/conflict does not become false.

#### FOREIGN.foreign_tax — Was foreign income tax paid, accrued, refunded or redetermined?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.account — Was there a foreign financial account, pension, insurance cash value or signature authority?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.max_values — What were maximum annual and year-end values, currency and ownership/signature capacity?

**IF:** `FOREIGN.account = true`
**Answer:** text. Unknown/conflict does not become false.

#### FOREIGN.aggregate — Has the maximum aggregate foreign-account value across all accounts/persons been calculated?

**IF:** `FOREIGN.account = true`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.assets — Were there specified foreign financial assets outside ordinary foreign accounts?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.fund — Were foreign mutual funds, ETFs, pooled investments or other possible PFIC interests held directly or indirectly?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.corporation — Was there ownership, control, directorship, acquisition or disposition involving a foreign corporation?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.partnership — Was there a foreign partnership interest, contribution, acquisition or disposition?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.branch — Was there a foreign disregarded entity or foreign branch?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.trust — Was the person a foreign trust owner, grantor, transferor or beneficiary, or did they receive loans/use of trust property?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.gift — Were gifts or bequests received from foreign persons, estates, corporations or partnerships?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.transfer — Was property transferred to a foreign corporation or other foreign entity?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.expatriation — Was citizenship relinquished or long-term permanent residence ended?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.territory — Was there residence in or income from a U.S. territory?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.treaty — Is a treaty-based position, totalization claim or unusual foreign pension treatment involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.late — Are earlier international information returns missing, late or potentially incorrect?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FOREIGN.domestic_foreign_owner — Is there a foreign-owned U.S. disregarded entity or other related-party U.S. entity reporting issue?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### FOREIGN.status — International residence classification workpaper

**IF:** `FOREIGN.residency = true`
**THEN, form candidates:** 1040-NR (individual_return_or_workpaper); 8843 (individual_return_or_workpaper); 8840 (individual_return_or_workpaper); 8833 (individual_return_or_workpaper)
- **Support: International residence classification workpaper** (`FOREIGN.doc_status`; support)
  - Extract/match: passport/travel records; I-94; visa; green card; exempt days; current/prior two years; tax home; treaty ties; elections
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: determine resident/nonresident/dual-status return treatment and filing exceptions before using a standard resident return.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.earned — Foreign earned income and housing packet

**IF:** `FOREIGN.earned = true`
**THEN, form candidates:** 2555 (individual_return_or_workpaper)
- **Support: Foreign earned income and housing packet** (`FOREIGN.doc_earned`; support)
  - Extract/match: employer; income by work location; dates; foreign tax home; residence/physical-presence; housing; U.S. workdays; prior election
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Coordinate exclusion, foreign tax credits, self-employment and prior elections; do not exclude income merely because paid overseas.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.tax — Foreign tax category and payment workpaper

**IF:** `FOREIGN.foreign_tax = true`
**THEN, form candidates:** 1116 (individual_return_or_workpaper)
- **Support: Foreign tax category and payment workpaper** (`FOREIGN.doc_tax`; support)
  - Extract/match: country; tax type; paid/accrued date; category; foreign income; exchange rate; refunds; carryovers; redeterminations
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Use separate categories and prohibit credit for taxes allocable to excluded income.
**Authority:** [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

#### FOREIGN.accounts — Foreign financial account inventory and valuation

**IF:** `FOREIGN.account = true`
**THEN, form candidates:** FinCEN 114 (separate_obligation_or_procedure); 8938 (individual_return_or_workpaper); Schedule B (individual_return_or_workpaper)
- **Support: Foreign financial account inventory and valuation** (`FOREIGN.doc_accounts`; support)
  - Extract/match: institution; country; owner/signatory; secure account reference; highest/year-end balance; currencies; Treasury exchange rate; aggregate maximum
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Evaluate FBAR separately from Form 8938. Filing one does not satisfy the other; signature authority and threshold rules differ.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.assets — Specified foreign financial asset schedule

**IF:** `FOREIGN.assets = true`
**THEN, form candidates:** 8938 (individual_return_or_workpaper)
- **Support: Specified foreign financial asset schedule** (`FOREIGN.doc_assets`; support)
  - Extract/match: asset type; country; ownership; maximum/year-end values; income; other international forms; living-abroad and filing status
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply filing-status/residence thresholds and duplication exceptions using a complete inventory.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.pfic — PFIC annual information and election history

**IF:** `FOREIGN.fund = true`
**THEN, form candidates:** 8621 (individual_return_or_workpaper)
- **Support: PFIC annual information and election history** (`FOREIGN.doc_pfic`; support)
  - Extract/match: each direct/indirect fund; purchase lots; annual statements; distributions; dispositions; PFIC analysis; QEF/MTM elections; prior years
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: identify each PFIC and regime; a foreign fund can matter even without a sale.
**Authority:** [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621)

#### FOREIGN.corporation — Foreign corporation ownership and transactions

**IF:** `FOREIGN.corporation = true`
**THEN, form candidates:** 5471 (individual_return_or_workpaper); 8992 (individual_return_or_workpaper); 8993 (individual_return_or_workpaper)
- **Support: Foreign corporation ownership and transactions** (`FOREIGN.doc_corporation`; support)
  - Extract/match: direct/indirect/constructive ownership; changes; officer/director status; financials; earnings; distributions; U.S. owners; related-party transactions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: determine filing categories and applicable inclusion/election rules.
**Authority:** [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471)

#### FOREIGN.partnership — Foreign partnership ownership and transfer packet

**IF:** `FOREIGN.partnership = true`
**THEN, form candidates:** 8865 (individual_return_or_workpaper)
- **Support: Foreign partnership ownership and transfer packet** (`FOREIGN.doc_partnership`; support)
  - Extract/match: ownership chain; contributions; acquisitions/dispositions; financial statements; allocations; related persons
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865)

#### FOREIGN.branch — Foreign disregarded entity or branch books

**IF:** `FOREIGN.branch = true`
**THEN, form candidates:** 8858 (individual_return_or_workpaper)
- **Support: Foreign disregarded entity or branch books** (`FOREIGN.doc_branch`; support)
  - Extract/match: entity classification; owner chain; country; financial statements; transfers; functional currency
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.trust — Foreign trust ownership/transaction packet

**IF:** `FOREIGN.trust = true`
**THEN, form candidates:** 3520 (separate_obligation_or_procedure); 3520-A (separate_obligation_or_procedure)
- **Support: Foreign trust ownership/transaction packet** (`FOREIGN.doc_trust`; support)
  - Extract/match: trust deed; grantor/owner; transfers; distributions; loans; use of property; beneficiary statements; trust tax year
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate filing obligations and deadlines; incomplete beneficiary statements require review.
**Authority:** [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520)

#### FOREIGN.gifts — Foreign gift/bequest aggregation

**IF:** `FOREIGN.gift = true`
**THEN, form candidates:** 3520 (separate_obligation_or_procedure)
- **Support: Foreign gift/bequest aggregation** (`FOREIGN.doc_gifts`; support)
  - Extract/match: donor identity/class; related donor grouping; dates; values; currency; bequest documents; income versus gift analysis
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review donor-type thresholds; a nontaxable gift may still create an information-return obligation.
**Authority:** [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520)

#### FOREIGN.transfer — Transfers to foreign entities

**IF:** `FOREIGN.transfer = true`
**THEN, form candidates:** 926 (individual_return_or_workpaper); 8865 (individual_return_or_workpaper)
- **Support: Transfers to foreign entities** (`FOREIGN.doc_transfer`; support)
  - Extract/match: recipient classification; property; adjusted basis; FMV; ownership before/after; dates; agreements
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: identify the exact transfer-reporting and gain-recognition provisions.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.expat — Expatriation and long-term resident termination packet

**IF:** `FOREIGN.expatriation = true`
**THEN, form candidates:** 8854 (individual_return_or_workpaper)
- **Support: Expatriation and long-term resident termination packet** (`FOREIGN.doc_expat`; support)
  - Extract/match: citizenship/residency history; termination date; five-year compliance; assets/liabilities; net worth; deferred compensation; trusts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: exit-tax, certification and continuing reporting are outside the standard resident-return path.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.territory — Territory residency and source-income workpaper

**IF:** `FOREIGN.territory = true`
**THEN, form candidates:** 8898 (individual_return_or_workpaper); 8689 (individual_return_or_workpaper); 1040-SS (individual_return_or_workpaper)
- **Support: Territory residency and source-income workpaper** (`FOREIGN.doc_territory`; support)
  - Extract/match: territory; residence days; tax home; closer connection; sources; prior moves; taxes paid
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Use the territory-specific adapter and identify where each return is filed.
**Authority:** [Publication 570: Territories](https://www.irs.gov/publications/p570)

#### FOREIGN.domestic — Foreign-owned domestic entity reporting

**IF:** `FOREIGN.domestic_foreign_owner = true`
**THEN, form candidates:** 5472 (separate_obligation_or_procedure); 1120 (separate_obligation_or_procedure)
- **Support: Foreign-owned domestic entity reporting** (`FOREIGN.doc_domestic`; support)
  - Extract/match: foreign owner; U.S. entity classification; related-party transactions; contributions/distributions; prior filings
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: assess separate entity information-return requirements; no income does not automatically remove them.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

#### FOREIGN.late — International late-filing and treaty review

**IF:** `(FOREIGN.late = true OR FOREIGN.treaty = true OR FOREIGN.spouse_election = true)`
**THEN, form candidates:** 8833 (individual_return_or_workpaper)
- **Support: International late-filing and treaty review** (`FOREIGN.doc_late`; support)
  - Extract/match: affected years; prior returns; treaty article; missing forms; legal position; available relief; signed elections
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: do not automatically submit late international forms or make elections without advice and explicit authorization.
**Authority:** [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)


<a id="debt"></a>
## DEBT — Canceled debt, foreclosure and bankruptcy

**Opening screen:** Was debt canceled, forgiven, settled, foreclosed, repossessed or discharged in bankruptcy?
**Unit:** Repeat for each debt event. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### DEBT.kind — What debt was involved?

**IF:** `Always within this active topic`
**Answer:** enum · Credit card / personal / Home mortgage / Student loan / Business/farm / Other. Unknown/conflict does not become false.

#### DEBT.date — What is the cancellation or identifiable-event date?

**IF:** `Always within this active topic`
**Answer:** date. Unknown/conflict does not become false.

#### DEBT.forms — Were Forms 1099-C or 1099-A issued, missing, corrected or disputed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DEBT.amount — What principal, accrued interest and other amounts were canceled?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### DEBT.bankruptcy — Was the discharge in a title 11 bankruptcy case?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DEBT.insolvent — Could liabilities exceed the FMV of all assets immediately before cancellation?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DEBT.property — Was property surrendered, foreclosed, repossessed or abandoned?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DEBT.recourse — Was the debt recourse, nonrecourse, or unresolved?

**IF:** `DEBT.property = true`
**Answer:** enum · Recourse / Nonrecourse / Unresolved. Unknown/conflict does not become false.

#### DEBT.special — Could qualified principal-residence, student-loan, farm or real-property-business debt rules apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DEBT.attributes — Are losses, basis or other tax attributes subject to reduction?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### DEBT.debt — Debt discharge agreement and information returns

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); 982 (individual_return_or_workpaper)
- **Support: Debt discharge agreement and information returns** (`DEBT.doc_debt`; support)
  - Extract/match: lender; borrower; 1099-C/A; principal; interest; cancellation date; disputed amounts; actual legal release
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not assume canceled debt is taxable or exempt solely from receiving or not receiving a 1099-C.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.insolvency — Immediately-before-discharge insolvency balance sheet

**IF:** `DEBT.insolvent = true`
**THEN, form candidates:** 982 (individual_return_or_workpaper)
- **Support: Immediately-before-discharge insolvency balance sheet** (`DEBT.doc_insolvency`; support)
  - Extract/match: all assets at FMV including exempt/retirement assets; all liabilities; contingent liabilities; timing; valuation evidence
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Use the balance sheet immediately before each discharge, not year-end net worth.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.bankruptcy — Bankruptcy court and discharge packet

**IF:** `DEBT.bankruptcy = true`
**THEN, form candidates:** 982 (individual_return_or_workpaper); 1041 (separate_obligation_or_procedure)
- **Support: Bankruptcy court and discharge packet** (`DEBT.doc_bankruptcy`; support)
  - Extract/match: petition; chapter; case dates; discharge order; estate representative; debt schedule
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate the individual return from a bankruptcy estate when applicable.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.property — Foreclosure/repossession disposition packet

**IF:** `DEBT.property = true`
**THEN, form candidates:** 4797 (individual_return_or_workpaper); 8949 (individual_return_or_workpaper)
- **Support: Foreclosure/repossession disposition packet** (`DEBT.doc_property`; support)
  - Extract/match: debt balance; recourse status; property basis; FMV; proceeds; foreclosure date; debt discharge
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Analyze gain/loss on disposition separately from cancellation-of-debt income.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.exclusion — Debt exclusion and attribute-reduction workpaper

**IF:** `(DEBT.special = true OR DEBT.attributes = true)`
**THEN, form candidates:** 982 (individual_return_or_workpaper)
- **Support: Debt exclusion and attribute-reduction workpaper** (`DEBT.doc_exclusion`; support)
  - Extract/match: qualifying debt purpose; legal program; dates; exclusions claimed; loss/basis attributes before reduction
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Verify year-specific exclusions and required attribute reduction.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.unmodeled_kind — Resolve unmodeled selection: DEBT.kind

**IF:** `DEBT.kind is one of ["Other"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

#### DEBT.unmodeled_recourse — Resolve unmodeled selection: DEBT.recourse

**IF:** `DEBT.recourse is one of ["Unresolved"]`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Dated preparer decision memo** (`REVIEW_MEMO`; workpaper)
  - Extract/match: issue; established facts; missing facts; authority and tax year; decision; preparer; date; affected forms
  - Look in: Preparer workpapers
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** BLOCK: clarify the exact facts and select the correctly modeled subtype or attach an approved specialist/jurisdiction adapter with its own questions, required forms, evidence, authority and closure decision. A generic Other or Unresolved selection does not establish completeness.
**Authority:** [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)


<a id="disaster"></a>
## DISASTER — Casualty, theft and disaster relief

**Opening screen:** Was there property damage, theft, a disaster-related loss, insurance recovery or disaster election?
**Unit:** Repeat for each loss event. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### DISASTER.event — Describe the event, date, location and affected property.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### DISASTER.use — Was the property personal-use, business/investment, or both?

**IF:** `Always within this active topic`
**Answer:** enum · Personal / Business/investment / Mixed. Unknown/conflict does not become false.

#### DISASTER.declaration — Was there a federal disaster declaration or other qualifying statutory disaster relief?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISASTER.insurance — Were claims filed and reimbursements received or reasonably expected?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISASTER.values — Are adjusted basis and before/after FMV supported?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISASTER.prior_election — Was a prior-year deduction election considered or already made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISASTER.gain — Did reimbursement exceed basis, or were replacement-property deferral rules considered?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### DISASTER.ponzi — Is this an investment-theft/Ponzi loss or another specialized theft claim?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### DISASTER.loss — Casualty/theft/disaster claim packet

**IF:** `Always within this active topic`
**THEN, form candidates:** 4684 (individual_return_or_workpaper)
- **Support: Casualty/theft/disaster claim packet** (`DISASTER.doc_loss`; support)
  - Extract/match: ownership; use; basis; event; declaration; appraisals; repair estimates; police reports; insurance claims; reimbursements; recoveries
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review eligibility and limitations separately for personal and business property. A casualty does not guarantee a federal deduction.
**Authority:** [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DISASTER.election — Disaster election and recovery history

**IF:** `(DISASTER.prior_election = true OR DISASTER.gain = true)`
**THEN, form candidates:** 1040-X (individual_return_or_workpaper); 4684 (individual_return_or_workpaper)
- **Support: Disaster election and recovery history** (`DISASTER.doc_election`; support)
  - Extract/match: original return year; election statement/deadline; reimbursements; replacement costs/dates; deferred gain
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Track prior-year elections and later recoveries as linked but separate return versions.
**Authority:** [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### DISASTER.theft — Investment-theft legal/recovery support

**IF:** `DISASTER.ponzi = true`
**THEN, form candidates:** 4684 (individual_return_or_workpaper)
- **Support: Investment-theft legal/recovery support** (`DISASTER.doc_theft`; support)
  - Extract/match: criminal charges/findings; investment basis; fictitious income; recovery claims; safe-harbor facts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: apply investment theft rules only where the legal and factual criteria are met.
**Authority:** [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)


<a id="gift"></a>
## GIFT — Gifts, inheritances and estate-related obligations

**Opening screen:** Were substantial gifts made/received, trust transfers, inheritances, estate distributions or gift-tax elections involved?
**Unit:** Repeat for each gift, donor/donee relationship or estate. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### GIFT.direction — Is this a gift made, gift received, inheritance received, or acting for an estate/trust?

**IF:** `Always within this active topic`
**Answer:** enum · Gift made / Gift received / Inheritance received / Estate/trust representative. Unknown/conflict does not become false.

#### GIFT.person — Identify donor, donee, relationship and U.S./foreign status.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### GIFT.property — What property was transferred, on which dates, at what FMV and basis?

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### GIFT.annual_total — What was the total transferred to this donee during the year?

**IF:** `GIFT.direction = "Gift made"`
**Answer:** number. Unknown/conflict does not become false.

#### GIFT.future_interest — Was a future interest, trust interest, bargain transfer, debt forgiveness or below-market loan involved?

**IF:** `GIFT.direction = "Gift made"`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.split — Is spouse gift-splitting or a five-year 529 election being considered?

**IF:** `GIFT.direction = "Gift made"`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.direct_payment — Were tuition or medical bills paid directly to the qualifying provider?

**IF:** `GIFT.direction = "Gift made"`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.gst — Is there a generation-skipping transfer, trust allocation or GST election issue?

**IF:** `GIFT.direction = "Gift made"`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.foreign — Was a foreign donor, trust, estate or noncitizen spouse involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.prior — Are prior Forms 709, valuation reports or exemption-usage schedules available?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.retirement — Did the inheritance include retirement accounts, deferred income or income in respect of a decedent?

**IF:** `GIFT.direction = "Inheritance received"`
**Answer:** boolean. Unknown/conflict does not become false.

#### GIFT.estate_filing — Could estate income, estate tax, portability or representative-authority filings be required?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### GIFT.gift — Gift transfer and annual aggregation

**IF:** `GIFT.direction = "Gift made"`
**THEN, form candidates:** 709 (separate_obligation_or_procedure)
- **Support: Gift transfer and annual aggregation** (`GIFT.doc_gift`; support)
  - Extract/match: donor; donee; dates; FMV; basis; appraisals; annual aggregate; gift type; direct tuition/medical payments; prior gifts
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review annual exclusions, future interests, spouse citizenship, gift splitting and GST. No gift tax payable does not mean no gift return.
**Authority:** [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### GIFT.prior — Prior gift-tax and exemption rollforward

**IF:** `GIFT.prior = true`
**THEN, form candidates:** 709 (separate_obligation_or_procedure)
- **Support: Prior gift-tax and exemption rollforward** (`GIFT.doc_prior`; support)
  - Extract/match: all prior Forms 709; taxable gifts; gift/GST exemption; allocations; appraisals; amendments
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### GIFT.estate — Inheritance and estate separation packet

**IF:** `(GIFT.direction = "Inheritance received" OR GIFT.direction = "Estate/trust representative" OR GIFT.estate_filing = true)`
**THEN, form candidates:** 1041 (separate_obligation_or_procedure); 706 (separate_obligation_or_procedure); 56 (individual_return_or_workpaper); 1310 (individual_return_or_workpaper)
- **Support: Inheritance and estate separation packet** (`GIFT.doc_estate`; support)
  - Extract/match: date of death; will/trust; letters testamentary; distributions; valuations; basis statement; K-1; estate income; portability review
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Separate the beneficiary’s 1040, decedent’s final 1040, estate/trust income return and estate-tax return; each has its own owner and deadline.
**Authority:** [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

#### GIFT.elections — Gift/GST/529 election workpaper

**IF:** `(GIFT.split = true OR GIFT.gst = true)`
**THEN, form candidates:** 709 (separate_obligation_or_procedure)
- **Support: Gift/GST/529 election workpaper** (`GIFT.doc_elections`; support)
  - Extract/match: spouse consent; prior elections; donee; trust terms; allocations; five-year gift schedule
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Elections require explicit taxpayer selection and the appropriate signed filing.
**Authority:** [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

**Linked track:** IF `GIFT.foreign = true` → FOREIGN. Review foreign transfer reporting. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="household"></a>
## HOUSEHOLD — Household workers and payroll

**Opening screen:** Was a nanny, caregiver, housekeeper, gardener or other household worker paid directly?
**Unit:** Repeat for each worker. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### HOUSEHOLD.worker — Identify worker, role and service dates.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### HOUSEHOLD.control — Did the household control both what work was done and how it was done?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.agency — Did an agency employ and pay the worker, rather than the household?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.relative — Was the worker a spouse, parent, child under 21 or someone under 18?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.cash_wages — What cash wages were paid to this worker in 2025?

**IF:** `Always within this active topic`
**Answer:** number. Unknown/conflict does not become false.

#### HOUSEHOLD.quarter — Were aggregate cash wages to all household employees at least $1,000 in any quarter of 2024 or 2025?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.withheld — Was federal income tax withheld by agreement?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.payroll — Did a payroll provider file W-2/W-3 and state payroll returns?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### HOUSEHOLD.state — Were state unemployment registration, contributions or other state requirements reviewed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### HOUSEHOLD.classification — Household worker classification and wage history

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule H (individual_return_or_workpaper)
- **Support: Household worker classification and wage history** (`HOUSEHOLD.doc_classification`; support)
  - Extract/match: control facts; agency contract; family/age exceptions; wages by worker; total quarterly wages; cash/noncash separation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review employee classification and statutory family/age exceptions. Contractor status is not established just by using a 1099.
**Authority:** [Instructions: Household employment](https://www.irs.gov/instructions/i1040sh)

#### HOUSEHOLD.payroll — Household payroll and prior filing packet

**IF:** `(HOUSEHOLD.cash_wages >= 2800 OR HOUSEHOLD.quarter = true OR HOUSEHOLD.withheld = true)`
**THEN, form candidates:** Schedule H (individual_return_or_workpaper); W-2 / W-3 (separate_obligation_or_procedure)
- **Support: Household payroll and prior filing packet** (`HOUSEHOLD.doc_payroll`; support)
  - Extract/match: EIN; wage ledger; withholding; W-2/W-3; payroll provider reports; state unemployment; deposits; filing acknowledgements
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** The 2025 $2,800 per-worker threshold is only one test; FUTA and voluntary withholding have separate triggers and exceptions.
**Authority:** [Instructions: Household employment](https://www.irs.gov/instructions/i1040sh)


<a id="farm"></a>
## FARM — Farming, fishing and natural resources

**Opening screen:** Was there farming, fishing, agricultural rental, timber, mineral/royalty activity or farm-specific carryover/election?
**Unit:** Repeat for each operation or interest. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### FARM.kind — Identify farming, fishing, crop-share rental, cash farmland rent, timber or minerals.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

#### FARM.participation — Did the owner materially participate in production or management?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.receipts — Were crops, livestock, cooperative payments, subsidies, crop insurance or disaster proceeds received?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.inventory — Were purchased/raised inventory, breeding livestock or capital assets involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.expenses — Were farm expenses, conservation, prepaid supplies or development costs incurred?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.deferral — Was crop insurance, disaster income or another farm receipt deferred or proposed for deferral?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.averaging — Could farm/fishing income averaging or special estimated-tax rules apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.royalty — Were mineral royalties, working interests or depletion deductions involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.sale — Was farmland, livestock, timber or a resource interest sold?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### FARM.special — Are conservation deductions, cooperative allocations, special farmland-sale payments or other specialized rules involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### FARM.farm — Agricultural/resource activity books and classification

**IF:** `Always within this active topic`
**THEN, form candidates:** Schedule F (individual_return_or_workpaper); Schedule E (individual_return_or_workpaper); 4835 (individual_return_or_workpaper); Schedule SE (individual_return_or_workpaper)
- **Support: Agricultural/resource activity books and classification** (`FARM.doc_farm`; support)
  - Extract/match: activity; ownership; participation; gross receipts; subsidies; inventory; expenses; assets; accounting method
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Determine trade/business versus agricultural rental or royalty treatment; farming rules are not identical to Schedule C.
**Authority:** [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

#### FARM.averaging — Farm/fishing averaging and payments workpaper

**IF:** `FARM.averaging = true`
**THEN, form candidates:** Schedule J (individual_return_or_workpaper)
- **Support: Farm/fishing averaging and payments workpaper** (`FARM.doc_averaging`; support)
  - Extract/match: current/prior three-year income; qualifying income; estimated payments; tax history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review income averaging separately from special estimated-tax timing.
**Authority:** [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

#### FARM.resource — Natural-resource basis and depletion packet

**IF:** `FARM.royalty = true`
**THEN, form candidates:** Schedule E (individual_return_or_workpaper)
- **Support: Natural-resource basis and depletion packet** (`FARM.doc_resource`; support)
  - Extract/match: leases; production; royalty statements; basis; reserves; cost/percentage depletion history
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: review working-interest, depletion, sale and recapture rules.
**Authority:** [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

#### FARM.special — Farm-specific elections and special transactions

**IF:** `(FARM.deferral = true OR FARM.sale = true OR FARM.special = true)`
**THEN, form candidates:** 4797 (individual_return_or_workpaper); 6252 (individual_return_or_workpaper)
- **Support: Farm-specific elections and special transactions** (`FARM.doc_special`; support)
  - Extract/match: event dates; qualifying proceeds; prior elections; sale contract; farm use; effective dates
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: identify exact forms and effective-date rules, including any new farmland-sale payment election.
**Authority:** [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)


<a id="carry"></a>
## CARRY — Prior-year attributes and carryovers

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CARRY.capital — Was there a prior capital loss carryover?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.passive — Were passive or at-risk losses/credits suspended?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.basis — Were losses suspended by partnership or S corporation basis limitations?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.nol — Were there net operating losses or excess-business-loss carryforwards?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.charity — Were charitable deductions carried forward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.interest — Was investment or business interest disallowed and carried forward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.foreign — Was there a foreign tax credit carryover or redetermination?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.amt — Is there an AMT credit or alternative basis history?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.qbi — Are QBI, REIT/PTP or qualified-business losses carried forward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.credits — Are energy, adoption, general business or other tax credits carried forward?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.depreciation — Are depreciation, amortization, home-office or expensing carryovers needed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.installment — Were installment-sale, deferred-gain or prior-year income-spread schedules still open?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CARRY.other — Is there another election, basis attribute or tax item surviving from a prior year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CARRY.capital — Capital loss carryforward rollforward

**IF:** `CARRY.capital = true`
**THEN, form candidates:** Schedule D (individual_return_or_workpaper)
- **Support: Capital loss carryforward rollforward** (`CARRY.doc_capital`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.passive — Passive/at-risk carryforward rollforward

**IF:** `CARRY.passive = true`
**THEN, form candidates:** 8582 (individual_return_or_workpaper); 6198 (individual_return_or_workpaper)
- **Support: Passive/at-risk carryforward rollforward** (`CARRY.doc_passive`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.basis — Owner basis-limited loss carryforward rollforward

**IF:** `CARRY.basis = true`
**THEN, form candidates:** 7203 (individual_return_or_workpaper); Schedule E (individual_return_or_workpaper)
- **Support: Owner basis-limited loss carryforward rollforward** (`CARRY.doc_basis`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.nol — NOL/excess business loss carryforward rollforward

**IF:** `CARRY.nol = true`
**THEN, form candidates:** Schedule 1 (individual_return_or_workpaper); 461 (individual_return_or_workpaper)
- **Support: NOL/excess business loss carryforward rollforward** (`CARRY.doc_nol`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.charity — Charitable deduction carryforward rollforward

**IF:** `CARRY.charity = true`
**THEN, form candidates:** Schedule A (individual_return_or_workpaper)
- **Support: Charitable deduction carryforward rollforward** (`CARRY.doc_charity`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.interest — Investment/business interest carryforward rollforward

**IF:** `CARRY.interest = true`
**THEN, form candidates:** 4952 (individual_return_or_workpaper); 8990 (individual_return_or_workpaper)
- **Support: Investment/business interest carryforward rollforward** (`CARRY.doc_interest`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.foreign — Foreign tax credit carryforward rollforward

**IF:** `CARRY.foreign = true`
**THEN, form candidates:** 1116 (individual_return_or_workpaper)
- **Support: Foreign tax credit carryforward rollforward** (`CARRY.doc_foreign`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.amt — AMT credit and alternative basis carryforward rollforward

**IF:** `CARRY.amt = true`
**THEN, form candidates:** 8801 (individual_return_or_workpaper); 6251 (individual_return_or_workpaper)
- **Support: AMT credit and alternative basis carryforward rollforward** (`CARRY.doc_amt`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.qbi — QBI loss carryforward rollforward

**IF:** `CARRY.qbi = true`
**THEN, form candidates:** 8995 (individual_return_or_workpaper); 8995-A (individual_return_or_workpaper)
- **Support: QBI loss carryforward rollforward** (`CARRY.doc_qbi`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.credits — Tax credit carryforward rollforward

**IF:** `CARRY.credits = true`
**THEN, form candidates:** Schedule 3 (individual_return_or_workpaper); 3800 (individual_return_or_workpaper)
- **Support: Tax credit carryforward rollforward** (`CARRY.doc_credits`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.depreciation — Depreciation/home-office carryforward rollforward

**IF:** `CARRY.depreciation = true`
**THEN, form candidates:** 4562 (individual_return_or_workpaper); 8829 (individual_return_or_workpaper)
- **Support: Depreciation/home-office carryforward rollforward** (`CARRY.doc_depreciation`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.installment — Deferred income/installment carryforward rollforward

**IF:** `CARRY.installment = true`
**THEN, form candidates:** 6252 (individual_return_or_workpaper); 8915-F (individual_return_or_workpaper)
- **Support: Deferred income/installment carryforward rollforward** (`CARRY.doc_installment`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

#### CARRY.other — Other surviving tax attribute carryforward rollforward

**IF:** `CARRY.other = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Other surviving tax attribute carryforward rollforward** (`CARRY.doc_other`; support)
  - Extract/match: origin year; owner/entity/activity; original support; each intervening year; allowed/disallowed/expired amounts; remaining balance; federal/state difference
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not copy an unexplained balance. Reconcile every intervening filed/amended year and preserve owner/activity distinctions.
**Authority:** [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)


<a id="credits"></a>
## CREDITS — Household credit eligibility screening

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CREDITS.earned — Did the taxpayer or spouse have wages or other earned income?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.home_us — Was the main home in the United States for more than half the year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.investment_income — Is total investment income for EIC purposes supported?

**IF:** `CREDITS.earned = true`
**Answer:** number. Unknown/conflict does not become false.

#### CREDITS.qualifying_children — Could there be EIC qualifying children or children/other dependents for dependent credits?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.ssn — Are citizenship/residency and timely-valid-SSN requirements for each proposed credit documented?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.disallowed — Was EIC, CTC/ACTC/ODC or AOTC disallowed in a prior year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.retirement_saver — Were eligible retirement contributions made, and could a retirement savings contribution credit apply?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.elderly — Could age/disability and income support the credit for elderly or disabled taxpayers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.child_account — Should optional Form 4547 elections be considered for a child not yet reviewed in PERSON?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CREDITS.other — Is there a mortgage interest credit certificate, prior business credit, fuel credit or another specialized individual credit?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CREDITS.eic — Earned income credit eligibility workpaper

**IF:** `CREDITS.earned = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Earned income credit eligibility workpaper** (`CREDITS.doc_eic`; support)
  - Extract/match: earned income; AGI; investment income; age; SSNs; U.S. residence; dependency; qualifying children; separated-spouse rules; foreign exclusion
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Evaluate EIC with and without a qualifying child. Schedule EIC is not needed merely because childless EIC is claimed.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.dependent_credits — Child and other dependent credit workpaper

**IF:** `CREDITS.qualifying_children = true`
**THEN, form candidates:** Schedule 8812 (individual_return_or_workpaper)
- **Support: Child and other dependent credit workpaper** (`CREDITS.doc_dependent_credits`; support)
  - Extract/match: dependency outcome; age; citizenship; timely SSN/ITIN; taxpayer/spouse SSN; income; release; home location
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Use benefit-specific 2025 ID and eligibility rules, not dependency status alone.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.disallow — Prior credit disallowance and recertification

**IF:** `CREDITS.disallowed = true`
**THEN, form candidates:** 8862 (individual_return_or_workpaper)
- **Support: Prior credit disallowance and recertification** (`CREDITS.doc_disallow`; support)
  - Extract/match: IRS notice; credit; year; reason; ban; subsequent allowance
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Check whether recertification is required or a ban remains in force.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.saver — Retirement savings contribution credit workpaper

**IF:** `CREDITS.retirement_saver = true`
**THEN, form candidates:** 8880 (individual_return_or_workpaper)
- **Support: Retirement savings contribution credit workpaper** (`CREDITS.doc_saver`; support)
  - Extract/match: age; student status; dependency; qualifying contributions; recent distributions; AGI
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.elderly — Elderly/disabled credit workpaper

**IF:** `CREDITS.elderly = true`
**THEN, form candidates:** Schedule R (individual_return_or_workpaper)
- **Support: Elderly/disabled credit workpaper** (`CREDITS.doc_elderly`; support)
  - Extract/match: birth date; disability certification; taxable disability income; retirement age; nontaxable pensions; AGI
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.other — Other credit eligibility packet

**IF:** `CREDITS.other = true`
**THEN, form candidates:** 8396 (individual_return_or_workpaper); 3800 (individual_return_or_workpaper); 4136 (individual_return_or_workpaper)
- **Support: Other credit eligibility packet** (`CREDITS.doc_other`; support)
  - Extract/match: exact credit; certificate/authority; qualified costs; income limits; carryover; prior claims
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: add exact credit-specific forms and evidence; do not treat this candidate list as a blanket entitlement.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

#### CREDITS.eic_child — Qualifying-child EIC schedule review

**IF:** `(CREDITS.earned = true AND CREDITS.qualifying_children = true)`
**THEN, form candidates:** Schedule EIC (individual_return_or_workpaper)
**Review gate:** File only if EIC is actually claimed with an eligible qualifying child.
**Authority:** [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

**Linked track:** IF `CREDITS.child_account = true` → PERSON. Review Form 4547 for the named child. Record the destination instance or a supported nonapplicability conclusion; do not silently change that topic's screen.


<a id="tax"></a>
## TAX — Additional taxes and calculation handoffs

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### TAX.high_income — Could combined wages, self-employment income or investment income approach an additional-tax threshold?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.niit_income — Was there taxable investment income, passive business income, rents, annuities or taxable gains?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.amt_items — Were there ISO exercises, private-activity bonds, AMT carryovers or other AMT adjustments?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.business — Was there business/pass-through income or loss requiring QBI or aggregate-loss calculations?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.multiple_w2 — Did one individual have wages from more than one employer?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.special_tax — Are retirement penalties, recapture, foreign inclusions, excess parachute payments or other additional taxes unresolved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.magi_ready — Are separate MAGI workpapers available for each benefit being tested?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.deduction_1a — Could the taxpayer claim tips, overtime, qualifying vehicle-loan interest or enhanced senior deductions?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.senior — Was either taxpayer/spouse born before January 2, 1961?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### TAX.filing_required — Has the full filing-requirement test been completed, including special filing triggers and refundable claims?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### TAX.niit — Net investment income tax threshold and allocation workpaper

**IF:** `(TAX.high_income = true OR TAX.niit_income = true)`
**THEN, form candidates:** 8960 (individual_return_or_workpaper)
- **Support: Net investment income tax threshold and allocation workpaper** (`TAX.doc_niit`; support)
  - Extract/match: filing status; NIIT MAGI; net investment income categories; allocable expenses; passive/nonpassive status; dispositions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** An investment receipt opens a threshold review; it does not automatically require Form 8960.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.medicare — Additional Medicare tax and withholding reconciliation

**IF:** `TAX.high_income = true`
**THEN, form candidates:** 8959 (individual_return_or_workpaper)
- **Support: Additional Medicare tax and withholding reconciliation** (`TAX.doc_medicare`; support)
  - Extract/match: each spouse wages/RRTA; self-employment income; filing status; thresholds; employer withholding
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.amt — AMT screening and alternative-basis workpaper

**IF:** `TAX.amt_items = true`
**THEN, form candidates:** 6251 (individual_return_or_workpaper); 8801 (individual_return_or_workpaper)
- **Support: AMT screening and alternative-basis workpaper** (`TAX.doc_amt`; support)
  - Extract/match: regular income; adjustments/preferences; filing status; exemptions; AMT basis; prior credits
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.qbi — Aggregate QBI and business-loss handoff

**IF:** `TAX.business = true`
**THEN, form candidates:** 8995 (individual_return_or_workpaper); 8995-A (individual_return_or_workpaper); 461 (individual_return_or_workpaper)
- **Support: Aggregate QBI and business-loss handoff** (`TAX.doc_qbi`; support)
  - Extract/match: all qualified activities; taxable income before QBI; capital gains; wages; UBIA; loss carryovers; SSTB; aggregation
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Coordinate computations downstream; this organizer does not calculate tax or phaseouts.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.social_security — Excess Social Security/RRTA withholding workpaper

**IF:** `TAX.multiple_w2 = true`
**THEN, form candidates:** Schedule 3 (individual_return_or_workpaper)
- **Support: Excess Social Security/RRTA withholding workpaper** (`TAX.doc_social_security`; support)
  - Extract/match: owner-specific employer wages; boxes 3/4/5/6; employer identity; refunds/corrections; annual limit
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not aggregate spouses for the wage-base test; same-employer overwithholding has a different recovery path.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.1a — Schedule 1-A eligibility and limitation coordination

**IF:** `(TAX.deduction_1a = true OR TAX.senior = true)`
**THEN, form candidates:** Schedule 1-A (individual_return_or_workpaper)
- **Support: Schedule 1-A eligibility and limitation coordination** (`TAX.doc_1a`; support)
  - Extract/match: qualified tips; overtime premium; qualifying loan interest; birth date; valid SSN; MAGI; filing status; no duplicate deductions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** These are separate deduction branches, not exclusions from payroll or gross-income reporting.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### TAX.filing — Filing requirement and independent-obligation review

**IF:** `Always within this active topic`
**THEN, form candidates:** 1040 (individual_return_or_workpaper); 1040-SR (individual_return_or_workpaper)
- **Support: Filing requirement and independent-obligation review** (`TAX.doc_filing`; workpaper)
  - Extract/match: filing status; age; dependency; gross and earned income; self-employment; special taxes; APTC; refund claims; standalone forms
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not end all work merely because income is below the normal Form 1040 threshold. Standalone retirement, payroll, gift and international obligations may remain.
**Authority:** [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="pay"></a>
## PAY — Withholding, payments, refunds and notices

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### PAY.withheld — Was federal, state or local tax withheld on any income statement?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.estimated — Were estimated tax payments made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.extension — Was an extension payment made?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.prior_applied — Was any prior-year refund applied to this year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.overseas — Were foreign taxes or foreign withholding paid?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.uneven — Was income uneven during the year or were estimated payments late/irregular?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.safe_harbor — Are prior-year tax, prior-year AGI, filing period and payments available for penalty screening?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.other_year — Were payments made in this calendar year for a different tax year?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.offset — Could a refund be offset or require an injured-spouse allocation?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.bank — Has the refund/payment destination been verified through a secure channel?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### PAY.balance_plan — Might a payment plan or other collection option need consideration?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### PAY.payments — Reconcile tax payments and applied refunds

**IF:** `(PAY.estimated = true OR PAY.extension = true OR PAY.prior_applied = true OR PAY.other_year = true)`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Tax payment confirmations and account reconciliation** (`PAYMENTS`; support)
  - Extract/match: payment amount; payment date; tax year applied; payment type; SSN/account attribution; confirmation ID; refunds or reversals
  - Look in: IRS/state online account; bank records; tax payment receipts
  - Accept only when: Distinguish estimated, extension, prior-year balance-due and next-year payments. Match confirmation and bank/account posting; do not infer the tax year from the payment date.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PAY.withholding — Withholding by owner and information statement

**IF:** `PAY.withheld = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Withholding by owner and information statement** (`PAY.doc_withholding`; support)
  - Extract/match: document; tax year; taxpayer; payer; federal/state/local amounts; corrected totals; duplicate removal
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PAY.penalty — Estimated tax and annualized-income workpaper

**IF:** `(PAY.estimated = true OR PAY.uneven = true OR PAY.safe_harbor = false)`
**THEN, form candidates:** 2210 (individual_return_or_workpaper); 2210-F (individual_return_or_workpaper)
- **Support: Estimated tax and annualized-income workpaper** (`PAY.doc_penalty`; support)
  - Extract/match: prior tax; prior AGI; current tax; payments by date; withholding allocation; quarterly income; retirement/disability/disaster exceptions
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Review form necessity, annualization and waivers with the actual calculation; do not assume a penalty from a balance due.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PAY.offset — Refund allocation and offset facts

**IF:** `PAY.offset = true`
**THEN, form candidates:** 8379 (individual_return_or_workpaper)
- **Support: Refund allocation and offset facts** (`PAY.doc_offset`; support)
  - Extract/match: joint return; debt owner; income/payment allocation; offset notice
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PAY.bank — Secure refund/payment instructions

**IF:** `Always within this active topic`
**THEN, form candidates:** 8888 (individual_return_or_workpaper)
- **Support: Secure refund/payment instructions** (`PAY.doc_bank`; verification)
  - Extract/match: account-owner verification; bank details secure reference; refund allocation; payment preference; taxpayer approval
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Only verify instructions here. No payment or filing is authorized by completing this organizer.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

#### PAY.collection — Payment-plan consideration

**IF:** `PAY.balance_plan = true`
**THEN, form candidates:** 9465 (separate_obligation_or_procedure)
- **Support: Payment-plan consideration** (`PAY.doc_collection`; support)
  - Extract/match: balance estimate; prior debts; filing compliance; payment capacity; proposed option
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Do not submit a payment-plan request or disclose personal data without explicit taxpayer authorization.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)


<a id="special"></a>
## SPECIAL — Military, clergy and uncommon situations

**Opening screen:** Was there military/clergy service, tribal-specific income, expatriate compensation, reportable transactions or another uncommon federal tax issue?
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### SPECIAL.military — Was there military service, combat pay, deployment or special residence/deduction relief?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### SPECIAL.clergy — Were clergy earnings, housing allowances, religious exemptions or ministerial self-employment involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### SPECIAL.tribal — Could tribal-source income or treaty/statutory exclusions affect tax treatment?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### SPECIAL.reportable — Was there a reportable/listed transaction disclosure, tax shelter or material tax-avoidance disclosure obligation?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### SPECIAL.accounting — Were accounting-method changes, fiscal-year returns or unusual amended-return procedures involved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### SPECIAL.other — Describe any remaining uncommon issue; enter none if none.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### SPECIAL.military — Military tax fact packet

**IF:** `SPECIAL.military = true`
**THEN, form candidates:** 3903 (individual_return_or_workpaper); 2106 (individual_return_or_workpaper)
- **Support: Military tax fact packet** (`SPECIAL.doc_military`; support)
  - Extract/match: orders; combat-zone dates; nontaxable combat pay; home of record; spouse status; moving/travel; deadline relief
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Apply specific military provisions and elections; preserve a separate state-residency review.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

#### SPECIAL.clergy — Clergy compensation and exemption packet

**IF:** `SPECIAL.clergy = true`
**THEN, form candidates:** Schedule SE (individual_return_or_workpaper); 4361 (separate_obligation_or_procedure); 4029 (separate_obligation_or_procedure)
- **Support: Clergy compensation and exemption packet** (`SPECIAL.doc_clergy`; support)
  - Extract/match: ministerial duties; W-2/1099; housing allowance designation; housing costs; fair rental value; approved exemption
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: income-tax exclusion and self-employment treatment can differ.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

#### SPECIAL.tribal — Tribal income source and statutory authority

**IF:** `SPECIAL.tribal = true`
**THEN, form candidates:** 1040 (individual_return_or_workpaper)
- **Support: Tribal income source and statutory authority** (`SPECIAL.doc_tribal`; support)
  - Extract/match: payor; income source; land/trust status; membership-related eligibility only where relevant; exact authority
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: do not infer a tax exclusion merely from tribal membership.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

#### SPECIAL.disclosure — Reportable-transaction disclosure packet

**IF:** `SPECIAL.reportable = true`
**THEN, form candidates:** 8886 (individual_return_or_workpaper)
- **Support: Reportable-transaction disclosure packet** (`SPECIAL.doc_disclosure`; support)
  - Extract/match: transaction description; tax benefit; promoters; prior disclosures; notices; participation years
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: disclosures may have separate filing copies, deadlines and penalties.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

#### SPECIAL.accounting — Special method/year/procedure memo

**IF:** `SPECIAL.accounting = true`
**THEN, form candidates:** 3115 (individual_return_or_workpaper)
- **Support: Special method/year/procedure memo** (`SPECIAL.doc_accounting`; support)
  - Extract/match: method; election; affected years; prior returns; consent; change adjustment
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** SPECIALIST: extend the rules and obtain a reasoned disposition before closing the branch.
**Authority:** [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)


<a id="close"></a>
## CLOSE — Completeness, exceptions and preparer handoff

**Opening screen:** Mandatory: always review.
**Unit:** return. Confirm the full roster and owner IDs for repeated tracks.

### Questions

#### CLOSE.all_people — Has the full household roster, including supported people living elsewhere, been confirmed?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.all_sources — Have current records been compared with prior-year payers, accounts, properties, entities and carryovers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.unreported — Has income without an information return been explicitly considered?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.counts — Have expected document counts been reconciled to received/verified counts by owner and source?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.versions — Have duplicate, corrected, voided and mismatched-year records been resolved?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.allocations — Have shared expenses/benefits been checked for duplicate use across all people and forms?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.independent — Are independent entity, payroll, gift, estate, foreign and state/local obligations separately tracked?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.deadlines — Has every applicable obligation been assigned its own verified deadline?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.unknown_codes — Have all unfamiliar form codes and statements been resolved or escalated?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.filer_review — Has the filer reviewed the factual summary and confirmed the explicit no answers?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.handoff — Has a preparer received the form-candidate inventory, evidence index and unresolved-decision log?

**IF:** `Always within this active topic`
**Answer:** boolean. Unknown/conflict does not become false.

#### CLOSE.remaining — List anything still unresolved or outside this catalog. Enter none only after explicit review.

**IF:** `Always within this active topic`
**Answer:** text. Unknown/conflict does not become false.

### Then: required support, form candidates and review gates

#### CLOSE.completeness — Completeness and handoff checklist

**IF:** `Always within this active topic`
**THEN, form candidates:** None implied by this rule alone.
- **Support: Completeness and handoff checklist** (`CLOSE.doc_completeness`; workpaper)
  - Extract/match: household roster; prior/current source comparison; expected document inventory; no-form income; corrected versions; unresolved issues; responsible owner; next action; deadlines
  - Look in: Authorized file library; taxpayer-provided records; relevant institution portal
  - Accept only when: Match the tax year, owner and specific entity; inspect the full record, not just a search hit; reconcile the listed fields and resolve corrections or conflicting versions.
  - Fallback: If unavailable, keep open and document the attempted sources. A preparer must approve any reconstructed or substitute support.
**Review gate:** Close only after all active facts, enumerations, evidence and required reviews are resolved. Organization completion is not approval to file.
**Authority:** [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

