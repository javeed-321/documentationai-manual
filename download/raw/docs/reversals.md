---
updatedAt: 2025-09-30T09:33:26.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Reversals and Reconciliation

When payments come back

## Reversals

A payment reversed by a payment scheme will appear with the type as either as PI\_REV or more commonly a PO\_REV. If you are sending money out, then a PO\_REV means that it is a Return of Previously Sent Outbound Payment. You will need to track back to your original payment request to reconcile.

## How they happen

For disbursement use cases and accounts both the Payin webhook and Get Payments endpoint are vital if payments are received into your account and need reviewing / reconciliation / returning to source. An unexpected credit into your account might be one of 4 scenarios:

1. A genuine scheme return of an outbound payment (type is PO\_REV)
2. A credit which relates to an outbound payment, but actually appears as a new payment from your payee account (types will start PI\_)
3. A credit which relates to an outbound payment, but appears as a new payment from a different account or even a different Sort Code and account (types will start PI\_)
4. A credit sent to your account incorrectly as the wrong destination account and should be sent back to source, no further reconciliation needed (types will start PI\_).

For option 4, a mis-keyed or unwanted payment that arrives unexpectedly can be paid to the sender using the Payer Details from the PAYIN webhook or GetPayments endpoint. You must copy their inbound payment reference into the PaymentReference field on your payment out. This enables the receiving institution to reconcile their mistake quickly.

It is only for a Scheme Reversal (PO\_REV), that a direct connection can be made to your payment out. Any of the other situations (2-4 listed above) will require a decision based on your investigations into the payer details, amount, description timing of payment out vs ‘new’ payment in, etc. Modulr can only provide the data available, we cannot signpost these for you when the inbound payment is not a formal scheme reversal.

For all ‘returns’ that are not scheme reversed and appear as a new inbound payment, the type will be one of PI\_FAST, PI\_SECT, PI\_SEPA\_INST, etc.

## Reconciliation for a Scheme Return - no webhooks

*An outbound payment returned via the scheme (Type = POREV) and the PAYIN/PAYOUT webhooks are not in use*

1. A Get Transactions API response will identify a PO\_REV in “type”, extract the “sourceId”. This is the Modulr Payment Reference (PBID) for the scheme inbound reversal.
2. Call Get Payments (2a) and in the “Id” field enter the “sourceId” from above, (the only query parameter needed). The API response (2b) will contain the JSON payload “returnDetails” which includes the “originalSchemeId” and “returnReasonCode”. SchemeId is the payment scheme reference that links the inbound reversal and your original outbound payment.
3. Call Get Payments (a second call), and in the “schemeId” field enter the “originalSchemeId (3a) prepended\* with “PAYPORT:” and a date within the last 6 months; PAYPORT:MODULO00P210FTW87G102067091562604 noting there is a longer example of the call below. The API response (3b) will return both: the “id” which is the Modulr PBID for the original outbound payment request and your “externalReference”, which is your system reference for the payment added at the time of the original payout request.
   1. These steps and data will allow you to reconcile the Inbound Reversal in an automated manner.
   2. \*prepend is “PAYPORT:” because this is a GBP payment. For SEPA Payments in EUR, you would instead need to prepend with “BOL:” instead. Without this necessary identifier an empty list will be returned.

![](https://files.readme.io/ba66eabad5aef37e07fabbfaf2dbb25678e7271bed6ed871ac766bb26944bcec-image.png)

## Reconciliation for a Scheme Return - with webhooks

*An outbound payment returned via the scheme (Type = PO\_REV) and the PAYIN/PAYOUT webhooks are subscribed to*

1. When Modulr process your outbound payment request the PAYOUT webhook will trigger. We advise you store, PBid, TBid and the payment schemeId (schemeInfo \ Id) against your payment record.
2. If a payment is reversed via the scheme, then the PAYIN Webhook will identify a PO\_REV in “type”, along with the “ReturnReasonCode” and the “OriginalSchemeId”. Note that the SchemeIno \ Id relates to the inbound payment. “OriginalSchemeId” links the inbound reversal and your original outbound payment.
3. Call Get Payments and in the “schemeId” field enter the “originalSchemeId (3a) prepended\* with “PAYPORT:” and a date within the last 6 months; PAYPORT:MODULO00P210FTW87G102067091562604 noting there is a longer example of the call below. The API response (3b) will return both: the “id” which is the Modulr PBID for the original outbound payment request and your “externalReference” which is your system reference for the payment added at the time of the original payout request.
   1. These steps and data will allow you to reconcile the Inbound Reversal in an automated manner.
   2. prepend is “PAYPORT:” because this is a GBP payment. For SEPA Payments in EUR, you would instead need to prepend with “BOL:” instead. Without this necessary identifier an empty list will be returned.

<br />

![](https://files.readme.io/3878726bac166830938dc12d758e156a038b6c70481d64bb5451f5c57eb3ab9a-image.png)