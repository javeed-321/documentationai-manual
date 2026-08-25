---
updatedAt: 2025-09-05T18:36:27.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Card Lifecycle

Below are details of the card lifecycle and descriptions for all statuses a card could be in:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Action
      </th>

      <th style={{ textAlign: "left" }}>
        Card Status
      </th>

      <th style={{ textAlign: "left" }}>
        Status Meaning
      </th>

      <th style={{ textAlign: "left" }}>
        How?
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Physical card has been requested
      </td>

      <td style={{ textAlign: "left" }}>
        CREATED
      </td>

      <td style={{ textAlign: "left" }}>
        Note: Applicable to Physical Cards only

        Card has been successfully requested & processed.
      </td>

      <td style={{ textAlign: "left" }}>
        [Create a new physical card](https://modulr.readme.io/reference/createphysicalcard)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Virtual card has been created

        OR

        Physical card has been activated
      </td>

      <td style={{ textAlign: "left" }}>
        ACTIVE
      </td>

      <td style={{ textAlign: "left" }}>
        Note: All Virtual Cards are immediately Active. 

        Card can be used for new authorisations
      </td>

      <td style={{ textAlign: "left" }}>
        [Create a new card](https://modulr.readme.io/reference/createcard)

        [Active physical card](https://modulr.readme.io/reference/activatecard)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card has been blocked
      </td>

      <td style={{ textAlign: "left" }}>
        BLOCKED
      </td>

      <td style={{ textAlign: "left" }}>
        If you wish to temporarily block the card to prevent any new authorisations against that card, you can block it.

        Please note that blocking the card does not prevent already approved authorisations from settling.
      </td>

      <td style={{ textAlign: "left" }}>
        [Block an existing card](https://modulr.readme.io/reference/blockcard)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card has been unblocked
      </td>

      <td style={{ textAlign: "left" }}>
        ACTIVE
      </td>

      <td style={{ textAlign: "left" }}>
        When the card is unblocked, it can be used for new authorisations again
      </td>

      <td style={{ textAlign: "left" }}>
        [Unblock an existing card](https://modulr.readme.io/reference/unblockcard)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card has been blocked by issuer
      </td>

      <td style={{ textAlign: "left" }}>
        SUSPENDED
      </td>

      <td style={{ textAlign: "left" }}>
        The card has been temporarily restricted from making any new authorisations following a decision from issuer e.g. in the event of suspicious card activity.

        The card can only be set to Active again by the card issuer.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card Expired
      </td>

      <td style={{ textAlign: "left" }}>
        EXPIRED
      </td>

      <td style={{ textAlign: "left" }}>
        Card has Expired.

        This is a final card status and would not change.
      </td>

      <td style={{ textAlign: "left" }}>
        Cards expire automatically at the end of the specified expiry month which is provided at the time of card creation
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Card has been Cancelled
      </td>

      <td style={{ textAlign: "left" }}>
        CANCELLED
      </td>

      <td style={{ textAlign: "left" }}>
        Card has been Cancelled.

        This is a final card status and would not change.

        Cancelling a card is similar to Blocking, with the main difference being that card cancellation is **irreversible**action. 
      </td>

      <td style={{ textAlign: "left" }}>
        [Cancel an existing card](https://modulr.readme.io/reference/cancelcard)
      </td>
    </tr>
  </tbody>
</Table>

> 📘 In general, all virtual cards will start as active whereas physical cards start as created and become active only after successful activation. All cards will either eventually automatically expire or will get manually cancelled, whichever comes first