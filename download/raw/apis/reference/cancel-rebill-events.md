---
updatedAt: 2025-09-22T15:01:54.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Cancel Rebill Events

## Cancel Rebill Created

A new cancel rebill was created.

```json Created [cancel]
{
  "id": "event_0aceddf7-6884-4d2c-a6fd-03aec5a9fa7a",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.created",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:51:09.829Z",
  "payload": {
    "status": "PENDING",
    "cancelRebillID": "cxl_rbl_5e05a2a7-d126-4706-a54d-774de4a19876",
    "reason": "FRAUD",
    "type": "CANCEL",
    "comment": "KLZT000433-001",
    "orderID": "KL.57fb70b3-6567-4dba-a572-834d4452f48c",
    "orderNo": "KLZT000433",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "metadata": {
      "orderTrans": "KLZT000433-001"
    },
    "currency": "USD"
  }
}
```
```json Created [price adjustment]
{
  "id": "event_04271306-c936-43aa-922c-2e8795b67e07",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.created",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:59:31.531Z",
  "payload": {
    "status": "PENDING",
    "cancelRebillID": "cxl_rbl_d6b3bf9a-4d7f-4bbf-bcae-c12dc4b1c0e6",
    "reason": "PRICE_ADJUSTMENT_PARTNER",
    "type": "PRICE_ADJUSTMENT",
    "comment": "KLYF000443-001",
    "orderID": "KL.7aa14498-9eb2-40fa-a24f-c84d40bfb975",
    "orderNo": "KLYF000443",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "adjustedPrice": 195.38,
    "metadata": {
      "orderTrans": "KLYF000443-001"
    },
    "currency": "USD"
  }
}
```
```json Created [commission adjustment]
{
  "id": "event_f62ad435-4456-4408-be31-8f76aa5ca937",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.created",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T13:08:48.819Z",
  "payload": {
    "status": "PENDING",
    "cancelRebillID": "cxl_rbl_39406223-7bf7-4891-8771-38d64f8fa602",
    "reason": "PARTNER_TECHNICAL_ERROR",
    "type": "COMMISSION_ADJUSTMENT",
    "orderID": "KL.cb0b570a-c575-43d8-8483-6825ee9212d1",
    "orderNo": "KLRK000499",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.234,
    "price": 192.93,
    "adjustedCommission": 2.49,
    "currency": "USD"
  }
}
```

## Cancel Rebill Updated

A cancel rebill was updated.

```json Updated [cancel]
{
  "id": "event_9e3d5a87-2c09-4833-bebf-f9043b2d34fa",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.updated",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:51:18.421Z",
  "payload": {
    "status": "APPROVED",
    "cancelRebillID": "cxl_rbl_5e05a2a7-d126-4706-a54d-774de4a19876",
    "reason": "FRAUD",
    "type": "CANCEL",
    "comment": "KLZT000433-001",
    "orderID": "KL.57fb70b3-6567-4dba-a572-834d4452f48c",
    "orderNo": "KLZT000433",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "metadata": {
      "orderTrans": "KLZT000433-001"
    },
    "currency": "USD"
    }
  }
```
```json Updated [price adjustment]
{
  "id": "event_0b2f56f6-6435-4a07-93e1-e6c871e1671f",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.updated",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:59:42.736Z",
  "payload": {
    "status": "APPROVED",
    "cancelRebillID": "cxl_rbl_d6b3bf9a-4d7f-4bbf-bcae-c12dc4b1c0e6",
    "reason": "PRICE_ADJUSTMENT_PARTNER",
    "type": "PRICE_ADJUSTMENT",
    "comment": "KLYF000443-001",
    "orderID": "KL.7aa14498-9eb2-40fa-a24f-c84d40bfb975",
    "orderNo": "KLYF000443",
    "rebillOrderID": "KL.cb538a96-63f6-4bca-b31a-b6b01242ed62",
    "rebillOrderNo": "KLEF000410",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "adjustedPrice": 195.38,
    "metadata": {
      "orderTrans": "KLYF000443-001"
    },
    "currency": "USD"
  }
}
```
```json Updated [commission adjustment]
{
  "id": "event_0a4bc149-f530-40a8-8d6e-3f25b1db9bfb",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.updated",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T13:08:57.355Z",
  "payload": {
    "status": "APPROVED",
    "cancelRebillID": "cxl_rbl_39406223-7bf7-4891-8771-38d64f8fa602",
    "reason": "PARTNER_TECHNICAL_ERROR",
    "type": "COMMISSION_ADJUSTMENT",
    "orderID": "KL.cb0b570a-c575-43d8-8483-6825ee9212d1",
    "orderNo": "KLRK000499",
    "rebillOrderID": "KL.44fa4ce1-7981-49a9-92fc-9a16e26b0660",
    "rebillOrderNo": "KLDM000436",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.234,
    "price": 192.93,
    "adjustedCommission": 2.49,
    "currency": "USD"
  }
}
```

