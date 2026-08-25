---
updatedAt: 2025-08-20T23:31:04.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Events via SQS

DriveWealth leverages Amazon Simple Queue Service (SQS) to asynchronously notify integrators about different changes in the system (ex. an order status being updated).

SQS is an Amazon-hosted queue that allows DriveWealth to publish messages to and subsequently allow integrators to read messages. To learn more about SQS, see [here](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html). By taking advantage of these event notifications, our integrators can greatly reduce the total number of API requests made to the DriveWealth infrastructure.

## Getting access

To get access to an SQS queue, you'll need to supply DriveWealth with the ARN of an IAM role or IAM user. To learn more about creating an IAM roles or IAM users, see [here](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html).

User Example: `arn:aws:iam::123456789012:user/JohnDoe`\
Role Example: `arn:aws:iam::123456789012:role/service-role/dw_sdx_sqs_role`

If a partner does not use SQS they can receive similar information by calling the DriveWealth REST APIs. Web hooks and other integration techniques are not available; partners must use SQS or the APIs.

## Example of Events

DriveWealth publishes events for many internal resource changes. Each event object is structured in similar fashion.

```json order.completed
{
    "id": "event_215cffec-112b-17fd-8c64-36ef645d9e99",
    "type": "orders.completed",
    "timestamp": "2023-01-12T14:30:02.239726118Z",
    "payload": {
        "id": "KA.7d7e5fe8-12dc-468c-b96f-a111e3c708c6",
        "orderNo": "KAXG000111",
        "type": "MARKET",
        "side": "SELL",
        "status": "FILLED",
        "symbol": "C",
        "averagePrice": 49.02,
        "averagePriceRaw": 49.02,
        "totalOrderAmount": 49.02,
        "cumulativeQuantity": 1,
        "quantity": 1,
        "fees": 2.99,
        "orderExpires": "2023-01-12T21:00:00.000Z",
        "createdBy": "88b65bf4-9b68-4231-93b8-b6839fec110c",
        "userID": "88b65bf4-9b68-4231-93b8-b6839fec110c",
        "accountID": "88b65bf4-9b68-4231-93b8-b6839fec110c.1635269702783",
        "accountNo": "TTC000005",
        "created": "2023-01-12T13:59:01.778Z",
        "lastExecuted": "2023-01-12T14:30:02.091Z",
        "lastPrice": 49.02,
        "lastShares": 1,
        "lastMarket": "TH"
    }
}
```

### Handling non-sequential Events

Due to the standard, asynchronous queue structure it's highly likely that Events will be received out of sequence. For example: a `FILLED` status `orders.completed` event may be received prior to a `PARTIAL_FILL` `orders.updated` event. To account for this discrepancy, consider where you may need to implement logic handling to determine whether or not to internalize a certain Event, or to ignore one.