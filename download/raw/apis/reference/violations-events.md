---
updatedAt: 2026-06-26T14:58:26.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Violation Events

## Violations Created

A user's account violation has been created (i.e. Good Faith or Pattern Day Trading). The event returns the total violation count.

> **⚠️ DEPRECATED:** Pattern Day Trading (PDT) violation events are deprecated. Please discontinue use of `patternDayTrades` payloads in production systems.

```json Created [goodfaith]
{
    "id": "event_ad1d0449-47c3-487c-ad6f-f61b6d738e30",
    "type": "violations.created",
    "timestamp": "2019-03-29T14:39:26.797655993Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "currentViolations": {
            "goodFaithViolations": {
                "count": 1
            }
        }
    }
}
```
```json Created [DEPRECATED pattern day trader]
{
    "id": "event_ad1d0449-47c3-487c-ad6f-f61b6d738e30",
    "type": "violations.created",
    "timestamp": "2019-03-29T14:39:26.797655993Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "currentViolations": {
            "patternDayTrades": {
                "count": 1
            }
        }
    }
}
```

## Violations Removed

A user's account violation has been removed (i.e. Good Faith or Pattern Day Trading). The event returns the total violation count.

> **⚠️ DEPRECATED:** Pattern Day Trading (PDT) violation events are deprecated. Please discontinue use of `patternDayTrades` payloads in production systems.

```json Removed [goodfaith]
{
    "id": "event_c28b794f-0ed6-4d86-ad41-4a1a4c78e626",
    "type": "violations.removed",
    "timestamp": "2019-03-29T14:37:46.769052659Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "currentViolations": {
            "goodFaithViolations": {
                "count": 0
            }
        }
    }
}
```
```json Removed [DEPRECATED pattern day trader]
{
    "id": "event_c28b794f-0ed6-4d86-ad41-4a1a4c78e626",
    "type": "violations.removed",
    "timestamp": "2019-03-29T14:37:46.769052659Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "currentViolations": {
            "patternDayTrades": {
                "count": 0
            }
        }
    }
}
```