---
updatedAt: 2025-09-05T18:46:26.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Sending Name Check Requests

To send a name check request, you can use the [Account Name Check API](https://modulr.readme.io/reference/createoutboundcop)

Information required:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        API Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
      </td>

      <td>
        The payee's account name. For increased accuracy you should provide the correct payee name as held at the receiving institution, and not a short name or nickname.  

        We recommend you obtain first name(s) and last name(s) separately for personal accounts wherever possible, to improve match rates.  

        Each name element must be separated by a space and you should not include titles or honorifics. Our API supports UTF-8 encoding so accents can be provided in the request.
      </td>
    </tr>

    <tr>
      <td>
        accountNumber
      </td>

      <td>
        The payee's account number.
      </td>
    </tr>

    <tr>
      <td>
        sortCode
      </td>

      <td>
        The payee's sort code.
      </td>
    </tr>

    <tr>
      <td>
        accountType
      </td>

      <td>
        The type of account that will be paid (either Personal or Business).
      </td>
    </tr>

    <tr>
      <td>
        paymentAccountId
      </td>

      <td>
        The ID of the Modulr account that the subsequent payment will be initiated from.
      </td>
    </tr>

    <tr>
      <td>
        secondaryAccountId (optional)
      </td>

      <td>
        Additional data, such as a Building Society Roll Number or Credit Card number, that is used by the receiving Payment Service Provider to identify the payee (often in conjunction with the account number and/ or sort code).  

        **This data must be provided if it is requested by the receiving Payment Service Provider otherwise they will be unable to identify the payee and carry out the name check.**  

        When a given account number, sort code and secondaryAccountId have been checked, you **must** re-check the details if the secondaryAccountId is later modified.  

        We maintain a list of PSPs that require this data, which may change from time to time, and recommend that you check it by making a GET call to [/account-name-check/srd-accounts](https://modulr.readme.io/reference/getsrdaccounts).
      </td>
    </tr>
  </tbody>
</Table>

***

# Testing your integration within the sandbox environment

* **You must always use sort code 000000**
* We will always return a MATCHED result unless simulating another result by supplying a value in the secondaryAccountID field

To test other scenarios as listed in this guide, you can provide the desired result in the secondaryAccountId field prefixed with a percent sign. For some results, we will append "z" to the end of the name string.

```json Example 1 Request
{
  "accountNumber": "12345678",
  "accountType": "PERSONAL",
  "name": "Joe Bloggs",
  "paymentAccountId": "A123AAA4",
  "sortCode": "000000"
}
```
```json Example 1 Response
{
  "id": "C12001569Z",
  "result": {
    "code": "MATCH"
  }
}
```
```json Example 2 Request
{
  "accountNumber": "12345678",
  "accountType": "PERSONAL",
  "name": "Joe Bloggs",
  "paymentAccountId": "A123AAA4",
  "sortCode": "000000",
  "secondaryAccountId": "%CLOSE_MATCH"
}
```
```json Example 2 Response
{
  "id": "C12001569Z",
  "result": {
    "code": "CLOSE_MATCH",
    "name": "Joseph Bloggsz"
  }
}
```

***

# Interpreting name check responses

There are three outcomes of a successful request:

**The details match.**

The account details (name and account type) you provided matched the information held by the payee’s bank so you can proceed with creating a new beneficiary or payment. You do not need to submit further account name check requests when using these account details in the future unless you believe the account details have changed.

Remember, you must still exercise caution when creating payments. The service is an account name checking service and does not protect against all types of fraud. If something does not seem right about a payment stop and question it even if the details match.

**The details are similar.**

The payee’s bank holds slightly different account name or account type information. Creating a payment could lead to the funds being sent to the wrong account and you may not be able to recover the money. If the account name you provided is similar to the account name held by the payee’s bank, the actual account name will be provided in the response body so that you can check the details and decide whether or not to proceed. If updated account details are obtained you can submit another account name check request before proceeding.

**The details do not match.**

The account name or account type provided do not match the account details held by the payee’s bank. Creating a payment could lead to the funds being sent to the wrong account and you may not be able to recover the money. You are advised to stop and double check the details of the payment. If updated account details are obtained you should submit another account name check request before proceeding. In this type of result the actual account name held by the payee’s bank is NOT returned.

**Result Codes**

This table lists the possible results of an account name check request and the action that we recommend you take in each scenario.

> ❗️
>
> If the sort code or account number are invalid (i.e. fail a modulus check) then the request will not be processed and we will return a 404 error.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        result.code
      </th>

      <th>
        HTTP Status Code
      </th>

      <th>
        Result Description
      </th>

      <th>
        Recommended Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        MATCHED
      </td>

      <td>
        201
      </td>

      <td>
        The account name and account type match the name and accountType provided.
      </td>

      <td>
        You can proceed with the creation of a beneficiary or payment.  

        **Remember, you must still exercise caution when sending payments. The service is an account name checking service and does not protect against all types of fraud.**
      </td>
    </tr>

    <tr>
      <td>
        NOT\_MATCHED
      </td>

      <td>
        201
      </td>

      <td>
        The account name and account type do not match the name and accountType provided.
      </td>

      <td>
        The account details should be checked carefully, and you are advised not to proceed with the creation of the beneficiary or payment. You should edit the details if possible, and submit another account name check request before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        CLOSE\_MATCH
      </td>

      <td>
        201
      </td>

      <td>
        The name provided is similar to the account name. The actual account name is provided in result.name.
      </td>

      <td>
        The account details should be checked carefully. If you decide to continue with the creation of the beneficiary/payment you should edit the details if necessary before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS\_ACCOUNT\_NAME\_MATCHED
      </td>

      <td>
        201
      </td>

      <td>
        The account name matches the name provided but the account is a business account, not a personal account.
      </td>

      <td>
        The account details should be checked carefully before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        PERSONAL\_ACCOUNT\_NAME\_MATCHED
      </td>

      <td>
        201
      </td>

      <td>
        The account name matches the name provided but the account is a personal account, not a business account.
      </td>

      <td>
        The account details should be checked carefully before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        BUSINESS\_ACCOUNT\_CLOSE\_MATCH
      </td>

      <td>
        201
      </td>

      <td>
        The name provided is similar to the account name and the account is a business account, not a personal account. The actual account name is provided in result.name.
      </td>

      <td>
        The account details should be checked carefully. If you decide to continue with the creation of the beneficiary/payment you should edit the details if necessary before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        PERSONAL\_ACCOUNT\_CLOSE\_MATCH
      </td>

      <td>
        201
      </td>

      <td>
        The name provided is similar to the account name and the account is a personal account, not a business account. The actual account name is provided in result.name.
      </td>

      <td>
        The account details should be checked carefully. If you decide to continue with the creation of the beneficiary/payment you should edit the details if necessary before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        ACCOUNT\_DOES\_NOT\_EXIST
      </td>

      <td>
        201
      </td>

      <td>
        The account does not exist.
      </td>

      <td>
        You should not proceed. The account details should be checked carefully. You should edit the details if possible and submit another account name check request before creating a beneficiary or payment.
      </td>
    </tr>

    <tr>
      <td>
        SECONDARY\_ACCOUNT\_ID\_NOT\_FOUND
      </td>

      <td>
        201
      </td>

      <td>
        The secondaryAccountId is not valid.
      </td>

      <td>
        The account details should be checked carefully. The account could not be identified using the secondary account reference. You should edit the details if possible and submit another account name check request before proceeding.
      </td>
    </tr>

    <tr>
      <td>
        ACCOUNT\_NOT\_SUPPORTED
      </td>

      <td>
        201
      </td>

      <td>
        The account does not support account name check requests.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>

    <tr>
      <td>
        ACCOUNT\_SWITCHED
      </td>

      <td>
        201
      </td>

      <td>
        The account has been switched using the Current Account Switching Service.
      </td>

      <td>
        You should not proceed with the creation of a beneficiary or payment using these account details. Obtain the new account details if possible, edit the details and submit another account name check request before creating a beneficiary or payment.
      </td>
    </tr>

    <tr>
      <td>
        WRONG\_PARTICIPANT
      </td>

      <td>
        500
      </td>

      <td>
        The account name check cannot be completed for the account number and sort code provided.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>

    <tr>
      <td>
        NO\_RESPONSE
      </td>

      <td>
        201
      </td>

      <td>
        The bank did not respond to the account name check request.  Try again later.
      </td>

      <td>
        It is recommended you try the check again after some time. If you do decide to continue with this result you should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>

    <tr>
      <td>
        NOT\_ENROLLED
      </td>

      <td>
        201
      </td>

      <td>
        The account name check could not be completed as the bank does not accept account name check requests.
      </td>

      <td>
        You should check the account details carefully and proceed only if you are satisfied that they are correct.
      </td>
    </tr>
  </tbody>
</Table>

# Important Information

## Use of the service

The service must only be used with the sole intention of subsequently creating beneficiaries or payments through your Modulr account. The use of the service for any other purpose is forbidden and is a violation of the terms and conditions of the service.

## End user applications

If you are using Confirmation of Payee within any customer facing application (such as a payment app or website), or in a way that directly or indirectly exposes the result of a check to an end user, there are additional requirements to take into consideration:

* Your service must be available 24/7 and must present name check results to end users in real time.
* There are several industry guidelines and best practice recommendations regarding the design of CoP user interfaces. We will provide a separate guide that contains the information required, including sample wireframes, to help you design an implementation that is compliant and provides the most optimal user experience.

## Auditing

We recommend that you maintain a secure audit trail of requests sent, responses received and the subsequent action taken (e.g. payment created) which can be referenced at a later date if needed.

***