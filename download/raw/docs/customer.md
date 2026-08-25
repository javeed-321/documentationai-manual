---
updatedAt: 2025-12-22T15:06:07.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Customers

> ❗️ Modulr Partners Only
>
> This section is applicable to Modulr Partners only.

Customers are the legal entities (businesses or individuals) that you setup within the Modulr platform and are created via the [Create a new Customer](https://modulr.readme.io/reference/createcustomer) endpoint.

The following information required to create a customer:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Customer Information
      </th>

      <th>
        Required by

        Regular Partners
      </th>

      <th>
        Required by

        Payment Clearing Partners
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Customer Type
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        **REQUIRED**
      </td>
    </tr>

    <tr>
      <td>
        Company Name  
        (except for individuals whose name is provided as an associate)
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Company Registration Number
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Company Registered and Trading Addresses  
        (depending on the type)
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Company Industry  
        (except for individuals) [See here →](https://modulr.readme.io/docs/industry-codes-for-modulr-kyc)
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Company Associate Details  
        (directors or partners)
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        **REQUIRED**  
        Individuals: First & last names & home address  
        Businesses: Company name & trading address
      </td>
    </tr>

    <tr>
      <td>
        Details of Uploaded Documents  
        (e.g. proof of ID)
      </td>

      <td>
        **[SEE BELOW](#details-of-uploaded-documents)**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Expected Monthly Spend
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Modulr T&C's agreed to
      </td>

      <td>
        **REQUIRED**
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        Legal Entity contracted with
      </td>

      <td>
        **[SEE BELOW](#legal-entity)**
      </td>

      <td>
        **[SEE BELOW](#legal-entity)**
      </td>
    </tr>

    <tr>
      <td>
        External Reference  
        (ideally the unique reference you hold for this customer)
      </td>

      <td>
        OPTIONAL
      </td>

      <td>
        OPTIONAL
      </td>
    </tr>
  </tbody>
</Table>

Successful creation of a customer will return a unique customer ID - more detailed information can be found in the [reference documentation](https://modulr.readme.io/reference/createcustomer).

## Details of Uploaded Documents

If your agreement with us requires you to provide us with KYC information, before creating the customer, you must upload the required documentation via the  [Upload](https://modulr.readme.io/reference/upload) endpoint.

The following information required:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Filename
      </td>

      <td>
        The name of the file being uploaded
      </td>
    </tr>

    <tr>
      <td>
        Content
      </td>

      <td>
        The Base64 encoded version of the file being uploaded.  
        Note that we only accept PNG, JPEG, JPG, and PDF files.
      </td>
    </tr>

    <tr>
      <td>
        Group
      </td>

      <td>
        Combination of Partner name and Customer name
      </td>
    </tr>
  </tbody>
</Table>

Example Request & Response:

```json Request
{
"content":"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…xQBg/arf/nrD/33R9qt/wDnrD/33W95Cf3F/wC+Kp311HYtbYg3+bKsPyr92gDN+1W//PWH/vuj7Vb/APPWH/vupbjxJpVjNNBdTR2zxDc5dflqa31zS7i7+yx3MElzu2eWnWqKKn2q3/56w/8AfdH2q3/56w/990+HxLpskPm+ZFGiff3/AMFM/wCEs0ePbJNcxRL5SyMznhf876AD7Vb/APPWH/vuj7Vb/wDPWH/vurMmvaalrdXCTRTR23+t8tfu07+29O+xz3STRPDEju5Rf7n36AKn2q3/AOesP/fdH2q3/wCesP8A33TF8Vab/o/2grbeYu8O6/J03f8AstXrfXtJu3hWK7t5Xm+5t/ioAqfarf8A56w/991xPxG+Fvhn4ptZr4gurie2st729lDeeSkVz/Bc/J/y2T+B/wCCvTNy/bfL2Ls8vf8Ad968k+Knxk1bwp4nTw7oHhWTV9RgtF1a7kmdEh+wq+JtmW+/QB3tl5en2NvA1+L+WKFFe4uHTdNx99/9qinfD/xVa/EPwfpXiG3spbODUIRNFDcou9VoqSTp6KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK5r4kf8AIman/uV0tc18SP8AkTNT/wBygDxzwj/yGP8AgH/s6V7D4s8N2Hi+ziiuXvLO4tpPOtru0V0mgfpuT5a8e8Hf8hj/AIB/7Olex+J9Yu9KutKjtLN9QN3deTKsY+dE7uP4fl/2qrl5glLlMzwB4B0j4b2V5Dp8d01xfT/aLu4uAd0khxk/IoRf91AF/OuqTydsy4kdZW+b909XqKkDgb74f6PcJAkJ1C28qWJt6S3BcbNn3efk3bE+f/Yrr7JbXT7WG3t4njhiTYiBH+Vav0UAQfao/wDa/wC/T0fao/8Aa/79PU9FAFR5oJJEdkZ3T7reS/y0yZ4ptn+t+Rt/+qer1FAGHLbxTXiTtD5zo/mRb0f5Pk2f3KypvB2jzoif2fs2/c2TTV2NFAGNZqmn26wQW6JCpchPn/vbv7lW/tkv/PJf++X/APiKvUUAUftkv/PJf++X/wDiKPtkv/PJf++X/wDiKvUUAUftkv8AzyX/AL5f/wCIo+2S/wDPJf8Avl//AIir1FAFH7ZL/wA8l/75f/4ij7ZL/wA8l/75f/4ir1FAFH7ZL/zyX/vl/wD4ij7ZL/zyX/vl/wD4ir1FAGdNdSzLtCbPm/uv/wDEVDfafYalcWs9xFJJNbtvifY/y/Oj/wDsiVr0UAcpF4T0SCa1lht54vs/3URptjf3S6fx/crpPtcf/TX/AL9P/hU9FAEH2qP/AGv+/T0fao/9r/v09T0UAU0lgg37Fddzb22xPUv2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09H2qP8A2v8Av09T0UAQfao/9r/v09QTNb3OzzEZ9j70/dP96r1FAGJfaPpd8ztLFLvZ9/y70+apobGwhmSVInR0bf8Acf8A2/8A4t61aKAMKbRtLuOfImR0X5XTzUdai/4R3R/u/Z7jYPuf675P9yuiooAxpNLsJIpYjFKiSLtfYjp/FvqC30q0hkuQEleOaLydux/uf7//AANq6CigDDn0XSrhXRreQq/3/lf5v876VNK06PyP3Nx+6fen3/v1t0UAUfMi+0ebiX7uz/VPXnnxG+Cng/4manb6lqlpdQ6kjoHvLMukksKf8sX/ANht9eo0UAYfhzRdH8G6La6Ro9l/Z+mWibIraCF9qCityigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArmviR/yJmp/7ldLXNfEj/kTNT/3KAPHPCP8AyGP+Af8As6V9EV87+Ef+Qx/wD/2dK+iKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArmviR/wAiZqf+5XS1zXxI/wCRM1P/AHKAPHPCP/IY/wCAf+zpX0RXzv4R/wCQx/wD/wBnSvoigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK5r4kf8iZqf8AuV0tc18SP+RM1P8A3KAPHPCP/IY/4B/7OlfRFfO/hH/kMf8AAP8A2dK+iKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArmviR/yJmp/7ldLXNfEj/kTNT/3KAPHPCP/ACGP+Af+zpX0RXzv4R/5DH/AP/Z0r6IoAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACua+JH/Iman/uV0tc18SP+RM1P/coA8c8I/wDIY/4B/wCzpX0RXzv4R/5DH/AP/Z0r6IoAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACua+JH/ACJmp/7ldLXNfEj/AJEzU/8AcoA8c8I/8hj/AIB/7OlfRFfO/hH/AJDH/AP/AGdK+iKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArmviR/yJmp/wC5RRQB454R/wCQx/wD/wBnSvoiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//Z",
"fileName":"Example File 1.jpg",
"group":"MODULR CLEGG CONSULTING LTD"
}
```
```json Response
{
"path": "MODULR+CLEGG+CONSULTING+LTD%2F20171025143744_Example+File+1.jpg",
"fileName": "Example File 1.jpg"
}
```

Once uploaded, documents are linked to a customer via the documentInfo field depending on what the document relates to. For example, if documents relate to a limited company then documents should be linked at the customer level. If they related to the Ultimate Beneficial Owner of the company then documents should be linked to the associate within the customer.

## Legal Entity

The legal entity field is required and must be set depending on which Modulr entity the customer is contracted with:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Modulr Entity Contracted with
      </th>

      <th>
        Option
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Modulr Financial Services Limited (MFSL), our UK regulated entity
      </td>

      <td>
        GB
      </td>
    </tr>

    <tr>
      <td>
        Modulr Finance B.V. (MFBV), our Dutch regulated entity  
        (regardless of the MFBV branch you are serviced by)
      </td>

      <td>
        NL
      </td>
    </tr>
  </tbody>
</Table>

Note that PCM Partners should set the legal entity based on the Modulr entity they as the partner are contracted with.