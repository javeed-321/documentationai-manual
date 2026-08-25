---
updatedAt: 2025-09-22T15:02:12.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Errors

DriveWealth uses standard HTTP response codes to indicate the success or failure of an API request.

* Codes in the `200` range indicate success.
* Codes in the `400` range indicate a failure given the information provided.
* Codes in the `500`range indicate an error with the DriveWealth servers (very uncommon).

In the occurrence of `4xx` response code, DriveWealth will provide a JSON error code message that briefly explains the error.

Each API request has an associated request identifier. You can find this value in the response headers, under `dw-request-id`. You should log this identifier as you would any other API response.

# Error Code Reference Tables

## Account Errors

| Error Code | Error Response                                 | Error Description                                                       |
| :--------- | :--------------------------------------------- | :---------------------------------------------------------------------- |
| **A010**   | *ACCOUNT\_MISSING\_PARAMETER*                  | A required parameter is missing or invalid in the request body.         |
| **A011**   | *ACCOUNTID\_MISSING\_INVALID*                  | A required accountID is missing or invalid.                             |
| **A012**   | *ACCOUNTNO\_MISSING\_INVALID*                  | A required accountNo is missing or invalid.                             |
| **A013**   | *ACCOUNT\_DATERANGE\_MISSING\_INVALID*         | A required date range is missing or invalid.                            |
| **A015**   | *ACCOUNT*INVALID\_USER*TYPE*                   | The given type of account cannot be created for the given user.         |
| **A020**   | *ACCOUNT\_BAD\_COMBINATION\_PARAMETER*         | One or more parameters in the given combination are missing or invalid. |
| **A035**   | *ACCOUNT\_MISSING\_USER\_PARAMETER*            | Unable to create account due to missing field(s) on the user.           |
| **A044**   | *ACCOUNT\_CASH\_TRANSFER\_INVALID\_AMOUNT*     | The amount of the cash to be transferred is missing or invalid.         |
| **A045**   | *ACCOUNT\_TRANSFER\_MISSING\_COMMENT*          | The `comment` of this transfer is missing.                              |
| **A047**   | *ACCOUNT\_CASH\_TRANSFER\_INSUFFICIENT\_FUNDS* | There is insufficient cash in the account to complete a transfer.       |
| **A050**   | *ACCOUNT*NOT*FOUND*                            | The account you were trying to retrieve was not found.                  |
| **A051**   | *ACCOUNT\_RESTRICTED*                          | Account has been restricted.                                            |
| **A055**   | *ACCOUNT*INVALID*OPERATION*                    | The requested operation cannot be performed on this account.            |
| **A062**   | *ACCOUNT\_CASH\_TRANSFER\_FROM\_FAILURE*       | Transferring cash from this account has failed.                         |
| **A063**   | *ACCOUNT\_CASH\_TRANSFER\_TO\_FAILURE*         | Transferring cash to this account has failed.                           |
| **A065**   | *ACCOUNT\_CASH\_TRANSFER\_OUTSIDE\_MMW*        | Transferring cash outside money movement window is not permitted.       |
| **A071**   | *ACCOUNT\_NOT\_HOUSE\_ACCOUNT*                 | The account is not a house account.                                     |
| **A072**   | *ACCOUNT\_INVALID\_RIA*                        | The user account does not belong to the given RIA.                      |
| **A100**   | *ACCOUNT\_ERROR*                               | There was an error in retrieving the account.                           |

## ACAT Errors

(Automated Customer Account Transfer)

| Error Code | Error Response                       | Error Description                                        |
| :--------- | :----------------------------------- | :------------------------------------------------------- |
| **AC001**  | *ACATS\_BAD\_SYMBOL\_REQUEST*        | ACATs Request rejected because Symbols are not available |
| **AC002**  | *ACATS\_INPUT\_INVALID*              | Input(s) invalid                                         |
| **AC003**  | *ACATS\_REQUEST\_ALREADY\_SUBMITTED* | Request has been already submitted.                      |

## Beneficiary Errors

