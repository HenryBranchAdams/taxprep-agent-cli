# Form-to-support reverse index

All entries are candidates, not automatic requirements. Each entry links a form to its activation conditions and supporting material. Confirm year-specific eligibility and actual assembly/filing unit before preparation.

## 1040

**Assembly unit:** per selected individual/joint return

### PERSON.dependency — Person-specific dependency and support worksheet
IF `PERSON.role = "Potential dependent or supported person"`
Lane: individual_return_or_workpaper
Support: Person-specific dependency and support worksheet [PERSON.doc_dependency]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### STATUS.status_workpaper — Filing-status and household-cost workpaper
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Filing-status and household-cost workpaper [STATUS.doc_status_workpaper]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### WAGE.w2 — Locate and reconcile this employer’s W-2
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Complete current-year W-2 or W-2c [W2]; Year-end payroll and earnings detail [PAYROLL]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### WAGE.deferrals — All-employer elective-deferral reconciliation
IF `WAGE.deferral_excess = true`
Lane: individual_return_or_workpaper
Support: All-employer elective-deferral reconciliation [WAGE.doc_deferrals]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### INVEST.tax_package — Collect this account’s complete tax package
IF `INVEST.taxable = true`
Lane: individual_return_or_workpaper
Support: Complete consolidated brokerage tax package [BROKER]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### INVEST.muni — Tax-exempt and private-activity bond detail
IF `INVEST.municipal = true`
Lane: individual_return_or_workpaper
Support: Tax-exempt and private-activity bond detail [INVEST.doc_muni]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### RETIRE.distribution — Classify retirement distributions
IF `RETIRE.distribution = true`
Lane: individual_return_or_workpaper
Support: Complete 1099-R and corrections [R1099]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.rollover — Rollover source-to-destination reconciliation
IF `(RETIRE.distribution = true AND RETIRE.rollover = true)`
Lane: individual_return_or_workpaper
Support: Rollover source-to-destination reconciliation [RETIRE.doc_rollover]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.inherited — Inherited-account beneficiary and distribution workpaper
IF `RETIRE.inherited = true`
Lane: individual_return_or_workpaper
Support: Inherited-account beneficiary and distribution workpaper [RETIRE.doc_inherited]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.qcd — Qualified charitable distribution evidence
IF `(RETIRE.distribution = true AND RETIRE.qcd = true)`
Lane: individual_return_or_workpaper
Support: Qualified charitable distribution evidence [RETIRE.doc_qcd]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.plan_basis — Pension or plan after-tax/stock basis
IF `(RETIRE.distribution = true AND RETIRE.aftertax_plan = true)`
Lane: individual_return_or_workpaper
Support: Pension or plan after-tax/stock basis [RETIRE.doc_plan_basis]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### PASS.special — Pass-through special allocations and disclosures
IF `(PASS.special = true OR PASS.final = true)`
Lane: individual_return_or_workpaper
Support: Pass-through special allocations and disclosures [PASS.doc_special]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### OTHER.receipt — Receipt classification and gross-payment record
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Receipt classification and gross-payment record [OTHER.doc_receipt]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.ssa — Social Security or railroad retirement statement
IF `OTHER.kind = "Social Security / railroad retirement"`
Lane: individual_return_or_workpaper
Support: Social Security or railroad retirement statement [OTHER.doc_ssa]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.disability — Benefit taxability and premium history
IF `OTHER.kind = "Disability / workers compensation / Medicaid waiver"`
Lane: individual_return_or_workpaper
Support: Benefit taxability and premium history [OTHER.doc_disability]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### ITEMIZE.compare — Standard/itemized comparison and restrictions
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Standard/itemized comparison and restrictions [ITEMIZE.doc_compare]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### CARRY.other — Other surviving tax attribute carryforward rollforward
IF `CARRY.other = true`
Lane: individual_return_or_workpaper
Support: Other surviving tax attribute carryforward rollforward [CARRY.doc_other]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### CREDITS.eic — Earned income credit eligibility workpaper
IF `CREDITS.earned = true`
Lane: individual_return_or_workpaper
Support: Earned income credit eligibility workpaper [CREDITS.doc_eic]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

### TAX.filing — Filing requirement and independent-obligation review
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Filing requirement and independent-obligation review [TAX.doc_filing]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### PAY.payments — Reconcile tax payments and applied refunds
IF `(PAY.estimated = true OR PAY.extension = true OR PAY.prior_applied = true OR PAY.other_year = true)`
Lane: individual_return_or_workpaper
Support: Tax payment confirmations and account reconciliation [PAYMENTS]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### PAY.withholding — Withholding by owner and information statement
IF `PAY.withheld = true`
Lane: individual_return_or_workpaper
Support: Withholding by owner and information statement [PAY.doc_withholding]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### SPECIAL.tribal — Tribal income source and statutory authority
IF `SPECIAL.tribal = true`
Lane: individual_return_or_workpaper
Support: Tribal income source and statutory authority [SPECIAL.doc_tribal]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 1040-NR

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.foreign_person — Foreign residency classification review
IF `PERSON.citizenship is one of ["Nonresident or dual status", "Unresolved"]`
Lane: individual_return_or_workpaper
Support: Dated preparer decision memo [REVIEW_MEMO]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### FOREIGN.status — International residence classification workpaper
IF `FOREIGN.residency = true`
Lane: individual_return_or_workpaper
Support: International residence classification workpaper [FOREIGN.doc_status]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 1040-SR

**Assembly unit:** optional alternate presentation of applicable individual return

