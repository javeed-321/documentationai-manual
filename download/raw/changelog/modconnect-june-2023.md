Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# ModConnect - June 2023

<Callout icon="💶" theme="default">
  ### Top picks this month

  * European Payments | Spain and France Branch Enablement
  * Open Banking Payment Initiation Service | UK Expansion
  * Modulr Portal | Invite Your Clients to Complete Applications
</Callout>

<Image align="center" src="https://files.readme.io/45617a9-MC_strip_2.png" />

## New Product Updates

### European Payments | Spain and France Branch Enablement

We have officially completed our branch set-up in both Spain and France, and you will be able to create EUR accounts with Spanish and French IBANs from July. By launching a selection of European IBANs (ES and FR IBANs, in addition to our existing IE and NL IBANs), we will be able to support your expansion ambitions to Europe, allowing you to issue accounts across the region. As a SEPA scheme participant, you can use our EUR accounts to send and receive payments via SEPA Credit Transfer and SEPA CT Instant.

If you would like more information on the above, please contact your Customer Success Manager.

### Open Banking Payment Initiation Service | UK Expansion

From July, you will be able to initiate payments from a wider selection of banks!\
Our Payment Initiation Service is already connected to the UK’s largest banks and building societies but that doesn’t mean our work is done! We regularly review our connectivity to reflect current market demand and your feedback and we are excited to share that we will soon be making new bank integrations available, including Virgin Money, Starling Bank and others.

You can find our full supported bank list and read about how to use the provider list API in our [Developer Guide](https://modulr.readme.io/docs/supported-banks-and-aspsps)Developer Guide.

If you would like more information on the above, please contact your Customer Success Manager.

## Modulr Portal – new features

### Invite Your Clients to Complete Applications

Partners can now invite their clients to complete applications themselves. This removes admin burden and shares the effort with your clients, making the process more efficient and collaborative.

> 📘 Please note
>
> Client Invite is only available to our In-house KYC Partners. Outsourced KYC will still see ‘Save & Exit’ only.

Building further on last month’s update, giving save in-progress capabilities to your applications, as a Partner you can now choose between completing the application yourself, or sending it out to your clients at any point during the application. This can be done by simply selecting the ‘Save or Send’ button in the top right of the screen, then selecting ‘Send to client’ and submitting the form.

<Image align="center" className="border" border={true} src="https://files.readme.io/efd37f3-MODCONNECT_32_-_2.png" />

![](https://files.readme.io/bc1d461-MODCONNECT_32_-_3.png)

You will see a new section in your ‘Applications’ list screen called ‘Sent to client’ which will allow you to keep track of any applications that are currently with your client. Within this section you will also see a 'Resend' button for whenever you need to redirect the application to a different email address.

<Image align="center" className="border" border={true} src="https://files.readme.io/a641fa2-MODCONNECT_32_-_4.png" />

Once the application is completed by you or your client, you will see your customers in your Customers list with a status of IN PROGRESS until CDD checks have been completed.

## Enhancements / Bugs Resolved

### Cards | Update to Card Activities endpoint

You can now easily reconcile your accounts with the new card ORIGINAL CREDIT transaction types, for both APPLIED and SETTLED states, as a result of a change we have made to the[ GET Card Activities endpoint](https://modulr.readme.io/reference/getcardactivities)<https://modulr.readme.io/reference/getcardactivities>).

### Cards | Replace a Card endpoint

You can now initiate a replacement  card for both CANCELLED and EXPIRED state for active accounts.