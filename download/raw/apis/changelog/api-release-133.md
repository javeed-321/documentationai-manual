Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.33

## API Release 1.33

| Environment | Status                       |
| :---------- | :--------------------------- |
| UAT         | RELEASED                     |
| Production  | RELEASED - February 17, 2022 |

### **Tax Forms Updated**

W-9, W-8BEN, and W-8BEN-E form templates have been updated to the newest version.

### **Process Improvement - Reconciliation**

Enhanced reconciliation remediation process for late dividends

### **Process Improvements - Virtual Accounts**

* Enhanced deposit instructions to include details to distinguish between model domestic wire, international wire, or ACH.
* Added validation to provide deposit instructions for live accounts only.
* Users can only deposit money when the account status for the virtual account is listed `OPEN` or `OPEN_NO_NEW_TRADES`.

### **Seasoning Validation**

Validation added to ensure seasoning has been updated prior to creating a financial transaction.

### **Process Improvement - Deposits**

Deposits will be prohibited if the account status is `PENDING`