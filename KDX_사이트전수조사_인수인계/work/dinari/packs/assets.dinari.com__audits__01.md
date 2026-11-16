# 읽기 묶음: assets.dinari.com / audits (1/1)


<<<PAGE https://assets.dinari.com/audits/Audit_Sherlock_230811.pdf>>>
---
url: https://assets.dinari.com/audits/Audit_Sherlock_230811.pdf
title: Audit_Sherlock_230811.pdf
description: PDF
fetched: 2026-11-16
method: pdf
plan: read
---

| SHERLOCK       |         | SECURITY |               | REVIEW | FOR |
| -------------- | ------- | -------- | ------------- | ------ | --- |
| Prepared       | for:    | Dinari   |               |        |     |
| Prepared       | by:     | Sherlock |               |        |     |
| Lead Security  | Expert: |          |               |        |     |
| Dates Audited: |         | July 3   | - July 6,2023 |        |     |
| Prepared       | on:     | August   | 11,2023       |        |     |

Introduction
Dinari securities backed tokens (dShares) provide direct exposure to the world’s
| most trusted |     | assets | such as | Google | and Apple | shares. |     |
| ------------ | --- | ------ | ------- | ------ | --------- | ------- | --- |
Scope
| Repository: | dinaricrypto/sbt-contracts               |        |     |             |          |     |     |
| ----------- | ---------------------------------------- | ------ | --- | ----------- | -------- | --- | --- |
| Branch:     | main                                     |        |     |             |          |     |     |
| Commit:     | 6d36760def25449c3f35f6ed38128a7eaf352903 |        |     |             |          |     |     |
| For the     | detailed                                 | scope, | see | the contest | details. |     |     |
Findings
| Each issue | has | an assigned |     | severity: |     |     |     |
| ---------- | --- | ----------- | --- | --------- | --- | --- | --- |
• Medium issues are security vulnerabilities that may not be directly exploitable
or may require certain conditions in order to be exploited. All major issues
| should | be  | addressed. |     |     |     |     |     |
| ------ | --- | ---------- | --- | --- | --- | --- | --- |
• High issues are directly exploitable security vulnerabilities that need to be
fixed.
| Issues     | found   |        |                 |          |              |     |          |
| ---------- | ------- | ------ | --------------- | -------- | ------------ | --- | -------- |
|            |         | Medium |                 |          |              |     | High     |
|            |         |        | 3               |          |              |     | 1        |
| Issues     | not     | fixed  | or acknowledged |          |              |     |          |
|            |         | Medium |                 |          |              |     | High     |
|            |         |        | 1               |          |              |     | 0        |
| Security   | experts |        | who found       |          | valid issues |     |          |
| volodya    |         |        |                 | ast3ros  |              |     | toshii   |
| ArmedGoose |         |        |                 | p-tsanev |              |     | chainNue |
| dirk_y     |         |        |                 | ctf_sec  |              |     | 0x007    |
| Kodyvim    |         |        |                 | hals     |              |     | bin2chen |
1

| Delvir0       | shtesesamoubiq | james_wu |
| ------------- | -------------- | -------- |
| osmanozdemir1 | bitsurfer      |          |
2

| Issue     |     | H-1: | Bypass |     | the | blacklist |      | restriction | because    | the |
| --------- | --- | ---- | ------ | --- | --- | --------- | ---- | ----------- | ---------- | --- |
| blacklist |     |      | check  | is  | not | done      | when | minting     | or burning |     |
Source: https://github.com/sherlock-audit/2023-06-dinari-judging/issues/64
| Found    |     | by      |           |     |        |     |     |     |     |     |
| -------- | --- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- |
| ctf_sec, |     | dirk_y, | p-tsanev, |     | toshii |     |     |     |     |     |
Summary
Bypass the blacklist restriction because the blacklist check is not done when
| minting       |     | or burning |        |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Vulnerability |     |            | Detail |     |     |     |     |     |     |     |
In the whitepaper:
the protocol emphasis that they implement a blacklist feature for
enforcing OFAC, AML and other account security requirements A
|     | blacklisted |     | will | not able | to  | send | or receive | tokens |     |     |
| --- | ----------- | --- | ---- | -------- | --- | ---- | ---------- | ------ | --- | --- |
the protocol want to use the whitelist feature to be compliant to not let the
| blacklisted |     | address |     | send | or receive | dSahres |     |     |     |     |
| ----------- | --- | ------- | --- | ---- | ---------- | ------- | --- | --- | --- | --- |
For this reason, before token transfer, the protocol check if address from or address
to is blacklisted and the blacklisted address can still create buy order or sell order
function _beforeTokenTransfer(address from, address to, uint256) internal
| ,!  | virtual |              | override | {       |     |             |     |         |     |     |
| --- | ------- | ------------ | -------- | ------- | --- | ----------- | --- | ------- | --- | --- |
|     | //      | Restrictions |          | ignored |     | for minting | and | burning |     |     |
// If transferRestrictor is not set, no restrictions are applied
|     | //  | @audit |       |         |       |      |          |               |     |     |
| --- | --- | ------ | ----- | ------- | ----- | ---- | -------- | ------------- | --- | --- |
|     | //  | why    | don't | you not | apply | mint | and burn | in blacklist? |     |     |
if (from == address(0) || to == address(0) || address(transferRestrictor)
| ,!  | ==  | address(0)) |     | {   |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
return;
}
|     | //                                            | Check | transfer | restrictions |     |     |     |      |     |     |
| --- | --------------------------------------------- | ----- | -------- | ------------ | --- | --- | --- | ---- | --- | --- |
|     | transferRestrictor.requireNotRestricted(from, |       |          |              |     |     |     | to); |     |     |
}
this is calling
3

function requireNotRestricted(address from, address to) external view virtual {
| // Check            | if either | account           | is restricted |     |
| ------------------- | --------- | ----------------- | ------------- | --- |
| if (blacklist[from] |           | || blacklist[to]) |               | {   |
revert AccountRestricted();
}
| // Otherwise, | do  | nothing |     |     |
| ------------- | --- | ------- | --- | --- |
}
but as we can see, when the dShare token is burned or minted, the blacklist does
| not apply | to address(to) |     |     |     |
| --------- | -------------- | --- | --- | --- |
this allows the blacklisted receiver to bypass the blacklist restriction and still send
| and receive | dShares | and cash out | their | dShares |
| ----------- | ------- | ------------ | ----- | ------- |
becausethemintingdSharesisnotblacklisted
a blacklisted user create a buy order with payment token and set the order receiver
| to a non-blacklisted | address |     |     |     |
| -------------------- | ------- | --- | --- | --- |
then later when the buy order is filled, the new dShares is transferred and minted
| to an not-blacklisted |     | address |     |     |
| --------------------- | --- | ------- | --- | --- |
becausetheburningdSharesisnotblacklisted
before the user is blacklisted, a user can frontrun the blacklist transaction to create
a sell order and transfer the dShares into the OrderProcessor
then later when the sell order is filled, the dShares in burnt from the SellOrderProce
ss escrow are burnt and the user can receive the payment token
Impact
Bypass the blacklist restriction because the blacklist check is not done when
| minting or   | burning |     |     |     |
| ------------ | ------- | --- | --- | --- |
| Code Snippet |         |     |     |     |
https://github.com/sherlock-audit/2023-06-dinari/blob/4851cb7ebc86a7bc26b8d
0d399a7dd7f9520f393/sbt-contracts/src/issuer/SellOrderProcessor.sol#L88
https://github.com/sherlock-audit/2023-06-dinari/blob/4851cb7ebc86a7bc26b8d
0d399a7dd7f9520f393/sbt-contracts/src/issuer/SellOrderProcessor.sol#L115
Tool used
| Manual Review |     |     |     |     |
| ------------- | --- | --- | --- | --- |
4

