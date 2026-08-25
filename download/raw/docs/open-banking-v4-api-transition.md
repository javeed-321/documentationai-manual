---
updatedAt: 2026-04-03T10:41:40.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Open Banking V4 API transition

Information on new fields & ASPSP transition dates

# Open Banking V4 API overview

The Open Banking Version 4 API standards were [released in June 2024](https://www.openbanking.org.uk/news/obl-publishes-open-banking-standard-v4-0-to-assure-future-ecosystem-growth/) with a requirement for the banks subject to the Competition an Markets Authority to migrate.

The majority of technical improvements do not impact client integrations using the Modulr Payment Initiation Service. There are improvements to payment statuses that clients may wish to incorporate.

As each institution (ASPSP) deprecates its V3.x Payment initiation API the service is transitioned to the equivalent V4.x API. Further details of ASPSP API versioning can be found in the Open Banking Limited [Transparency Calendar](https://openbanking.atlassian.net/wiki/spaces/DZ/pages/1145209627/Transparency+Calendar)

# Additional payment status fields in V4

## Single immediate payment

| Payment status                            | Type of Change     | Payment Status Description                                                                                                                                                                                                                                                                 |
| ----------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rejected                                  | Existing           | Payment instruction has been rejected.                                                                                                                                                                                                                                                     |
| Pending                                   | Existing           | Payment instruction is pending. Further checks and status update will be performed.                                                                                                                                                                                                        |
| AcceptedSettlementInProcess               | Existing           | All preceding checks such as technical validation and customer profile were successful and therefore the payment instruction has been accepted for execution.                                                                                                                              |
| AcceptedWithoutPosting                    | Existing           | Payment instruction included in the credit transfer is accepted without being posted to the payee's customer’s account. **Note that most banks do not provide this information.**                                                                                                          |
| AcceptedSettlementCompleted               | Updated (see note) | This is replaced in the V4 API with a new status (AcceptedSettlementCompletedCreditorAccount); to mitigate this as a breaking change for clients the Modulr platform will internally generate a AcceptedSettlementCompleted status for V4 ASPSPs when this replacement status is received. |
| AcceptedCreditSettlementCompleted         | Deprecated         | Note that most banks did not provide this information.                                                                                                                                                                                                                                     |
| AcceptedCustomerProfile                   | New                | Preceding check of technical validation was successful. Customer profile check was also successful.                                                                                                                                                                                        |
| PartiallyAcceptedTechnicalCorrect         | New                | Payment initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful.                                                                                                                                  |
| AcceptedFundsChecked                      | New                | Preceding check of technical validation and customer profile was successful and an automatic funds check was positive.                                                                                                                                                                     |
| AcceptedSettlementCompletedDebitorAccount | New                | Settlement completed. Only used by bilateral agreement for Market Infrastructure reporting to Infrastructure Participant or an Account Servicer to Account Owner to report that the transaction account entry has been completed; Note most ASPSPs will not use this status                |
| AcceptedWithChange                        | New                | Instruction is accepted but a change will be made, such as date or remittance not sent.                                                                                                                                                                                                    |
| Blocked                                   | New                | Payment transaction previously reported with status 'ACWP' is blocked, for example, funds will neither be posted to the Creditor's account, nor be returned to the Debtor.                                                                                                                 |
| Received                                  | New                | Payment instruction has been received.                                                                                                                                                                                                                                                     |
| AcceptedTechnicalValidation               | New                | Authentication and syntactical and semantical validation are successful                                                                                                                                                                                                                    |

## Fixed Recurring Payments (Standing order)

| Payment Status                    | Type of change | Payment Status Description                                                                                                                                |
| --------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| InitiationFailed                  | Existing       | Standing order has been setup successfully but the individual payment has failed                                                                          |
| InitiationCompleted               | Existing       | Standing order has been setup successfully and the individual payment has been successfully completed.                                                    |
| Received                          | New            | Payment instruction has been received.                                                                                                                    |
| Rejected                          | New            | Payment instruction has been rejected.                                                                                                                    |
| Cancelled                         | New            | Payment initiation has been successfully cancelled after having received a request for cancellation.                                                      |
| PartiallyAcceptedTechnicalCorrect | New            | Payment initiation needs multiple authentications, where some but not yet all have been performed. Syntactical and semantical validations are successful. |
| Pending                           | Updated        | This replaces the InitiationPending status - Payment instruction is pending. Further checks and status update will be performed.                          |
| AcceptedTechnicalValidation       | New            | Authentication and syntactical and semantical validation are successful                                                                                   |

## Payment Context Codes

As part of the v4 update, payment context codes have been remapped to their new equivalents. This means there is no change required for you today, we continue to support those inputs and will automatically translate them.

Note that there are two new codes you may choose to optionally start using.

### v3 to v4 codes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        V3 code
      </th>

      <th>
        Mapped V4 code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        BILLPAYMENT("BillPayment")
      </td>

      <td>
        BILLINGGOODSANDSERVICESINADVANCE  
        ("BillingGoodsAndServicesInAdvance")
      </td>
    </tr>

    <tr>
      <td>
        ECOMMERCEGOODS("EcommerceGoods")
      </td>

      <td>
        ECOMMERCEMERCHANTINITIATEDPAYMENT  
        ("EcommerceMerchantInitiatedPayment")
      </td>
    </tr>

    <tr>
      <td>
        ECOMMERCESERVICES("EcommerceServices")
      </td>

      <td>
        ECOMMERCEMERCHANTINITIATEDPAYMENT  
        ("EcommerceMerchantInitiatedPayment")
      </td>
    </tr>

    <tr>
      <td>
        PARTYTOPARTY("PartyToParty")
      </td>

      <td>
        TRANSFERTOSELF("TransferToSelf")
      </td>
    </tr>

    <tr>
      <td>
        OTHER("Other")
      </td>

      <td>
        TRANSFERTOTHRIDPARTY("TransferToThirdParty")
      </td>
    </tr>
  </tbody>
</Table>

### New v4 codes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        v4 code
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        BILLINGGOODSANDSERVICESINARREARS
        ("BillingGoodsAndServicesInArrears")
      </td>

      <td>
        Post-paid billing scenarios
      </td>
    </tr>

    <tr>
      <td>
        FACETOFACEPOINTOFSALE  
        ("FaceToFacePointOfSale")
      </td>

      <td>
        In-person payments
      </td>
    </tr>
  </tbody>
</Table>

# ASPSP (institution) v3 deprecation dates

The table below lists current dates of ASPSP switchover to only supporting PIS requests using the Open Banking v4 API standard. Payment status updates will be available shortly before these dates.

| ASPSP/Bank Brand     | Date of V3 deprecation |
| -------------------- | ---------------------- |
| HSBC Business        | 13 June 2025           |
| HSBC Personal        | 13 June 2025           |
| First Direct         | 13 June 2025           |
| Danske Bank          | 21 February 2026       |
| RBS (NatWest Group)  | March 2026             |
| Nationwide           | 1 April 2026           |
| Mettle               | 29 April 2026          |
| Santander UK         | 30 April 2026          |
| Allied Irish Bank    | 18 June 2026           |
| Lloyds Banking Group | 1 June 2026            |

<br />