| Error Code | Error Response                  | Error Description                                      |
| :--------- | :------------------------------ | :----------------------------------------------------- |
| **B001**   | *BENEFICIARIES\_ACCOUNT\_ERROR* | Beneficiaries account request failed.                  |
| **B050**   | *BOD\_NOT\_FOUND*               | Unable to generate BOD summary. Contact administrator. |

## Commission Errors

| Error Code | Error Response                   | Error Description                                                                                   |
| :--------- | :------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **C010**   | *COMMISSION\_NO\_COMMISSION\_ID* | No commissions set for current BackOffice user. Contact administrator to get a commission schedule. |

## Document Errors

| Error Code | Error Response                     | Error Description                                                                                     |
| :--------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **D001**   | *DOCUMENT\_TOO\_LARGE*             | Document is too large to upload. Please resize your document.                                         |
| **D011**   | *DOCUMENT\_INVALID\_CONTENT\_TYPE* | Content type not accepted.                                                                            |
| **D050**   | *DOCUMENT\_NOT\_FOUND*             | The document you were trying to retrieve was not found.                                               |
| **D100**   | *DOCUMENT\_ERROR*                  | There was an error in retrieving the document.                                                        |
| **D200**   | *DOCUMENT\_APPROVED*               | Document has been Approved.                                                                           |
| **D201**   | *DOCUMENT\_PENDING*                | Document approval is Pending.                                                                         |
| **D202**   | *DOCUMENT\_REJECTED*               | Document has been Rejected.                                                                           |
| **D203**   | *DOCUMENT\_NOT\_SUBMITTED*         | Document has not been submitted for approval.                                                         |
| **D204**   | *DOCUMENT\_UPLOAD\_DENIED*         | User does not have permission to upload Document. Please check your User Status for more information. |
| **D205**   | *DOCUMENT\_UNKNOWN*                | Document is unknown.                                                                                  |

## Request Errors

| Error Code | Error Response                        | Error Description                                                              |
| :--------- | :------------------------------------ | :----------------------------------------------------------------------------- |
| **E005**   | *STALE\_REQUEST*                      | Request date header too old.                                                   |
| **E006**   | *FUTURE\_REQUEST*                     | Request date header is in the future.                                          |
| **E010**   | *NO\_REQUEST\_BODY*                   | No request body provided.                                                      |
| **E015**   | *UNSUPPORTED\_FORMAT*                 | Unsupported Format.                                                            |
| **E020**   | *DUPLICATE\_VALUE*                    | Value Exists Already.                                                          |
| **E025**   | *BAD\_REQUEST*                        | Invalid or badly formatted request.                                            |
| **E030**   | *BAD\_MISSING\_PARAMETERS\_URL*       | Invalid or missing parameters in the request URL.                              |
| **E031**   | *BAD\_MISSING\_PARAMETERS\_URL\_BODY* | Invalid or missing parameters in the request URL or body.                      |
| **E032**   | *BAD\_MISSING\_PARAMETERS\_BODY*      | Invalid or missing parameters in the request body.                             |
| **E033**   | *INVALID\_PARAMETER\_BODY*            | Invalid parameter in message body.                                             |
| **E035**   | *INVALID\_ACTION\_BODY*               | Invalid action in message body.                                                |
| **E040**   | *BAD\_COMBINATION\_PARAMETERS\_URL*   | A combination of two or more parameters in the URL is missing or invalid.      |
| **E050**   | *NOT\_FOUND*                          | The resource you were trying to retrieve was not found.                        |
| **E075**   | *DUPLICATE\_REQUEST*                  | The action you are trying to perform is a duplicate.                           |
| **E090**   | *REQUIRED\_PARAMETER\_MISSING*        | A required parameter needed to maintain state is missing.                      |
| **E099**   | *ERROR\_UNKNOWN*                      | Oops! Something went wrong in processing your request. Please contact support. |
| **E100**   | *ERROR*                               | There was an error in processing your request.                                 |
| **E101**   | *ERROR\_IDEMPOTENT\_REQUEST\_RETRY*   | Maximum retry attempt limit of 5 has been reached. Please contact support.     |