Recommendation
implement proper check when burning and minting of the dShares to not let user
game the blacklist system, checking if the receiver of the dShares is blacklisted
when minting, before filling sell order and burn the dShares, check if the requestor
| of the sell | order is blacklisted |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
do not let blacklisted address create buy order and sell order
Discussion
jaketimothy
Fixes for this should be considered in combination with #55 as it creates more
| opportunities | for locking | up orders. |     |     |
| ------------- | ----------- | ---------- | --- | --- |
jaketimothy
Fixed in
• https://github.com/dinaricrypto/sbt-contracts/pull/126
• https://github.com/dinaricrypto/sbt-contracts/pull/131
ctf-sec
| PR #131 | fix goods good |     |     |     |
| ------- | -------------- | --- | --- | --- |
PR #126 only fix only check if the recipient or requestor is blocklisted by the asset
token transferRestrictor
if (
BridgedERC20(orderRequest.assetToken).isBlacklisted(orderRequest.recipient)
,!
|| BridgedERC20(orderRequest.assetToken).isBlacklisted(msg.sender)
| )   | revert Blacklist(); |     |     |     |
| --- | ------------------- | --- | --- | --- |
the protocol may want to consider checking if the orderRequest.recipient or
| msg.sender | is blocklisted | by the payment | token | as well |
| ---------- | -------------- | -------------- | ----- | ------- |
jaketimothy
| Additional | blacklist checks | in  |     |     |
| ---------- | ---------------- | --- | --- | --- |
• https://github.com/dinaricrypto/sbt-contracts/pull/164
ctf-sec
| Fix looks | good! |     |     |     |
| --------- | ----- | --- | --- | --- |
5

| Issue  | M-1: In | case   | of stock | split and    | reverse    | split, the |
| ------ | ------- | ------ | -------- | ------------ | ---------- | ---------- |
| Dshare | token   | holder | will     | gain or loss | his Dshare | token      |
value
Source: https://github.com/sherlock-audit/2023-06-dinari-judging/issues/29
| Found | by  |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
ast3ros
Summary
Stock split and reverse split may cause the token accounting to be inaccurate.
| Vulnerability | Detail |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- |
Stock split and reverse split are very common in the stock market. There are many
examples here: https://companiesmarketcap.com/amazon/stock-splits/
For instance, in a 2-for-1 stock split, a shareholder receives an additional share for
each share held. However, the DShare token holder still holds only one DShare
token after the split. If a DShare token holder owns 100 DShare tokens before the
split, he will still own 100 DShare tokens after the split. However, he should own
| 200 DShare | tokens | after the | split. |     |     |     |
| ---------- | ------ | --------- | ------ | --- | --- | --- |
Currently, users can buy 1 DShare token at the current market price of the
| underlying | share. | https://sbt.dinari.com/tokens |     |     |     |     |
| ---------- | ------ | ----------------------------- | --- | --- | --- | --- |
This means that after the stock split, a new Dshare token holder can buy a Dshare
at half the price of the previous Dshare token holder. This is unfair to the previous
Dshare token holder. In other words, the original Dshare token holder will lose 50%
| of his   | Dshare token  | value after | the stock | split. |     |     |
| -------- | ------------- | ----------- | --------- | ------ | --- | --- |
| The same | logic applies | to stock    | reverse   | split. |     |     |
Impact
The Dshare token holder will gain or loss his Dshare token value after the stock split
| or reverse | split.  |     |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- | --- |
| Code       | Snippet |     |     |     |     |     |
https://github.com/sherlock-audit/2023-06-dinari/blob/50eb49260ab54e02748c2
f6382fd95284d271f06/sbt-contracts/src/BridgedERC20.sol#L13
6

Tool used
Manual Review
Recommendation
The Operator should have a mechanism to mint or burn DShare tokens of holders
when the underlying share is split or reverse split.
Discussion
jaketimothy
While this would be catastrophic if unaddressed, our current - admittedly
undocumented - approach is to halt and cancel all orders for assets at the end of
the day the split is announced. Then deploy a new token with a burn->mint
migration contract at the appropriate split ratio, add the new token to the issuers,
and re-enable orders with the new token.
This accounts for various scenarios where the original tokens may be locked in
other contracts without Dinari having to push airdrop transactions for every split -
or maintaining burn privileges on all owners/holders.
ctf-sec
The amazon last stock split is 20 years ago. I think this report is out of scope
The Operator should have a mechanism to mint or burn DShare tokens of
holders when the underlying share is split or reverse split.
The operator is a privileged central party that can do that.
Oot2k
I still think this issue is valid. Stock splits happen fairly often, for example Tesla in
2020 and 2022. I think this is a valid medium, because the offchain system was not
mentioned anywhere and there still can be issues when deploying a token
manually. There wont be direct loss of funds, but protocols that integrate with
dinari will have problems (Dex, lending etc.)
ctf-sec
While the stock and offline logic is out of scope,
In 2-for-1 stock split, a shareholder receives an additional share for each
share held
In the current implementation, this would require the admin mint stock for user
In a stock reverse split,
In the current implementation, admin can't burn stock for user
7

function burn(uint256 value) external virtual onlyRole(BURNER_ROLE) {
|     |     | _burn(msg.sender, |     |     | value); |     |     |     |
| --- | --- | ----------------- | --- | --- | ------- | --- | --- | --- |
}
| if       | the implementation    |              |     | is    |         |        |          |         |
| -------- | --------------------- | ------------ | --- | ----- | ------- | ------ | -------- | ------- |
| function |                       | burn(address |     | from, | uint256 | value) | external | virtual |
|          | onlyRole(BURNER_ROLE) |              |     |       | {       |        |          |         |
,!
|     |     | _burn(from, | value); |     |     |     |     |     |
| --- | --- | ----------- | ------- | --- | --- | --- | --- | --- |
}
I would agree this is a low severity and out of scope finding,
| but  | since | the      | admin   | can't | actually | burn for user, |     |         |
| ---- | ----- | -------- | ------- | ----- | -------- | -------------- | --- | ------- |
| this | can   | be valid | medium, |       | severity | is definitely  | not | high :) |
thangtranth
Escalate
| I believe |     | this issue | is  | a high | severity | because: |     |     |
| --------- | --- | ---------- | --- | ------ | -------- | -------- | --- | --- |
• Impact: As the sponsor mentioned, the impact is catastrophic if unaddressed.
It breaks the invariant 1 share : 1 token of the protocol. Some token holders
will unfairly lose/gain X times the value. In addition, protocols that integrate
with Dinari will have problems. It is not considered an acceptable risk
• Frequency: Stock splits and reverse splits are very common events. Because
Dinari covers many publicly traded securities, not just one stock, the
frequency of the events should be counted using the whole stock market, not
frequency of one stock. There are events happening every month.
https://www.marketbeat.com/stock-splits/history/
• The mechanism that the sponsor mentioned was not available anywhere
during the contest: from the contest README to the white paper. It is new
|     | information |     | that | came | after | the contest | was | finished. |
| --- | ----------- | --- | ---- | ---- | ----- | ----------- | --- | --------- |
• As the lead Watson pointed out, even the workaround of owner minting and
burning directly to users does not work, because the admin cannot burn other
users’ tokens. And I don’t think using the mint and burn functions in the token
contract and minting manually to each user is a good solution.
sherlock-admin
Escalate
|     | I   | believe | this issue | is  | a high | severity because: |     |     |
| --- | --- | ------- | ---------- | --- | ------ | ----------------- | --- | --- |
8

