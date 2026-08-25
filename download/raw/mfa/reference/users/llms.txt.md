# Akamai MFA Documentation

> Akamai MFA is a workforce MFA service that enables enterprises to provide additional security to the existing identity validation mechanisms for users’ authentication and access to cloud, on-premise, web-based, SaaS, and IaaS applications.

Fetch the complete documentation index at: https://techdocs.akamai.com/mfa/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Users
- [Add a user](https://techdocs.akamai.com/mfa/reference/post-user.md): Create a new user.
- [List users](https://techdocs.akamai.com/mfa/reference/get-users.md): List user accounts configured in Akamai MFA, optionally filtered and paginated.
- [Get a user](https://techdocs.akamai.com/mfa/reference/get-user.md): Get details about a specific user account, including the `userId`, `status`, and `username`. It also lists the `alias` information and `groups` that the user belongs to.
- [Update a user](https://techdocs.akamai.com/mfa/reference/put-user.md): Modify a user's basic information. To add an alias or assign a group to a user, run the [Add an alias to a user](ref:post-alias-to-user) and [Assign groups](ref:post-assign-groups-to-user) operations.
- [Delete a user](https://techdocs.akamai.com/mfa/reference/delete-user.md): Permanently delete a specific user account. You can delete any active user account from your Akamai MFA service. For manually added users, deleting means permanently removing the user accounts together with any enrolled authentication device. User accounts that still exist in the external source directory reappear after the next synchronization.
- [Add an alias to a user](https://techdocs.akamai.com/mfa/reference/post-alias-to-user.md): Add an alternative username for a user.
- [Delete an alias assigned to a user](https://techdocs.akamai.com/mfa/reference/delete-user-alias.md): Permanently delete a user's alias.
- [Assign groups](https://techdocs.akamai.com/mfa/reference/post-assign-groups-to-user.md): Assign a set of groups to a user account. With this operation you can modify the users' group assignment when their role in the organization changes. After you modify the users' group membership, you can manage their access to different integrations at group level.
- [Assign policies](https://techdocs.akamai.com/mfa/reference/post-assign-policies-to-user.md): Assign a set of policies to a user account. With this operation you can modify the users' access privileges when their role in the organization changes. After you modify the users' policy assignation, the users need to meet the requirements of a specific authentication policy before they can access a protected application.
- [Create a bypass code](https://techdocs.akamai.com/mfa/reference/post-bypass-code.md): Generate a new bypass code for a specific user account.
- [List bypass codes](https://techdocs.akamai.com/mfa/reference/get-bypass-codes.md): List all the bypass codes generated for a specific user account.
- [List the user's devices](https://techdocs.akamai.com/mfa/reference/get-user-devices.md): List all the user's authentication devices.
- [Assign a hardware token](https://techdocs.akamai.com/mfa/reference/post-assign-hardware-token.md): Assign a hardware token to a specific user account. To assign a hardware token, you need the token's serial number. You can also unassign and reassign a hardware token from one active user account to another. A hardware token assigned to a user account gets automatically unassigned when the account is deleted, and returns to the pool of available tokens that you can assign to another user.
- [Disable a device](https://techdocs.akamai.com/mfa/reference/post-disable-user-device.md): Deactivate the user's authentication device.
- [Enable a device](https://techdocs.akamai.com/mfa/reference/post-enable-user-device.md): Activate the user's authentication device.
