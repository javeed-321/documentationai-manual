---
updatedAt: 2025-08-21T06:39:06.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Setting up SSO(with Okta)

This guide walks you through setting up Single Sign-On (SSO) with Okta for seamless access to DriveHub. It outlines the required configurations in both Okta and DriveWealth for a secure, integrated login experience.

## Create SSO App in Okta

1. Create a new application by clicking ‘New App Integration’ button, then selecting ‘OIDC - OpenID Connect’ then select ‘Web Application’ for application type. Select Next to move forward.
2. Fill in the details for the application.
   * Enter a name for the application.
   * Add sign in redirect URI.
   * Skip group assignments if you want to do it later.
3. **Share the ClientID, Client Secret and tenant URL securely with DriveWealth.**
4. Update the group mapping on the Sign-On tab. (Recommend this be set to ‘Starts With’ and ‘DriveHub’)

<Image align="center" className="border" border={true} src="https://files.readme.io/962aa48de0305af4ae0b6655466bf49be2aac6b76290a6833a76fafb35add4e9-image.png" />

<br />

> ❗️
>
> Using the wildcard “\*” and having a user with over 100 groups can break the authentication which is why its recommended to narrow what groups are sent.\
> Refer: [Okta Help Center](https://support.okta.com/help/s/article/how-to-exceed-the-100-groups-limitation-on-a-claim?language=en_US)

## Create Bookmark App

1. In Okta, go to the Browse App Integration Catalog and search for Bookmark.
2. Click on Bookmark App and Add Integration.
3. Enter a name such as DriveHub `<environment name>`
4. Enter the URL for DriveHub.
5. Click done and assign users.

## Create SCIM App in Okta

1. In Okta create a new custom application.
2. Select Secure Web Authentication (SWA).
   * Enter a name for the application.
   * Enter the login page URL, this URL is not used and doesn’t matter but has to have a URL. You can enter <https://www.auth0.com>.
   * Check the box to hide the application from users.
   * Check the box under app type to mark that this is an internal application.
   * Click finish
3. On the general tab, change provisioning from ‘None’ to ‘SCIM’ then save.
4. Click the Provisioning tab.

   * Enter the SCIM connector base URL that was shared.
   * Enter userName for the unique identifier field for users.
   * For supported provisioning actions, select ‘Push New Users’ and ‘Push Profile Updates’.
   * For Authentication Mode, change it to HTTP Header.
   * For the Bearer token, enter the token that was shared.
   * Click ‘Test Connector Configuration’ to verify the connection works.
   * Then click Save.

<Image align="center" className="border" border={true} src="https://files.readme.io/99353caf75fd985163e9c2580651af8c68a0111eaded9c0917d03a112dd5da1e-image.png" />

5. Click on the To App tab.
   * Check enable for ‘Create Users’, Update User Attributes' and ‘Deactivate Users’.

<Image align="center" className="border" border={true} src="https://files.readme.io/dad58796b255df0f631fd477969a2a9c74d903a47447bbb1e795d33a8e709cd8-image.png" />

6. From here you can add groups and assign users and they will sync with Auth0.

## Creating The Role Sync

*❗You will repeat this process for each role. Update display and variable names as appropriate.*

1. Navigate to Directory then Profile Editor and select “User (default)” or another user type if you chose.
2. Click on “Custom” then click “+ Add Attribute”.

<Image align="center" className="border" border={true} src="https://files.readme.io/9dbd53dfd0b399e1df4c7c6cd8b91e3822e6a38d2edee83f9e03263f7fec4425-image.png" />

3. Set the attribute to the following settings:
   * Data type: boolean
   * Display name: DriveHub Role - `<rolename>` (Can be anything you want/need, just recommend)
   * Variable name: dh`<rolename>` (Can be anything you want/need, just recommend)
   * Description: DriveHub Role (Can be anything you want/need, just recommend)
   * User permission: Hide
   * Click “Save Attribute”
   * Click Profile Editor and search for the SCIM application.
   * Click on “Custom” then click “+ Add Attribute”.

<Image align="center" className="border" border={true} src="https://files.readme.io/050efbe0446b10cb2a594b7d041e25955d2c7efe321d132e5cf578684e84bc88-image.png" />

<br />

4. Set the attribute to the following settings:
   * Data type: string
   * Display Name: `<rolename>` Role
   * Variable name: `<rolename>`Role
   * External name: roles. \[type==`<rolename>`role].value
   * External namespace: urn:ietf:params:scim:schemas:core:2.0:User
   * Description: DriveHub Role
   * Attribute type: Personal
   * Click “Save Attribute”
5. Click “Mappings” then click the user type you want to modify.
6. Click Okta User to “name of your application”.

<Image align="center" className="border" border={true} src="https://files.readme.io/427b9ccd82e2e7c068980c7148da9efa850e856bedda2ac3c7713d3ccf104778-image.png" />

7. Scroll to bottom and add the following to each role you want to map over.\
   (user.`<booleanattributename>` == true) ? `<roleID>`  :''

Once your Okta SSO configuration is complete, users will be able to access DriveHub using their Okta credentials. If you have any questions or run into issues, please reach out to your DriveWealth Contact for support.

> 📘 Okta Reference Materials
>
> Auth0 Okta Workforce Reference: [Connect Your Auth0 Application with Okta Workforce Enterprise Connection](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/okta)
>
> Auth0 SCIM Reference: [Inbound SCIM for Okta Workforce Connections](https://auth0.com/docs/authenticate/protocols/scim/inbound-scim-for-okta-workforce-connections)
>
> Okta Role Sync Reference: [Okta Help Center (Lightning)](https://support.okta.com/help/s/article/How-to-add-multivalue-roles-in-SCIM-Cloud-integration?language=en_US)