---
updatedAt: 2025-09-05T18:35:31.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Payment rules

After you have set up your accounts and are able to send and receive payments, you can start automating your payment flows. For example, when a payment is received into an account, you might want to automatically forward 10% of the money to to an external company account and the remaining 90% to an external client account. This can be done using our Payment Rule functionality.

Before creating any rules, you will need to have Accounts and Beneficiaries setup, as rules need a Modulr account to be applied to, and at least one beneficiary's unique reference as a destination.

## Types of rules

### Split

Incoming payments are automatically split into specified percentages to beneficiaries. Split percentages can be specified up to 2 decimal places.

### Conditional Split

Incoming payments are automatically split into specified percentages to beneficiaries until a fixed amount is met. Thereafter, incoming payments can be automatically split to a different set of beneficiaries, or can remain in the account.

### Sweep

At a specified frequency, all money in an account will be automatically transferred into a beneficiary account. This process runs at 3pm UK time. Optional settings allow the rule to only run if the balance is above a certain amount, and to leave a certain amount in the account after the sweep has run.

### Funding

When there is an outgoing payment from an account that does not have sufficient funds, the account can be automatically funded from a secondary account. This rule is only available if the ‘Hold For Funds’ feature has been enabled.

## Examples of payment rules

**Split**\
Move 7.25% of each incoming payment to a beneficiary.

```text
{
    "name": "Split Example",
    "type": "SPLIT",
    "accountId": "A1000001",
    "data": {
        "splits": [
            {
                "percent": "7.25",
                "destinationId": "B1000001"
            }
        ]
    }
}
```

**Conditional Split**\
When an incoming payment is received, transfer 10% to B1000001 and 5% to B1000002 until 100 GBP has been sent to B1000001. The remaining 85% remains in account. Once the amount of 100 GBP has been met, 100% of incoming payments will be transferred to B1000003.

```text
{
    "name": "Conditional Split Example",
    "type": "SPLIT",
    "accountId": "A1000001",
    "data": {
        "splits": [
            {
                "percent": "100",
                "destinationId": "B1000003"
            }
        ],
        "conditionalSplits": [
            {
                "percent": "5",
                "destinationId": "B1000002"
            }
        ],
        "conditionalSplitConfig": {
            "percent": "10",
            "destinationId": "B1000001",
            "conditionAmount": 100
        }
    }
}
```

**Sweep**\
Each day all funds will be automatically transferred to B1000001.

```text
{
    "name": "Sweep Example",
    "type": "SWEEP",
    "accountId": "A1000001",
    "data": {
        "daysToRun": [
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY"
        ],
        "frequency": "Daily",
        "destinationId": "B1000001"
    }
}
```

**Funding**\
The account A1000001 will be funded from secondary account A1000002 if required.

```text
{
    "name": "Funding Example",
    "type": "FUNDING",
    "accountId": "A1000001",
    "data": {
        "sourceId": "A1000002"
    }
}
```

**Example Scenario**

*Collecting 10% commission automatically from each Modulr Customer account into one Modulr account, which then gets transferred daily to an external account.*

To do this you will need to set up a Split rule on all your Customer accounts that transfers 10% of any payment into their accounts into your main Modulr account, then setup a daily Sweep rule on your main Modulr account.