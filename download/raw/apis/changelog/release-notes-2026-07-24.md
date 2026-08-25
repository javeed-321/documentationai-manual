Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Release Notes 2026-07-24

# API Release 2026-07-24

| Status                      | Environment |
| :-------------------------- | :---------: |
| 🧱👷🏽‍♂️ Under development |     DEV     |
| 🧪👨🏾‍🔬 Quality testing   |      QA     |
| 👌🤌 Try it                 |     SDX     |
| ✨💃🏻 Prime Time            |     PROD    |

# 🚀 New Features

Accounts API/Users API:

* **FPSL Program Support**
  * Accounts now include `fpslEnrolled` field indicating enrollment status in the Fully Paid Securities Lending program
  * New `FPSL_Disclosure` type for capturing user agreement acceptance

# 🎉 Feature Enhancements

<br />

# 👠🐛 Bug Fixes

<br />

# 🪵 ChangeLog

## Modified endpoints

`POST /accounts`

* Request payload:
* Modified the `200` response:

`GET /accounts/{accountID}`

* Modified the `200` response:

`PATCH /accounts/{accountID}`

* Request payload:
* Modified the `200` response:

`POST /users`

* Request payload:
* Modified the `200` response:

`PATCH /users/{userID}`

* Request payload:

<br />