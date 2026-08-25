Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Release Notes 2026-08-25

The DriveWealth platform is periodically updated with new API features, additional
documentation, and fixes for known issues. These release notes document these updates
with new notes at every release of an updated API or new API.

Subscribe to the DriveWealth Changelog RSS feed. Click below to copy the feed link directly to your clipboard.

<button id="cleanRssCopyBtn" style="
 background-color: #f1b924;
 color: #000000;
 padding: 12px 24px;
 font-size: 14px;
 font-weight: 600;
 border: none;
 border-radius: 6px;
 cursor: pointer;
 transition: background-color 0.2s ease, color 0.2s ease;
 display: inline-flex;
 align-items: center;
 gap: 8px;
 box-shadow: 0 2px 4px rgba(0,0,0,0.05);
">
 📋 Copy RSS Feed Link
</button>

# 🎉 Feature Enhancements

<br />

# 🐛 Bug Fixes

<br />

# 📚️ Documentation

Documentation

# 🪵 Changelog

## API Changes

### GET /accounts/{accountID}

* :warning: added the new `ACCOUNT_REOPENING` enum value to the `account/statusChangeHistory/statusChangeReason` response property for the response status `200`
* :warning: added the new `ACCOUNT_REOPENING` enum value to the `account/statusChangeReason/name` response property for the response status `200`

### PATCH /accounts/{accountID}

* :warning: added the new `ACCOUNT_REOPENING` enum value to the `account/statusChangeHistory/statusChangeReason` response property for the response status `200`
* :warning: added the new `ACCOUNT_REOPENING` enum value to the `account/statusChangeReason/name` response property for the response status `200`
* added the new `ACCOUNT_REOPENING` enum value to the request property `statusChangeReason`