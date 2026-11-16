---
url: https://assets.dinari.com/audits/Audit_Hacken_231212.pdf
title: Audit_Hacken_231212.pdf
description: PDF
fetched: 2026-11-16
method: pdf
plan: read
---

| SMART     | CONTRACT     |          | CODE |
| --------- | ------------ | -------- | ---- |
| REVIEW    | AND          | SECURITY |      |
| ANALYSIS  |              | REPORT   |      |
| Customer: | Dinari       |          |      |
| Date:     | 12 December, | 2023     |      |

This report may contain confidential information about IT systems and the
intellectual property of the Customer, as well as information about
| potential | vulnerabilities | and methods | of their | exploitation. |     |
| --------- | --------------- | ----------- | -------- | ------------- | --- |
The report can be disclosed publicly after prior consent by another Party.
Any subsequent publication of this report shall be without mandatory
consent.
Document
Name Smart Contract Code Review and Security Analysis Report for Dinari
|          | Paul Fomichov | | Lead Solidity  | SC       | Auditor at | Hacken OÜ    |
| -------- | ------------- | ---------------- | -------- | ---------- | ------------ |
| Approved | By            |                  |          |            |              |
|          | Grzegorz      | Trawiński | Lead | Solidity | SC Auditor | at Hacken OÜ |
Tags
|             | ERC20, Vault |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- |
| Platform    | EVM          |     |     |     |     |
| Language    | Solidity     |     |     |     |     |
| Methodology | Link         |     |     |     |     |
Website
https://paidnetwork.com/
|     | 21.11.2023 | – Initial Review |     |     |     |
| --- | ---------- | ---------------- | --- | --- | --- |
Changelog
|     | 12.12.2023 | – Second Review |     |     |     |
| --- | ---------- | --------------- | --- | --- | --- |
www.hacken.io
2

| Table        |          | of           | contents   |         |               |        |               |         |     |
| ------------ | -------- | ------------ | ---------- | ------- | ------------- | ------ | ------------- | ------- | --- |
| Introduction |          |              |            |         |               |        |               |         | 4   |
| System       | Overview |              |            |         |               |        |               |         | 4   |
| Executive    |          | Summary      |            |         |               |        |               |         | 6   |
| Risks        |          |              |            |         |               |        |               |         | 7   |
| Findings     |          |              |            |         |               |        |               |         | 8   |
|              | Critical |              |            |         |               |        |               |         | 8   |
|              | High     |              |            |         |               |        |               |         | 8   |
|              | H01.     | Any          | Address    | Can     | Be Restricted |        | by Privileged | Account | 8   |
|              | H02.     | Unrestricted |            | Locking |               | of the | xdShare       |         | 9   |
|              | Medium   |              |            |         |               |        |               |         | 10  |
|              | M01.     | Lack         | of Minimal |         | Threshold     | for    | Distribution  | Entity  | 10  |
M02. Unrestricted DISTRIBUTOR_ROLE in DividendDistribution 10
|     | Low |     |     |     |     |     |     |     | 11  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L01. Undocumented Functionality - Changing of USDC Token Address 11
|     | L02.          | Roles   | Documentation |           | Mismatch |            |               |     | 11  |
| --- | ------------- | ------- | ------------- | --------- | -------- | ---------- | ------------- | --- | --- |
|     | Informational |         |               |           |          |            |               |     | 12  |
|     | I01.          | Missing | Zero-Address  |           |          | Validation | for Addresses |     | 12  |
|     | I02.          | Owner   | Role          | is Not    | Used     |            |               |     | 12  |
|     | I03.          | CEI     | Pattern       | Violation |          |            |               |     | 12  |
|     | I04.          | Unused  | Import        |           |          |            |               |     | 13  |
I05. Solidity Style Guide Violation - Contract Naming Conventions Violation
13
| Disclaimers |               |             |        |             |     |     |     |     | 14  |
| ----------- | ------------- | ----------- | ------ | ----------- | --- | --- | --- | --- | --- |
| Appendix    |               | 1. Severity |        | Definitions |     |     |     |     | 15  |
|             | Risk Levels   |             |        |             |     |     |     |     | 15  |
|             | Impact        | Levels      |        |             |     |     |     |     | 16  |
|             | Likelihood    |             | Levels |             |     |     |     |     | 16  |
|             | Informational |             |        |             |     |     |     |     | 16  |
| Appendix    |               | 2. Scope    |        |             |     |     |     |     | 17  |
www.hacken.io
3

