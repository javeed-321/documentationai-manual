---
updatedAt: 2026-06-24T15:56:59.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Inbound Payments via SWIFT

> ❗️ **Only applicable to customers authorised for payments via SWIFT**
>
> Any payments received via SWIFT to credit customers who are not authorised will be returned.
>
> Note that this will cause inconvenience to those paying and as there are no standard timescales for returns via SWIFT.

# Required information

To receive payments into your Modulr accounts via SWIFT, you will need to provide the payer with the following information:

* The IBAN & BIC of the Modulr account you wish to receive the funds into
* The routing information for the payment (so correspondent banks in the chain know where to send the funds).

### The IBAN & BIC of your Modulr account:

The IBAN & BIC of your Modulr account can be found in the customer portal or by using the <https://modulr.readme.io/reference/getaccount> endpoint.

Below is a truncated example response:

```json GET ACCOUNT RESPONSE
{
    "id": "A1111111",
    "name": "SWIFT Account",
    "balance": "123456.78",
    "availableBalance": "123456.78",
    "currency": "USD",
    "status": "ACTIVE",
    "identifiers": [
        {
            "type": "IBAN",
            "iban": "GB99MODR12345612345678",
            "bic": "MODRGB23XXX",
```

### The routing information:

The routing information for the payment is provided in the table below.

You will need to provide the payer with the following information based on the BIC & Currency of your account:

* Modulr Account BIC and Account number (typically IBAN)
* Correspondent BIC needed to reach Modulr
* Modulr Entity Name
* Modulr Entity Address

Your Modulr Account BIC and correspondent details to use will vary depending on the currency and location your account is held. Use the dropdowns below to find the relevant details

<Accordion title="Account held at Modulr UK" icon="fa-info-circle">
  <table>
    <thead>
      <tr>
        <th>
          <p>Your</p>
          <p>BIC (Account with Institution)</p>
        </th>

        <th>
          <p>Your</p>
          <p>Account Currency</p>
        </th>

        <th>
          <p>Correspondent (Intermediary) BIC needed to reach Modulr</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Name</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Address</p>
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <p>MODRGB23XXX</p>
        </td>

        <td>
          <p>AED, AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD,
          THB, TRY, USD</p>
        </td>

        <td>
          <p>CHASGB2LXXX</p>
        </td>

        <td>
          <p>Modulr FS Ltd</p>
          <p>LEI 984500BFFA6CBFA57C93</p>
        </td>

        <td>
          <p>Scale Space, 58 Wood Lane, London W12 7RZ</p>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

<Accordion title="Account held with Modulr EU (Netherlands)" icon="fa-info-circle">
  <table>
    <thead>
      <tr>
        <th>
          <p>Your</p>
          <p>BIC (Account with Institution)</p>
        </th>

        <th>
          <p>Your</p>
          <p>Account Currency</p>
        </th>

        <th>
          <p>Correspondent (Intermediary) BIC needed to reach Modulr</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Name</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Address</p>
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <p>MODRNL22XXX</p>
        </td>

        <td>
          <p>EUR</p>
        </td>

        <td>
          <p>CHASDEFXXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V.,</p>
          <p>LEI 2138009BPIB3N98CK876</p>
        </td>

        <td>
          <p>Strawinskylaan 4117
          Amsterdam, 1077ZX</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>MODRNL22XXX</p>
        </td>

        <td>
          <p>AED, AUD, CAD, CHF, CZK, DKK, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD,
          THB, TRY, USD</p>
        </td>

        <td>
          <p>CHASNL2XXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V.,</p>
          <p>LEI 2138009BPIB3N98CK876</p>
        </td>

        <td>
          <p>Strawinskylaan 4117
          Amsterdam, 1077ZX</p>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

<Accordion title="Account held with Modulr EU (Irish Branch)" icon="fa-info-circle">
  <table>
    <thead>
      <tr>
        <th>
          <p>Your</p>
          <p>BIC (Account with Institution)</p>
        </th>

        <th>
          <p>Your</p>
          <p>Account Currency</p>
        </th>

        <th>
          <p>Correspondent (Intermediary) BIC needed to reach Modulr</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Name</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Address</p>
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <p>MODRIE22XXX</p>
        </td>

        <td>
          <p>EUR</p>
        </td>

        <td>
          <p>CHASDEFXXXX</p>
        </td>

        <td>
          <p>Modulr Finance, B.V., Irish Branch</p>
          <p>LEI 98450052C5E7SZ5EA950</p>
        </td>

        <td>
          <p>77 Sir John Rogerson’s Quay, Dublin 2, D02 NP08</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>MODRIE22XXX</p>
        </td>

        <td>
          <p>AED, AUD, CAD, CHF, CZK, DKK, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD,
          THB, TRY, USD</p>
        </td>

        <td>
          <p>CHASNL2XXXX</p>
        </td>

        <td>
          <p>Modulr Finance, B.V., Irish Branch</p>
          <p>LEI 98450052C5E7SZ5EA950</p>
        </td>

        <td>
          <p>77 Sir John Rogerson’s Quay, Dublin 2, D02 NP08</p>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