## Header Errors

| Error Code | Error Response                                          | Error Description                                                                    |
| :--------- | :------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| **H050**   | *HEADER\_APP\_KEY\_NOT\_FOUND*                          | Client App Key header not found. Contact tech support if you do not have an app key. |
| **H055**   | *HEADER\_APP\_KEY\_INVALID*                             | Client App Key header invalid. Contact tech support.                                 |
| **H060**   | *HEADER\_AUTH\_TOKEN\_NOT\_FOUND*                       | Auth token header not found. Log in first to obtain an auth token.                   |
| **H065**   | *HEADER\_AUTH\_TOKEN\_INVALID*                          | Invalid auth token header. If problem persists, try re-log in.                       |
| **H070**   | *HEADER\_DW\_CUSTOMER\_NOT\_FOUND*                      | DW custom userID header not found. This header is required for this operation.       |
| **H075**   | *HEADER\_DW\_CUSTOMER\_ACCOUNT\_NOT\_FOUND*             | DW custom accountID header not found. This header is required for this operation.    |
| **H080**   | *HEADER\_BEARER\_TOKEN\_ALGORITHM\_MISSING\_INVALID*    | Algorithm in bearer token is missing/invalid.                                        |
| **H081**   | *HEADER\_BEARER\_TOKEN\_ISSUER\_MISSING\_INVALID*       | Issuer in bearer token is missing/invalid.                                           |
| **H082**   | *HEADER\_BEARER\_TOKEN\_ENVIRONMENTS\_MISSING\_INVALID* | Allowed environments in bearer token are missing/invalid.                            |
| **H085**   | *HEADER\_BEARER\_TOKEN\_WEB\_KEY\_NOT\_FOUND*           | Unable to retrieve web key from token key ID.                                        |
| **H090**   | *HEADER\_BEARER\_TOKEN\_INVALID*                        | Bearer token is invalid.                                                             |
| **H100**   | *HEADER\_BEARER\_TOKEN\_ERROR*                          | Bearer token error. Contact tech support.                                            |

## Instrument Errors

| Error Code | Error Response                        | Error Description                                            |
| :--------- | :------------------------------------ | :----------------------------------------------------------- |
| **I010**   | *INSTRUMENT\_INVALID\_TRADE\_STATUS*  | Invalid trade status.                                        |
| **I011**   | *INSTRUMENT\_INVALID\_EXCHANGE\_ID*   | Invalid exchangeID.                                          |
| **I012**   | *INSTRUMENT\_INVALID\_TYPE*           | Invalid instrument type.                                     |
| **I013**   | *INSTRUMENT\_INVALID\_ORDER\_SIZE*    | Invalid order size(min/max/step).                            |
| **I014**   | *INSTRUMENT\_MISSING\_SYMBOL*         | Symbol is required when updating the instrument image.       |
| **I015**   | *INSTRUMENT\_UPDATE\_FORBIDDEN*       | Some fields of an instrument can not be updated.             |
| **I016**   | *INSTRUMENT\_GROUP\_INVALID\_TYPE*    | Invalid instrument group type.                               |
| **I017**   | *INSTRUMENT\_GROUP\_INVALID\_STATUS*  | Invalid instrument group status.                             |
| **I018**   | *INSTRUMENT\_GROUP\_INVALID\_ID*      | Invalid instrument group ID.                                 |
| **I019**   | *INSTRUMENT\_GROUP\_INVALID\_SYMBOLS* | Invalid symbol(s) in the request body.                       |
| **I050**   | *INSTRUMENT\_NOT\_FOUND*              | The instrument(s) you were trying to retrieve was not found. |

## Idempotency Errors