Introduction
Hacken OÜ (Consultant) was contracted by Dinari (Customer) to conduct a
Smart Contract Code Review and Security Analysis. This report presents the
findings of the security assessment of the Customer's smart contracts.
System Overview
Dinari is a Decentralized Stock Trading Platform and a Smart Wallet for
| buying liquidities |     | called | dShares: |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
● DShare — a contract that is used by Dual Distributor for representing
| the ERC20-supporting |     |     | liquidities |     | of  | the protocol. |     |     |     |     |
| -------------------- | --- | --- | ----------- | --- | --- | ------------- | --- | --- | --- | --- |
● XDShare — a contract used as a wrapper over DShare token and as a
| reinvestment |     | token. |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
● TransferRestrictor — a contract holding the logic for restricting an
unrestricting access to the protocol financial operations with the
| use of               | a blacklist |     | mapping. |     |          |         |     |          |     |     |
| -------------------- | ----------- | --- | -------- | --- | -------- | ------- | --- | -------- | --- | --- |
| DividendDistribution |             |     | —        | a   | contract | holding |     | the data | for | the |
●
distributions (payments in USDC) and functions creating, executing or
| reclaiming | them. |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
● DualDistributor — a contract wrapping the distribution logic for both
dShares and USDCs, using DividentDistribution for the latter.
| Privileged | roles           |            |             |         |               |                    |      |               |         |     |
| ---------- | --------------- | ---------- | ----------- | ------- | ------------- | ------------------ | ---- | ------------- | ------- | --- |
| ●          | The owner       | of         | the dShare  |         | contract      | can:               |      |               |         |     |
|            | ○ Set           | the        | name,       | symbol  | and           | transferRestrictor |      |               | address | of  |
|            | the             | liquidity. |             |         |               |                    |      |               |         |     |
|            | ○ Grant         |            | and revoke  |         | roles.        |                    |      |               |         |     |
| ●          | The MINTER_ROLE |            | of          | the     | DShare        | contract           | can: |               |         |     |
|            | ○ Mint          | new        | tokens      | without |               | restrictions.      |      |               |         |     |
| ●          | The BURNER_ROLE |            | of          | the     | DShare        | contract           | can: |               |         |     |
|            | ○ Burn          | tokens     |             | without | restrictions. |                    |      |               |         |     |
| ●          | The owner       | of         | the XDShare |         | contract      | can:               |      |               |         |     |
|            | ○ Lock          | and        | unlock      | the     | Contract      | without            |      | restrictions. |         |     |
● The RESTRICTOR_ROLE of the TransferRestrictor contract can:
|     | ○ Can |     | restrict |     | (blacklist) |     | any | address |     | without |
| --- | ----- | --- | -------- | --- | ----------- | --- | --- | ------- | --- | ------- |
restrictions.
● The DISTRIBUTOR_ROLE of the DividendDistribution contract can:
|     | ○ Can                | create, |     | execute        | and                 | reclaim | distributions. |          |      |     |
| --- | -------------------- | ------- | --- | -------------- | ------------------- | ------- | -------------- | -------- | ---- | --- |
| ●   | The DISTRIBUTOR_ROLE |         |     | of             | the DualDistributor |         |                | contract | can: |     |
|     | Can                  | execute |     | distributions. |                     |         |                |          |      |     |
○
● The DEFAULT_ADMIN_ROLE of the DualDistributor contract can:
|     | ○ Set    | the | address |     | of            | the | DividentDistribution |     |     | Smart |
| --- | -------- | --- | ------- | --- | ------------- | --- | -------------------- | --- | --- | ----- |
|     | Contract |     | without |     | restrictions. |     |                      |     |     |       |
www.hacken.io
4

| ○ Set | the XDShare | (extension | and | reinvestment | token) for |
| ----- | ----------- | ---------- | --- | ------------ | ---------- |
| any   | dShare.     |            |     |              |            |
● The DEFAULT_ADMIN_ROLE of the DividendDistributioncontract can:
| ○ Manage | all other | roles | if the Smart | Contract. |     |
| -------- | --------- | ----- | ------------ | --------- | --- |
www.hacken.io
5