<Accordion title="Account with Modulr EU (Spanish Branch)" icon="fa-info-circle">
  <table>
    <thead>
      <tr>
        <th>
          <p>Your</p>
          <p>BIC (Account with Institution)</p>
        </th>

        <th>
          <p>Your</p>
          <p>Account Currency</p>
        </th>

        <th>
          <p>Correspondent (Intermediary) BIC needed to reach Modulr</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Name</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Address</p>
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <p>MODRESB2XXX</p>
        </td>

        <td>
          <p>EUR</p>
        </td>

        <td>
          <p>CHASDEFXXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V., SPAIN BRANCH</p>
          <p>LEI 959800DZC2UKMCTEN383</p>
        </td>

        <td>
          <p>The Shed CoWorking Calle de Hermosilla 481st Floor ; Postal code: 28001</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>MODRESB2XXX</p>
        </td>

        <td>
          <p>AED, AUD, CAD, CHF, CZK, DKK, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD,
          THB, TRY, USD</p>
        </td>

        <td>
          <p>CHASNL2XXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V., SPAIN BRANCH</p>
          <p>LEI 959800DZC2UKMCTEN383</p>
        </td>

        <td>
          <p>The Shed CoWorking Calle de Hermosilla 481st Floor ; Postal code: 28001</p>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

<Accordion title="Account with Modulr EU (French Branch)" icon="fa-info-circle">
  <table>
    <thead>
      <tr>
        <th>
          <p>Your</p>
          <p>BIC (Account with Institution)</p>
        </th>

        <th>
          <p>Your</p>
          <p>Account Currency</p>
        </th>

        <th>
          <p>Correspondent (Intermediary) BIC needed to reach Modulr</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Name</p>
        </th>

        <th>
          <p>Modulr</p>
          <p>Entity Address</p>
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          <p>MODRFRP2XXX</p>
        </td>

        <td>
          <p>EUR</p>
        </td>

        <td>
          <p>CHASDEFXXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V., FRANCE BRANCH</p>
          <p>LEI 254900XUU0FVXPTGEF04</p>
        </td>

        <td>
          <p>54 Rue De Londres, Paris, France 75008</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>MODRFRP2XXX</p>
        </td>

        <td>
          <p>AED, AUD, CAD, CHF, CZK, DKK, GBP, HKD, HUF, JPY, NOK, NZD, PLN, RON, SEK, SGD,
          THB, TRY, USD</p>
        </td>

        <td>
          <p>CHASNL2XXXX</p>
        </td>

        <td>
          <p>MODULR FINANCE B.V., FRANCE BRANCH</p>
          <p>LEI 254900XUU0FVXPTGEF04</p>
        </td>

        <td>
          <p>54 Rue De Londres, Paris, France 75008</p>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

# Making the payment

The sending payment institution should be provided the IBAN & BIC of your Modulr account along with the correct routing information (BIC and currency dependent).

Notes:

* Many sending payment institutions will auto-complete routing information to simplify sending payments; unless the the institution requires correspondent/intermediary as a mandatory field do not enter this information.
* If the sending payment institution auto-completes information, populating a correspondent/intermediary that is different to the above, it is strongly advised that the payment institution is asked to update their SSI records before the payment is initiated.
* Payments sent via SWIFT will typically be received within 1 business day, however it can take up to 3 to 5 business days with longer time scales applying if there are issues/errors requiring manual intervention by correspondent banks.
* Queries on the status of a payment made via SWIFT to a Modulr account must be raised directly with the sending bank as Modulr may not have visibility of the payment.

### Troubleshooting a payment:

If a payment sent via SWIFT has been returned, you should ask the sending payment institution for the MT103 message that they sent.

The required information above must be populated correctly within the message. The table below shows an example the minimum requirement for sending to GB account:

| Requirement                               | Row/Field | Example                |
| :---------------------------------------- | :-------- | :--------------------- |
| Modulr’s correspondent (intermediary) BIC | :56A:     | CHASGB2LXXX            |
| Your Modulr account BIC                   | :57A:     | MODRGB23XXX            |
| Your Modulr account IBAN                  | :59:      | GB99MODR12345612345678 |

If this information isn't present or is populated incorrectly, you should correct with the sending payment institution and resubmit the payment.

<br />