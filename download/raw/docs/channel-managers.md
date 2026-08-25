---
updatedAt: 2025-11-05T09:35:52.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Managers

## What is a Channel Manager?

A Channel Manager is a third party integrator that works directly with Online Travel Agencies (OTA) to support them in sourcing and fulfilling bookings.  They will be responsible for completing the booking and completing the relevant administration so that the payment can be made to whichever merchant needs payment.

Channel Managers integrating at Modulr will be able to complete the set up of virtual cards on behalf of the OTA (also integrated at Modulr) to the relevant specifications that the OTA has available, and if PCI compliant, will be able to pass on the secured card details to the merchant that requires the payment.

They will also be allowed to add any additional information to each card set up via the custom reference fields that an OTA has created.

> 📘 Set Up Required
>
> Both the OTA and the Channel Manager are required to be onboarded at Modulr to allow the service to work, OTA's wont be able to use this service for a Channel Manager not integrated at Modulr and equally Channel Managers will not be able to pass requests through for OTA's also not onboarded at Modulr

> 🚧 PCI Compliance
>
> If a Channel Manager is not PCI compliant then they will not be able to get the secured card details from any card creation, the Channel Manager will need to follow the [Secure Card Details](https://modulr.readme.io/docs/retrieve-secure-card-details#/) flow to be able to obtain these.