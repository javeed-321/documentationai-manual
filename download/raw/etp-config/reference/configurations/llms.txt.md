# SIA Configuration API Documentation

> Akamai's Secure Internet Access (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events. A distributed configuration encapsulates all the rules for how to process DNS requests for your enterprise.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-config/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Configurations
- [List configurations](https://techdocs.akamai.com/etp-config/reference/get-configs.md): Returns configuration IDs. Use this value for a `configId` parameter in subsequent operations.
- [Onboard a contract](https://techdocs.akamai.com/etp-config/reference/post-config.md): Onboards the specified contract.
- [Create an acknowledgment](https://techdocs.akamai.com/etp-config/reference/post-config-acknowledgment.md): Create an acknowledgment number for the configuration.
- [Get an acknowledgment](https://techdocs.akamai.com/etp-config/reference/get-config-acknowledgment.md): Returns SIA keys.
- [Get a custom error page](https://techdocs.akamai.com/etp-config/reference/get-custom-error-page.md): Gets the custom error page for the configuration.
- [Update a custom error page](https://techdocs.akamai.com/etp-config/reference/put-custom-error-page.md): Updates the custom error page details.
- [Get the first time wizard state](https://techdocs.akamai.com/etp-config/reference/get-firsttimewizard.md): Provides the first time wizard status.
- [Update the first time wizard](https://techdocs.akamai.com/etp-config/reference/put-firsttimewizard.md): Updates the status of the first time wizard.
- [Create a bulk log export destination config](https://techdocs.akamai.com/etp-config/reference/post-log-export-destination.md): Creates a bulk log export destination configuration, which includes three default export schedules. Supports Linode and Azure storage destinations.
- [Get a bulk log export destination config](https://techdocs.akamai.com/etp-config/reference/get-log-export-destination.md): Retrieves the bulk log export destination configuration.
- [List bulk log export schedule configurations](https://techdocs.akamai.com/etp-config/reference/get-log-export-schedules.md): Returns all bulk log export schedule configurations.
- [Disable a bulk log export schedule](https://techdocs.akamai.com/etp-config/reference/post-disable-log-export-schedule.md): Disables a bulk log export schedule. Schedules are disabled by default.
- [Enable a bulk log export schedule](https://techdocs.akamai.com/etp-config/reference/post-enable-log-export-schedule.md): Enables a bulk log export schedule. Schedules are disabled by default.
- [Update a bulk log export destination config](https://techdocs.akamai.com/etp-config/reference/post-update-log-export-destination.md): Updates the bulk log export destination configuration.
- [Create a group-based policy mapping](https://techdocs.akamai.com/etp-config/reference/post-group-policy.md): Creates a group-based policy mapping.
- [List group-based policy mappings](https://techdocs.akamai.com/etp-config/reference/get-group-policy-mappings.md): Returns all group-based policies.
- [Delete all group policy mappings for an IDP](https://techdocs.akamai.com/etp-config/reference/delete-group-policies-for-idp.md): Deletes all group policy mappings for an IDP.
- [Get a group-based policy mapping](https://techdocs.akamai.com/etp-config/reference/get-group-policy.md): Gets a group-based policy mapping.
- [Update a group-based policy mapping](https://techdocs.akamai.com/etp-config/reference/put-group-policy.md): Update a group-based policy mapping.
- [Delete a group-based policy mapping](https://techdocs.akamai.com/etp-config/reference/delete-group-policy.md): Deletes a group-based policy mapping.
