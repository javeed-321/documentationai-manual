# Invoicing API Documentation

> Use the Akamai Invoicing API to develop your own tools to track invoice files, and keep others updated about their status.

Fetch the complete documentation index at: https://techdocs.akamai.com/invoicing/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Notifications
- [Create a notification](https://techdocs.akamai.com/invoicing/reference/post-notification.md): Creates a notification informing a set of users about new invoices, credit memos, or debit memos for a set of contracts. Each notification needs to specify a unique set of contracts. The request yields an error if the set of `contractId` values matches that of another notification.
- [List notifications for an account](https://techdocs.akamai.com/invoicing/reference/get-notifications.md): Returns notifications for the current account. Notifications inform a set of users whenever there are changes to an invoice, credit memo, or debit memo.
- [Get a notification](https://techdocs.akamai.com/invoicing/reference/get-notification.md): Accesses a specific notification, for example when making modifications to a specific notification.
- [Modify a notification](https://techdocs.akamai.com/invoicing/reference/put-notification.md): Updates a notification. Any read-only members retained from a GET operation are ignored on subsequent PUTs.
- [Remove a notification](https://techdocs.akamai.com/invoicing/reference/delete-notification.md): Deletes a notification.