## Cancel Rebill Completed

A cancel rebill was completed.

```json Completed [cancel]
{
  "id": "event_4a51fc98-eba5-4907-8709-920ab1e6d1d3",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.completed",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:51:18.423Z",
  "payload": {
    "status": "COMPLETED",
    "cancelRebillID": "cxl_rbl_5e05a2a7-d126-4706-a54d-774de4a19876",
    "reason": "FRAUD",
    "type": "CANCEL",
    "comment": "KLZT000433-001",
    "orderID": "KL.57fb70b3-6567-4dba-a572-834d4452f48c",
    "orderNo": "KLZT000433",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "metadata": {
      "orderTrans": "KLZT000433-001"
    },
    "currency": "USD",
    "clientAccountOrders": {
      "cancelOrderID": "KL.5ac4c496-d9b3-49a6-b7b9-80e462eeb4e4",
      "cancelOrderNo": "KLDX000483"
    },
    "errorAccountOrders": {
      "cancelOrderID": "KL.bd7ed14a-18c0-4cc3-b3de-ca2b74e136fd",
      "cancelOrderNo": "KLDF000519"
    }
  }
}
```
```json Completed [price adjustment]
{
  "id": "event_9cdac0da-454f-41b7-b7c8-e0bccbe4bb39",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.completed",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T12:59:42.738Z",
  "payload": {
    "status": "COMPLETED",
    "cancelRebillID": "cxl_rbl_d6b3bf9a-4d7f-4bbf-bcae-c12dc4b1c0e6",
    "reason": "PRICE_ADJUSTMENT_PARTNER",
    "type": "PRICE_ADJUSTMENT",
    "comment": "KLYF000443-001",
    "orderID": "KL.7aa14498-9eb2-40fa-a24f-c84d40bfb975",
    "orderNo": "KLYF000443",
    "rebillOrderID": "KL.cb538a96-63f6-4bca-b31a-b6b01242ed62",
    "rebillOrderNo": "KLEF000410",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.5,
    "price": 192.93,
    "adjustedPrice": 293.38,
    "metadata": {
      "orderTrans": "KLYF000443-001"
    },
    "currency": "USD",
    "clientAccountOrders": {
      "cancelOrderID": "KL.9710c193-4a31-4702-bd9c-e7b21baaf46f",
      "cancelOrderNo": "KLVA000475",
      "rebillOrderID": "KL.cb538a96-63f6-4bca-b31a-b6b01242ed62",
      "rebillOrderNo": "KLEF000410"
    },
    "errorAccountOrders": {
      "cancelOrderID": "KL.c6fd57e8-8418-4b37-9c12-cb4d78d3f9b0",
      "cancelOrderNo": "KLXT000471",
      "rebillOrderID": "KL.a5b427aa-9576-4a05-b4c5-a59af304b501",
      "rebillOrderNo": "KLSM000404"
    }
  }
}
```
```json Completed [commission adjustment]
{
  "id": "event_772c4a77-e083-4bf3-b6bd-7c13443c27a5",
  "ibID": "64c9fe7b-1c2d-43c0-bb09-a185f6377c4e",
  "type": "transfers.cancelRebill.completed",
  "object": "CANCEL_REBILL",
  "timestamp": "2023-12-09T13:08:57.355Z",
  "payload": {
    "status": "COMPLETED",
    "cancelRebillID": "cxl_rbl_39406223-7bf7-4891-8771-38d64f8fa602",
    "reason": "PARTNER_TECHNICAL_ERROR",
    "type": "COMMISSION_ADJUSTMENT",
    "orderID": "KL.cb0b570a-c575-43d8-8483-6825ee9212d1",
    "orderNo": "KLRK000499",
    "rebillOrderID": "KL.44fa4ce1-7981-49a9-92fc-9a16e26b0660",
    "rebillOrderNo": "KLDM000436",
    "accountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1701707751260",
    "accountNo": "KRHX000841",
    "errorAccountNo": "KRNS000731",
    "errorAccountID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f.1695742201416",
    "userID": "27d5b713-6f56-4f6b-a1c4-0ff7ecbb569f",
    "quantity": 1.234,
    "price": 192.93,
    "adjustedCommission": 2.49,
    "currency": "USD",
    "clientAccountOrders": {
      "cancelOrderID": "KL.7f9d83d7-6b8c-42d2-8c72-7114b506b0cc",
      "cancelOrderNo": "KLHA000541",
      "rebillOrderID": "KL.44fa4ce1-7981-49a9-92fc-9a16e26b0660",
      "rebillOrderNo": "KLDM000436"
    }
  }
}
```