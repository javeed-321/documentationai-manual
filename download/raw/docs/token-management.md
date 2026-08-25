---
updatedAt: 2025-09-05T18:29:43.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Token Management

## Token Support

To be able to manage tokens throughout their lifecycle you will utilise our dedicated endpoints, these will help support your cardholder's tokens.

Below are a list of the functions and the endpoints you will require to manage tokens:

| Token Action       | Endpoint                               |
| :----------------- | :------------------------------------- |
| List of all tokens | GET/cards/\{id}/tokens                 |
| Deactivate a token | POST/card-tokens/\{tokenId}/deactivate |
| Suspend a token    | POST/card-tokens/\{tokenId}/suspend    |
| Unsuspend a token  | POST/card-tokens/\{tokenId}/unsuspend  |

> 📘 Card Status Updates
>
> Please note that all tokens are directly linked to cards therefore if the card is put into a state where it stops the ability to use the card, the token will also be put into this state automatically
>
> E.g. if the card has been suspended the token will also be put into a suspended state

> 👍 Card Replacement
>
> If a card has been requested to be replaced then we will automatically update the token associated with that card so that it can carry on being used

> 🚧 Getting Tokens
>
> When retrieving all tokens linked to a card please note that it will also return all tokens that have been created by an acquirer