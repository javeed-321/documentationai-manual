---
updatedAt: 2026-08-13T09:07:51.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Customer Verification SDK

## Overview

The Modulr Customer Verification SDK manages the complete customer verification journey in the browser. It handles the full lifecycle - checking the current application status, rendering the verification UI when additional information is required, and polling for the final outcome. The SDK is framework-agnostic and integrates with React, Vue, Angular, or plain JavaScript.

***

## Installation

Add the SDK to your project via npm or Yarn:

```bash
npm install @modulrfinance/customer-verification-sdk
# or
yarn add @modulrfinance/customer-verification-sdk
```

***

## Initialization

```javascript
const sdk = await ModulrCustomerVerificationSdk.init({
  applicationId: 'your-application-id',
  token: 'your-token',
  hmac: 'your-hmac',
  //callbacks
});
```

### Required fields

| Field           | Type     | Description                                                |
| --------------- | -------- | ---------------------------------------------------------- |
| `applicationId` | `string` | The Modulr application ID for the customer being verified. |
| `token`         | `string` | Your API token.                                            |
| `hmac`          | `string` | Your HMAC secret.                                          |

### Optional fields

| Field        | Type                                  | Default | Description                                                                       |
| ------------ | ------------------------------------- | ------- | --------------------------------------------------------------------------------- |
| `onSuccess`  | `(result: InitSuccessResult) => void` | —       | Called once when the SDK initialises successfully, before any status event fires. |
| `onEvent`    | `(event: SdkEvent) => void`           | —       | Called whenever the application status changes. See Application Status Events.    |
| `onError`    | `(error: SdkErrorResult) => void`     | —       | Called on any SDK error. Does not suppress the thrown error.                      |
| `production` | `boolean`                             | `true`  | When `false`, the SDK targets sandbox API endpoints.                              |

***

## Opening the SDK

Call `sdk.open()` to present the verification UI after the SDK has initialised.

```javascript
await sdk.open({
  loadingText: 'Processing your details…',
  onSuccess: (result) => console.log('Opened:', result.message),
  onComplete: (data) => console.log('Verification complete:', data),
  onError: (error) => console.error('Open error:', error.message),
  onClose: () => console.log('SDK closed')
});
```

### Optional fields

| Option        | Type                                  | Description                                                                                         |
| ------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `containerId` | `string`                              | ID of the DOM element to mount the UI into. Omit for modal mode.                                    |
| `loadingText` | `string`                              | Text shown in the loading spinner while status polling is active. Omit for a spinner with no label. |
| `onSuccess`   | `(result: OpenSuccessResult) => void` | Called when the SDK opens successfully.                                                             |
| `onComplete`  | `(data: unknown) => void`             | Called when the verification journey is completed.                                                  |
| `onError`     | `(error: SdkErrorResult) => void`     | Called if `open()` fails.                                                                           |
| `onClose`     | `() => void`                          | Called when the SDK closes, either via `sdk.close()` or internally after a terminal status.         |

### Embedded mode

Supply a `containerId` to render the verification UI inside an existing DOM element rather than as a modal overlay.

```html
<div id="customer-verification-host"></div>
```

```javascript
await sdk.open({ containerId: 'customer-verification-host' });
```

***

## Closing the SDK

Call `sdk.close()` to dismiss the SDK programmatically.

```javascript
sdk.close({
  onSuccess: (result) => console.log('Closed:', result.message),
  onError: (error) => console.error('Close error:', error.message)
});
```

### Optional fields

| Option      | Type                                   | Description                              |
| ----------- | -------------------------------------- | ---------------------------------------- |
| `onSuccess` | `(result: CloseSuccessResult) => void` | Called when the SDK closes successfully. |
| `onError`   | `(error: SdkErrorResult) => void`      | Called if `close()` fails.               |

> **Note:** The SDK closes itself automatically after a terminal status is reached. You only need to call `close()` if you want to dismiss it before the verification journey completes.

***

## Angular Example

```typescript
import { Component, OnDestroy, OnInit } from '@angular/core';
import {
  ModulrCustomerVerificationSdk,
  SdkEventType,
  type CustomerVerificationSdkInstance,
  type SdkEvent
} from '@modulr/customer-verification-sdk';

@Component({
  selector: 'app-verification',
  standalone: true,
  template: `
    <button (click)="open()">Start Verification</button>
    <p *ngIf="statusMessage">{{ statusMessage }}</p>
  `
})
export class VerificationComponent implements OnInit, OnDestroy {
  isReady = false;
  statusMessage = '';
  private sdk: CustomerVerificationSdkInstance | null = null;

  async ngOnInit(): Promise<void> {
    this.sdk = await ModulrCustomerVerificationSdk.init({
      applicationId: 'your-application-id',
      token: 'your-token',
      hmac: 'your-hmac',
      onEvent: (event: SdkEvent) => {
        this.statusMessage = event.message;
      },
      onError: (error) => {
        this.statusMessage = error.message;
      }
    });
  }

  async open(): Promise<void> {
    await this.sdk?.open({
      onComplete: () => {
        // triggered on complete
      },
      onClose: () => {
        // triggered on close
      }
    });
  }

  ngOnDestroy(): void {
    this.sdk?.close();
  }
}
```