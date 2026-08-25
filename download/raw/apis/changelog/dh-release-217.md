Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# DH Release 2.17

## DH Release 2.17

| Date            | Version | Status       |
| :-------------- | :------ | :----------- |
| August 31, 2023 | 2.17.0  | **RELEASED** |

DriveHub 2.17.0 Release includes a number of new features, feature enhancements and bug fixes.

## Cancel/Rebill Dashboard

The new dashboard in DriveHub is tied to our new Cancel/Rebill API. It enables our Internal Operations team to review and approve requests initiated by partners via API, and enables partners to monitor the status of their requests. This finally enables partners to initiate cancel/rebills on their own, process requests faster, and have transparency

![](https://files.readme.io/2e8011b-Screenshot_2023-09-05_at_12.43.18_PM.png)

## Cancel/Rebill from Ticket Audit

In addition to the primary expectation for our partners to initiate Cancel and Rebills via API, both our Internal Operations team and partners will have the ability to initiate it from the Ticket Audit screen in DriveHub, ultimately hitting the same API and landing on the same dashboard above. At launch, it will only support equities, but we will expand to support Mutual Funds in the future.

![](https://files.readme.io/1e6db6a-Screenshot_2023-09-05_at_12.41.46_PM.png)

## Frozen Account Status

DriveHub users now have the ability to select the Frozen status when editing a customer’s account details. When it is selected, a secondary new field ‘Reason for Status Change’ will display, and the user will be required to select from a list of reasons.

![](https://files.readme.io/1dc3d4d-Screenshot_2023-09-05_at_12.41.33_PM.png)

## Other Enhancements

**Recent Search History -** When user clicks on the search bar, we are now pinning the top 5 most recent unique searches.

![](https://files.readme.io/da7ea80-Screenshot_2023-09-05_at_12.40.53_PM.png)

**Batch -** For the 'Promotion Cash Transfer' and 'Promotion Share Transfer' batch types that our partners have access to, we have implemented restrictions so that they cannot be run on official market holidays.

**Instrument Details Page -** Minor revisions to the details page layout to be updated to our current design standard; surfacing more relevant hero metrics to the top.

**Account Details Metadata -** On Account Details page, added section to pull in account metadata where applicable.

## Bug Fixes

**Tag colors on Transactions tab -** We have resolved an issue with tag colors being inverted and causing accessibility issues.

![](https://files.readme.io/3dc3772-Screenshot_2023-09-05_at_12.45.11_PM.png)

**Broken icons -** We have fixed broken icons across various filter modules across various pages, including Transactions and Margin Calls.

**Date picker discrepancy -** Fixed a discrepancy where the user would select a date, but what was displayed was a day off.

**Batch -** Fixing time restriction and copy to reflect correct time window for partners. We encountered an issue where the time window was showing a full 24 hour period, for example, 12:00AM to 12:00AM. We’ve fixed this to reflect the actual intended time window.