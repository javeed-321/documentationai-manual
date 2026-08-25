Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ACH Deposits & Withdrawals

## ACH Deposits & Withdrawals

Before May 1, 2022, a validation was added to prevent Non US residents from initiating an ACH deposit or withdrawal.

If a customer that is not a US resident attempts to create an ACH deposit or withdrawal request, an [error](https://developer.drivewealth.com/reference/errors-1) will be given:

```json ACH Error - Y025
{
  "errorCode": "Y025",
  "message": "Unable to initiate/authorize payment. Reason: ACH payments are allowed for US residents only."
}
```