| Executive |     | Summary |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The score measurement details can be found in the corresponding section of
| the scoring   |               | methodology. |           |              |                |           |          |            |        |      |        |
| ------------- | ------------- | ------------ | --------- | ------------ | -------------- | --------- | -------- | ---------- | ------ | ---- | ------ |
| Documentation |               | quality      |           |              |                |           |          |            |        |      |        |
| The total     | Documentation |              |           | Quality      | score          | is 10     | out      | of 10.     |        |      |        |
|               | ○             | Functional   |           | requirements |                | are       | provided |            | in the | form | of the |
|               |               | protocol’s   |           | website.     |                |           |          |            |        |      |        |
| ●             | Technical     | description  |           |              | is partially   | provided. |          |            |        |      |        |
|               | ○             | NatSpec      | comments  |              | are provided.  |           |          |            |        |      |        |
|               | ○             | Project      | technical |              | specifications |           | are      | extensive. |        |      |        |
Code quality
| The total | Code            | Quality |             | score | is 10 | out of      | 10. |     |     |     |     |
| --------- | --------------- | ------- | ----------- | ----- | ----- | ----------- | --- | --- | --- | --- | --- |
| ●         | The development |         | environment |       | is    | configured. |     |     |     |     |     |
Test coverage
| Code coverage |            | of       | the project |              | is 100.0% | (branch  | coverage)%. |      |        |     |     |
| ------------- | ---------- | -------- | ----------- | ------------ | --------- | -------- | ----------- | ---- | ------ | --- | --- |
| ●             | Deployment |          | and user    | interactions |           | are      | covered     | with | tests. |     |     |
| ●             | Some       | negative | scenarios   |              | are not   | covered. |             |      |        |     |     |
| Security      | score      |          |             |              |           |          |             |      |        |     |     |
As a result of the audit, the code contains no issues. The security score
| is 10     | out of | 10. |               |     |        |            |     |          |     |     |     |
| --------- | ------ | --- | ------------- | --- | ------ | ---------- | --- | -------- | --- | --- | --- |
| All found | issues |     | are displayed |     | in the | “Findings” |     | section. |     |     |     |
Summary
According to the assessment, the Customer's smart contract has the
following score: 10.0. The system users should acknowledge all the risks
| summed | up in | the | risks | section | of the | report. |     |     |     |     |     |
| ------ | ----- | --- | ----- | ------- | ------ | ------- | --- | --- | --- | --- | --- |
Table.Thedistributionofissuesduringtheaudit
| Review      | date |      |     | Low |     | Medium |     |     | High | Critical |     |
| ----------- | ---- | ---- | --- | --- | --- | ------ | --- | --- | ---- | -------- | --- |
| 21 November |      | 2023 |     |     | 2   |        | 2   |     | 2    |          | 0   |
| 12 December |      | 2023 |     |     | 0   |        | 0   |     | 0    |          | 0   |
www.hacken.io
6

Risks
● The RESTRICTOR_ROLE can restrict any address from financial
operations inside the protocol for the purpose of AML policies.
● The protocol is highly centralized, with any financial operations
being entitled only to privileged roles of the protocol.
www.hacken.io
7

Findings
Critical
| No  | critical | severity |     | issues |     | were | found. |     |     |
| --- | -------- | -------- | --- | ------ | --- | ---- | ------ | --- | --- |
High
| H01. Any   | Address | Can | Be     | Restricted |     | by  | Privileged | Account |     |
| ---------- | ------- | --- | ------ | ---------- | --- | --- | ---------- | ------- | --- |
| Impact     |         |     | Medium |            |     |     |            |         |     |
| Likelihood |         |     | High   |            |     |     |            |         |     |
The role of RESTRICTOR_ROLE, essentially representing the Protocol
Administrator, grants the capability to impose restrictions on any
| address |     | without |     | necessitating |     |     | prior | conditions. | This action |
| ------- | --- | ------- | --- | ------------- | --- | --- | ----- | ----------- | ----------- |
effectively results in the immobilization of user funds. It is
imperative to furnish comprehensive documentation elucidating the
necessity and intended use cases for this particular functionality.
function _beforeTokenTransfer(address from, address to, uint256) internal view
| override |     | {              |            |         |          |                       |     |               |        |
| -------- | --- | -------------- | ---------- | ------- | -------- | --------------------- | --- | ------------- | ------ |
|          |     | // Apply       | underlying |         | transfer | restrictions          |     | to this vault | token. |
|          |     | xdShareStorage |            | storage | $ =      | _getxdShareStorage(); |     |               |        |
ITransferRestrictor restrictor = $._underlyingDShare.transferRestrictor();
|     |     | if (address(restrictor)               |     |     | !=  | address(0)) | {   |      |     |
| --- | --- | ------------------------------------- | --- | --- | --- | ----------- | --- | ---- | --- |
|     |     | restrictor.requireNotRestricted(from, |     |     |     |             |     | to); |     |
}
}
| Path:  | ./src/TransferRestrictor.sol |           |     |      |        |     | : restrict() |     |     |
| ------ | ---------------------------- | --------- | --- | ---- | ------ | --- | ------------ | --- | --- |
| Proof  | of                           | Concept:  |     |      |        |     |              |     |     |
| 1. The | user                         | purchases |     | some | amount | of  | dShares.     |     |     |
2. The protocol administrator adds the user’s address to the blacklist
| by  | calling | restrict() |     | function. |     |     |     |     |     |
| --- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
3. Both the user’s stablecoins and dShares are locked inside the
protocol until the administrator has unrestricted the user’s address.
www.hacken.io
8

