---
updatedAt: 2026-08-04T18:14:30.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Single Sign-On (SSO)

DriveHub supports Single Sign-On (SSO) to allow users to authenticate using their firm's existing Identity Provider (IdP). DriveHub currently supports ***Okta*** and ***Microsoft Entra ID (formerly Azure AD)***.

<Callout icon="📘" theme="info">
  **About SSO Integration**

  SSO streamlines the login process and centralizes identity management. To initiate SSO configuration, contact your DriveWealth Relationship Manager.
</Callout>

Authentication Flows DriveHub supports both IdP-Initiated and SP-Initiated login sequences:

* **IdP-Initiated:** Users access DriveHub directly via their firm's application dashboard (e.g., clicking a "chiclet" in Okta).
* **SP-Initiated:** Users navigate to [dash.drivewealth.com](dash.drivewealth.com) and are redirected to their IdP for authentication.

## User Provisioning (SSO)

This section provides technical guidance for IT Administrators managing user access via SSO.

**Workflow: First-Time Provisioning**

* **Registration:** The IT Admin registers the DriveHub application within the firm's internal IdP for specific users.
* **Auto-Assignment:** DriveHub automatically maps authenticated users to their designated Organization within Auth0.
* **Role Assignment:** New users enter a "no access" state upon their first login. A Team Admin or Partner Principal must then assign the appropriate permissions via the Manage Team page.

<Callout icon="❗️" theme="error">
  **Provisioning Constraints**

  DriveHub currently does not support provisioning via User Groups. IT Administrators must provision SSO access to users on an individual, one-by-one basis.
</Callout>

## Multi-tenant Partner Setup

Firms operating under multiple Introducing Broker Identifiers (IBIDs) must configure access for each corresponding DriveHub Organization individually.

<Callout icon="📘" theme="info">
  About IBID Mapping Each unique IBID maps directly to a specific DriveHub / Auth0 Organization. Administrators must manage team members within the context of each individual Organization.
</Callout>

**User Provisioning Options**

* **Shared Identity:** Use the exact same email address across multiple Organizations. This allows one set of credentials (username, password, MFA) to access different environments, though roles may vary by Organization.
* **Distinct Identities:** Utilize email aliasing (e.g., <user+alpha@firm.com>) to create unique users for each Organization if strict separation is required.

<Callout icon="❗️" theme="error">
  SSO Limitations for Multi-IBID For SSO-enabled partners, each Auth0 Organization requires a unique OpenID Connect (OIDC) connection. Users must be registered with distinct IdPs or maintain separate dashboard "chiclets" for each IBID/Environment combination.
</Callout>