| Error Code | Error Response                      | Error Description                                                                 |
| :--------- | :---------------------------------- | :-------------------------------------------------------------------------------- |
| **IK010**  | *IDEMPOTENCY\_KEY\_INVALID\_LENGTH* | Idempotency Key too short. Must be at least 16 characters.                        |
| **IK025**  | *IDEMPOTENCY\_KEY\_BAD\_TOKEN*      | Error in processing idempotency request token. Contact support.                   |
| **IK075**  | *IDEMPOTENCY\_KEY\_RESPONSE\_ERROR* | Something went wrong in retrieving cached response. Aborting with error response. |

## Bank Account Errors

| Error Code | Error Response                         | Error Description                                                                   |
| :--------- | :------------------------------------- | :---------------------------------------------------------------------------------- |
| **K050**   | *BANK\_ACCOUNT\_NOT\_FOUND*            | Bank account temporarily disabled or not found. Contact customer support.           |
| **K075**   | *BANK\_ACCOUNT\_INVALID*               | Invalid bank account for this operation. Contact customer support if this persists. |
| **K100**   | *BANK\_ACCOUNT\_ERROR*                 | Bank account error.                                                                 |
| **K110**   | *BANK\_ACCOUNT\_INVALID\_PLAID\_TOKEN* | Plaid processor token provided is invalid.                                          |

## Login Errors

| Error Code | Error Response                     | Error Description                                                                       |
| :--------- | :--------------------------------- | :-------------------------------------------------------------------------------------- |
| **L010**   | *LOGIN\_2FA\_MISSING*              | Missing Two Factor Authentication information.                                          |
| **L011**   | *LOGIN\_2FA\_TYPE\_SELECTION*      | Missing or invalid 2FA type selection.                                                  |
| **L015**   | *LOGIN\_PHONE\_NUMBER\_NOT\_VALID* | Phone number format not recognized. Use email verification or contact customer support. |
| **L019**   | *LOGIN\_MISSING\_TEMP\_CODE*       | Missing temp code. Provide a valid temp code issued at log in.                          |
| **L020**   | *LOGIN\_INVALID\_TEMP\_CODE*       | Invalid temp code. Please log in again.                                                 |
| **L022**   | *LOGIN\_NULL\_TEMP\_CODE*          | Temp code has already been used or was never issued. Please log in again.               |
| **L024**   | *LOGIN\_NO\_HEARTBEAT*             | Auth Token expired due to inactivity. Please log in again.                              |
| **L025**   | *LOGIN\_EXPIRED*                   | Auth Token expired. Please log in Again.                                                |
| **L050**   | *LOGIN\_INVALID*                   | Invalid Credentials.                                                                    |
| **L065**   | *LOGIN\_INVALID\_TOKEN*            | Invalid auth token. Please log in again.                                                |
| **L070**   | *LOGIN\_2FA\_REQUIRED*             | Two factor authentication required for login. Re-login via 2FA.                         |
| **L075**   | *LOGIN\_LOGGED\_OUT*               | User already logged out. Please log in again.                                           |
| **L090**   | *LOGIN\_AUTH\_FAILURE*             | Something went wrong in trying to retrieve your auth token. Please log in again.        |
| **L100**   | *LOGIN\_FAILURE*                   | Login Failure.                                                                          |

## Managed Account Errors

| Error Code | Error Response                              | Error Description                                                 |
| :--------- | :------------------------------------------ | :---------------------------------------------------------------- |
| **M010**   | *MANAGED\_ACCOUNT\_INVALID*                 | The riaID is not valid or not active.                             |
| **M011**   | *MANAGED\_ACCOUNT\_CLIENT\_INVALID*         | The accountID/accountNo does not belong to the master account.    |
| **M012**   | *MANAGED\_ACCOUNT\_INVALID\_CASH\_TRANSFER* | The riaID is not valid for transferring cash from/to sub account. |
| **M013**   | *MANAGED\_ACCOUNT\_INACTIVE\_ACCOUNT*       | The account is NOT active.                                        |

## Instant Funding Errors

