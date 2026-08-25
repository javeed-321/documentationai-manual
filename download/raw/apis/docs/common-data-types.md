---
updatedAt: 2026-07-13T22:46:02.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Common data types

## **Name Field Requirements**

DriveWealth's clearing system requires that `firstName` and `lastName` contain only **ASCII-compatible Latin characters**. Accounts submitted with unsupported characters will fail at the clearing stage with an `Invalid Account Name` error and will need to be corrected before the account can be activated.

## **Supported Characters**

| Type                         | Examples                    |
| :--------------------------- | :-------------------------- |
| Standard Latin letters       | `A–Z`, `a–z`                |
| Hyphens                      | `O-Brien`, `Al-Saadi`       |
| Spaces, apostrophes, periods | `Mary J. Blige`, `O'Connor` |

## **Unsupported Characters**

| Type                             | Examples             |
| :------------------------------- | :------------------- |
| Arabic script                    | `أحمد`, `فارازانجوم` |
| CJK characters                   | `振廙`, `范`            |
| Accented/diacritic characters    | `José`, `Müller`     |
| Any non-Latin Unicode characters | —                    |

## **Handling International Customers**

Transliterate the name to its Latin ASCII equivalent before submitting. The transliterated name should match how the customer's name appears on their government-issued ID in Latin characters (many international IDs include this).

```json
// ❌ Will fail
{ "firstName": "أحمد", "lastName": "السعدي" }

// ✅ Correct
{ "firstName": "Ahmed", "lastName": "Al-Saadi" }
```

⚠️ **Note:** The transliterated name must still match the customer's official ID. If their ID only shows non-Latin script, submit the most commonly accepted romanization.

## **Dates & Times**

All timestamps across the DriveWealth API are expressed in **ISO 8601 format** and returned in **UTC**.

```
2024-03-15T14:30:00.000Z
```

When submitting date parameters in query strings (e.g. for filtering transactions or statements), use the `YYYY-MM-DD` format:

```
GET /back-office/accounts/{accountID}/transactions?from=2024-01-01&to=2024-03-31
```

**Key conventions:**

* All API responses return timestamps in UTC — your platform is responsible for converting to the user's local timezone for display
* Market hours and settlement cutoffs are expressed in **US Eastern Time (ET)** in this documentation
* Settlement dates follow the **T+N** convention, where T is the trade date and N is the number of business days to settlement

📘 **Note:** Weekend and US market holidays are not counted as business days for settlement purposes.

***

## **Monetary Amounts**

All monetary values in the DriveWealth API are expressed as **floating point numbers in USD**, unless otherwise specified.

```json
{
  "cashAvailableForTrade": 1250.75,
  "cashBalance": 1500.00
}
```

**Key conventions:**

* All amounts are in USD by default
* Fractional amounts are supported and returned with up to 8 decimal places for share quantities (e.g. `"openQty": 0.00250000`)
* Monetary values (cash, market value) are typically returned with 2 decimal places
* Never round monetary values before submitting to the API — pass the full precision received

🚧 **Important:** DriveWealth does not perform currency conversion. Non-USD clients should handle FX conversion on their side before submitting funding amounts.

***

##

***

## **Error Handling**

DriveWealth uses standard **HTTP status codes** alongside a structured error response body to communicate failures.

**HTTP status codes used:**

| Code  | Meaning                                                                                  |
| :---- | :--------------------------------------------------------------------------------------- |
| `200` | Success                                                                                  |
| `400` | Bad Request — invalid parameters or missing required fields                              |
| `401` | Unauthorized — invalid or expired session token                                          |
| `403` | Forbidden — valid credentials but insufficient permissions                               |
| `404` | Not Found — the requested resource does not exist                                        |
| `409` | Conflict — duplicate request or state conflict                                           |
| `422` | Unprocessable Entity — request is valid but cannot be executed (e.g. insufficient funds) |
| `429` | Too Many Requests — rate limit exceeded                                                  |
| `500` | Internal Server Error — contact DriveWealth support                                      |

**Error response format:**

```json
{
  "errorCode": "INSUFFICIENT_FUNDS",
  "errorMessage": "The account does not have sufficient cash available for trade.",
  "statusCode": 422
}
```

**Best practices:**

* Always parse the `errorCode` field programmatically — do not rely solely on `errorMessage` strings, which may change
* Implement retry logic with **exponential backoff** for `500` and `429` errors
* `409` conflicts on order submission should be investigated before retrying — do not auto-retry blindly
* Surface meaningful error states to your users rather than generic failure messages

***

## **Idempotency**

For critical operations such as deposits, withdrawals, and order submissions, DriveWealth supports idempotency keys to prevent duplicate transactions in the event of network failures or timeouts.

Pass a unique idempotency key in the request header:

```
Idempotency-Key: {your-unique-uuid}
```

**Key conventions:**

* Idempotency keys must be a **UUID v4**
* Keys are valid for 3 days
* If a request is retried with the same key, the original response is returned without executing the operation again
* Each unique operation should use a fresh idempotency key — never reuse keys across different transactions

🚧 **Important:** Submitting an order or funding request without an idempotency key in an unreliable network environment risks duplicate execution. Always use idempotency keys for money movement and order operations.

***

### **Generating a UUID v4**

| Language | Library / Method                 | Docs                                                                                   |
| :------- | :------------------------------- | :------------------------------------------------------------------------------------- |
| Node.js  | `crypto.randomUUID()` (built-in) | [nodejs.org](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions)               |
| Python   | `uuid.uuid4()` (stdlib)          | [docs.python.org](https://docs.python.org/3/library/uuid.html)                         |
| Ruby     | `SecureRandom.uuid` (stdlib)     | [ruby-doc.org](https://ruby-doc.org/stdlib/libdoc/securerandom/rdoc/SecureRandom.html) |
| PHP      | `ramsey/uuid`                    | [uuid.ramsey.dev](https://uuid.ramsey.dev)                                             |

<br />