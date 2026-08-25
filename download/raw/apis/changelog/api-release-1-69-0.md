Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release v1.69.0

Hey, we are back with another release. We are always improving the platform and if you have any questions regarding any release, feel free to contact your relations manager or email us directly at [RMteam@drivewealth.com](mailto:rmteam@drivewealth.com).

| Status           | Environment |
| :--------------- | :---------: |
| ✨💃🏻 Prime Time |     PROD    |

# 🚀 New features

## Commission Rate

We are proud to be introducing commission rate onto our [Orders](https://developer.drivewealth.com/apis/reference/post_orders) API. Starting after this release you will be able to send in a commission rate onto the order and be able to charge a percentage to that assiocated order. The functionality for commission as a dollar value is still acceptable as well just not both at the same time. To learn more check out our [Orders](https://developer.drivewealth.com/apis/reference/post_orders) API.

## Stop Limit

We official now support stop limit [Orders](https://developer.drivewealth.com/apis/reference/post_orders) through our APIs. Check out our [Orders](https://developer.drivewealth.com/apis/reference/post_orders) API for more details.

## Time In Force

We have added support of market on close, immediate or cancel, and fill or kill to our timeinforced options. These are not currently support by the rest API but are support by the fix API.

# 🎉 Feature enhancements

## Linked Bank Accounts

We now have made our [Linked Bank Accounts](https://developer.drivewealth.com/apis/reference/get_users-userid-bank-accounts) API smarter. Starting with this release, if you're try to [remove](https://developer.drivewealth.com/apis/reference/delete_bank-accounts-bankaccountid) a linked bank account and there is are assiocated [Recurring Deposits](https://developer.drivewealth.com/apis/reference/get_funding-recurring-deposits-recurringid) it will not allow you to remove the bank. You must first [remove](https://developer.drivewealth.com/apis/reference/delete_funding-recurring-deposits-recurringid) the all the recurring deposits prior to removing the linked bank account.

## Withdrawal time window

We have extended our [Withdrawal](https://developer.drivewealth.com/apis/reference/post_funding-redemptions) time window until 3:30 PM ET daily, unless its a particular day where the banks close early then that time is 1:30 PM ET. Generally, banks close early the day before a federal holiday. This means that withdrawals recieved by 3:30 PM ET will be processed same day and those place after 3:30 PM ET will be processed next day. The same logic applies for early closing but the time is 1:30 PM ET.

## Instruments

We have update our [Options Expiration](https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid-options-expiration-dates) API we have updated `issuePrice` to `issuePricePercent` and added a bunch of fields like `sector`, `duration`, `nextCallDate`, `debtRankType` and more. Check out our [Option Expiration](https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid-options-expiration-dates) API for more details.

## Depth Of Book

We made a slight change in [Depth Of Book](https://developer.drivewealth.com/apis/reference/getquotedepth) API by changing `datetime` to date. Check out [Depth Of Book](https://developer.drivewealth.com/apis/reference/getquotedepth) API to learn more.

# 👠🐛 Squashing bugs

We are always squashing bugs, but nothing significant during this release that should be called out.

# 🪵 ChangeLog

```markdown
## Modified endpoints

**`GET /accounts/{accountID}/reports/order-history`**

- Modified the `200` response:
    - Changed array property `orders`
        - Modified the schema option `0`

**`GET /accounts/{accountID}/summary`**

- Modified the `200` response:
    - Changed array property `orders`
        - Modified the schema option `0`
    - Changed array property `transactions`
        - Modified the schema option `0`

**`GET /instruments`**

- Modified the `200` response:
    - Changed root array

**`POST /instruments/filter`**

- Modified the `200` response:
    - Changed root array

**`GET /instruments/{symbolOrInstrumentID}`**

- Modified the `200` response:
    - Modified the schema option `0`
    - Modified the schema option `1`
    - Modified the schema option `2`

**`POST /orders`**

- Request payload:
    - Added property `commissionRate`
- Added a new `400` response

**`GET /orders/options`**

- Modified the `200` response:
    - Changed array property `data`
        - Changed nested object schema
            - Changed enum values for property `type`
                - Added values `STOP_LIMIT`

**`POST /quotes/depth`**

- Modified the `200` response:
    - Changed root array
        - Changed nested object schema
            - Changed array property `recentTrades`
                - Changed nested object schema
                    - Added property `date`
                    - Removed property `dateTime`

**`GET /users/{userID}/managed/orders`**

- Modified the `200` response:
    - Changed root array
        - Modified the schema option `0`

**`GET /users/{userID}/managed/orders/summary`**

- Modified the `200` response:
    - Changed array property `orders`
        - Modified the schema option `0`
```