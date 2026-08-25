Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.39

## API Release 1.39

| Environment | Released           |
| :---------- | :----------------- |
| UAT         | RELEASED           |
| PRODUCTION  | RELEASED - 6/23/22 |

### **API Update - Managed Accounts - Allocations API**

For partners using the POST `https://bo-api.drivewealth.io/back-office/managed/allocations` endpoint  - We recently identified a bug in the `comment` field of this API endpoint and have applied a fix and introduced a new field - `clientComment` -  in the /GET request.

Prior to this fix, when a comment was passed, the response returned in the GET `https://bo-api.drivewealth.io/back-office/managed/allocations/{allocationID}` was an internal DriveWealth comment. We have now updated the response to include both the internal DriveWealth comment and the comment that was supplied by the /POST request now called `clientComment` on the /GET request. The payload from the /POST request will not change however the /GET will now include `comment` and `clientComment` inside of the allocations object.

It is advised that you make the necessary updates on your end to avoid any potential issues.\
Please let us know if you have any questions or seek clarifications.