| Error Code | Error Response                          | Error Description                                                    |
| :--------- | :-------------------------------------- | :------------------------------------------------------------------- |
| **N010**   | *INSTANT\_FUNDING\_NO\_ACCOUNT*         | Instant funding account not set. Contact administrator.              |
| **N015**   | *INSTANT\_FUNDING\_EXISTING\_ACCOUNT*   | Instant funding account already exists. Contact administrator.       |
| **N020**   | *INSTANT\_FUNDING\_ACCOUNT\_INACTIVE*   | Instant funding account is disabled. Contact administrator.          |
| **N030**   | *INSTANT\_FUNDING\_INVALID\_AMOUNT*     | Invalid amount for deposit.                                          |
| **N050**   | *INSTANT\_FUNDING\_NO\_FUNDS*           | Instant funding threshold reached. Contact administrator.            |
| **N050**   | *INSTANT\_FUNDING\_INSUFFICIENT\_FUNDS* | Insufficient funds in IFA account. Contact administrator.            |
| **N060**   | *FUND\_INVALID\_FUND\_TYPE*             | Invalid fund type.                                                   |
| **N100**   | *INSTANT\_FUNDING\_ERROR*               | There was an error in processing the instant money movement request. |

## Order Errors

| Error Code | Error Response                        | Error Description                                                                     |
| :--------- | :------------------------------------ | :------------------------------------------------------------------------------------ |
| **O005**   | *ORDER\_INVALID\_ORDER\_TYPE*         | Invalid order type.                                                                   |
| **O006**   | *ORDER\_INVALID\_ORDER\_SIDE*         | Invalid order side.                                                                   |
| **O010**   | *ORDER\_INVALID\_STOP\_REQUEST*       | Incomplete stop order. One or more parameters may be missing or invalid.              |
| **O011**   | *ORDER\_INVALID\_LIMIT\_REQUEST*      | Incomplete limit order. One or more parameters may be missing or invalid.             |
| **O012**   | *ORDER\_INVALID\_MARKET\_REQUEST*     | Invalid market order. One or more parameters may be missing or invalid.               |
| **O015**   | *ORDER\_EITHER\_QTY\_OR\_CASH*        | Invalid order. Enter one from amount OR order quantity.                               |
| **O016**   | *ORDER\_INVALID\_ORDER\_METHOD*       | Invalid order method.                                                                 |
| **O017**   | *ORDER\_INVALID\_MIT\_REQUEST*        | Incomplete `marketIfTouched` order. One or more parameters may be missing or invalid. |
| **O018**   | *ORDER\_INVALID\_TIF\_REQUEST*        | Invalid Time In Force. One or more parameters may be missing or invalid.              |
| **O019**   | *ORDER\_INVALID\_EXPIRATION\_REQUEST* | Invalid order expiration. One or more parameters may be missing or invalid.           |
| **O050**   | *ORDER\_NOT\_FOUND*                   | Requested order resource was not found.                                               |
| **O098**   | *ORDER\_ACCOUNT\_ERROR*               | Orders can only be placed on open accounts.                                           |
| **O099**   | *ORDER\_ERROR*                        | There was an error processing your order.                                             |
| **O123**   | *ORDER\_EXPIRED*                      | The order has expired.                                                                |
| **O124**   | *DIVIDENDS*                           | The corporate action was canceled, specifically dividends.                            |

## Permissions Errors

| Error Code | Error Response                                   | Error Description                                                                                               |
| :--------- | :----------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **P020**   | *PERMISSIONS\_NO\_PERMISSIONS*                   | No permissions have been assigned to this user. Contact your administrator.                                     |
| **P045**   | *PERMISSIONS\_GROUP\_ID\_NOT\_FOUND*             | There was an error retrieving your permission group. If problem persists, contact your administrator.           |
| **P050**   | *PERMISSION\_NOT\_FOUND*                         | Requested/assigned permission not found. Contact your administrator.                                            |
| **P075**   | *PERMISSIONS\_UNAUTHORIZED*                      | User does not have permissions to perform this operation. Contact your administrator.                           |
| **P087**   | *PERMISSIONS\_RESOURCE\_PARENTIB\_NOT\_ASSIGNED* | No parentIB assigned to the resource entity. Contact your administrator.                                        |
| **P088**   | *PERMISSIONS\_BO\_PARENTIB\_NOT\_ASSIGNED*       | No parentIB assigned to the back office user. Contact your administrator.                                       |
| **P090**   | *PERMISSIONS\_PARENTIB\_NO\_MATCH*               | The operator user and the operated resource do not belong to the same organization. Contact your administrator. |