Recommendation: Clearly document the specific use cases and scenarios
where the RESTRICTOR_ROLE is intended to impose restrictions on user
addresses. This documentation should outline the legitimate reasons
| and          | protocols |                                          | for employing         |     | this functionality. |              |     |     |                 |          |
| ------------ | --------- | ---------------------------------------- | --------------------- | --- | ------------------- | ------------ | --- | --- | --------------- | -------- |
| Found        | in:       | 65162eb0fc00225622c6965ad638c00d1db29e42 |                       |     |                     |              |     |     |                 |          |
| Status:      | Fixed     |                                          |                       |     |                     |              |     |     |                 |          |
| Remediation: |           |                                          | Documentation         |     | now                 | mentions     |     | the | RESTRICTOR_ROLE |          |
| privileges:  |           |                                          | “The RESTRICTOR_ROLE, |     |                     | representing |     |     | the             | protocol |
compliance administrators, possesses the authority to blacklist
addresses, effectively restricting their ability to engage in
| transactions      |     | with | Dinari  | tokens.”. |         |     |     |     |     |     |
| ----------------- | --- | ---- | ------- | --------- | ------- | --- | --- | --- | --- | --- |
| H02. Unrestricted |     |      | Locking | of the    | xdShare |     |     |     |     |     |
| Impact            |     |      | Medium  |           |         |     |     |     |     |     |
| Likelihood        |     |      | High    |           |         |     |     |     |     |     |
The xdShare Smart Contract allows for arbitrary locking at any given
| moment | through |     | the | invocation | of  | the | lock() |     | function | by the |
| ------ | ------- | --- | --- | ---------- | --- | --- | ------ | --- | -------- | ------ |
Contract's owner. This effectively locks the whole distribution
functionality inside the DualDistributor, as it reverts in case of
| xdShare | being |     | locked. |     |     |     |     |     |     |     |
| ------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
function distribute(address dShare, uint256 usdcAmount, uint256 dShareAmount,
| uint256 | endTime) |     |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
external
onlyRole(DISTRIBUTOR_ROLE)
returns (uint256)
{
|        | address                            | xdShare       | = dShareToXdShare[dShare]; |        |                       |            |                       |         |     |     |
| ------ | ---------------------------------- | ------------- | -------------------------- | ------ | --------------------- | ---------- | --------------------- | ------- | --- | --- |
|        | if (xdShare                        |               | == address(0))             |        | revert ZeroAddress(); |            |                       |         |     |     |
|        | if (!IxdShare(xdShare).isLocked()) |               |                            |        |                       | revert     | XdshareIsNotLocked(); |         |     |     |
| Path:  | ./src/dividend/xdShare.sol         |               |                            |        | :                     | lock()     |                       |         |     |     |
| Proof  | of Concept:                        |               |                            |        |                       |            |                       |         |     |     |
| 1. The | user purchases                     |               | some                       | amount | of dShares.           |            |                       |         |     |     |
| 2. The | protocol                           | administrator |                            | locks  | that                  | particular |                       | dShare. |     |     |
3. Both the user’s stablecoins and dShares are locked inside the
protocol until the administrator has unrestricted the user’s address.
www.hacken.io
9

Recommendation: Document the cases for locking functionality clearly
| in      | the contract's |                                          | documentation. |       |     |          |     |     |         |
| ------- | -------------- | ---------------------------------------- | -------------- | ----- | --- | -------- | --- | --- | ------- |
| Found   | in:            | 65162eb0fc00225622c6965ad638c00d1db29e42 |                |       |     |          |     |     |         |
| Status: |                |                                          |                | Fixed |     | (Revised |     |     | commit: |
afccda3cf1f705df3e31fe6b0771a864b7d31668)
| Remediation: |     | Removed |     | lock | check. |     |     |     |     |
| ------------ | --- | ------- | --- | ---- | ------ | --- | --- | --- | --- |
Medium
| M01. Lack  | of Minimal |     | Threshold |     | for Distribution |     | Entity |     |     |
| ---------- | ---------- | --- | --------- | --- | ---------------- | --- | ------ | --- | --- |
| Impact     |            |     | Low       |     |                  |     |        |     |     |
| Likelihood |            |     | Medium    |     |                  |     |        |     |     |
It is possible to create a distribution that ends in the very next
block. When combined with the reclaimDistribution() function, this
can potentially open avenues for manipulations of distributions by
| entities | possessing |     |     | the | DISTRIBUTOR_ROLE. |     |     |     |     |
| -------- | ---------- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
Path: ./src/dividend/DividendDistribution.sol : createDistribution()
Recommendation: Implement a validation check within the distribution
creation process to ensure that the end time of a distribution is set
to a future block timestamp. This check should prevent the creation
of distributions that end in the same block or in the very next
block.
| By            | introducing |                                          | this   |            | validation, | the      | risk | of manipulative |         |
| ------------- | ----------- | ---------------------------------------- | ------ | ---------- | ----------- | -------- | ---- | --------------- | ------- |
| distributions |             |                                          | can be | mitigated. |             |          |      |                 |         |
| Found         | in:         | 65162eb0fc00225622c6965ad638c00d1db29e42 |        |            |             |          |      |                 |         |
| Status:       |             |                                          |        | Fixed      |             | (Revised |      |                 | commit: |
77f660e9c79cac042d73ef0b3b683bc7c0f2dcb1)
Remediation: Minimum gap between block.timestamp and distribution
time was added. This gap is 1 day by default, but can be changed by
| the               | DEFAULT_ADMIN_ROLE |     |                  | with | emitting | an event.            |     |     |     |
| ----------------- | ------------------ | --- | ---------------- | ---- | -------- | -------------------- | --- | --- | --- |
| M02. Unrestricted |                    |     | DISTRIBUTOR_ROLE |      | in       | DividendDistribution |     |     |     |
| Impact            |                    |     | Medium           |      |          |                      |     |     |     |
| Likelihood        |                    |     | High             |      |          |                      |     |     |     |
The DISTRIBUTOR_ROLE within the DividendDistribution Smart Contract
possesses unrestricted authority to disburse funds to any recipient
without the presence of checks or imposed restrictions within the
www.hacken.io
10

Distribution struct. This can lead to the protocol sending funds to
| the   | wrong recipients                        |         | by  | mistake |              | or intention. |     |           |              |     |          |     |
| ----- | --------------------------------------- | ------- | --- | ------- | ------------ | ------------- | --- | --------- | ------------ | --- | -------- | --- |
| Path: | ./src/dividend/DividendDistribution.sol |         |     |         |              |               |     | :         | distribute() |     |          |     |
| Proof | of Concept:                             |         |     |         |              |               |     |           |              |     |          |     |
|       | 1. The user                             | expects |     | a       | distribution |               |     | according | to           | the | protocol |     |
rules.
2. The protocol owner sends to a third party address or omits
sending the distribution to the given recipient for an unknown
|     | duration | of  | time. |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Recommendation: Implement a robust access control mechanism that
restricts the DISTRIBUTOR_ROLE from sending funds without appropriate
checks and restrictions. This may involve the following steps:
● Within the Distribution struct or relevant functions, introduce
|     | comprehensive |     | validation |     |     | checks | to  | ensure | that | any | outgoing |     |
| --- | ------------- | --- | ---------- | --- | --- | ------ | --- | ------ | ---- | --- | -------- | --- |
funds meet predetermined criteria or requirements. These checks
should include verification of recipient addresses, validation
|     | of distribution |     | amounts, |            | and     | any            | other    | relevant |            | conditions.   |        |     |
| --- | --------------- | --- | -------- | ---------- | ------- | -------------- | -------- | -------- | ---------- | ------------- | ------ | --- |
|     | ● Document      | the | access   |            | control |                | policies | and      | validation |               | checks |     |
|     | clearly         | in  | the      | contract's |         | documentation. |          |          | This       | documentation |        |     |
should outline the specific criteria that need to be met for a
|                  | distribution                                 |       | to be | executed.     |     |         |            |           |     |     |        |     |
| ---------------- | -------------------------------------------- | ----- | ----- | ------------- | --- | ------- | ---------- | --------- | --- | --- | ------ | --- |
| Found            | in: 65162eb0fc00225622c6965ad638c00d1db29e42 |       |       |               |     |         |            |           |     |     |        |     |
| Status:          | Fixed                                        |       |       |               |     |         |            |           |     |     |        |     |
| Remediation:     |                                              | Added |       | documentation |     |         | justifying |           | the |     | design | of  |
| DISTRIBUTOR_ROLE |                                              | both  | in    | docs          | and | NatSpec |            | comments. |     |     |        |     |
Low
L01. Undocumented Functionality - Changing of USDC Token Address
| Impact     |     |     | Low |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Likelihood |     |     | Low |     |     |     |     |     |     |     |     |     |
The contract permits the alteration of the USDC stablecoin address;
however, the rationale behind this modification remains undocumented.
This lack of documentation introduces the possibility of a scenario
wherein the protocol's functionality may become unusable temporarily
if the token address is inadvertently set to an incorrect one or
| altered | without                            | clear | purpose. |     |     |     |     |             |     |     |     |     |
| ------- | ---------------------------------- | ----- | -------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
| Path:   | ./src/dividend/DualDistributor.sol |       |          |     |     |     |     | : setUSDC() |     |     |     |     |
Recommendation:
● Document the purpose and intended use cases for the ability to
change the USDC stablecoin address within the contract. Provide
www.hacken.io
11

clear explanations in the contract's documentation regarding
when and why such changes might be necessary.
● Add an event emittance in case of USDC address change.
Found in: 65162eb0fc00225622c6965ad638c00d1db29e42
Status: Fixed (Revised commit:
d9cec3672883a02e77e819b92923bd5ac0234b10)
Remediation: Stable coin address is removed from state variables and
is now passed directly to the method.
L02. Roles Documentation Mismatch
Impact Low
Likelihood Low
The statement "Maintains a single owner who can add or remove
accounts from isBlacklisted" is made in the contract documentation.
However, in the current implementation, the owner does not possess
any privileges in this regard. Instead, the RESTRICTOR_ROLE
exclusively holds the authority to restrict user access.
Path: ./src/TransferRestrictor.sol
Recommendation: Update the contract documentation to accurately
reflect the implemented access control and functionality.
Found in: 65162eb0fc00225622c6965ad638c00d1db29e42
Status: Fixed (Revised commit:
61ff124ac5db8c5903da8cd3ba2a0235ada15d42)
Remediation: NatSpec comments now correctly reflect the roles
privileges: “Maintains the `RESTRICTOR_ROLE  who can add or remove
accounts from `isBlacklisted`”.
Informational
I01. Missing Zero-Address Validation for Addresses
It is possible to call the constructor and the initialization
function with zero address, which can lead to an unintended behavior
of the Smart Contracts.
Paths: ./src/dividend/DividendDistribution.sol : constructor();
src/dividend/xdShare.sol: initialize()
Recommendation: Implement a zero-address validation check to prevent
the Smart Contract from being initialized with zero addresses.
Status: Fixed (Revised commit:
62313de20cb35e82f91dc5d534d8d1408c8a4a26)
Remediation: Zero-address validation is now added.
www.hacken.io
12

| I02. Owner | Role  | is        | Not | Used      |     |     |       |                |     |     |
| ---------- | ----- | --------- | --- | --------- | --- | --- | ----- | -------------- | --- | --- |
| The        | Smart | Contracts |     | implement |     | an  | Owner | role; however, | it  | is  |
noteworthy that this role does not possess any additional privileges
beyond the default ones provided by the OpenZeppelin library.
| Paths: |     |     |     |     | ./src/dividend/DividendDistribution.sol; |     |     |     |     |     |
| ------ | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
./src/TransferRestrictor.sol
Recommendation: Remove redundant roles in the Smart Contracts.
| Found   | in:   | 65162eb0fc00225622c6965ad638c00d1db29e42 |     |     |     |     |     |     |     |     |
| ------- | ----- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status: | Fixed |                                          |     |     |     |     |     |     |     |     |
Remediation: Documentation now mentions the DEFAULT_ADMIN_ROLE
| privileges |         | of managing |     | other | roles | of  | the Smart | Contract. |     |     |
| ---------- | ------- | ----------- | --- | ----- | ----- | --- | --------- | --------- | --- | --- |
| I03. CEI   | Pattern | Violation   |     |       |       |     |           |           |     |     |
The Smart Contracts deviate from the CEI (Check-Effects-Interaction)
pattern on multiple occasions, initially emitting an event and
| subsequently                       |     | updating |                                         | the           | Smart | Contract               | state.       |     |     |     |
| ---------------------------------- | --- | -------- | --------------------------------------- | ------------- | ----- | ---------------------- | ------------ | --- | --- | --- |
| Paths:                             |     |          | ./src/dividend/DividendDistribution.sol |               |       |                        |              |     |     | :   |
| createDistribution(),              |     |          |                                         | distribute(), |       | reclaimDistribution(); |              |     |     |     |
| ./src/dividend/DualDistributor.sol |     |          |                                         |               |       | :                      | distribute() |     |     |     |
Recommendation: To align with best practices and enhance code
readability and security, it is recommended to refactor the Smart
Contracts to adhere to the CEI (Check-Effect-Interact) pattern
consistently. This pattern ensures that state changes occur before
emitting events, reducing the potential for unexpected behavior and
providing a clear sequence of operations within the contracts.
| Status: |     |     |     | Fixed |     |     | (Revised |     | commit: |     |
| ------- | --- | --- | --- | ----- | --- | --- | -------- | --- | ------- | --- |
83a128513532961a94fe4272b0002d7fbefbff20)
Remediation: Event emittance was rearranged in order to conform with
| CEI         | pattern. |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I04. Unused | Import   |     |     |     |     |     |     |     |     |     |
The Smart Contract imports ReentrancyGuard, although it is not
| utilized |                            | anywhere | within | the | contract. |     |     |     |     |     |
| -------- | -------------------------- | -------- | ------ | --- | --------- | --- | --- | --- | --- | --- |
| Path:    | ./src/dividend/xdShare.sol |          |        |     |           |     |     |     |     |     |
www.hacken.io
13

Recommendation: To optimize the contract and reduce unnecessary
dependencies, it is recommended to remove the import statement for
ReentrancyGuard if it is not being utilized in the contract's
functions or logic. This removal will streamline the contract code
| and enhance | its                                      | clarity | by eliminating | unused   | imports. |         |
| ----------- | ---------------------------------------- | ------- | -------------- | -------- | -------- | ------- |
| Found in:   | 65162eb0fc00225622c6965ad638c00d1db29e42 |         |                |          |          |         |
| Status:     |                                          |         | Fixed          | (Revised |          | commit: |
8b589f7ae39845b005197ef10a280939ec4e3f3c)
| Remediation: | Redundant |     | imports are | now removed. |     |     |
| ------------ | --------- | --- | ----------- | ------------ | --- | --- |
I05. Solidity Style Guide Violation - Contract Naming Conventions
Violation
Solidity follows a naming convention where smart contracts are
typically named using CamelCase with the first letter capitalized.
| Using lowercase |     | letters | for | smart contract | names can | lead to |
| --------------- | --- | ------- | --- | -------------- | --------- | ------- |
confusion and is not in compliance with the Solidity style guide.
| Paths: ./src/dividend/xdShare.sol; |     |     |     | ./src/dShare.sol |     |     |
| ---------------------------------- | --- | --- | --- | ---------------- | --- | --- |
Recommendation: It is recommended to rename the smart contract using
CamelCase with the first letter capitalized. This will enhance code
| readability | and                                      | align | with industry | standards. |     |         |
| ----------- | ---------------------------------------- | ----- | ------------- | ---------- | --- | ------- |
| Found in:   | 65162eb0fc00225622c6965ad638c00d1db29e42 |       |               |            |     |         |
| Status:     |                                          |       | Fixed         | (Revised   |     | commit: |
3c02dbaa453ce46ac19eb35a267b8c8854df7223)
| Remediation: | Contract |     | is now renamed | to DShare. |     |     |
| ------------ | -------- | --- | -------------- | ---------- | --- | --- |
www.hacken.io
14

Disclaimers
Hacken Disclaimer
The smart contracts given for audit have been analyzed based on best
industry practices at the time of the writing of this report, with
cybersecurity vulnerabilities and issues in smart contract source code, the
details of which are disclosed in this report (Source Code); the Source
Code compilation, deployment, and functionality (performing the intended
functions).
The report contains no statements or warranties on the identification of
all vulnerabilities and security of the code. The report covers the code
submitted and reviewed, so it may not be relevant after any modifications.
Do not consider this report as a final and sufficient assessment regarding
the utility and safety of the code, bug-free status, or any other contract
statements.
While we have done our best in conducting the analysis and producing this
report, it is important to note that you should not rely on this report
only — we recommend proceeding with several independent audits and a public
bug bounty program to ensure the security of smart contracts.
English is the original language of the report. The Consultant is not
responsible for the correctness of the translated versions.
Technical Disclaimer
Smart contracts are deployed and executed on a blockchain platform. The
platform, its programming language, and other software related to the smart
contract can have vulnerabilities that can lead to hacks. Thus, the
Consultant cannot guarantee the explicit security of the audited smart
contracts.
www.hacken.io
15

| Appendix |     | 1.  | Severity |     | Definitions |     |     |     |     |
| -------- | --- | --- | -------- | --- | ----------- | --- | --- | --- | --- |
When auditing smart contracts Hacken is using a risk-based approach that
considers the potential impact of any vulnerabilities and the likelihood of
them being exploited. The matrix of impact and likelihood is a commonly
used tool in risk management to help assess and prioritize risks.
The impact of a vulnerability refers to the potential harm that could
result if it were to be exploited. For smart contracts, this could include
the loss of funds or assets, unauthorized access or control, or
| reputational |     | damage. |     |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
The likelihood of a vulnerability being exploited is determined by
considering the likelihood of an attack occurring, the level of skill or
resources required to exploit the vulnerability, and the presence of any
mitigating controls that could reduce the likelihood of exploitation.
|        | Risk       | Level |     | High     | Impact |     | Medium | Impact | Low Impact |
| ------ | ---------- | ----- | --- | -------- | ------ | --- | ------ | ------ | ---------- |
| High   | Likelihood |       |     | Critical |        |     |        | High   | Medium     |
| Medium | Likelihood |       |     |          | High   |     |        | Medium | Low        |
| Low    | Likelihood |       |     |          | Medium |     |        | Low    | Low        |
Risk Levels
Critical: Critical vulnerabilities are usually straightforward to exploit
and can lead to the loss of user funds or contract state manipulation.
High: High vulnerabilities are usually harder to exploit, requiring
specific conditions, or have a more limited scope, but can still lead to
| the | loss | of user | funds | or contract |     | state | manipulation. |     |     |
| --- | ---- | ------- | ----- | ----------- | --- | ----- | ------------- | --- | --- |
Medium: Medium vulnerabilities are usually limited to state manipulations
and, in most cases, cannot lead to asset loss. Contradictions and
requirements violations. Major deviations from best practices are also in
this category.
Low: Major deviations from best practices or major Gas inefficiency. These
issues will not have a significant impact on code execution, do not affect
| security |     | score but | can | affect | code | quality | score. |     |     |
| -------- | --- | --------- | --- | ------ | ---- | ------- | ------ | --- | --- |
www.hacken.io
16

Impact Levels
High Impact: Risks that have a high impact are associated with financial
losses, reputational damage, or major alterations to contract state. High
impact issues typically involve invalid calculations, denial of service,
token supply manipulation, and data consistency, but are not limited to
those categories.
Medium Impact: Risks that have a medium impact could result in financial
losses, reputational damage, or minor contract state manipulation. These
risks can also be associated with undocumented behavior or violations of
requirements.
Low Impact: Risks that have a low impact cannot lead to financial losses or
state manipulation. These risks are typically related to unscalable
functionality, contradictions, inconsistent data, or major violations of
best practices.
Likelihood Levels
High Likelihood: Risks that have a high likelihood are those that are
expected to occur frequently or are very likely to occur. These risks could
be the result of known vulnerabilities or weaknesses in the contract, or
could be the result of external factors such as attacks or exploits
targeting similar contracts.
Medium Likelihood: Risks that have a medium likelihood are those that are
possible but not as likely to occur as those in the high likelihood
category. These risks could be the result of less severe vulnerabilities or
weaknesses in the contract, or could be the result of less targeted attacks
or exploits.
Low Likelihood: Risks that have a low likelihood are those that are
unlikely to occur, but still possible. These risks could be the result of
very specific or complex vulnerabilities or weaknesses in the contract, or
could be the result of highly targeted attacks or exploits.
Informational
Informational issues are mostly connected to violations of best practices,
typos in code, violations of code style, and dead or redundant code.
Informational issues are not affecting the score, but addressing them will
be beneficial for the project.
www.hacken.io
17

Appendix 2. Scope
The scope of the project includes the following smart contracts from the
provided repository:
Initial review scope
Repository https://github.com/dinaricrypto/sbt-contracts
Commit 65162eb0fc00225622c6965ad638c00d1db29e42
Whitepaper Not Provided
Requirements https://docs.dinari.com/user-guide/wallet-basics
Technical
Not Provided
Requirements
Contracts dShare.sol
IdShare.sol
ITransferRestrictor.sol
TransferRestrictor.sol
dividend/DividendDistribution.sol
dividend/DualDistributor.sol
dividend/IDividendDistributor.sol
dividend/IxdShare.sol
dividend/xdShare.sol
Second review scope
Repository https://github.com/dinaricrypto/sbt-contracts
Commit 77f660e9c79cac042d73ef0b3b683bc7c0f2dcb1
Whitepaper Not Provided
Requirements https://docs.dinari.com/user-guide/wallet-basics
Technical
https://docs.dinari.com/architecture/overview/
Requirements
Contracts DShare.sol
IDShare.sol
ITransferRestrictor.sol
TransferRestrictor.sol
dividend/DividendDistribution.sol
www.hacken.io
18

dividend/DualDistributor.sol
dividend/IDividendDistributor.sol
dividend/XDShare.sol
www.hacken.io
19