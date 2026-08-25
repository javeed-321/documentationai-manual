# EdgeKV Documentation

> Akamai's EdgeKV is a key-value store database at the edge. It enables you to build data-driven EdgeWorker applications that require fast, frequent reads and infrequent writes.

Fetch the complete documentation index at: https://techdocs.akamai.com/edgekv/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Access tokens
- [Create an access token](https://techdocs.akamai.com/edgekv/reference/post-tokens.md): Generate an access token that allows an EdgeWorkers code bundle to access the specified namespace. Any new tokens that you create refresh automatically without expiring. You don't need to update tokens inside your `edgekv_tokens.js` file. Tokens created before the enhanced token workflow implementation will still expire. You need to replace these expired tokens in your code bundle. To learn more about access tokens, refer to the [EdgeKV guide](doc:generate-and-retrieve-edgekv-access-tokens).
- [List access tokens](https://techdocs.akamai.com/edgekv/reference/get-tokens.md): View a list of EdgeKV access tokens.
- [Download an access token](https://techdocs.akamai.com/edgekv/reference/get-token.md): Download a previously created EdgeKV access token. To get a token, you need to know the token `name`. Tokens created using the enhanced token workflow don't include the JWT value in the response. To learn more about access tokens, refer to the [EdgeKV guide](doc:generate-and-retrieve-edgekv-access-tokens).
- [Revoke an access token](https://techdocs.akamai.com/edgekv/reference/delete-token.md): Once you revoke an access token, you can't undo it. You also need to update any deployed EdgeWorkers code bundles that use the old token with a new token, or requests to EdgeKV fail. Any requests from an EdgeWorkers code bundle using a revoked token cause a 401 error. To learn more about access tokens, refer to the [EdgeKV guide](doc:generate-and-retrieve-edgekv-access-tokens).
- [Refresh an access token](https://techdocs.akamai.com/edgekv/reference/post-refresh-token.md): Refresh a previously created EdgeKV access token before scheduled automatic refresh.