## Reports Errors

| Error Code | Error Response          | Error Description                                                       |
| :--------- | :---------------------- | :---------------------------------------------------------------------- |
| **R010**   | *REPORT\_INVALID\_DATE* | Invalid date.There are no reports available for the date(s) provided.   |
| **R011**   | *REPORT\_FUTURE\_DATE*  | Date in future.There are no reports available for the date(s) provided. |

## Records Errors

| Error Code | Error Response               | Error Description                                                                      |
| :--------- | :--------------------------- | :------------------------------------------------------------------------------------- |
| **S100**   | *SEARCH\_NO\_RECORDS\_FOUND* | No records were found for the given search criteria. Modify your search and try again. |

## Product Errors

| Error Code | Error Response                        | Error Description                                      |
| :--------- | :------------------------------------ | :----------------------------------------------------- |
| **T010**   | *PRODUCT\_RIA\_ID\_INVALID\_MISSING*  | The riaID of product is missing or invalid.            |
| **T011**   | *PRODUCT\_TYPE\_INVALID\_MISSING*     | A required type of product is missing or invalid.      |
| **T012**   | *PRODUCT\_FUND\_ID\_INVALID\_MISSING* | A required fundID of product is missing or invalid.    |
| **T013**   | *PRODUCT\_OVERWEIGHT\_ERROR*          | A total weight of product is over 100%.                |
| **P050**   | *PRODUCT\_NOT\_FOUND*                 | The product you were trying to retrieve was not found. |

## Quotes Errors

| Error Code | Error Response       | Error Description                                       |
| :--------- | :------------------- | :------------------------------------------------------ |
| **Q050**   | *QUOTES\_NOT\_FOUND* | The quote you were trying to retrieve is not available. |
| **Q100**   | *QUOTES\_ERROR*      | There was an error in retrieving quotes.                |

## User Errors

| Error Code | Error Response                           | Error Description                                                                              |
| :--------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------- |
| **U010**   | *USERNAME\_NOT\_UNIQUE*                  | The username already exists.                                                                   |
| **U025**   | *USER\_INVALID\_MISSING\_PARAMETER*      | Invalid or missing required parameter on the user. Refer to the API documentation for details. |
| **U040**   | *USER\_INFO\_DOCUMENT\_MISSING*          | A required document for the specified user or account type is missing incomplete.              |
| **U045**   | *USER\_NO\_KYC*                          | The user is not in the KYC Queue.                                                              |
| **U050**   | *USER\_NOT\_FOUND*                       | The user you were trying to retrieve was not found. Please check the User ID and try again.    |
| **U060**   | *USER\_NO\_PARENTIB\_SET*                | User does not have a parentIB set. Contact your administrator.                                 |
| **U062**   | *USER\_INVALID\_PARENTIB\_SET*           | Unable to find parentIB associated with the user. Contact your administrator.                  |
| **U064**   | *USER\_NO\_REFERRER\_PARENTIB\_SET*      | Referrer does not have a parentIB set. Contact your administrator.                             |
| **U065**   | *USER\_INVALID\_REFERRER\_PARENTIB\_SET* | Unable to find parentIB associated with the referrer. Contact your administrator.              |
| **U070**   | *USER\_NO\_PRIVILEGES*                   | User does not have permissions to access this information. Contact your administrator.         |
| **U072**   | *USER\_NO\_ACCESS*                       | User is not allowed to access this resource.                                                   |
| **U075**   | *USER\_UNABLE\_RETRIEVE*                 | Unable to validate the user associated with the log in information.                            |
| **U080**   | *USER\_INVALID\_ID\_NO*                  | The specified identification value is not appropriate for the specified Citizenship.           |
| **U090**   | *USER\_MISSING\_INFORMATION*             | User is missing required information to process this request.                                  |
| **U100**   | *USER\_ERROR*                            | There was an error in retrieving the user.                                                     |
| **U101**   | *USER\_ERROR*                            | User's info has not been submitted for KYC.                                                    |
| **U102**   | *USER\_PENDING*                          | User's info required.                                                                          |
| **U103**   | *USER\_KYC\_PENDING*                     | KYC verification failed.                                                                       |
| **U104**   | *USER\_INFO\_REQUIRED*                   | User is waiting for approval.                                                                  |
| **U105**   | *USER\_REJECTED*                         | There was an error in processing the deposit request.                                          |
| **U106**   | *USER\_PENDING\_APPROVAL*                | User is waiting for approval.                                                                  |