• Impact: As the sponsor mentioned, the impact is catastrophic if
unaddressed. It breaks the invariant 1 share : 1 token of the protocol.
Some token holders will unfairly lose/gain X times the value. In
addition, protocols that integrate with Dinari will have problems. It is
| not | considered | an acceptable |     | risk |     |
| --- | ---------- | ------------- | --- | ---- | --- |
• Frequency: Stock splits and reverse splits are very common events.
Because Dinari covers many publicly traded securities, not just one
stock, the frequency of the events should be counted using the
whole stock market, not frequency of one stock. There are events
| happening |     | every month. |     |     |     |
| --------- | --- | ------------ | --- | --- | --- |
https://www.marketbeat.com/stock-splits/history/
| • The | mechanism | that | the sponsor | mentioned | was not available |
| ----- | --------- | ---- | ----------- | --------- | ----------------- |
anywhere during the contest: from the contest README to the white
paper. It is new information that came after the contest was finished.
• As the lead Watson pointed out, even the workaround of owner
minting and burning directly to users does not work, because the
admin cannot burn other users’ tokens. And I don’t think using the
mint and burn functions in the token contract and minting manually
| to             | each user | is a good   | solution. |     |     |
| -------------- | --------- | ----------- | --------- | --- | --- |
| You've created | a valid   | escalation! |           |     |     |
To remove the escalation from consideration: Delete your comment.
You may delete or edit your escalation comment anytime before the 48-hour
escalation window closes. After that, the escalation becomes final.
ctf-sec
Escalate
| I believe | this issue | is a high | severity | because: |     |
| --------- | ---------- | --------- | -------- | -------- | --- |
• Impact: As the sponsor mentioned, the impact is catastrophic if
unaddressed. It breaks the invariant 1 share : 1 token of the protocol.
Some token holders will unfairly lose/gain X times the value. In
addition, protocols that integrate with Dinari will have problems. It is
| not | considered | an acceptable |     | risk |     |
| --- | ---------- | ------------- | --- | ---- | --- |
• Frequency: Stock splits and reverse splits are very common events.
Because Dinari covers many publicly traded securities, not just one
stock, the frequency of the events should be counted using the
whole stock market, not frequency of one stock. There are events
| happening |     | every month. |     |     |     |
| --------- | --- | ------------ | --- | --- | --- |
https://www.marketbeat.com/stock-splits/history/
| • The | mechanism | that | the sponsor | mentioned | was not available |
| ----- | --------- | ---- | ----------- | --------- | ----------------- |
anywhere during the contest: from the contest README to the white
9

paper. It is new information that came after the contest was finished.
• As the lead Watson pointed out, even the workaround of owner
minting and burning directly to users does not work, because the
admin cannot burn other users’ tokens. And I don’t think using the
mint and burn functions in the token contract and minting manually
to each user is a good solution.
I find it difficult to think this is a high severity issue, stock just don't split every day.
How does the sponsor handle the stock split is not in scope of auditing, severity at
most medium if not out of scope, we could say, if the stock company rug and
delisted, all dShare lose its value... this is expected, which is not in scope of the
auditing as well
https://docs.sherlock.xyz/audits/judging/judging
Medium: There is a viable scenario (even if unlikely) that could cause the
protocol to enter a state where a material amount of funds can be lost.
The attack path is possible with assumptions that either mimic on-chain
conditions or reflect conditions that have a reasonable chance of
becoming true in the future.
and
As the lead Watson pointed out, even the workaround of owner minting
and burning directly to users does not work, because the admin cannot
burn other users’ tokens. And I don’t think using the mint and burn
functions in the token contract and minting manually to each user is a
good solution
there is no mention about this in the original report
and
I really feel like not dispute as low and out of scope and argue a medium is already
what I can do the best for this report because this report does show creativity.
https://www.marketplace.org/2022/02/11/whats-a-stock-split-anyway/
10

ctf-sec
btw the while the resolving the escalation is one story, the fix is another.
@jaketimothy
| Maybe | can use this |     |     |
| ----- | ------------ | --- | --- |
https://docs.openzeppelin.com/contracts/3.x/api/token/erc20#ERC20Snapshot
Implement as rebasing token to modify the ERC20 token balance can help as well!
| Agree this | is not a easy | fix. |     |
| ---------- | ------------- | ---- | --- |
jaketimothy
Thank you for sharing @ctf-sec. I'm racking my brain trying to avoid rebasing token.
Oot2k
Stocksplits are known well in advance, so trading can be haltet and shares
converted. I still think all offchain fixes are not recommended which means this is a
| valid medium | issue. |     |     |
| ------------ | ------ | --- | --- |
jaketimothy
Fixed in
• https://github.com/dinaricrypto/sbt-contracts/pull/135
hrishibhat
Result: Medium Unique Given that this is an external condition that is well-known
beforehand. This issue can be fairly considered a valid medium because the code
cannot handle the stock-split situation and the off-chain/on-chain solutions were
| not previously | present. |     |     |
| -------------- | -------- | --- | --- |
sherlock-admin2
| Escalations | have been | resolved | successfully! |
| ----------- | --------- | -------- | ------------- |
11

Escalation status:
• thangtranth: rejected
12

| IssueM-2: |     |      | Escrowrecordnotclearedoncancellationand |     |     |     |     |     |     |     |
| --------- | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| order     |     | fill |                                         |     |     |     |     |     |     |     |
Source: https://github.com/sherlock-audit/2023-06-dinari-judging/issues/56
| Found | by  |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Delvir0, bin2chen, bitsurfer, chainNue, ctf_sec, dirk_y, hals, volodya
Summary
In DirectBuyIssuer.sol, a market buy requires the operator to take the payment
token as escrow prior to filling the order. Checks are in place so that the math
works out in terms of how much escrow has been taken vs the order's remaining fill
amount. However, if the user cancels the order or fill the order, the escrow record is
not cleared.
The escrow record will exists as a positive amount which can lead to accounting
issues.
| Vulnerability |     |           | Detail   |     |     |     |     |     |     |     |
| ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Take          | the | following | example: |     |     |     |     |     |     |     |
• Operator broadcasts a takeEscrow() transaction around the same time that
|     | the        | user calls    | requestCancel() |             |     | for the       | order  |              |     |              |
| --- | ---------- | ------------- | --------------- | ----------- | --- | ------------- | ------ | ------------ | --- | ------------ |
|     | • Operator | also          | broadcasts      |             | a   | cancelOrder() |        | transaction  |     |              |
|     | • If the   |               |                 | transaction |     | is mined      | before | the          |     | transaction, |
|     |            | cancelOrder() |                 |             |     |               |        | takeEscrow() |     |              |
then the contract will transfer out token when it should not be able to.
|              |               | simply | checks  |     | that | the                     |     |     | is less | than or equal |
| ------------ | ------------- | ------ | ------- | --- | ---- | ----------------------- | --- | --- | ------- | ------------- |
| takeEscrow() |               |        |         |     |      | getOrderEscrow[orderId] |     |     |         |               |
| to           | the requested |        | amount: |     |      |                         |     |     |         |               |
bytes32 orderId = getOrderIdFromOrderRequest(orderRequest, salt);
| uint256                 |                      | escrow    | = getOrderEscrow[orderId]; |                         |                   |           |     |          |     |     |
| ----------------------- | -------------------- | --------- | -------------------------- | ----------------------- | ----------------- | --------- | --- | -------- | --- | --- |
| if                      | (amount              | > escrow) |                            | revert                  | AmountTooLarge(); |           |     |          |     |     |
| //                      | Update               | escrow    | tracking                   |                         |                   |           |     |          |     |     |
| getOrderEscrow[orderId] |                      |           |                            | = escrow                |                   | - amount; |     |          |     |     |
| //                      | Notify               | escrow    | taken                      |                         |                   |           |     |          |     |     |
| emit                    | EscrowTaken(orderId, |           |                            | orderRequest.recipient, |                   |           |     | amount); |     |     |
13