### TAX.filing — Filing requirement and independent-obligation review
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Filing requirement and independent-obligation review [TAX.doc_filing]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 1040-SS

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.territory — Territory residency and source-income workpaper
IF `FOREIGN.territory = true`
Lane: individual_return_or_workpaper
Support: Territory residency and source-income workpaper [FOREIGN.doc_territory]
Authority: [Publication 570: Territories](https://www.irs.gov/publications/p570)

## 1040-X

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CORE.amend — Originally filed return and amendment change log
IF `CORE.return_kind = "Amended"`
Lane: individual_return_or_workpaper
Support: Originally filed return and amendment change log [CORE.doc_amend]
Authority: [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### DISASTER.election — Disaster election and recovery history
IF `(DISASTER.prior_election = true OR DISASTER.gain = true)`
Lane: individual_return_or_workpaper
Support: Disaster election and recovery history [DISASTER.doc_election]
Authority: [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 1041

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DEBT.bankruptcy — Bankruptcy court and discharge packet
IF `DEBT.bankruptcy = true`
Lane: separate_obligation_or_procedure
Support: Bankruptcy court and discharge packet [DEBT.doc_bankruptcy]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### GIFT.estate — Inheritance and estate separation packet
IF `(GIFT.direction = "Inheritance received" OR GIFT.direction = "Estate/trust representative" OR GIFT.estate_filing = true)`
Lane: separate_obligation_or_procedure
Support: Inheritance and estate separation packet [GIFT.doc_estate]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 1065

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.entity_1065 — Separate Partnership return handoff
IF `BUSINESS.structure = "Partnership"`
Lane: separate_obligation_or_procedure
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 1099 series

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### INVEST.nominee — Nominee income allocation
IF `INVEST.nominee = true`
Lane: separate_obligation_or_procedure
Support: Nominee income allocation [INVEST.doc_nominee]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### BUSINESS.workers — Worker payments and employer reporting packet
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.workers = true)`
Lane: separate_obligation_or_procedure
Support: Worker payments and employer reporting packet [BUSINESS.doc_workers]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 1116

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### INVEST.foreign_tax — Investment foreign-tax detail
IF `INVEST.foreign_tax = true`
Lane: individual_return_or_workpaper
Support: Investment foreign-tax detail [INVEST.doc_foreign_tax]
Authority: [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### PASS.foreign — K-3 and foreign allocations
IF `PASS.foreign = true`
Lane: individual_return_or_workpaper
Support: K-3 and foreign allocations [PASS.doc_foreign]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### FOREIGN.tax — Foreign tax category and payment workpaper
IF `FOREIGN.foreign_tax = true`
Lane: individual_return_or_workpaper
Support: Foreign tax category and payment workpaper [FOREIGN.doc_tax]
Authority: [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.foreign — Foreign tax credit carryforward rollforward
IF `CARRY.foreign = true`
Lane: individual_return_or_workpaper
Support: Foreign tax credit carryforward rollforward [CARRY.doc_foreign]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 1120

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.domestic — Foreign-owned domestic entity reporting
IF `FOREIGN.domestic_foreign_owner = true`
Lane: separate_obligation_or_procedure
Support: Foreign-owned domestic entity reporting [FOREIGN.doc_domestic]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

### BUSINESS.entity_1120 — Separate C corporation return handoff
IF `BUSINESS.structure = "C corporation"`
Lane: separate_obligation_or_procedure
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 1120-S

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.entity_1120-S — Separate S corporation return handoff
IF `BUSINESS.structure = "S corporation"`
Lane: separate_obligation_or_procedure
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 1310

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.deceased — Death and representative authority
IF `PERSON.death = true`
Lane: individual_return_or_workpaper
Support: Death and representative authority [PERSON.doc_deceased]
Authority: [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559)

### GIFT.estate — Inheritance and estate separation packet
IF `(GIFT.direction = "Inheritance received" OR GIFT.direction = "Estate/trust representative" OR GIFT.estate_filing = true)`
Lane: individual_return_or_workpaper
Support: Inheritance and estate separation packet [GIFT.doc_estate]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 14039

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CORE.identity — Identity issue and IP PIN resolution evidence
IF `CORE.identity_issue = true`
Lane: separate_obligation_or_procedure
Support: Identity issue and IP PIN resolution evidence [CORE.doc_identity]
Authority: [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 2106

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### ADJUST.employee — Special employee expense packet
IF `ADJUST.reservist = true`
Lane: individual_return_or_workpaper
Support: Special employee expense packet [ADJUST.doc_employee]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### SPECIAL.military — Military tax fact packet
IF `SPECIAL.military = true`
Lane: individual_return_or_workpaper
Support: Military tax fact packet [SPECIAL.doc_military]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 2120

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.multiple_support — Multiple-support agreement
IF `(PERSON.role = "Potential dependent or supported person" AND PERSON.multiple_support = true)`
Lane: individual_return_or_workpaper
Support: Multiple-support agreement [PERSON.doc_multiple_support]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 2210

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PAY.penalty — Estimated tax and annualized-income workpaper
IF `(PAY.estimated = true OR PAY.uneven = true OR PAY.safe_harbor = false)`
Lane: individual_return_or_workpaper
Support: Estimated tax and annualized-income workpaper [PAY.doc_penalty]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 2210-F

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PAY.penalty — Estimated tax and annualized-income workpaper
IF `(PAY.estimated = true OR PAY.uneven = true OR PAY.safe_harbor = false)`
Lane: individual_return_or_workpaper
Support: Estimated tax and annualized-income workpaper [PAY.doc_penalty]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 2441

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.benefits — Employer benefit details
IF `WAGE.benefits = true`
Lane: individual_return_or_workpaper
Support: Employer benefit details [WAGE.doc_benefits]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### CARE.care — Dependent-care qualification and payments
IF `CARE.kind = "Dependent care"`
Lane: individual_return_or_workpaper
Support: Dependent-care qualification and payments [CARE.doc_care]
Authority: [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

### CARE.fsa — Dependent-care benefit allocation
IF `(CARE.kind = "Dependent care" AND CARE.benefits = true)`
Lane: individual_return_or_workpaper
Support: Dependent-care benefit allocation [CARE.doc_fsa]
Authority: [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 2555

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.earned — Foreign earned income and housing packet
IF `FOREIGN.earned = true`
Lane: individual_return_or_workpaper
Support: Foreign earned income and housing packet [FOREIGN.doc_earned]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 3115

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.special — Special business tax issues
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.special = true OR BUSINESS.hobby = true))`
Lane: individual_return_or_workpaper
Support: Special business tax issues [BUSINESS.doc_special]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### SPECIAL.accounting — Special method/year/procedure memo
IF `SPECIAL.accounting = true`
Lane: individual_return_or_workpaper
Support: Special method/year/procedure memo [SPECIAL.doc_accounting]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 3520

**Assembly unit:** per filer/foreign-trust or gift reporting requirements; separate filing

### FOREIGN.trust — Foreign trust ownership/transaction packet
IF `FOREIGN.trust = true`
Lane: separate_obligation_or_procedure
Support: Foreign trust ownership/transaction packet [FOREIGN.doc_trust]
Authority: [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520)

### FOREIGN.gifts — Foreign gift/bequest aggregation
IF `FOREIGN.gift = true`
Lane: separate_obligation_or_procedure
Support: Foreign gift/bequest aggregation [FOREIGN.doc_gifts]
Authority: [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520)

## 3520-A

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.trust — Foreign trust ownership/transaction packet
IF `FOREIGN.trust = true`
Lane: separate_obligation_or_procedure
Support: Foreign trust ownership/transaction packet [FOREIGN.doc_trust]
Authority: [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520)

## 3800

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.special — Special business tax issues
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.special = true OR BUSINESS.hobby = true))`
Lane: individual_return_or_workpaper
Support: Special business tax issues [BUSINESS.doc_special]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.special — Pass-through special allocations and disclosures
IF `(PASS.special = true OR PASS.final = true)`
Lane: individual_return_or_workpaper
Support: Pass-through special allocations and disclosures [PASS.doc_special]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.credits — Tax credit carryforward rollforward
IF `CARRY.credits = true`
Lane: individual_return_or_workpaper
Support: Tax credit carryforward rollforward [CARRY.doc_credits]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### CREDITS.other — Other credit eligibility packet
IF `CREDITS.other = true`
Lane: individual_return_or_workpaper
Support: Other credit eligibility packet [CREDITS.doc_other]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 3903

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### ADJUST.moving — Qualified military move packet
IF `ADJUST.moving = true`
Lane: individual_return_or_workpaper
Support: Qualified military move packet [ADJUST.doc_moving]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### SPECIAL.military — Military tax fact packet
IF `SPECIAL.military = true`
Lane: individual_return_or_workpaper
Support: Military tax fact packet [SPECIAL.doc_military]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 4029

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### SPECIAL.clergy — Clergy compensation and exemption packet
IF `SPECIAL.clergy = true`
Lane: separate_obligation_or_procedure
Support: Clergy compensation and exemption packet [SPECIAL.doc_clergy]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 4136

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CREDITS.other — Other credit eligibility packet
IF `CREDITS.other = true`
Lane: individual_return_or_workpaper
Support: Other credit eligibility packet [CREDITS.doc_other]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 4137

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.unreported_tips — Unreported-tip reconciliation
IF `(WAGE.tips = true AND WAGE.unreported_tips = true)`
Lane: individual_return_or_workpaper
Support: Unreported-tip reconciliation [WAGE.doc_unreported_tips]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

## 4255

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### VEHICLE.recapture — Vehicle credit change/recapture facts
IF `VEHICLE.disposed = true`
Lane: individual_return_or_workpaper
Support: Vehicle credit change/recapture facts [VEHICLE.doc_recapture]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 4361

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### SPECIAL.clergy — Clergy compensation and exemption packet
IF `SPECIAL.clergy = true`
Lane: separate_obligation_or_procedure
Support: Clergy compensation and exemption packet [SPECIAL.doc_clergy]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 4547

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.new_account — Optional child-account election support
IF `(PERSON.role = "Potential dependent or supported person" AND PERSON.trump_account = true)`
Lane: individual_return_or_workpaper
Support: Optional child-account election support [PERSON.doc_new_account]
Authority: [Instructions: Trump account elections](https://www.irs.gov/instructions/i4547)

## 4562

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.business_asset — Business-asset disposition workpaper
IF `DISPOSE.business_use = true`
Lane: individual_return_or_workpaper
Support: Business-asset disposition workpaper [DISPOSE.doc_business_asset]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### BUSINESS.vehicle — Business vehicle log and method history
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.vehicle = true))`
Lane: individual_return_or_workpaper
Support: Business vehicle log and method history [BUSINESS.doc_vehicle]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### BUSINESS.assets — Fixed-asset additions and dispositions
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.assets = true)`
Lane: individual_return_or_workpaper
Support: Historical fixed-asset and depreciation schedule [DEPR]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.improvements — Repairs versus improvements and asset additions
IF `RENTAL.repairs_assets = true`
Lane: individual_return_or_workpaper
Support: Repairs versus improvements and asset additions [RENTAL.doc_improvements]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### CARRY.depreciation — Depreciation/home-office carryforward rollforward
IF `CARRY.depreciation = true`
Lane: individual_return_or_workpaper
Support: Depreciation/home-office carryforward rollforward [CARRY.doc_depreciation]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 461

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.limits — Business loss, interest and participation limits
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.loss = true)`
Lane: individual_return_or_workpaper
Support: Business loss, interest and participation limits [BUSINESS.doc_limits]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.limits — Pass-through limitation and activity workpaper
IF `PASS.loss = true`
Lane: individual_return_or_workpaper
Support: Pass-through limitation and activity workpaper [PASS.doc_limits]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.nol — NOL/excess business loss carryforward rollforward
IF `CARRY.nol = true`
Lane: individual_return_or_workpaper
Support: NOL/excess business loss carryforward rollforward [CARRY.doc_nol]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.qbi — Aggregate QBI and business-loss handoff
IF `TAX.business = true`
Lane: individual_return_or_workpaper
Support: Aggregate QBI and business-loss handoff [TAX.doc_qbi]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 4684

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.loss_event — Worthlessness or loss-event substantiation
IF `DISPOSE.worthless = true`
Lane: individual_return_or_workpaper
Support: Worthlessness or loss-event substantiation [DISPOSE.doc_loss_event]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DISASTER.loss — Casualty/theft/disaster claim packet
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Casualty/theft/disaster claim packet [DISASTER.doc_loss]
Authority: [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### DISASTER.election — Disaster election and recovery history
IF `(DISASTER.prior_election = true OR DISASTER.gain = true)`
Lane: individual_return_or_workpaper
Support: Disaster election and recovery history [DISASTER.doc_election]
Authority: [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### DISASTER.theft — Investment-theft legal/recovery support
IF `DISASTER.ponzi = true`
Lane: individual_return_or_workpaper
Support: Investment-theft legal/recovery support [DISASTER.doc_theft]
Authority: [Publication 547: Casualties and disasters](https://www.irs.gov/publications/p547); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 4797

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.special — Complex securities workpaper
IF `DISPOSE.special = true`
Lane: individual_return_or_workpaper
Support: Complex securities workpaper [DISPOSE.doc_special]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DISPOSE.business_asset — Business-asset disposition workpaper
IF `DISPOSE.business_use = true`
Lane: individual_return_or_workpaper
Support: Business-asset disposition workpaper [DISPOSE.doc_business_asset]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### BUSINESS.assets — Fixed-asset additions and dispositions
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.assets = true)`
Lane: individual_return_or_workpaper
Support: Historical fixed-asset and depreciation schedule [DEPR]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### BUSINESS.startup — Business start/acquisition/closure packet
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.startup = true)`
Lane: individual_return_or_workpaper
Support: Business start/acquisition/closure packet [BUSINESS.doc_startup]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.sale — Rental property closing and disposition packet
IF `RENTAL.sold = true`
Lane: individual_return_or_workpaper
Support: Rental property closing and disposition packet [RENTAL.doc_sale]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.sale — Interest disposition and ordinary-income reconciliation
IF `PASS.sale = true`
Lane: individual_return_or_workpaper
Support: Interest disposition and ordinary-income reconciliation [PASS.doc_sale]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### HOME.home_use — Home-sale special use and depreciation
IF `(HOME.rental = true OR HOME.depreciation = true)`
Lane: individual_return_or_workpaper
Support: Home-sale special use and depreciation [HOME.doc_home_use]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### DEBT.property — Foreclosure/repossession disposition packet
IF `DEBT.property = true`
Lane: individual_return_or_workpaper
Support: Foreclosure/repossession disposition packet [DEBT.doc_property]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### FARM.special — Farm-specific elections and special transactions
IF `(FARM.deferral = true OR FARM.sale = true OR FARM.special = true)`
Lane: individual_return_or_workpaper
Support: Farm-specific elections and special transactions [FARM.doc_special]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

## 4835

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FARM.farm — Agricultural/resource activity books and classification
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Agricultural/resource activity books and classification [FARM.doc_farm]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

## 4852

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.replacement — W-2 recovery/correction workflow
IF `(WAGE.w2_issued = false OR WAGE.w2_correct = false)`
Lane: individual_return_or_workpaper
Support: Dated preparer decision memo [REVIEW_MEMO]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

## 4868

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CORE.extension — Extension acknowledgement and separately identified extension payments
IF `CORE.extension = true`
Lane: individual_return_or_workpaper
Support: Extension acknowledgement and separately identified extension payments [CORE.doc_extension]
Authority: [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 4952

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### INVEST.margin — Investment-interest allocation
IF `INVEST.margin = true`
Lane: individual_return_or_workpaper
Support: Investment-interest allocation [INVEST.doc_margin]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CARRY.interest — Investment/business interest carryforward rollforward
IF `CARRY.interest = true`
Lane: individual_return_or_workpaper
Support: Investment/business interest carryforward rollforward [CARRY.doc_interest]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 4972

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### RETIRE.plan_basis — Pension or plan after-tax/stock basis
IF `(RETIRE.distribution = true AND RETIRE.aftertax_plan = true)`
Lane: individual_return_or_workpaper
Support: Pension or plan after-tax/stock basis [RETIRE.doc_plan_basis]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

## 5329

**Assembly unit:** per individual with applicable parts

### RETIRE.rollover_exception — Late or restricted rollover support
IF `RETIRE.late_rollover = true`
Lane: individual_return_or_workpaper
Support: Late or restricted rollover support [RETIRE.doc_rollover_exception]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.roth_basis — Roth contribution/conversion ordering history
IF `(RETIRE.distribution = true AND RETIRE.roth_distribution = true)`
Lane: individual_return_or_workpaper
Support: Roth contribution/conversion ordering history [RETIRE.doc_roth_basis]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.early — Early-distribution exception evidence
IF `(RETIRE.distribution = true AND RETIRE.early = true)`
Lane: individual_return_or_workpaper
Support: Early-distribution exception evidence [RETIRE.doc_early]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.inherited — Inherited-account beneficiary and distribution workpaper
IF `RETIRE.inherited = true`
Lane: individual_return_or_workpaper
Support: Inherited-account beneficiary and distribution workpaper [RETIRE.doc_inherited]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.shortfall — RMD correction and reasonable-error relief packet
IF `(RETIRE.rmd = true AND RETIRE.rmd_shortfall = true)`
Lane: individual_return_or_workpaper
Support: RMD correction and reasonable-error relief packet [RETIRE.doc_shortfall]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.correction — Retirement correction/recharacterization packet
IF `RETIRE.excess = true`
Lane: individual_return_or_workpaper
Support: Retirement correction/recharacterization packet [RETIRE.doc_correction]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### EDUCATION.allocation — Student-level education expense allocation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Student-level education expense allocation [EDUCATION.doc_allocation]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### EDUCATION.529 — 529/Coverdell distributions and eligibility
IF `EDUCATION.529 = true`
Lane: individual_return_or_workpaper
Support: 529/Coverdell distributions and eligibility [EDUCATION.doc_529]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### HSA.correction — Savings-account excess/correction packet
IF `HSA.excess = true`
Lane: individual_return_or_workpaper
Support: Savings-account excess/correction packet [HSA.doc_correction]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### HSA.able — ABLE eligibility and expense allocation
IF `HSA.type = "ABLE"`
Lane: individual_return_or_workpaper
Support: ABLE eligibility and expense allocation [HSA.doc_able]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 5471

**Assembly unit:** per filer/foreign corporation subject to filing-category rules

### FOREIGN.corporation — Foreign corporation ownership and transactions
IF `FOREIGN.corporation = true`
Lane: individual_return_or_workpaper
Support: Foreign corporation ownership and transactions [FOREIGN.doc_corporation]
Authority: [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471)

## 5472

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.domestic — Foreign-owned domestic entity reporting
IF `FOREIGN.domestic_foreign_owner = true`
Lane: separate_obligation_or_procedure
Support: Foreign-owned domestic entity reporting [FOREIGN.doc_domestic]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 5500-EZ

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.retirement — Self-employed plan and contribution workpaper
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.retirement = true)`
Lane: separate_obligation_or_procedure
Support: Self-employed plan and contribution workpaper [BUSINESS.doc_retirement]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 56

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.deceased — Death and representative authority
IF `PERSON.death = true`
Lane: individual_return_or_workpaper
Support: Death and representative authority [PERSON.doc_deceased]
Authority: [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559)

### GIFT.estate — Inheritance and estate separation packet
IF `(GIFT.direction = "Inheritance received" OR GIFT.direction = "Estate/trust representative" OR GIFT.estate_filing = true)`
Lane: individual_return_or_workpaper
Support: Inheritance and estate separation packet [GIFT.doc_estate]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 5695

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### ENERGY.energy — Energy credit installation and eligibility packet
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Energy credit installation and eligibility packet [ENERGY.doc_energy]
Authority: [Instructions: Residential energy credits](https://www.irs.gov/instructions/i5695)

### ENERGY.carry — Prior residential clean energy credit carryforward
IF `ENERGY.carry = true`
Lane: individual_return_or_workpaper
Support: Prior residential clean energy credit carryforward [ENERGY.doc_carry]
Authority: [Instructions: Residential energy credits](https://www.irs.gov/instructions/i5695)

## 6198

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.limits — Business loss, interest and participation limits
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.loss = true)`
Lane: individual_return_or_workpaper
Support: Business loss, interest and participation limits [BUSINESS.doc_limits]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.carry — Property-specific suspended-loss history
IF `RENTAL.losses = true`
Lane: individual_return_or_workpaper
Support: Property-specific suspended-loss history [RENTAL.doc_carry]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.basis — Outside basis, debt basis and at-risk rollforward
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Outside basis, debt basis and at-risk rollforward [PASS.doc_basis]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### PASS.limits — Pass-through limitation and activity workpaper
IF `PASS.loss = true`
Lane: individual_return_or_workpaper
Support: Pass-through limitation and activity workpaper [PASS.doc_limits]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.passive — Passive/at-risk carryforward rollforward
IF `CARRY.passive = true`
Lane: individual_return_or_workpaper
Support: Passive/at-risk carryforward rollforward [CARRY.doc_passive]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 6251

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.iso — ISO exercise and disposition records
IF `(WAGE.equity = true AND WAGE.iso = true)`
Lane: individual_return_or_workpaper
Support: ISO exercise and disposition records [WAGE.doc_iso]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### INVEST.muni — Tax-exempt and private-activity bond detail
IF `INVEST.municipal = true`
Lane: individual_return_or_workpaper
Support: Tax-exempt and private-activity bond detail [INVEST.doc_muni]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CARRY.amt — AMT credit and alternative basis carryforward rollforward
IF `CARRY.amt = true`
Lane: individual_return_or_workpaper
Support: AMT credit and alternative basis carryforward rollforward [CARRY.doc_amt]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.amt — AMT screening and alternative-basis workpaper
IF `TAX.amt_items = true`
Lane: individual_return_or_workpaper
Support: AMT screening and alternative-basis workpaper [TAX.doc_amt]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 6252

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.installment — Installment sale agreement and amortization
IF `DISPOSE.installment = true`
Lane: individual_return_or_workpaper
Support: Installment sale agreement and amortization [DISPOSE.doc_installment]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### PASS.sale — Interest disposition and ordinary-income reconciliation
IF `PASS.sale = true`
Lane: individual_return_or_workpaper
Support: Interest disposition and ordinary-income reconciliation [PASS.doc_sale]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### HOME.exception — Reduced-exclusion or special home-sale support
IF `(HOME.reduced = true OR HOME.special = true)`
Lane: individual_return_or_workpaper
Support: Reduced-exclusion or special home-sale support [HOME.doc_exception]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### FARM.special — Farm-specific elections and special transactions
IF `(FARM.deferral = true OR FARM.sale = true OR FARM.special = true)`
Lane: individual_return_or_workpaper
Support: Farm-specific elections and special transactions [FARM.doc_special]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

### CARRY.installment — Deferred income/installment carryforward rollforward
IF `CARRY.installment = true`
Lane: individual_return_or_workpaper
Support: Deferred income/installment carryforward rollforward [CARRY.doc_installment]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 6781

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.special — Complex securities workpaper
IF `DISPOSE.special = true`
Lane: individual_return_or_workpaper
Support: Complex securities workpaper [DISPOSE.doc_special]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

## 706

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### GIFT.estate — Inheritance and estate separation packet
IF `(GIFT.direction = "Inheritance received" OR GIFT.direction = "Estate/trust representative" OR GIFT.estate_filing = true)`
Lane: separate_obligation_or_procedure
Support: Inheritance and estate separation packet [GIFT.doc_estate]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 709

**Assembly unit:** per donor per year; separate filing

### GIFT.gift — Gift transfer and annual aggregation
IF `GIFT.direction = "Gift made"`
Lane: separate_obligation_or_procedure
Support: Gift transfer and annual aggregation [GIFT.doc_gift]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### GIFT.prior — Prior gift-tax and exemption rollforward
IF `GIFT.prior = true`
Lane: separate_obligation_or_procedure
Support: Prior gift-tax and exemption rollforward [GIFT.doc_prior]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### GIFT.elections — Gift/GST/529 election workpaper
IF `(GIFT.split = true OR GIFT.gst = true)`
Lane: separate_obligation_or_procedure
Support: Gift/GST/529 election workpaper [GIFT.doc_elections]
Authority: [Instructions: Gift and GST tax](https://www.irs.gov/instructions/i709); [Publication 559: Survivors and estates](https://www.irs.gov/publications/p559); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

## 7203

**Assembly unit:** per shareholder per S corporation

### CARRY.basis — Owner basis-limited loss carryforward rollforward
IF `CARRY.basis = true`
Lane: individual_return_or_workpaper
Support: Owner basis-limited loss carryforward rollforward [CARRY.doc_basis]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### PASS.s_basis_form — S corporation shareholder-basis form test
IF `(PASS.kind = "1120-S S corporation" AND (PASS.loss = true OR PASS.distributions = true OR PASS.sale = true OR PASS.contributed = true))`
Lane: individual_return_or_workpaper
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

## 7206

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.insurance — Self-employed health insurance allocation
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.insurance = true)`
Lane: individual_return_or_workpaper
Support: Self-employed health insurance allocation [BUSINESS.doc_insurance]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 8283

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CHARITY.noncash — Noncash donation inventory and valuation
IF `CHARITY.noncash = true`
Lane: individual_return_or_workpaper
Support: Noncash donation inventory and valuation [CHARITY.doc_noncash]
Authority: [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

### CHARITY.appraisal — Required appraisal and signed donation acknowledgements
IF `(CHARITY.noncash = true AND CHARITY.appraisal = true)`
Lane: individual_return_or_workpaper
Support: Required appraisal and signed donation acknowledgements [CHARITY.doc_appraisal]
Authority: [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

### CHARITY.vehicle — Donated vehicle special documentation
IF `CHARITY.kind = "Vehicle / boat / aircraft"`
Lane: individual_return_or_workpaper
Support: Donated vehicle special documentation [CHARITY.doc_vehicle]
Authority: [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

## 8332

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.custody — Custody calendar and release/revocation records
IF `(PERSON.role = "Potential dependent or supported person" AND PERSON.custody = true)`
Lane: individual_return_or_workpaper
Support: Custody calendar and release/revocation records [PERSON.doc_custody]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8379

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### STATUS.spouse_relief — Spouse-liability or offset fact packet
IF `STATUS.spouse_debt = true`
Lane: individual_return_or_workpaper
Support: Spouse-liability or offset fact packet [STATUS.doc_spouse_relief]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### PAY.offset — Refund allocation and offset facts
IF `PAY.offset = true`
Lane: individual_return_or_workpaper
Support: Refund allocation and offset facts [PAY.doc_offset]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8396

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CREDITS.other — Other credit eligibility packet
IF `CREDITS.other = true`
Lane: individual_return_or_workpaper
Support: Other credit eligibility packet [CREDITS.doc_other]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 8582

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.limits — Business loss, interest and participation limits
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.loss = true)`
Lane: individual_return_or_workpaper
Support: Business loss, interest and participation limits [BUSINESS.doc_limits]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.services — Short-stay and substantial-services classification
IF `RENTAL.shortstay = true`
Lane: individual_return_or_workpaper
Support: Short-stay and substantial-services classification [RENTAL.doc_services]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.sale — Rental property closing and disposition packet
IF `RENTAL.sold = true`
Lane: individual_return_or_workpaper
Support: Rental property closing and disposition packet [RENTAL.doc_sale]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.participation — Rental participation and grouping workpaper
IF `RENTAL.participation = true`
Lane: individual_return_or_workpaper
Support: Rental participation and grouping workpaper [RENTAL.doc_participation]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.carry — Property-specific suspended-loss history
IF `RENTAL.losses = true`
Lane: individual_return_or_workpaper
Support: Property-specific suspended-loss history [RENTAL.doc_carry]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.limits — Pass-through limitation and activity workpaper
IF `PASS.loss = true`
Lane: individual_return_or_workpaper
Support: Pass-through limitation and activity workpaper [PASS.doc_limits]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.passive — Passive/at-risk carryforward rollforward
IF `CARRY.passive = true`
Lane: individual_return_or_workpaper
Support: Passive/at-risk carryforward rollforward [CARRY.doc_passive]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 8594

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.startup — Business start/acquisition/closure packet
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.startup = true)`
Lane: individual_return_or_workpaper
Support: Business start/acquisition/closure packet [BUSINESS.doc_startup]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 8606

**Assembly unit:** per individual for own IRAs; inherited IRAs may require separate forms and decedent-specific basis

### RETIRE.ira_basis — IRA after-tax basis and pro-rata workpaper
IF `(RETIRE.nondeductible = true OR RETIRE.conversion = true)`
Lane: individual_return_or_workpaper
Support: Prior Forms 8606 and IRA basis rollforward [IRA_HISTORY]; December 31 values of every relevant traditional, SEP and SIMPLE IRA for the same individual [IRA_DEC31]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.roth_basis — Roth contribution/conversion ordering history
IF `(RETIRE.distribution = true AND RETIRE.roth_distribution = true)`
Lane: individual_return_or_workpaper
Support: Roth contribution/conversion ordering history [RETIRE.doc_roth_basis]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### RETIRE.correction — Retirement correction/recharacterization packet
IF `RETIRE.excess = true`
Lane: individual_return_or_workpaper
Support: Retirement correction/recharacterization packet [RETIRE.doc_correction]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

## 8615

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.child_return — Child’s income and parent-return coordination
IF `(PERSON.role = "Potential dependent or supported person" AND PERSON.child_income = true)`
Lane: individual_return_or_workpaper
Support: Child’s income and parent-return coordination [PERSON.doc_child_return]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8621

**Assembly unit:** per filer/PFIC subject to exceptions

### FOREIGN.pfic — PFIC annual information and election history
IF `FOREIGN.fund = true`
Lane: individual_return_or_workpaper
Support: PFIC annual information and election history [FOREIGN.doc_pfic]
Authority: [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621)

## 8689

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.territory — Territory residency and source-income workpaper
IF `FOREIGN.territory = true`
Lane: individual_return_or_workpaper
Support: Territory residency and source-income workpaper [FOREIGN.doc_territory]
Authority: [Publication 570: Territories](https://www.irs.gov/publications/p570)

## 8801

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.iso — ISO exercise and disposition records
IF `(WAGE.equity = true AND WAGE.iso = true)`
Lane: individual_return_or_workpaper
Support: ISO exercise and disposition records [WAGE.doc_iso]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### CARRY.amt — AMT credit and alternative basis carryforward rollforward
IF `CARRY.amt = true`
Lane: individual_return_or_workpaper
Support: AMT credit and alternative basis carryforward rollforward [CARRY.doc_amt]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.amt — AMT screening and alternative-basis workpaper
IF `TAX.amt_items = true`
Lane: individual_return_or_workpaper
Support: AMT screening and alternative-basis workpaper [TAX.doc_amt]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8814

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.child_return — Child’s income and parent-return coordination
IF `(PERSON.role = "Potential dependent or supported person" AND PERSON.child_income = true)`
Lane: individual_return_or_workpaper
Support: Child’s income and parent-return coordination [PERSON.doc_child_return]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8815

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### INVEST.bond — Bond and savings-bond detail
IF `INVEST.bond = true`
Lane: individual_return_or_workpaper
Support: Bond and savings-bond detail [INVEST.doc_bond]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8824

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.exchange — Like-kind exchange closing packet
IF `DISPOSE.like_kind = true`
Lane: individual_return_or_workpaper
Support: Like-kind exchange closing packet [DISPOSE.doc_exchange]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

## 8829

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.home — Home-office qualification and expense workpaper
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.home_office = true))`
Lane: individual_return_or_workpaper
Support: Home-office qualification and expense workpaper [BUSINESS.doc_home]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### CARRY.depreciation — Depreciation/home-office carryforward rollforward
IF `CARRY.depreciation = true`
Lane: individual_return_or_workpaper
Support: Depreciation/home-office carryforward rollforward [CARRY.doc_depreciation]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 8833

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.status — International residence classification workpaper
IF `FOREIGN.residency = true`
Lane: individual_return_or_workpaper
Support: International residence classification workpaper [FOREIGN.doc_status]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

### FOREIGN.late — International late-filing and treaty review
IF `(FOREIGN.late = true OR FOREIGN.treaty = true OR FOREIGN.spouse_election = true)`
Lane: individual_return_or_workpaper
Support: International late-filing and treaty review [FOREIGN.doc_late]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8839

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.benefits — Employer benefit details
IF `WAGE.benefits = true`
Lane: individual_return_or_workpaper
Support: Employer benefit details [WAGE.doc_benefits]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### CARE.adoption — Adoption costs, finalization and benefits packet
IF `CARE.kind = "Adoption"`
Lane: individual_return_or_workpaper
Support: Adoption costs, finalization and benefits packet [CARE.doc_adoption]
Authority: [Publication 503: Dependent care](https://www.irs.gov/publications/p503); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 8840

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.foreign_person — Foreign residency classification review
IF `PERSON.citizenship is one of ["Nonresident or dual status", "Unresolved"]`
Lane: individual_return_or_workpaper
Support: Dated preparer decision memo [REVIEW_MEMO]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### FOREIGN.status — International residence classification workpaper
IF `FOREIGN.residency = true`
Lane: individual_return_or_workpaper
Support: International residence classification workpaper [FOREIGN.doc_status]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8843

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.foreign_person — Foreign residency classification review
IF `PERSON.citizenship is one of ["Nonresident or dual status", "Unresolved"]`
Lane: individual_return_or_workpaper
Support: Dated preparer decision memo [REVIEW_MEMO]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### FOREIGN.status — International residence classification workpaper
IF `FOREIGN.residency = true`
Lane: individual_return_or_workpaper
Support: International residence classification workpaper [FOREIGN.doc_status]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8853

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### HSA.msa — MSA reporting support
IF `HSA.type = "Archer or Medicare Advantage MSA"`
Lane: individual_return_or_workpaper
Support: MSA reporting support [HSA.doc_msa]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8854

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.expat — Expatriation and long-term resident termination packet
IF `FOREIGN.expatriation = true`
Lane: individual_return_or_workpaper
Support: Expatriation and long-term resident termination packet [FOREIGN.doc_expat]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8857

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### STATUS.spouse_relief — Spouse-liability or offset fact packet
IF `STATUS.spouse_debt = true`
Lane: separate_obligation_or_procedure
Support: Spouse-liability or offset fact packet [STATUS.doc_spouse_relief]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8858

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.branch — Foreign disregarded entity or branch books
IF `FOREIGN.branch = true`
Lane: individual_return_or_workpaper
Support: Foreign disregarded entity or branch books [FOREIGN.doc_branch]
Authority: [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8862

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CORE.notices — Full IRS and state notice packet
IF `CORE.notices = true`
Lane: individual_return_or_workpaper
Support: Full IRS and state notice packet [CORE.doc_notices]
Authority: [IRS intake and interview process](https://apps.irs.gov/app/vita/content/0507/0507_00_020.jsp); [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### EDUCATION.prior_credit — Prior AOTC claims and disallowances
IF `(EDUCATION.aotc_years > 0 OR EDUCATION.disallowed = true)`
Lane: individual_return_or_workpaper
Support: Prior AOTC claims and disallowances [EDUCATION.doc_prior_credit]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### CREDITS.disallow — Prior credit disallowance and recertification
IF `CREDITS.disallowed = true`
Lane: individual_return_or_workpaper
Support: Prior credit disallowance and recertification [CREDITS.doc_disallow]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 8863

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### EDUCATION.tuition — Education source documents
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: 1098-T plus detailed school account and payment records [TUITION]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### EDUCATION.allocation — Student-level education expense allocation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Student-level education expense allocation [EDUCATION.doc_allocation]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### EDUCATION.refund — Education refund and credit recapture
IF `EDUCATION.refund = true`
Lane: individual_return_or_workpaper
Support: Education refund and credit recapture [EDUCATION.doc_refund]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### EDUCATION.prior_credit — Prior AOTC claims and disallowances
IF `(EDUCATION.aotc_years > 0 OR EDUCATION.disallowed = true)`
Lane: individual_return_or_workpaper
Support: Prior AOTC claims and disallowances [EDUCATION.doc_prior_credit]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

## 8865

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.partnership — Foreign partnership ownership and transfer packet
IF `FOREIGN.partnership = true`
Lane: individual_return_or_workpaper
Support: Foreign partnership ownership and transfer packet [FOREIGN.doc_partnership]
Authority: [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865)

### FOREIGN.transfer — Transfers to foreign entities
IF `FOREIGN.transfer = true`
Lane: individual_return_or_workpaper
Support: Transfers to foreign entities [FOREIGN.doc_transfer]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8880

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### CREDITS.saver — Retirement savings contribution credit workpaper
IF `CREDITS.retirement_saver = true`
Lane: individual_return_or_workpaper
Support: Retirement savings contribution credit workpaper [CREDITS.doc_saver]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## 8886

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### SPECIAL.disclosure — Reportable-transaction disclosure packet
IF `SPECIAL.reportable = true`
Lane: individual_return_or_workpaper
Support: Reportable-transaction disclosure packet [SPECIAL.doc_disclosure]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

## 8888

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PAY.bank — Secure refund/payment instructions
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Secure refund/payment instructions [PAY.doc_bank]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8889

**Assembly unit:** per individual across relevant HSAs

### HSA.hsa_forms — HSA activity reporting
IF `(HSA.type = "HSA" AND (HSA.contribution = true OR HSA.distribution = true OR HSA.lastmonth = true OR HSA.carry_issue = true))`
Lane: individual_return_or_workpaper
Support: HSA contribution and distribution statements [HSA_DOCS]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### HSA.medical — Substantiate HSA distributions
IF `(HSA.type = "HSA" AND HSA.distribution = true)`
Lane: individual_return_or_workpaper
Support: Unreimbursed qualified medical expense allocation for HSA distributions [HSA_MED]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### HSA.eligibility — HSA month-by-month eligibility and contribution limit
IF `(HSA.type = "HSA" AND HSA.contribution = true)`
Lane: individual_return_or_workpaper
Support: HSA month-by-month eligibility and contribution limit [HSA.doc_eligibility]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### HSA.testing — HSA last-month and testing-period history
IF `(HSA.lastmonth = true OR HSA.carry_issue = true)`
Lane: individual_return_or_workpaper
Support: HSA last-month and testing-period history [HSA.doc_testing]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8898

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.territory — Territory residency and source-income workpaper
IF `FOREIGN.territory = true`
Lane: individual_return_or_workpaper
Support: Territory residency and source-income workpaper [FOREIGN.doc_territory]
Authority: [Publication 570: Territories](https://www.irs.gov/publications/p570)

## 8911

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### VEHICLE.charger — Charging equipment credit facts
IF `VEHICLE.kind = "Charging equipment"`
Lane: individual_return_or_workpaper
Support: Charging equipment credit facts [VEHICLE.doc_charger]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8915-F

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### RETIRE.disaster — Retirement disaster distribution and repayment history
IF `RETIRE.disaster = true`
Lane: individual_return_or_workpaper
Support: Retirement disaster distribution and repayment history [RETIRE.doc_disaster]
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

### CARRY.installment — Deferred income/installment carryforward rollforward
IF `CARRY.installment = true`
Lane: individual_return_or_workpaper
Support: Deferred income/installment carryforward rollforward [CARRY.doc_installment]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 8919

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.classification — Worker-classification facts
IF `WAGE.misclassified = true`
Lane: individual_return_or_workpaper
Support: Worker-classification facts [WAGE.doc_classification]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

## 8936

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### VEHICLE.credit — Clean vehicle eligibility and seller report
IF `VEHICLE.ev = true`
Lane: individual_return_or_workpaper
Support: Clean vehicle eligibility and seller report [VEHICLE.doc_credit]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### VEHICLE.recapture — Vehicle credit change/recapture facts
IF `VEHICLE.disposed = true`
Lane: individual_return_or_workpaper
Support: Vehicle credit change/recapture facts [VEHICLE.doc_recapture]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8938

**Assembly unit:** per applicable return/reporting unit

### PASS.foreign — K-3 and foreign allocations
IF `PASS.foreign = true`
Lane: individual_return_or_workpaper
Support: K-3 and foreign allocations [PASS.doc_foreign]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### FOREIGN.accounts — Foreign financial account inventory and valuation
IF `FOREIGN.account = true`
Lane: individual_return_or_workpaper
Support: Foreign financial account inventory and valuation [FOREIGN.doc_accounts]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

### FOREIGN.assets — Specified foreign financial asset schedule
IF `FOREIGN.assets = true`
Lane: individual_return_or_workpaper
Support: Specified foreign financial asset schedule [FOREIGN.doc_assets]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 8949

**Assembly unit:** return-level categories with transaction-level workpapers

### WAGE.equity — Equity compensation lifecycle packet
IF `WAGE.equity = true`
Lane: individual_return_or_workpaper
Support: Equity compensation lifecycle packet [WAGE.doc_equity]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### INVEST.sales — Open asset-disposition inventory
IF `INVEST.sales = true`
Lane: individual_return_or_workpaper
Support: Acquisition and adjusted-basis history [BASIS]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### DISPOSE.sales_packet — Sale ledger and basis reconciliation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Acquisition and adjusted-basis history [BASIS]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DISPOSE.wash — Cross-account wash-sale workpaper
IF `DISPOSE.wash = true`
Lane: individual_return_or_workpaper
Support: Cross-account wash-sale workpaper [DISPOSE.doc_wash]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DISPOSE.exclusion — Special asset exclusion/deferral support
IF `DISPOSE.qsbs = true`
Lane: individual_return_or_workpaper
Support: Special asset exclusion/deferral support [DISPOSE.doc_exclusion]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DISPOSE.loss_event — Worthlessness or loss-event substantiation
IF `DISPOSE.worthless = true`
Lane: individual_return_or_workpaper
Support: Worthlessness or loss-event substantiation [DISPOSE.doc_loss_event]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DIGITAL.taxable_disposal — Digital-asset disposition ledger
IF `(DIGITAL.disposal = true OR DIGITAL.fee_crypto = true)`
Lane: individual_return_or_workpaper
Support: Digital-asset disposition ledger [DIGITAL.doc_taxable_disposal]
Authority: [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### PASS.sale — Interest disposition and ordinary-income reconciliation
IF `PASS.sale = true`
Lane: individual_return_or_workpaper
Support: Interest disposition and ordinary-income reconciliation [PASS.doc_sale]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### OTHER.personal1099 — Personal payments and erroneous information-return reconciliation
IF `OTHER.kind = "Personal payment / reimbursement / 1099-K"`
Lane: individual_return_or_workpaper
Support: Personal payments and erroneous information-return reconciliation [OTHER.doc_personal1099]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### HOME.home_sale — Home sale proceeds and exclusion packet
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Home sale proceeds and exclusion packet [HOME.doc_home_sale]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### HOME.exception — Reduced-exclusion or special home-sale support
IF `(HOME.reduced = true OR HOME.special = true)`
Lane: individual_return_or_workpaper
Support: Reduced-exclusion or special home-sale support [HOME.doc_exception]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### DEBT.property — Foreclosure/repossession disposition packet
IF `DEBT.property = true`
Lane: individual_return_or_workpaper
Support: Foreclosure/repossession disposition packet [DEBT.doc_property]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## 8958

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### STATUS.community — Community/separate income and withholding allocation
IF `STATUS.community = true`
Lane: individual_return_or_workpaper
Support: Community/separate income and withholding allocation [STATUS.doc_community]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8959

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### TAX.medicare — Additional Medicare tax and withholding reconciliation
IF `TAX.high_income = true`
Lane: individual_return_or_workpaper
Support: Additional Medicare tax and withholding reconciliation [TAX.doc_medicare]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8960

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### TAX.niit — Net investment income tax threshold and allocation workpaper
IF `(TAX.high_income = true OR TAX.niit_income = true)`
Lane: individual_return_or_workpaper
Support: Net investment income tax threshold and allocation workpaper [TAX.doc_niit]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8962

**Assembly unit:** return-level with policy/month allocations

### HEALTH.policy — Marketplace reporting and reconciliation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Final Form 1095-A for every Marketplace policy [HEALTH_A]; Marketplace coverage and household reconciliation [ACA_MONTHS]
Authority: [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

### HEALTH.shared — Shared-policy allocation agreement/workpaper
IF `HEALTH.shared = true`
Lane: individual_return_or_workpaper
Support: Shared-policy allocation agreement/workpaper [HEALTH.doc_shared]
Authority: [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

### HEALTH.coverage — Other-coverage and employer-offer eligibility
IF `(HEALTH.other_coverage = true OR HEALTH.hra = true)`
Lane: individual_return_or_workpaper
Support: Other-coverage and employer-offer eligibility [HEALTH.doc_coverage]
Authority: [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

### HEALTH.exception — Marketplace household-change or exception support
IF `(HEALTH.marriage = true OR HEALTH.mfs_relief = true)`
Lane: individual_return_or_workpaper
Support: Marketplace household-change or exception support [HEALTH.doc_exception]
Authority: [Instructions: Premium tax credit](https://www.irs.gov/instructions/i8962)

## 8990

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.limits — Business loss, interest and participation limits
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.loss = true)`
Lane: individual_return_or_workpaper
Support: Business loss, interest and participation limits [BUSINESS.doc_limits]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### CARRY.interest — Investment/business interest carryforward rollforward
IF `CARRY.interest = true`
Lane: individual_return_or_workpaper
Support: Investment/business interest carryforward rollforward [CARRY.doc_interest]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## 8992

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.corporation — Foreign corporation ownership and transactions
IF `FOREIGN.corporation = true`
Lane: individual_return_or_workpaper
Support: Foreign corporation ownership and transactions [FOREIGN.doc_corporation]
Authority: [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471)

## 8993

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.corporation — Foreign corporation ownership and transactions
IF `FOREIGN.corporation = true`
Lane: individual_return_or_workpaper
Support: Foreign corporation ownership and transactions [FOREIGN.doc_corporation]
Authority: [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471)

## 8995

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.qbi — Business QBI information
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.qbi = true)`
Lane: individual_return_or_workpaper
Support: Business QBI information [BUSINESS.doc_qbi]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.qbi — Rental QBI qualification file
IF `RENTAL.qbi = true`
Lane: individual_return_or_workpaper
Support: Rental QBI qualification file [RENTAL.doc_qbi]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.qbi — Pass-through QBI supplement
IF `PASS.qbi = true`
Lane: individual_return_or_workpaper
Support: Pass-through QBI supplement [PASS.doc_qbi]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.qbi — QBI loss carryforward rollforward
IF `CARRY.qbi = true`
Lane: individual_return_or_workpaper
Support: QBI loss carryforward rollforward [CARRY.doc_qbi]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.qbi — Aggregate QBI and business-loss handoff
IF `TAX.business = true`
Lane: individual_return_or_workpaper
Support: Aggregate QBI and business-loss handoff [TAX.doc_qbi]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8995-A

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.qbi — Business QBI information
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.qbi = true)`
Lane: individual_return_or_workpaper
Support: Business QBI information [BUSINESS.doc_qbi]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.qbi — Rental QBI qualification file
IF `RENTAL.qbi = true`
Lane: individual_return_or_workpaper
Support: Rental QBI qualification file [RENTAL.doc_qbi]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.qbi — Pass-through QBI supplement
IF `PASS.qbi = true`
Lane: individual_return_or_workpaper
Support: Pass-through QBI supplement [PASS.doc_qbi]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### CARRY.qbi — QBI loss carryforward rollforward
IF `CARRY.qbi = true`
Lane: individual_return_or_workpaper
Support: QBI loss carryforward rollforward [CARRY.doc_qbi]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.qbi — Aggregate QBI and business-loss handoff
IF `TAX.business = true`
Lane: individual_return_or_workpaper
Support: Aggregate QBI and business-loss handoff [TAX.doc_qbi]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 8997

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DISPOSE.exclusion — Special asset exclusion/deferral support
IF `DISPOSE.qsbs = true`
Lane: individual_return_or_workpaper
Support: Special asset exclusion/deferral support [DISPOSE.doc_exclusion]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

## 926

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FOREIGN.transfer — Transfers to foreign entities
IF `FOREIGN.transfer = true`
Lane: individual_return_or_workpaper
Support: Transfers to foreign entities [FOREIGN.doc_transfer]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## 9465

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PAY.collection — Payment-plan consideration
IF `PAY.balance_plan = true`
Lane: separate_obligation_or_procedure
Support: Payment-plan consideration [PAY.doc_collection]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## 982

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DEBT.debt — Debt discharge agreement and information returns
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Debt discharge agreement and information returns [DEBT.doc_debt]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### DEBT.insolvency — Immediately-before-discharge insolvency balance sheet
IF `DEBT.insolvent = true`
Lane: individual_return_or_workpaper
Support: Immediately-before-discharge insolvency balance sheet [DEBT.doc_insolvency]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### DEBT.bankruptcy — Bankruptcy court and discharge packet
IF `DEBT.bankruptcy = true`
Lane: individual_return_or_workpaper
Support: Bankruptcy court and discharge packet [DEBT.doc_bankruptcy]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### DEBT.exclusion — Debt exclusion and attribute-reduction workpaper
IF `(DEBT.special = true OR DEBT.attributes = true)`
Lane: individual_return_or_workpaper
Support: Debt exclusion and attribute-reduction workpaper [DEBT.doc_exclusion]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## FinCEN 114

**Assembly unit:** per reporting person per calendar year; separate FinCEN filing

### FOREIGN.accounts — Foreign financial account inventory and valuation
IF `FOREIGN.account = true`
Lane: separate_obligation_or_procedure
Support: Foreign financial account inventory and valuation [FOREIGN.doc_accounts]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## SS-8

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.classification — Worker-classification facts
IF `WAGE.misclassified = true`
Lane: separate_obligation_or_procedure
Support: Worker-classification facts [WAGE.doc_classification]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

## Schedule 1

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DIGITAL.income — Digital-asset income valuation records
IF `(DIGITAL.rewards = true OR DIGITAL.services = true)`
Lane: individual_return_or_workpaper
Support: Digital-asset income valuation records [DIGITAL.doc_income]
Authority: [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### BUSINESS.retirement — Self-employed plan and contribution workpaper
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.retirement = true)`
Lane: individual_return_or_workpaper
Support: Self-employed plan and contribution workpaper [BUSINESS.doc_retirement]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### OTHER.receipt — Receipt classification and gross-payment record
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Receipt classification and gross-payment record [OTHER.doc_receipt]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.refund — Prior-year tax-benefit recovery workpaper
IF `OTHER.kind = "State/local tax refund"`
Lane: individual_return_or_workpaper
Support: Prior-year tax-benefit recovery workpaper [OTHER.doc_refund]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.alimony — Alimony agreement and payment history
IF `OTHER.kind = "Alimony"`
Lane: individual_return_or_workpaper
Support: Alimony agreement and payment history [OTHER.doc_alimony]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.gambling — Gambling winnings and session/loss records
IF `OTHER.kind = "Gambling"`
Lane: individual_return_or_workpaper
Support: Gambling winnings and session/loss records [OTHER.doc_gambling]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.disability — Benefit taxability and premium history
IF `OTHER.kind = "Disability / workers compensation / Medicaid waiver"`
Lane: individual_return_or_workpaper
Support: Benefit taxability and premium history [OTHER.doc_disability]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.settlement — Settlement agreement and gross legal proceeds
IF `OTHER.kind = "Lawsuit settlement / insurance"`
Lane: individual_return_or_workpaper
Support: Settlement agreement and gross legal proceeds [OTHER.doc_settlement]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.personal1099 — Personal payments and erroneous information-return reconciliation
IF `OTHER.kind = "Personal payment / reimbursement / 1099-K"`
Lane: individual_return_or_workpaper
Support: Personal payments and erroneous information-return reconciliation [OTHER.doc_personal1099]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### ADJUST.student — Student-loan interest support
IF `ADJUST.student_loan = true`
Lane: individual_return_or_workpaper
Support: Student-loan interest support [ADJUST.doc_student]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### ADJUST.educator — Educator qualification and expenses
IF `ADJUST.educator = true`
Lane: individual_return_or_workpaper
Support: Educator qualification and expenses [ADJUST.doc_educator]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### ADJUST.alimony — Alimony paid agreement and support
IF `ADJUST.alimony = true`
Lane: individual_return_or_workpaper
Support: Alimony paid agreement and support [ADJUST.doc_alimony]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### ADJUST.penalty — Savings early-withdrawal penalty statement
IF `ADJUST.penalty = true`
Lane: individual_return_or_workpaper
Support: Savings early-withdrawal penalty statement [ADJUST.doc_penalty]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### ADJUST.special — Other adjustment legal basis and support
IF `ADJUST.legal = true`
Lane: individual_return_or_workpaper
Support: Other adjustment legal basis and support [ADJUST.doc_special]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 970: Education benefits](https://www.irs.gov/publications/p970); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504)

### EDUCATION.scholarships — Scholarship and grant terms
IF `EDUCATION.scholarships = true`
Lane: individual_return_or_workpaper
Support: Scholarship and grant terms [EDUCATION.doc_scholarships]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### EDUCATION.529 — 529/Coverdell distributions and eligibility
IF `EDUCATION.529 = true`
Lane: individual_return_or_workpaper
Support: 529/Coverdell distributions and eligibility [EDUCATION.doc_529]
Authority: [Publication 970: Education benefits](https://www.irs.gov/publications/p970)

### HSA.able — ABLE eligibility and expense allocation
IF `HSA.type = "ABLE"`
Lane: individual_return_or_workpaper
Support: ABLE eligibility and expense allocation [HSA.doc_able]
Authority: [Publication 969: HSA and other health plans](https://www.irs.gov/publications/p969); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### DEBT.debt — Debt discharge agreement and information returns
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Debt discharge agreement and information returns [DEBT.doc_debt]
Authority: [Publication 4681: Canceled debt](https://www.irs.gov/publications/p4681); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### CARRY.nol — NOL/excess business loss carryforward rollforward
IF `CARRY.nol = true`
Lane: individual_return_or_workpaper
Support: NOL/excess business loss carryforward rollforward [CARRY.doc_nol]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### RETIRE.deduction_candidate — Potential IRA / self-employed retirement deduction
IF `(RETIRE.contribution = true AND RETIRE.type is one of ["Traditional IRA", "SEP IRA", "SIMPLE IRA"])`
Lane: individual_return_or_workpaper
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 590A: IRA contributions](https://www.irs.gov/publications/p590a); [Publication 590B: IRA distributions](https://www.irs.gov/publications/p590b); [Instructions: Nondeductible IRAs](https://www.irs.gov/instructions/i8606); [Instructions: Retirement and savings account additional taxes](https://www.irs.gov/instructions/i5329)

## Schedule 1-A

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### WAGE.tips — Tip records and qualifying-tip deduction workpaper
IF `WAGE.tips = true`
Lane: individual_return_or_workpaper
Support: Tip records and qualifying-tip deduction workpaper [WAGE.doc_tips]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### WAGE.overtime — Overtime hours and premium substantiation
IF `WAGE.overtime = true`
Lane: individual_return_or_workpaper
Support: Overtime hours and premium substantiation [WAGE.doc_overtime]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### VEHICLE.loan — Vehicle-loan interest qualification and payments
IF `VEHICLE.loan = true`
Lane: individual_return_or_workpaper
Support: Vehicle-loan interest qualification and payments [VEHICLE.doc_loan]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### TAX.1a — Schedule 1-A eligibility and limitation coordination
IF `(TAX.deduction_1a = true OR TAX.senior = true)`
Lane: individual_return_or_workpaper
Support: Schedule 1-A eligibility and limitation coordination [TAX.doc_1a]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## Schedule 3

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### OTHER.repayment — Repayment and claim-of-right evidence
IF `OTHER.repaid = true`
Lane: individual_return_or_workpaper
Support: Repayment and claim-of-right evidence [OTHER.doc_repayment]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CARRY.credits — Tax credit carryforward rollforward
IF `CARRY.credits = true`
Lane: individual_return_or_workpaper
Support: Tax credit carryforward rollforward [CARRY.doc_credits]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

### TAX.social_security — Excess Social Security/RRTA withholding workpaper
IF `TAX.multiple_w2 = true`
Lane: individual_return_or_workpaper
Support: Excess Social Security/RRTA withholding workpaper [TAX.doc_social_security]
Authority: [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251); [Instructions: Additional Medicare tax](https://www.irs.gov/instructions/i8959); [Instructions: Net investment income tax](https://www.irs.gov/instructions/i8960); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## Schedule 8812

**Assembly unit:** return-level using individual dependent tests

### PERSON.dependency — Person-specific dependency and support worksheet
IF `PERSON.role = "Potential dependent or supported person"`
Lane: individual_return_or_workpaper
Support: Person-specific dependency and support worksheet [PERSON.doc_dependency]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CREDITS.dependent_credits — Child and other dependent credit workpaper
IF `CREDITS.qualifying_children = true`
Lane: individual_return_or_workpaper
Support: Child and other dependent credit workpaper [CREDITS.doc_dependent_credits]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## Schedule A

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### OTHER.gambling — Gambling winnings and session/loss records
IF `OTHER.kind = "Gambling"`
Lane: individual_return_or_workpaper
Support: Gambling winnings and session/loss records [OTHER.doc_gambling]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### OTHER.repayment — Repayment and claim-of-right evidence
IF `OTHER.repaid = true`
Lane: individual_return_or_workpaper
Support: Repayment and claim-of-right evidence [OTHER.doc_repayment]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### ITEMIZE.medical — Medical expense and reimbursement ledger
IF `ITEMIZE.medical = true`
Lane: individual_return_or_workpaper
Support: Medical expense and reimbursement ledger [ITEMIZE.doc_medical]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### ITEMIZE.taxes — Tax payments eligible for itemized deductions
IF `ITEMIZE.taxes = true`
Lane: individual_return_or_workpaper
Support: Tax payments eligible for itemized deductions [ITEMIZE.doc_taxes]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### ITEMIZE.mortgage — All home mortgage statements and acquisition-debt tracing
IF `ITEMIZE.mortgage = true`
Lane: individual_return_or_workpaper
Support: All home mortgage statements and acquisition-debt tracing [ITEMIZE.doc_mortgage]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### ITEMIZE.refinance — Refinance, cash-out and points history
IF `(ITEMIZE.mortgage = true AND ITEMIZE.refinance = true)`
Lane: individual_return_or_workpaper
Support: Refinance, cash-out and points history [ITEMIZE.doc_refinance]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### ITEMIZE.other — Other itemized deduction substantiation
IF `ITEMIZE.other = true`
Lane: individual_return_or_workpaper
Support: Other itemized deduction substantiation [ITEMIZE.doc_other]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### ITEMIZE.compare — Standard/itemized comparison and restrictions
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Standard/itemized comparison and restrictions [ITEMIZE.doc_compare]
Authority: [Instructions: Itemized deductions](https://www.irs.gov/instructions/i1040sca); [Publication 502: Medical expenses](https://www.irs.gov/publications/p502); [Publication 936: Mortgage interest](https://www.irs.gov/publications/p936); [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526)

### CHARITY.cash — Charitable payment and eligibility records
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Charitable payment and eligibility records [CHARITY.doc_cash]
Authority: [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

### CHARITY.carryover — Charitable carryforward schedule
IF `CHARITY.carryover = true`
Lane: individual_return_or_workpaper
Support: Charitable carryforward schedule [CHARITY.doc_carryover]
Authority: [Publication 526: Charitable contributions](https://www.irs.gov/publications/p526); [Publication 561: Donated property valuation](https://www.irs.gov/publications/p561); [Instructions: Noncash charitable contributions](https://www.irs.gov/instructions/i8283)

### CARRY.charity — Charitable deduction carryforward rollforward
IF `CARRY.charity = true`
Lane: individual_return_or_workpaper
Support: Charitable deduction carryforward rollforward [CARRY.doc_charity]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## Schedule A (Form 8936)

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### VEHICLE.credit — Clean vehicle eligibility and seller report
IF `VEHICLE.ev = true`
Lane: individual_return_or_workpaper
Support: Clean vehicle eligibility and seller report [VEHICLE.doc_credit]
Authority: [Instructions: Clean vehicle credits](https://www.irs.gov/instructions/i8936); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

## Schedule B

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### INVEST.tax_package — Collect this account’s complete tax package
IF `INVEST.taxable = true`
Lane: individual_return_or_workpaper
Support: Complete consolidated brokerage tax package [BROKER]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### INVEST.nominee — Nominee income allocation
IF `INVEST.nominee = true`
Lane: individual_return_or_workpaper
Support: Nominee income allocation [INVEST.doc_nominee]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### INVEST.bond — Bond and savings-bond detail
IF `INVEST.bond = true`
Lane: individual_return_or_workpaper
Support: Bond and savings-bond detail [INVEST.doc_bond]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### FOREIGN.accounts — Foreign financial account inventory and valuation
IF `FOREIGN.account = true`
Lane: individual_return_or_workpaper
Support: Foreign financial account inventory and valuation [FOREIGN.doc_accounts]
Authority: [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519); [Publication 54: Citizens and residents abroad](https://www.irs.gov/publications/p54); [Instructions: Specified foreign financial assets](https://www.irs.gov/instructions/i8938); [FinCEN foreign account reporting](https://www.fincen.gov/report-foreign-bank-and-financial-accounts); [Instructions: Foreign trusts and gifts](https://www.irs.gov/instructions/i3520); [Instructions: PFIC reporting](https://www.irs.gov/instructions/i8621); [Instructions: Foreign corporations](https://www.irs.gov/instructions/i5471); [Instructions: Foreign partnerships](https://www.irs.gov/instructions/i8865); [Instructions: Foreign disregarded entities and branches](https://www.irs.gov/instructions/i8858)

## Schedule C

**Assembly unit:** per business (qualified joint venture may require separate spouse schedules)

### WAGE.statutory — Statutory-employee expense routing
IF `WAGE.statutory = true`
Lane: individual_return_or_workpaper
Support: Business income and expense ledger with reconciliations [BUS_BOOKS]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### DIGITAL.income — Digital-asset income valuation records
IF `(DIGITAL.rewards = true OR DIGITAL.services = true)`
Lane: individual_return_or_workpaper
Support: Digital-asset income valuation records [DIGITAL.doc_income]
Authority: [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### BUSINESS.inventory — Inventory and cost-of-goods-sold workpaper
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.inventory = true)`
Lane: individual_return_or_workpaper
Support: Inventory and cost-of-goods-sold workpaper [BUSINESS.doc_inventory]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### BUSINESS.expenses — Business expense substantiation
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.expenses = true)`
Lane: individual_return_or_workpaper
Support: Business expense substantiation [BUSINESS.doc_expenses]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### BUSINESS.vehicle — Business vehicle log and method history
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND (BUSINESS.expenses = true AND BUSINESS.vehicle = true))`
Lane: individual_return_or_workpaper
Support: Business vehicle log and method history [BUSINESS.doc_vehicle]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.services — Short-stay and substantial-services classification
IF `RENTAL.shortstay = true`
Lane: individual_return_or_workpaper
Support: Short-stay and substantial-services classification [RENTAL.doc_services]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### OTHER.gambling — Gambling winnings and session/loss records
IF `OTHER.kind = "Gambling"`
Lane: individual_return_or_workpaper
Support: Gambling winnings and session/loss records [OTHER.doc_gambling]
Authority: [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### BUSINESS.sole_forms — Sole proprietor / qualified joint venture form review
IF `BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"]`
Lane: individual_return_or_workpaper
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## Schedule D

**Assembly unit:** return-level capital aggregation

### WAGE.equity — Equity compensation lifecycle packet
IF `WAGE.equity = true`
Lane: individual_return_or_workpaper
Support: Equity compensation lifecycle packet [WAGE.doc_equity]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525)

### INVEST.sales — Open asset-disposition inventory
IF `INVEST.sales = true`
Lane: individual_return_or_workpaper
Support: Acquisition and adjusted-basis history [BASIS]
Authority: [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### DISPOSE.sales_packet — Sale ledger and basis reconciliation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Acquisition and adjusted-basis history [BASIS]
Authority: [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 551: Property basis](https://www.irs.gov/publications/p551); [Publication 550: Investment income](https://www.irs.gov/publications/p550)

### DIGITAL.taxable_disposal — Digital-asset disposition ledger
IF `(DIGITAL.disposal = true OR DIGITAL.fee_crypto = true)`
Lane: individual_return_or_workpaper
Support: Digital-asset disposition ledger [DIGITAL.doc_taxable_disposal]
Authority: [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### RENTAL.sale — Rental property closing and disposition packet
IF `RENTAL.sold = true`
Lane: individual_return_or_workpaper
Support: Rental property closing and disposition packet [RENTAL.doc_sale]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### HOME.home_sale — Home sale proceeds and exclusion packet
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Home sale proceeds and exclusion packet [HOME.doc_home_sale]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### HOME.home_use — Home-sale special use and depreciation
IF `(HOME.rental = true OR HOME.depreciation = true)`
Lane: individual_return_or_workpaper
Support: Home-sale special use and depreciation [HOME.doc_home_use]
Authority: [Publication 523: Selling a home](https://www.irs.gov/publications/p523); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### CARRY.capital — Capital loss carryforward rollforward
IF `CARRY.capital = true`
Lane: individual_return_or_workpaper
Support: Capital loss carryforward rollforward [CARRY.doc_capital]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## Schedule E

**Assembly unit:** return-level schedule with separate properties/activities

### RENTAL.rental_packet — Property income, costs and depreciation
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Property-specific rental income and expense ledger [RENT_BOOKS]; Historical fixed-asset and depreciation schedule [DEPR]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### RENTAL.use — Rental and personal-use calendar
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Rental and personal-use calendar [RENTAL.doc_use]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### PASS.k1_packet — Complete pass-through reporting package
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Final Schedule K-1 package and all attachments [K1]
Authority: [Publication 541: Partnerships](https://www.irs.gov/publications/p541); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: S corporation shareholder basis](https://www.irs.gov/instructions/i7203); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116)

### FARM.farm — Agricultural/resource activity books and classification
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Agricultural/resource activity books and classification [FARM.doc_farm]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

### FARM.resource — Natural-resource basis and depletion packet
IF `FARM.royalty = true`
Lane: individual_return_or_workpaper
Support: Natural-resource basis and depletion packet [FARM.doc_resource]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

### CARRY.basis — Owner basis-limited loss carryforward rollforward
IF `CARRY.basis = true`
Lane: individual_return_or_workpaper
Support: Owner basis-limited loss carryforward rollforward [CARRY.doc_basis]
Authority: [Publication 17: Federal income tax](https://www.irs.gov/publications/p17); [Publication 550: Investment income](https://www.irs.gov/publications/p550); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Instructions: Qualified business income](https://www.irs.gov/instructions/i8995); [Instructions: Foreign tax credit](https://www.irs.gov/instructions/i1116); [Instructions: Alternative minimum tax](https://www.irs.gov/instructions/i6251)

## Schedule EIC

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.dependency — Person-specific dependency and support worksheet
IF `PERSON.role = "Potential dependent or supported person"`
Lane: individual_return_or_workpaper
Support: Person-specific dependency and support worksheet [PERSON.doc_dependency]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CREDITS.eic_child — Qualifying-child EIC schedule review
IF `(CREDITS.earned = true AND CREDITS.qualifying_children = true)`
Lane: individual_return_or_workpaper
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## Schedule F

**Assembly unit:** per farm business

### FARM.farm — Agricultural/resource activity books and classification
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Agricultural/resource activity books and classification [FARM.doc_farm]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

## Schedule H

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### HOUSEHOLD.classification — Household worker classification and wage history
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Household worker classification and wage history [HOUSEHOLD.doc_classification]
Authority: [Instructions: Household employment](https://www.irs.gov/instructions/i1040sh)

### HOUSEHOLD.payroll — Household payroll and prior filing packet
IF `(HOUSEHOLD.cash_wages >= 2800 OR HOUSEHOLD.quarter = true OR HOUSEHOLD.withheld = true)`
Lane: individual_return_or_workpaper
Support: Household payroll and prior filing packet [HOUSEHOLD.doc_payroll]
Authority: [Instructions: Household employment](https://www.irs.gov/instructions/i1040sh)

## Schedule J

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### FARM.averaging — Farm/fishing averaging and payments workpaper
IF `FARM.averaging = true`
Lane: individual_return_or_workpaper
Support: Farm/fishing averaging and payments workpaper [FARM.doc_averaging]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

## Schedule R

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### PERSON.disability — Benefit-specific blindness or disability support
IF `(PERSON.blind = true OR PERSON.disabled = true)`
Lane: individual_return_or_workpaper
Support: Benefit-specific blindness or disability support [PERSON.doc_disability]
Authority: [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Publication 504: Divorce and separation](https://www.irs.gov/publications/p504); [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi)

### CREDITS.elderly — Elderly/disabled credit workpaper
IF `CREDITS.elderly = true`
Lane: individual_return_or_workpaper
Support: Elderly/disabled credit workpaper [CREDITS.doc_elderly]
Authority: [Publication 596: Earned income credit](https://www.irs.gov/publications/p596); [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 501: Dependents and filing status](https://www.irs.gov/publications/p501); [Instructions: Adoption](https://www.irs.gov/instructions/i8839)

## Schedule SE

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### DIGITAL.income — Digital-asset income valuation records
IF `(DIGITAL.rewards = true OR DIGITAL.services = true)`
Lane: individual_return_or_workpaper
Support: Digital-asset income valuation records [DIGITAL.doc_income]
Authority: [IRS digital assets guidance](https://www.irs.gov/filing/digital-assets); [Instructions: Capital dispositions](https://www.irs.gov/instructions/i8949); [Publication 551: Property basis](https://www.irs.gov/publications/p551)

### RENTAL.services — Short-stay and substantial-services classification
IF `RENTAL.shortstay = true`
Lane: individual_return_or_workpaper
Support: Short-stay and substantial-services classification [RENTAL.doc_services]
Authority: [Publication 527: Residential rental property](https://www.irs.gov/publications/p527); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### FARM.farm — Agricultural/resource activity books and classification
IF `Always within this active topic`
Lane: individual_return_or_workpaper
Support: Agricultural/resource activity books and classification [FARM.doc_farm]
Authority: [Publication 225: Farming](https://www.irs.gov/publications/p225); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544); [Publication 925: Passive activity and at-risk rules](https://www.irs.gov/publications/p925)

### SPECIAL.clergy — Clergy compensation and exemption packet
IF `SPECIAL.clergy = true`
Lane: individual_return_or_workpaper
Support: Clergy compensation and exemption packet [SPECIAL.doc_clergy]
Authority: [Instructions: 1040 and Schedules 1, 1-A, 2, 3](https://www.irs.gov/instructions/i1040gi); [Publication 525: Taxable and nontaxable income](https://www.irs.gov/publications/p525); [Publication 519: U.S. tax guide for aliens](https://www.irs.gov/publications/p519)

### BUSINESS.sole_forms — Sole proprietor / qualified joint venture form review
IF `BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"]`
Lane: individual_return_or_workpaper
Support: Use the linked fact/evidence tracks and recorded eligibility decision.
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

## W-2 / W-3

**Assembly unit:** Confirm person/entity/return-level aggregation and attachment rules in the applicable instructions.

### BUSINESS.workers — Worker payments and employer reporting packet
IF `(BUSINESS.structure is one of ["Sole proprietor / disregarded single-member LLC", "Qualified joint venture candidate"] AND BUSINESS.workers = true)`
Lane: separate_obligation_or_procedure
Support: Worker payments and employer reporting packet [BUSINESS.doc_workers]
Authority: [Publication 334: Small business](https://www.irs.gov/publications/p334); [Publication 463: Travel and vehicle expenses](https://www.irs.gov/publications/p463); [Publication 587: Home office](https://www.irs.gov/publications/p587); [Publication 544: Property dispositions](https://www.irs.gov/publications/p544)

### HOUSEHOLD.payroll — Household payroll and prior filing packet
IF `(HOUSEHOLD.cash_wages >= 2800 OR HOUSEHOLD.quarter = true OR HOUSEHOLD.withheld = true)`
Lane: separate_obligation_or_procedure
Support: Household payroll and prior filing packet [HOUSEHOLD.doc_payroll]
Authority: [Instructions: Household employment](https://www.irs.gov/instructions/i1040sh)