## Payment Errors

| Error Code | Error Response                             | Error Description                                         |
| :--------- | :----------------------------------------- | :-------------------------------------------------------- |
| **Y025**   | *PAYMENT\_NOT\_ALLOWED*                    | Unable to initiate/authorize payment.                     |
| **Y044**   | *PAYMENT\_DEPOSIT\_AMOUNT\_BELOW\_MINIMUM* | Deposit does not meet the required minimum amount.        |
| **Y050**   | *PAYMENT\_REDEMPTION\_NOT\_FOUND*          | The redemption you were trying to retrieve was not found. |
| **Y051**   | *PAYMENT\_DEPOSIT\_NOT\_FOUND*             | The deposit you were trying to retrieve was not found.    |
| **Y060**   | *PAYMENT\_RECURRING\_DETAILS\_NOT\_FOUND*  | The recurring deposit details were not found.             |
| **Y075**   | *PAYMENT\_INSUFFICIENT\_BALANCE*           | The redemption amount is more than the cash available.    |
| **Y099**   | *PAYMENT\_DEPOSIT\_ERROR*                  | The redemption you were trying to retrieve was not found. |

## KYC Document Errors

| Error Code | Error Response               | Error Description                                                                                                                                                      |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **K001**   | *AGE\_VALIDATION*            | The age calculated from the documents date of birth point is greater than or equal to the minimum accepted age set at the account level                                |
| **K002**   | *POOR\_PHOTO\_QUALITY*       | "Poor photo quality. ID may be too dark, damaged, blurry, cut off, or have a glare"                                                                                    |
| **K003**   | *POOR\_DOC\_QUALITY*         | "Abnormal document quality. ID may have obscured data points, obscured security features, a corner removed, punctures, or watermarks obscured by digital text overlay" |
| **K004**   | *SUSPECTED\_DOCUMENT\_FRAUD* | Tampering and forgery found on the document                                                                                                                            |
| **K005**   | *INCORRECT\_SIDE*            | The incorrect side of the document had been uploaded. Choose the correct side of the document and re-upload                                                            |
| **K006**   | *NO\_DOC\_IN\_IMAGE*         | "No document was found in the image, or there is a blank image"                                                                                                        |
| **K007**   | *TWO\_DOCS\_UPLOADED*        | Two different documents were submitted as the same document type                                                                                                       |
| **K008**   | *EXPIRED\_DOCUMENT*          | Document is expired or invalid format of expiry date                                                                                                                   |
| **K009**   | *MISSING\_BACK*              | The back of the document is missing                                                                                                                                    |
| **K010**   | UNSUPPORTED\_DOCUMENT        | Document is not supported                                                                                                                                              |
| **K011**   | *DOB\_NOT\_MATCH\_ON\_DOC*   | The DOB listed on the customer’s ID is not the same DOB listed on the customer’s application                                                                           |
| **K012**   | *NAME\_NOT\_MATCH\_ON\_DOC*  | The Name on the the customer’s ID is not the same Name listed on the customer’s application                                                                            |
| **K050**   | *INVALID\_DOCUMENT*          | Unable to process your document. File is corrupted and can't be opened.                                                                                                |

