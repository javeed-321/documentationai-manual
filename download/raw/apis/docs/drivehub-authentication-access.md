---
updatedAt: 2026-08-04T18:13:34.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# DriveHub Authentication & Access

DriveHub SSO implements a unified identity management system to ensure secure, compliant access to Drivehub  dashboard. Access is governed by multi-factor authentication (MFA) and supports both standard and federated identity protocols.

# Access Methods

DriveHub supports two primary methods for authenticating users into the platform:

* **Basic Authentication**: Drivehub users manage a unique username and password.
* **Single Sign-On (SSO)**: For enterprise partners, DriveWealth integrates with your firm's Identity Provider (IdP) such as Okta or Microsoft Entra ID.

# Security Requirements

To maintain the integrity of the financial ecosystem, all access methods are subject to the following security constraints:

* Mandatory MFA Multi-Factor Authentication (MFA) is strictly required for all users. Whether using Basic Auth or SSO, a second factor must be verified. Legacy authentication methods that do not support MFA are not permitted.
* Credential Lifespan For Basic Authentication users, invitation and password reset links are valid for 5 calendar days. If a link expires before activation, an administrator must re-trigger the invitation from the Manage Team dashboard.