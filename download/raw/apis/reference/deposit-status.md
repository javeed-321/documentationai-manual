---
updatedAt: 2025-08-20T23:31:45.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Deposit Status

> 📘 Status Number vs. Status Enum
>
> "Status Number" should be referenced when retrieving (`GET`) all deposits requests. "Status Enum" should only be used when updating (`PATCH`) a deposit request.

| Status Description | Status Number | Status Enum    |                                                                                                                                                 |
| :----------------- | :------------ | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Started**        | `0`           | `"STARTED"`    | Deposit has been initiated.                                                                                                                     |
| **Pending**        | `1`           | `"PENDING"`    | Every new deposit for a self-directed account is set to "Pending". From here, the deposit can be marked as "Rejected", "On Hold" or "Approved". |
| **Successful**     | `2`           | `"SUCCESSFUL"` | A Deposit has been successfully processed and completed.                                                                                        |
| **Failed**         | `3`           | `"FAILED"`     | The Deposit was unable to be completed.                                                                                                         |
| **Approved**       | `14`          | `"APPROVED"`   | Once marked as "Approved", the deposit will be processed.                                                                                       |
| **Rejected**       | `15`          | `"REJECTED"`   | Updating a deposit to "Rejected" will immediately set it's status to "Failed".                                                                  |
| **On Hold**        | `16`          | `"ON_HOLD"`    | Status is reserved for deposits that are not ready for processing.                                                                              |
| **Returned**       | `5`           | `"RETURNED"`   | A deposit is marked as returned if DriveWealth receives notification from our bank that the deposit had failed.                                 |
| **Unknown**        | `-1`          |                | Reserved for errors.                                                                                                                            |