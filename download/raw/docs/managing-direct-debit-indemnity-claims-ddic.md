---
updatedAt: 2026-06-12T14:20:06.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Managing Direct Debit Indemnity Claims (DDIC)

**Description**

A webhook notification raised whenever a Direct Debit Indemnity Claim (DDIC) has been received or changes status. This webhook enables Partners and Customers to receive real-time notifications when a new DDIC advice is received from Bacs, when a claim is cancelled following a successful challenge, or when a claim settles against a Collateral account.

This webhook can be subscribed to at Partner or Customer level and fires for each status transition on an Indemnity Claim and is available to subscribe from June 30' 2026.

<br />

<Callout icon="📘" theme="info">
  This webhook is part of the DDIC Report Automation project and is available to subscribe from June 30' 2026. It replaces manual email notifications that were previously sent by Payment Operations. Partners or Customers who wish to receive real-time claim notifications must **explicitly subscribe to this webhook.**
</Callout>

**When Does this webhook raised?**

The webhook notification will be raised if subscribed by the Partner/Customer on each of the following status transitions:

| Working day | Event                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NEW         | A new DDIC advice has been received from Bacs and processed by Direct Debit Service. A new Indemnity Claim record has been created.                       |
| CANCELLED   | A cancellation advice has been received from Bacs. The DDIC was successfully challenged and the existing Indemnity Claim record has been cancelled.       |
| SETTLED     | The DDIC settlement transaction has been processed via STS transactional output. The claim amount has been debited from the Partner's Collateral account. |

<br />

**Webhook Details**

The webhook details including examples is available at <https://modulr.readme.io/docs/webhook-direct-debit-collections-ddic#/>

**Retrieving DDIC Details**

DDIC details can be retrieved on receiving a DD\_INDEMNITY\_CLAIM\_STATUS webhook, Customers can use the indemnityClaimId to retrieve the full details of the DDIC via the API:

| Method | Endpoint                                                                              |
| ------ | ------------------------------------------------------------------------------------- |
| GET    | /direct-debit-service/indemnity-claims/{'{indemnityClaimId}'}                         |
| GET    | /direct-debit-service/indemnity-claims?accountId={'{accountId}'}\&status={'{status}'} |

Both endpoints require the DIRECTDEBIT READ permission. Partners can only access claims associated with their own accounts.

<br />

**Challenging a DDIC**

If you believe a DDIC has been raised incorrectly, or you have valid grounds to dispute it, you have until the end of working day 9 (from the day the DDIC advice is made available) to raise a challenge. Challenges are submitted via the Bacs Payment Services Website (PSW).

<br />

**Getting Access to PSW**

All Modulr Service Users can register on the Bacs Payment Services Website using their Service User Number (SUN). To register and access the DDIC challenge functionality, visit:

<https://www.bacs.co.uk>

Once registered, you will need the following PSW privilege to raise challenges: Messaging Engine: DDIC Raise Challenge Manual Entry (input/approve). Your Primary Security Contact (PSC) can assign this privilege to contacts within your organisation.

<br />

**How to Raise a Challenge**

Once logged in to PSW with PKI or ASM credentials, follow these steps:

<Table>
  <thead>
    <tr>
      <th>
        Number
      </th>

      <th>
        Step
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        From the Services menu, go to Submissions & Payment Processing > DDIC Challenge.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        Select the DDIC Advices tab. Search for the relevant DDIC advice and click the Edit icon.
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        On the New DDIC Challenge screen, select a Challenge Reason from the drop-down. Valid grounds for challenge include (among others):

        a). The contract signed by the payer details the amounts and collection dates (evidence attached)

        b). The payer has provided authority for Direct Debit with the service user (evidence attached)

        c). The advance notice details the amounts and collection dates (evidence attached)

        d). Indemnity claim has been submitted more than once or directed to the wrong service user

        e). Amount of the indemnity claim does not match the value of the payments collected on the dates stated
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        Attach supporting evidence by clicking Upload Evidence. Up to 5 files are permitted (jpg, gif or pdf; max 5 MB each). Evidence must be uploaded individually.
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        Click Submit Challenge and confirm. The challenge moves to Pending PSP review status.
      </td>
    </tr>

    <tr>
      <td>
        6
      </td>

      <td>
        The PSP reviews the challenge. If accepted, the DDIC is cancelled automatically and you will receive a CANCELLED webhook. If rejected, you may relodge the challenge up to end of working day 9.
      </td>
    </tr>
  </tbody>
</Table>

<br />

**Key Timelines**

| Working day      | Event                                                                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Day 1            | DDIC advice is made available on PSW. You will receive a `NEW` webhook from Modulr.                                                                                                       |
| By end of Day 9  | Deadline to submit a challenge via PSW. Any DDIC not challenged by this point is automatically accepted by the Bacs system.                                                               |
| By end of Day 11 | PSP must respond to the challenge. If no response is received, the challenge is auto-accepted by Bacs and the DDIC is automatically cancelled. And `CANCELLED` webhook will be triggered. |
| Day 13 (approx.) | If the claim is unchallenged or the challenge is unsuccessful, the DDIC settles against your Collateral account. You will receive a `SETTLED` webhook.                                    |

<br />

**Step-by-Step Guide for DDIC challenge process**

The complete step-by-step guide "**DDIC Challenge Process via PSW — Service User Guide v1.5**" to the DDIC challenge process (v1.5) is available on the Bacs website. Registration is required to access it — all Modulr Service Users can register using their Service User Number (SUN).

The guide covers raising and editing challenges, attaching evidence, authorising requests, requesting Reason Code 7 refunds, and accessing challenge and response reports.

**Unchallenged or Unsuccessful Claims — Collateral Debit**

Any DDIC that is not successfully challenged will result in a debit to your Collateral account. If insufficient funds are held, you are required to provide funds to Modulr immediately in line with the Terms and Conditions of your contract.

A DDIC will settle against your Collateral account in the following circumstances:

1. The claim was not challenged before the end of working day 9 — it is automatically accepted by the Bacs system.
2. A challenge was raised but ultimately rejected by the PSP and not relodged before the day 9 deadline.

When a claim settles, the amount will be debited from your Modulr Collateral account and you will receive a DD\_INDEMNITY\_CLAIM\_STATUS webhook with status SETTLED. The transaction on your account statement will show the DDIC reference and service user reference for your reconciliation (e.g. "Debit DDIC \[DDIC-10223264] ref: AA3473475").

<br />

**Insufficient Funds**

If your Collateral account does not hold sufficient funds to cover the DDIC settlement at the point of debit, you are required to transfer the required amount to Modulr immediately. This obligation is set out in the Terms and Conditions of your contract with Modulr. Failure to do so in a timely manner may result in further action in accordance with those Terms and Conditions.

We strongly recommend monitoring your Collateral account balance — particularly around anticipated DDIC settlement dates (approximately 13 working days after the initial DDIC advice) — to ensure sufficient funds are available.

<br />