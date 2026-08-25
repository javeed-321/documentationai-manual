---
updatedAt: 2025-10-24T12:36:27.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Document Events

## Documents Created

A new document has been created for a W8 user.

```json Created
{
  "id": "event_c8e667a2-04ea-4660-a230-6379336f003a",
  "type": "documents.created",
  "object": "TAX",
  "timestamp": "2025-09-29T21:19:45.398Z",
  "payload": {
    "userID": "a4eebg8b-yfd9-4f78-8a87-a99e3t4482f0",
    "documentID": "g1afd865-b327-4ete-a93b-f5d0y718fcc0",
    "taxForm": {
      "type": "W-8BEN",
      "w8expires": "2028-12-31",
      "w8Received": "2025-09-29",
      "s3UrlLink": "https://S3URLLink...."
    }
  }
}
```

A new document has been created for a W9 user.

```json Created
{
  "id": "event_c8e667a2-04ea-4660-a230-6379336f003a",
  "type": "documents.created",
  "object": "TAX",
  "timestamp": "2025-09-29T21:19:45.398Z",
  "payload": {
    "userID": "a4eebg8b-yfd9-4f78-8a87-a99e3t4482f0",
    "documentID": "g1afd865-b327-4ete-a93b-f5d0y718fcc0",
    "taxForm": {
      "s3UrlLink": "https://S3URLLink...."
    }
  }
}
```