## KYC Non-Document Errors

| Error Code | Error Response             | Error Description                                                                                                                                |
| ---------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **K101**   | *ADDRESS\_NOT\_MATCH*      | No match found for address or invalid format in address                                                                                          |
| **K102**   | *SSN\_NOT\_MATCH*          | No match found for Social Security Number                                                                                                        |
| **K103**   | *DOB\_NOT\_MATCH*          | No match found for Date of Birth                                                                                                                 |
| **K104**   | *NAME\_NOT\_MATCH*         | No match found for firstName / lastName or invalid characters found                                                                              |
| **K106**   | *SANCTION\_WATCHLIST*      | User is under sanction watch list                                                                                                                |
| **K107**   | *SANCTION\_OFAC*           | User is found in OFAC SDN list                                                                                                                   |
| **K108**   | *INVALID\_PHONE\_NUMBER*   | The phone number listed on the customer’s application is not a valid number of digits for a phone number                                         |
| **K109**   | *INVALID\_EMAIL\_ADDRESS*  | The emailID listed on the customer’s application is not valid or unable to verify in watch list.                                                 |
| **K110**   | *INVALID\_NAME\_TOO\_LONG* | The first name or last name listed on the customer's application is not valid. First name or last name should not be greater than 36 characters. |
| **K111**   | *UNSUPPORTED\_COUNTRY*     | The KYC is not supported in the country.                                                                                                         |
| **K801**   | *AGED\_ACCOUNT*            | KYC is not verified by user within 30 days                                                                                                       |
| **K802**   | *ACCOUNT\_INTEGRITY*       | Account information provided may not be legitimate and/or is being used by multiple account holders                                              |
| **U999**   | *UNKNOWN*                  | Unrecognized error                                                                                                                               |

## Bars Errors

| Error Code | Error Response                                 | Error Description                                                                             |
| :--------- | :--------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **B100**   | *INVALID\_REQUEST\_FOR\_DAILY\_BARS*           | The number of bars requested has exceeded the maximum allowed of 10 Years for Daily bars.     |
| **B100**   | *INVALID\_REQUEST\_FOR\_ONE\_MINUTE\_BARS*     | The number of bars requested has exceeded the maximum allowed of 1 Month for 1 minute bars.   |
| **B100**   | *INVALID\_REQUEST\_FOR\_FIVE\_MINUTES\_BARS*   | The number of bars requested has exceeded the maximum allowed of 2 Months for 5 minutes bars. |
| **B100**   | *INVALID\_REQUEST\_FOR\_THIRTY\_MINUTES\_BARS* | The number of bars requested has exceeded the maximum allowed of 1 Year for 30 minutes bars.  |
| **B100**   | *INVALID\_REQUEST\_FOR\_ONE\_HOUR\_BARS*       | The number of bars requested has exceeded the maximum allowed of 2 Years for 1 hour bars.     |
| **B100**   | *INVALID\_REQUEST\_FOR\_WEEKLY\_BARS*          | The number of bars requested has exceeded the maximum allowed of 20 Years for Weekly bars.    |
| **OT002**  | *ONE\_TICK\_BARS\_REQUEST\_EXCEEDED*           | The Number of Bars request has exceeded the maximum allowed Bars.                             |
| **OT003**  | *OTHER\_ONE\_TICK\_ERRORS*                     | Unable to retrieve bars data.                                                                 |

## Asset Transfer Errors

| Error Code | Error Response                     | Error Description                                                        |
| :--------- | :--------------------------------- | :----------------------------------------------------------------------- |
| **T003**   | *ASSETS\_TRANSFER\_NEGATIVE\_CASH* | Assets Transfer cannot initiate because of negative cash in the account. |
| **T004**   | *ASSETS\_TRANSFER\_REJECTED*       | Assets Transfer cannot initiate.                                         |
| **T005**   | *ASSETS\_TRANSFER\_UNAUTHORIZED*   | Unauthorized to initiate Assets Transfer.                                |