| //  | Take | escrowed | payment |     |     |     |     |     |
| --- | ---- | -------- | ------- | --- | --- | --- | --- | --- |
IERC20(orderRequest.paymentToken).safeTransfer(msg.sender, amount);
| Cancelling |     | the | order does | not | clear | the |     | record: |
| ---------- | --- | --- | ---------- | --- | ----- | --- | --- | ------- |
getOrderEscrow
function _cancelOrderAccounting(OrderRequest calldata order, bytes32
|     | orderId, | OrderState |     | memory | orderState) |     |     |     |
| --- | -------- | ---------- | --- | ------ | ----------- | --- | --- | --- |
,!
internal
virtual
override
{
// Prohibit cancel if escrowed payment has been taken and not returned
|     | ,! or | filled  |        |                            |     |     |     |     |
| --- | ----- | ------- | ------ | -------------------------- | --- | --- | --- | --- |
|     |       | uint256 | escrow | = getOrderEscrow[orderId]; |     |     |     |     |
if (orderState.remainingOrder != escrow) revert UnreturnedEscrow();
|     |     | // Standard                         | buy | order | accounting |     |          |              |
| --- | --- | ----------------------------------- | --- | ----- | ---------- | --- | -------- | ------------ |
|     |     | super._cancelOrderAccounting(order, |     |       |            |     | orderId, | orderState); |
}
}
This can lead to an good-faith and trusted operator accidentally taking funds from
| the | contract | that | should | not | be able | to leave. |     |     |
| --- | -------- | ---- | ------ | --- | ------- | --------- | --- | --- |
coming up with the fact that the transaction does not have deadline or expiration
date:
| consider |                 | the case | below:   |     |        |              |            |     |
| -------- | --------------- | -------- | -------- | --- | ------ | ------------ | ---------- | --- |
|          | 1. a good-faith |          | operator |     | send a | transaction, | takeEscrow |     |
2. the transaction is pending in the mempool for a long long long time
|     | 3. then   | user       | fire a cancel |               | order  | request   |       |     |
| --- | --------- | ---------- | ------------- | ------------- | ------ | --------- | ----- | --- |
|     | 4. the    | operator   | help          | user          | cancel | the order |       |     |
|     | 5. the    | operator   | send          | a transcation |        | cancel    | order |     |
|     | 6. cancel | order      | transaction   |               | land   | first     |       |     |
|     | 7. the    | takeEscrow |               | transaction   |        | lands     |       |     |
because escrow state is not clear up, the fund (other user's fund) is taken
It's also worth noting that the operator would not be able to call returnEscrow()
because the order state has already been cleared by the cancellation.
| getRemainingOrder() |     |     |     | would | return | 0.  |     |     |
| ------------------- | --- | --- | --- | ----- | ------ | --- | --- | --- |
14

function returnEscrow(OrderRequest calldata orderRequest, bytes32 salt, uint256
amount)
,!
external
onlyRole(OPERATOR_ROLE)
{
|     | // No      | nonsense    |        |              |        |     |     |
| --- | ---------- | ----------- | ------ | ------------ | ------ | --- | --- |
|     | if (amount | == 0)       | revert | ZeroValue(); |        |     |     |
|     | // Can     | only return | unused |              | amount |     |     |
bytes32 orderId = getOrderIdFromOrderRequest(orderRequest, salt);
|     | uint256   | remainingOrder |                          | = getRemainingOrder(orderId); |       |             |        |
| --- | --------- | -------------- | ------------------------ | ----------------------------- | ----- | ----------- | ------ |
|     | uint256   | escrow =       | getOrderEscrow[orderId]; |                               |       |             |        |
|     | // Unused | amount         | = remaining              |                               | order | - remaining | escrow |
if (escrow + amount > remainingOrder) revert AmountTooLarge();
Impact
• Insolvency due to pulling escrow that should not be allowed to be taken
| Code | Snippet |     |     |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- | --- | --- |
https://github.com/sherlock-audit/2023-06-dinari/blob/4851cb7ebc86a7bc26b8d
0d399a7dd7f9520f393/sbt-contracts/src/issuer/DirectBuyIssuer.sol#L130-L142
Tool used
| Manual | Review |     |     |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- | --- | --- |
Recommendation
| Clear | the | escrow record | upon | canceling |     | the order. |     |
| ----- | --- | ------------- | ---- | --------- | --- | ---------- | --- |
Discussion
jaketimothy
Fixed in
• https://github.com/dinaricrypto/sbt-contracts/pull/122
ctf-sec
| The | fix reset | the escrow | balance |     | after | cancelling |     |
| --- | --------- | ---------- | ------- | --- | ----- | ---------- | --- |
the protocol may want to consider handling the escrow accounting properly when
the order is filled as well (such as reset the escrow balance to 0)
jaketimothy
15

| The fix reset | the escrow | balance after | cancelling |
| ------------- | ---------- | ------------- | ---------- |
the protocol may want to consider handling the escrow accounting
properly when the order is filled as well (such as reset the escrow
| balance to | 0)  |     |     |
| ---------- | --- | --- | --- |
Because the escrow must be taken before filling, the escrow balance will always be
| zero after total | fulfillment. |     |     |
| ---------------- | ------------ | --- | --- |
ctf-sec
| ok, then fix looks | good |     |     |
| ------------------ | ---- | --- | --- |
16

| Issue |     | M-3:     | Cancellation |     |           | refunds | should | return | tokens | to  |
| ----- | --- | -------- | ------------ | --- | --------- | ------- | ------ | ------ | ------ | --- |
| order |     | creator, |              | not | recipient |         |        |        |        |     |
Source: https://github.com/sherlock-audit/2023-06-dinari-judging/issues/61
| Found |     | by  |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0x007, ArmedGoose, Kodyvim, ctf_sec, dirk_y, james_wu, osmanozdemir1,
shtesesamoubiq
Summary
When an order is cancelled, the refund is sent to instead of the
order.recipient
order creator because it is the order creator (requestor) pay the payment token for
| buy | order | or pay | the | dShares | for | sell order |     |     |     |     |
| --- | ----- | ------ | --- | ------- | --- | ---------- | --- | --- | --- | --- |
As is the standard in many L1/L2 bridges, cancelled deposits should be returned to
the order creator instead of the recipient. In Dinari's current implementation, a
| refund        |     | acts as | a transfer | with | a middle-man. |     |     |     |     |     |
| ------------- | --- | ------- | ---------- | ---- | ------------- | --- | --- | --- | --- | --- |
| Vulnerability |     |         | Detail     |      |               |     |     |     |     |     |
Simply, the _cancelOrderAccounting() function returns the refund to the
order.recipient:
function _cancelOrderAccounting(OrderRequest calldata orderRequest, bytes32
|     | orderId, |     | OrderState | memory | orderState) |     |     |     |     |     |
| --- | -------- | --- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- |
,!
internal
virtual
override
{
...
|     | uint256 | refund |     | = orderState.remainingOrder |     |     | +   |     |     |     |
| --- | ------- | ------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
feeState.remainingPercentageFees;
,!
...
if (refund + feeState.feesEarned == orderRequest.quantityIn) {
|     |     | _closeOrder(orderId, |                            |              | orderRequest.paymentToken, |              |      | 0); |     |     |
| --- | --- | -------------------- | -------------------------- | ------------ | -------------------------- | ------------ | ---- | --- | --- | --- |
|     |     | // Refund            |                            | full payment |                            |              |      |     |     |     |
|     |     | refund               | = orderRequest.quantityIn; |              |                            |              |      |     |     |     |
|     | }   | else {               |                            |              |                            |              |      |     |     |     |
|     |     | // Otherwise         |                            | close        | order                      | and transfer | fees |     |     |     |
_closeOrder(orderId, orderRequest.paymentToken, feeState.feesEarned);
}
17

| //  | Return | escrow |     |     |
| --- | ------ | ------ | --- | --- |
IERC20(orderRequest.paymentToken).safeTransfer(orderRequest.recipient,
refund);
,!
}
Refunds should be returned to the order creator in cases where the input recipient
was an incorrect address or simply the user changed their mind prior to the order
being filled.
Impact
| • Potential |         | for irreversible | loss of funds |     |
| ----------- | ------- | ---------------- | ------------- | --- |
| • Inability |         | to truly cancel  | order         |     |
| Code        | Snippet |                  |               |     |
https://github.com/sherlock-audit/2023-06-dinari/blob/4851cb7ebc86a7bc26b8d
0d399a7dd7f9520f393/sbt-contracts/src/issuer/BuyOrderIssuer.sol#L193-L215
Tool used
| Manual | Review |     |     |     |
| ------ | ------ | --- | --- | --- |
Recommendation
| Return | the | funds to the order | creator, not | the recipient. |
| ------ | --- | ------------------ | ------------ | -------------- |
Discussion
bizzyvinci
Escalate
This issue ought to be high because it doesn't require external conditions or
specific states for users to lose a significant amount. It is very likely that
msg.sender
cause msg.sender and recipient could be different entities trying to
!= recipient
have a deal either EOA-EOA or contract-EOA or contract-contract. Canceling order
| is meant | to  | be a | as mentioned | by the sponsor. |
| -------- | --- | ---- | ------------ | --------------- |
perfectunwind
This issue affects every single cancelled order, both buy, direct buy and sell orders.
sherlock-admin
Escalate
18

This issue ought to be high because it doesn't require external conditions
or specific states for users to lose a significant amount. It is very likely
that msg.sender != recipient cause msg.sender and recipient could be
different entities trying to have a deal either EOA-EOA or contract-EOA
or contract-contract. Canceling order is meant to be a perfectunwind
| as  | mentioned | by the sponsor. |     |     |
| --- | --------- | --------------- | --- | --- |
This issue affects every single cancelled order, both buy, direct buy and
| sell | orders. |     |     |     |
| ---- | ------- | --- | --- | --- |
The escalation could not be created because you are not exceeding the escalation
threshold.
You can view the required number of additional valid issues/judging contest
| payouts | in your Profile | page, in the | Sherlock | webapp. |
| ------- | --------------- | ------------ | -------- | ------- |
jaketimothy
Fixed in
• https://github.com/dinaricrypto/sbt-contracts/pull/117
ctf-sec
| Fix looks | good |     |     |     |
| --------- | ---- | --- | --- | --- |
19

<<<PAGE https://assets.dinari.com/audits/Audit_Hacken_241230.pdf>>>
---
url: https://assets.dinari.com/audits/Audit_Hacken_241230.pdf
title: Audit_Hacken_241230.pdf
description: PDF
fetched: 2026-11-16
method: pdf
plan: read
---

Smart Contract Code
Review And Security
Analysis Report
Customer: Dinari SA
Date: 30/12/2024

We express our gratitude to the Dinari SA team for the collaborative engagement that
enabled the execution of this Smart Contract Security Assessment.
Dinari Securities Backed Tokens (dShares) provide direct exposure to the world's most trusted
assets such as Google and Apple shares.
Document
Smart Contract Code Review and Security Analysis Report for Dinari
Name
SA
Audited By Stepan Chekhovskoi
Approved By Przemyslaw Swiatowiec
Website https://dinari.com
Changelog 12/12/2024 - Preliminary Report
30/12/2024 - Second Report
Platform Plume
Language Solidity
Tags Vault, DeFi
Methodology https://hackenio.cc/sc_methodology
Review Scope
Repository https://github.com/dinaricrypto/sbt-contracts
Initial Commit 1fa1a298373cefc252694984640db62d8f3a6b33
Second Commit d327ea9a6fc5f86caf73769dd1983b5333e774b8
2

Audit Summary
The system users should acknowledge all the risks summed up in the risks section of the
report
| 1              | 0        | 1        | 0         |
| -------------- | -------- | -------- | --------- |
| Total Findings | Resolved | Accepted | Mitigated |
Findings by Severity
Severity Count
Critical 0
High 0
Medium 1
Low 0

| Vulnerability |     |     | Severity |
| ------------- | --- | --- | -------- |
F-2024-7639 - Possibly Invalid Swap Rate due to Using Unreliable Market Price Medium
3

Documentation quality
Functional Requirements are partially missed.
Technical Description is provided.
Code quality
The code architecture is clean and easy to read.
The development environment is configured.
While the NatSpec comments mention OrderProcessor provides price with 18 decimals, the
calculations imply 36 - dShare.decimals().
The OracleLib functionality does not revert transaction in case of overflow and returns zero.
Test coverage
Code coverage of the project is 74% (branch coverage).
Deployment and basic user interactions are covered with tests.
Negative cases coverage is partially missed.
4

Table of Contents
System Overview 6
Privileged Roles 6
Potential Risks 7
Findings 8
Vulnerability Details 8
Observation Details 10
Disclaimers 12
Appendix 1. Definitions 13
Severities 13
Potential Risks 13
Appendix 2. Scope 14
Appendix 3. Additional Valuables 15

System Overview
DinariAdapterToken is a vault contract developed to use ETF dShare as one of liquid assets in
Plume Nest money market.
The vault is built on top of out-of-scope ComponentToken contract - ERC-4626 Vault with ERC-7540
and ERC-7575 extensions.
The contract integrates external OrderProcessor used to exchange vault asset token to dShare
and back.
Implemented functionality:
convertToShares, convertToAssets - ComponentToken overrides provide info on the vault rate based
on conversion rate from OrderProcessor,
requestDeposit, requestRedeem - asynchronous vault deposit and redeem processing funds
through the OrderProcessor,
processSubmittedOrders, processNextSubmittedOrder - functions to validate if the OrderProcessor have
executed the submitted requests.
Privileged roles
The system is designed to work exclusively with Nest Staking.
The system owner can upgrade the contract.
6

Potential Risks
System Reliance on External Contracts: The functioning of the system significantly
relies on Order Processor and Nest Staking external contracts. Any flaws or vulnerabilities
in these contracts adversely affect the audited project, potentially leading to security
breaches or loss of funds.
Dependency on External Logic for Implemented Logic: The DinariAdapterToken logic
highly depends on ComponentToken external contract not covered by the audit. This reliance
introduces risks if these external contracts are compromised or contain vulnerabilities,
affecting the audited project's integrity.
Dynamic Array Iteration Gas Limit Risks: The processSubmittedOrders iterates over large
dynamic arrays, which leads to excessive Gas costs, risking denial of service due to out-of-
gas errors, alternative processNextSubmittedOrder function can be used to process requests
one-by-one.
Single Points of Failure and Control: The project is mostly centralized, introducing
single points of failure and control. This centralization can lead to vulnerabilities in
decision-making and operational processes, making the system more susceptible to
targeted attacks or manipulation.
Flexibility and Risk in Contract Upgrades: The project's contracts are upgradeable,
allowing the administrator to update the contract logic at any time. While this provides
flexibility in addressing issues and evolving the project, it also introduces risks if upgrade
processes are not properly managed or secured, potentially allowing for unauthorized
changes that could compromise the project's integrity and security.
Token Decimals Reliance: The system relies on the dShare token has 18 decimals.
Missing the invariant may cause inconsistencies in price decimals calculation leading to
the price interpreted incorrectly breaking the conversion rate.
Zero Output in Case of Overflow: The system returns zero shares in exchange for
assets or zero assets in exchange for shares in case overflow happens in internal price
calculations. Consider simulate transaction before executing to avoid the edge cases.
7

Findings
Vulnerability Details
F-2024-7639 - Possibly Invalid Swap Rate due to Using Unreliable
Market Price - Medium
Description: The latestFillPrice function over external OrderProcessor contract is
used for calculations in the convertToShares and convertToAssets
functions.
The latestFillPrice function is documented with get the latest fill price
for a token pair what means it returns latest market data. Latest
market data is supposed to on-chain price manipulations as it is a
temporary value. To guarantee price consistency time-weighted
price should be used.
The function returns PricePoint structure of uint256 price and uint64
blocktime. The blocktime parameter is not validated causing outdated
price might be used.
This may lead to unexpectedly high amount of shares minted in the
vault inflating the vault shares value.
function convertToShares(uint256 assets) public view override(ComponentToken)
returns (uint256 shares) {
...
IOrderProcessor.PricePoint memory price = orderContract.latestFillPrice($
.dshareToken, paymentToken);
return wrappedDshareToken.convertToShares(((orderAmount + fees) * price.p
rice) / 1 ether);
}
function convertToAssets(uint256 shares) public view override(ComponentToken)
returns (uint256 assets) {
...
IOrderProcessor.PricePoint memory price = orderContract.latestFillPrice(d
shareToken, paymentToken);
...
uint256 proceeds = ((dshares / precisionReductionFactor) * precisionReduc
tionFactor * 1 ether) / price.price;
...
return proceeds - fees;
}
8

Assets:
DinariAdapterToken.sol [https://github.com/dinaricrypto/sbt-
contracts]
Status: Accepted
Classification
Impact: 3/5
Likelihood: 4/5
Exploitability: Independent
Complexity: Simple
Severity: Medium
Recommendations
Remediation: Consider integrating trusted oracle and implementing validation that
the price is not stale.
IOrderProcessor.PricePoint memory price = orderContract.latestFillPrice(dshar
eToken, paymentToken);
if (block.timestamp - price.blocktime > threshold) revert OutdatedPrice(block
.timestamp, price.blocktime);
Resolution: The Finding is partially fixed in the commit
d2af1d51230b73249acba101f76c6365e1c62689.
The _getDSharePrice function wraps the orderContract.latestFillPrice
external call with the necessary return value validations.
Usage of latestFillPrice as price source may lead to third party is able
to manipulate the conversion rate impacting the system security and
integrity. It is highly recommended to integrate or implement a
trusted Oracle to enhance the price security.
9

Observation Details
F-2024-7625 - Public Functions that Can be External - Info
Description: Functions intended to be invoked exclusively from external sources
should be designated as external rather than public.
This is essential to enhance both Gas efficiency and the overall
security of the contract.
The visibility of the following functions can be restricted from public
to external.
processNextSubmittedOrder
processSubmittedOrders
getNextSubmittedOrder
getSubmittedOrderInfo
initialize
Assets:
DinariAdapterToken.sol [https://github.com/dinaricrypto/sbt-
contracts]
Status: Fixed
Recommendations
Remediation: Consider updating functions which are exclusively utilized by
external entities from their current public visibility to external
visibility.
Resolution: The Finding is fixed in the commit a22f003e9ee21b83d349e03f6afee03ea44c5f38.
The functions visibility modifiers are changed to external.
10

F-2024-7626 - Floating Pragma - Info
Description: The contracts use floating pragma ^0.8.25.
This may result in the contracts being deployed using the wrong
pragma version, which is different from the one they were tested
with. For example, contracts might be deployed using an outdated
pragma version which may include bugs that affect the system
negatively.
Assets:
DinariAdapterToken.sol [https://github.com/dinaricrypto/sbt-
contracts]
Status: Fixed
Recommendations
Remediation: Consider locking the pragma version whenever possible and avoid
using a floating pragma in the final deployment. Consider known
bugs for the compiler version that is chosen.
Resolution: The Finding is fixed in the commit 842badab61436398c5d1dcd06c34ef30f5236786.
The compiler version in pinned to 0.8.25.
11

Disclaimers
Hacken Disclaimer
The smart contracts given for audit have been analyzed based on best industry practices at
the time of the writing of this report, with cybersecurity vulnerabilities and issues in smart
contract source code, the details of which are disclosed in this report (Source Code); the
Source Code compilation, deployment, and functionality (performing the intended functions).
The report contains no statements or warranties on the identification of all vulnerabilities and
security of the code. The report covers the code submitted and reviewed, so it may not be
relevant after any modifications. Do not consider this report as a final and sufficient
assessment regarding the utility and safety of the code, bug-free status, or any other contract
statements.
While we have done our best in conducting the analysis and producing this report, it is
important to note that you should not rely on this report only — we recommend proceeding
with several independent audits and a public bug bounty program to ensure the security of
smart contracts.
English is the original language of the report. The Consultant is not responsible for the
correctness of the translated versions.
Technical Disclaimer
Smart contracts are deployed and executed on a blockchain platform. The platform, its
programming language, and other software related to the smart contract can have
vulnerabilities that can lead to hacks. Thus, the Consultant cannot guarantee the explicit
security of the audited smart contracts.
12

Appendix 1. Definitions
Severities
When auditing smart contracts, Hacken is using a risk-based approach that considers
Likelihood, Impact, Exploitability and Complexity metrics to evaluate findings and score
severities.
Reference on how risk scoring is done is available through the repository in our Github
organization:
hknio/severity-formula
Severity Description
Critical vulnerabilities are usually straightforward to exploit and can lead to the
Critical
loss of user funds or contract state manipulation.
High vulnerabilities are usually harder to exploit, requiring specific conditions, or
High have a more limited scope, but can still lead to the loss of user funds or contract
state manipulation.
Medium vulnerabilities are usually limited to state manipulations and, in most
Medium cases, cannot lead to asset loss. Contradictions and requirements violations. Major
deviations from best practices are also in this category.
Major deviations from best practices or major Gas inefficiency. These issues will
Low
not have a significant impact on code execution.
Potential Risks
The "Potential Risks" section identifies issues that are not direct security vulnerabilities but
could still affect the project’s performance, reliability, or user trust. These risks arise from
design choices, architectural decisions, or operational practices that, while not immediately
exploitable, may lead to problems under certain conditions. Additionally, potential risks can
impact the quality of the audit itself, as they may involve external factors or components
beyond the scope of the audit, leading to incomplete assessments or oversight of key areas.
This section aims to provide a broader perspective on factors that could affect the project's
long-term security, functionality, and the comprehensiveness of the audit findings.
13

Appendix 2. Scope
The scope of the project includes the following smart contracts from the provided repository:
Scope Details
Repository https://github.com/dinaricrypto/sbt-contracts
Initial Commit 1fa1a298373cefc252694984640db62d8f3a6b33
Second Commit d327ea9a6fc5f86caf73769dd1983b5333e774b8
Whitepaper https://assets.dinari.com/forms/dinari-whitepaper.pdf
Requirements Notes shared internally
Technical Requirements README.md
Asset Type
DinariAdapterToken.sol [https://github.com/dinaricrypto/sbt-contracts] Smart Contract
14

Appendix 3. Additional Valuables
Additional Recommendations
The smart contracts in the scope of this audit could benefit from the introduction of automatic
emergency actions for critical activities, such as unauthorized operations like ownership
changes or proxy upgrades, as well as unexpected fund manipulations, including large
withdrawals or minting events. Adding such mechanisms would enable the protocol to react
automatically to unusual activity, ensuring that the contract remains secure and functions as
intended.
To improve functionality, these emergency actions could be designed to trigger under specific
conditions, such as:
Detecting changes to ownership or critical permissions.
Monitoring large or unexpected transactions and minting events.
Pausing operations when irregularities are identified.
These enhancements would provide an added layer of security, making the contract more
robust and better equipped to handle unexpected situations while maintaining smooth
operations.
15

<<<PAGE https://assets.dinari.com/audits/Audit_Hacken_231212.pdf>>>
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

<<<PAGE https://assets.dinari.com/audits/Audit_Pashov_241224.pdf>>>
---
url: https://assets.dinari.com/audits/Audit_Pashov_241224.pdf
title: Audit_Pashov_241224.pdf
description: PDF
fetched: 2026-11-16
method: pdf
plan: read
---

Dinari Security Review
Pashov Audit Group
Conducted by: 0xunforgiven, 0xCiphky, merlinboii
December 7th - December 11th

Contents
1. About Pashov Audit Group
2
2. Disclaimer
2
3. Introduction
2
4. About Dinari
2
5. Risk Classification
3
5.1. Impact
3
5.2. Likelihood
3
5.3. Action required for severity levels
4
6. Security Assessment Summary
4
7. Executive Summary
5
8. Findings
7
8.1. High Findings
7
[H-01] Incorrect handling of token decimals
7
8.2. Medium Findings
9
[M-01] rebaseMul() not working as intended
9
[M-02] Attacker can DOS privateMint()
9
[M-03] The deprecated privateMint() prone to many
10
issues
[M-04] Lack of data validation for oracle price feed
11
[M-05] Users can frontrun rebase functions
12
8.3. Low Findings
14
[L-01] Code would behave unexpectedly if the price
14
reaches 0
[L-02] Overriding function is missing "override" specifier
14
[L-03] Reducing the limit from the maximum takes the
14
full duration to replenish
[L-04] Functions do not have slippage protection
15
[L-05] burn() should round up when calculating share
16
amounts
1

1. About Pashov Audit Group
Pashov Audit Group consists of multiple teams of some of the best smart contract
security researchers in the space. Having a combined reported security
vulnerabilities count of over 1000, the group strives to create the absolute very best
audit journey possible - although 100% security can never be guaranteed, we do
guarantee the best efforts of our experienced researchers for your blockchain
protocol. Check our previous work here or reach out on Twitter @pashovkrum.
2. Disclaimer
A smart contract security review can never verify the complete absence of
vulnerabilities. This is a time, resource and expertise bound effort where we try to
find as many vulnerabilities as possible. We can not guarantee 100% security after
the review or even if the review will find any problems with your smart contracts.
Subsequent security reviews, bug bounty programs and on-chain monitoring are
strongly recommended.
3. Introduction
A time-boxed security review of the dinaricrypto/usdplus-contracts repository
was done by Pashov Audit Group, with a focus on the security aspects of the
application's smart contracts implementation.
4. About Dinari
Dinari allows users to trade tokens backed by US securities using stablecoins.
USD+ is a stablecoin backed by short-term US treasuries offering a stable value and
monthly yield distributions. The process involves minting USD+ with USDC and
redeeming it through a smart contract, with liquidity ensuring redemptions are
completed in up to 3 days.
2

5. Risk Classification
Severity Impact: High Impact: Medium Impact: Low
Likelihood: High Critical High Medium
Likelihood: Medium High Medium Low
Likelihood: Low Medium Low Low
5.1. Impact
High - leads to a significant material loss of assets in the protocol or significantly
harms a group of users.
Medium - only a small amount of funds can be lost (such as leakage of value) or a
core functionality of the protocol is affected.
Low - can lead to any kind of unexpected behavior with some of the protocol's
functionalities that's not so critical.
5.2. Likelihood
High - attack path is possible with reasonable assumptions that mimic on-chain
conditions, and the cost of the attack is relatively low compared to the amount of
funds that can be stolen or lost.
Medium - only a conditionally incentivized attack vector, but still relatively
likely.
Low - has too many or too unlikely assumptions or requires a significant stake by
the attacker with little or no incentive.
3

5.3. Action required for severity levels
Critical - Must fix as soon as possible (if already deployed)
High - Must fix (before deployment if not already deployed)
Medium - Should fix
Low - Could fix
6. Security Assessment Summary
review commit hash - 1ed01b15d1f69828d8320c5384175c30cdd14377
fixes review commit hash - 1de4ba609a7ef187c75b0e5be53da3fa73479feb
Scope
The following smart contracts were in scope of the audit:
ERC7281Min
SelfPermit
TransferRestrictor
UsdPlus
UsdPlusMinter
UsdPlusRedeemer
WrappedUsdPlus
4

7. Executive Summary
Over the course of the security review, 0xunforgiven, 0xCiphky, merlinboii engaged
with Dinari to review Dinari. In this period of time a total of 11 issues were
uncovered.
Protocol Summary
Protocol Name Dinari
Repository https://github.com/dinaricrypto/usdplus-contracts
Date December 7th - December 11th
Protocol Type Stablecoin
Findings Count
Severity Amount
High 1
Medium 5
Low 5
Total Findings 11
5

Summary of Findings
| ID     | Title                                | Severity | Status   |
| ------ | ------------------------------------ | -------- | -------- |
| [H-01] | Incorrect handling of token decimals | High     | Resolved |
| [M-01] | rebaseMul() not working as intended  | Medium   | Resolved |
| [M-02] | Attacker can DOS privateMint()       | Medium   | Resolved |
The deprecated privateMint() prone
| [M-03] |     | Medium | Resolved |
| ------ | --- | ------ | -------- |
to many issues
Lack of data validation for oracle
| [M-04] |     | Medium | Resolved |
| ------ | --- | ------ | -------- |
price feed
[M-05] Users can frontrun rebase functions Medium Acknowledged
Code would behave unexpectedly if
| [L-01] |     | Low | Resolved |
| ------ | --- | --- | -------- |
the price reaches 0
Overriding function is missing
| [L-02] |     | Low | Resolved |
| ------ | --- | --- | -------- |
"override" specifier
Reducing the limit from the
| [L-03] | maximum takes the full duration to | Low | Resolved |
| ------ | ---------------------------------- | --- | -------- |
replenish
Functions do not have slippage
| [L-04] |     | Low | Resolved |
| ------ | --- | --- | -------- |
protection
burn() should round up when
| [L-05] |     | Low | Resolved |
| ------ | --- | --- | -------- |
calculating share amounts
6

8. Findings
8.1. High Findings
[H-01] Incorrect handling of token decimals
Severity
Impact: High
Likelihood: Medium
Description
| The              |     |     | ,             |     | ,                 |  and |
| ---------------- | --- | --- | ------------- | --- | ----------------- | ---- |
| previewDeposit() |     |     | previewMint() |     | previewWithdraw() |      |
 calculate returned amounts without accounting for the
previewRedeem()
| decimals of the  |     | paymentToken |     | .   |     |     |
| ---------------- | --- | ------------ | --- | --- | --- | --- |
This can result in precision discrepancies during operations, leading to
incorrect amounts being processed.
Assume the following scenario:
| The  paymentToken |              |     |  has  18     |  decimals (e.g.,  | DAI ). |     |
| ----------------- | ------------ | --- | ------------ | ----------------- | ------ | --- |
| The  USD          | + token has  |     | 6  decimals. |                   |        |     |
Impact on using each functions:
| previewDeposit() |     |                                   | :   |     |     |           |
| ---------------- | --- | --------------------------------- | --- | --- | --- | --------- |
| The              |     |  to mint is calculated using the  |     |     |     |  decimals |
usdPlusAmount paymentToken
(18), resulting in an overestimated USD+ amount for the user (scaled up by
1e12 ).
previewMint()
The  paymentTokenAmount  required to mint is calculated using the USD+
decimals (6), causing the user to pay less than intended to mint USD+.
7

previewWithdraw()
The transaction may revert due to insufficient funds, as the returned
usdPlusAmount is calculated in 18 decimals, representing an unrealistically
large amount.
previewRedeem()
The paymentTokenAmount is tracked with the smaller USD+ decimals (6),
leading to users receiving less value than expected when their redemption is
fulfilled.
Recommendations
Consider handling accepted payment token decimals across all calculations.
8

8.2. Medium Findings
[M-01] not working as intended
rebaseMul()
Severity
Impact: Low
Likelihood: High
Description
Function rebaseMul() increases the balance per share value by a factor. The
issue is that the code only accepts integer factors and it will not be possible to
increase the balance per share by small percentages.
function rebaseMul(uint128 factor) external onlyRole(OPERATOR_ROLE) {
uint128 _balancePerShare = balancePerShare() * factor;
UsdPlusStorage storage $ = _getUsdPlusStorage();
$._balancePerShare = _balancePerShare;
emit BalancePerShareSet(_balancePerShare);
}
Recommendations
Use the denominator and nominator to specify the increase factor.
[M-02] Attacker can DOS
privateMint()
Severity
Impact: Medium
Likelihood: Medium
Description
Function privateMint() calls permit() to set the allowance before token
transfer:
9

IERC20Permit(address(paymentToken)).permit(permit.owner, address
(this), permit.value, permit.deadline, v, r, s);
usdPlusAmount = permit.value;
_issue(
paymentToken,
permit.value,
permit.value,
permit.owner,
permit.owner
);
The issue is that the attacker can watch the mempool and use the signature to
call permit and it would cause the original transaction to revert because of the
used nonce. As a result, the attacker can DOS the calls to privateMint()
function. The same issue exists in selfPermit() function too.
Recommendations
Use try/catch when calling permit and if the current allowance is bigger than
the spending amount allow logic to be executed. link
[M-03] The deprecated prone
privateMint()
to many issues
Severity
Impact: High
Likelihood: Low
Description
The privateMint() is marked as a deprecated function. However, this
function is prone to several issues:
1. The splitSignature() , which is only used for privateMint() , does not
work with short signatures (64-length signature): link
2. The direct value for USD+ minting ( usdPlusAmount ) is used without
performing oracle conversion to reflect the real amount especially when
the paymentToken is not USD+ (e.g., USDC, which also has permit
10

functionalities). This can lead to over- or under-pricing of USD tokens at
the time of minting.
Recommendations
Consider removing the deprecated function to ensure the protocol operates
correctly and reduce attack vectors, or update the function to handle the work
correctly:
1. For splitSignature() , refer to this for handling short signatures: link
2. Consider using the previewDeposit() to calculate the minting value
along with the current oracle price of the paymentToken .
[M-04] Lack of data validation for oracle
price feed
Severity
Impact: High
Likelihood: Low
Description
There are several issues with the validation of price feed data in the
USDPlusMinter and USDPlusRedeemer (when using Chainlink's
latestRoundData() ):
Missing Validation for Price > 0: There is no check to ensure the price is
greater than 0, which could allow invalid price data.
Price Staleness Not Checked: The contracts do not verify whether the
price feed data is up-to-date, risking reliance on stale or outdated prices.
Sequencer Downtime Handling: The GRACE_PERIOD following sequencer
downtime is not enforced.
Recommendations
11

Implement a validation check to ensure the price is valid and fresh. Each
token's oracle can have a different heartbeat, so the freshness validation should
account for these differences separately. link
For sequencer downtime handling, follow the documentation: link
[M-05] Users can frontrun rebase functions
Severity
Impact: High
Likelihood: Low
Description
The UsdPlus Contract contains the rebaseAdd , rebaseMul , and rebaseSub
functions, which allow an address with the OPERATOR_ROLE to perform a
rebase. These functions adjust the value of $._balancePerShare , either
increasing or decreasing it depending on the action executed.
function rebaseAdd(uint128 value) external onlyRole(OPERATOR_ROLE) {
uint256 _supply = totalSupply();
uint128 _balancePerShare = uint128(FixedPointMathLib.fullMulDiv
(balancePerShare(), _supply + value, _supply));
UsdPlusStorage storage $ = _getUsdPlusStorage();
$._balancePerShare = _balancePerShare;
emit BalancePerShareSet(_balancePerShare);
}
This functionality can be exploited in the following ways:
Users can front-run a positive rebase to acquire tokens at a lower rate. Once
the rebase is executed, they can submit a withdrawal request, locking in the
higher rate. Although the redemption process can take up to three days, the
request function locks the rate in the user’s request ticket, allowing them to
secure profits.
Users can also front-run a negative rebase by submitting a withdrawal request
before the rebase is executed, locking in the rate prior to the update. This
allows them to avoid losses associated with the negative rebase, effectively
bypassing the intended impact of the rebase adjustment.
Recommendations
12

A small withdrawal fee could be implemented to make such exploit attempts
less desirable. Additionally, a delay could also be introduced between deposit
and withdrawal requests.
13

8.3. Low Findings
[L-01] Code would behave unexpectedly if
the price reaches 0
The operator can update the share price value by calling rebaseSub() . If for
some reason protocol loses all its deposits (for example in early deployments)
then after the operator calls to rebaseSub() the _balancePerShare value will
be 0 while some users have a positive balance. Then if somebody makes a
deposit and mints USD+ token, the code would use
_INITIAL_BALANCE_PER_SHARE as the price:
function balancePerShare() public view override returns (uint128) {
// Override with default if not set due to upgrade
if (_balancePerShare == 0) return _INITIAL_BALANCE_PER_SHARE;
return _balancePerShare;
}
As a result, the depositor's balance would be less than what he deposited and
those old depositors who had 0 balance would get a higher balance value. The
issue is that the code assumes if _balancePerShare is 0 then the code is in the
beginning state. To avoid this issue it's better to let the share price always be
higher than 0 when calling rebaseSub() .
[L-02] Overriding function is missing
"override" specifier
The functions mintingMaxLimitOf() , burningMaxLimitOf() ,
mintingCurrentLimitOf() , and burningCurrentLimitOf() do not include the
override specifier, even though they are inherited from the IERC7281Min
interface.
[L-03] Reducing the limit from the
maximum takes the full duration to
14

replenish
The _changeMintingLimit() and _changeBurningLimit() incorrectly wait for
the full replenishment duration before the new limit can be fully used.
When the limit is reduced from type(uint256).max to any new limit, the
function uses type(uint256).max as the oldMaxLimit to calculate the current
and new limits. This approach results in the new current limit being returned as
0, 1-day replenishment before the limit is available to use.
The limit type(uint256).max is a special case that bypasses the checks and
allows the limit to be used immediately. In contrast, when the limit is set to any
other value for the first time, it can be used immediately without waiting for
the full 1-day replenishment duration.
function _calculateNewCurrentLimit
(uint256 newMaxLimit, uint256 oldMaxLimit, uint256 currentLimit)
internal
pure
returns (uint256)
{
if (newMaxLimit > oldMaxLimit) {
return currentLimit + (newMaxLimit - oldMaxLimit);
}
uint256 difference = oldMaxLimit - newMaxLimit;
@> return currentLimit > difference ? currentLimit - difference : 0;
}
Recommendations
Consider treating the oldMaxLimit separately when it changes from
type(uint256).max to any other limit. For example, treat it as a new limit
being created.
[L-04] Functions do not have slippage
protection
During the mint and withdraw process, users specify the token or USD+
amount and the code calculates the receiving or sending amount based on
oracle price. The issue is that the deposit/withdraw asset price or USD+ share
price may change while the transaction is in mempool and there's no way for
the user to specify slippage to protect against price changes and as result user
may receive unfair exchange.
15

function mint(IERC20 paymentToken, uint256 usdPlusAmount, address receiver)
function requestRedeem
(IERC20 paymentToken, uint256 usdplusAmount, address receiver, address owner)
Allow users to specify the minimum/maximum amounts during the
deposit/withdraw process.
[L-05] should round up when
burn()
calculating share amounts
Function burn() in UsdPlus contract, burns specified USD+ tokens from the
caller. It has been used during the withdrawal process.
/// @notice burn USD+ from msg.sender
function burn(uint256 value) external {
address from = _msgSender();
_useBurningLimits(from, value);
_burn(from, value);
}
Because USD+ is a rebasing token to calculate the share burn amount code use
_balancePerShare and divide the USD+ amount by this value.
function balanceToShares(uint256 balance) public view returns (uint256) {
return mulDiv(balance, _INITIAL_BALANCE_PER_SHARE, balancePerShare
//()); // floor
}
The issue is that by doing this the share amount would be rounded down and as
a result code would burn less than what the caller specified. This would cause
small profit for the caller and in some circumstances, malicious users can
extract value because of this.
Round up in favor of the contract when calculating the share amount in
burn() .
16