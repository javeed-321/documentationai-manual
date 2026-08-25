Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Rate Limits

## Rate Limits

Beginning May 11, 2022, the following rate limits will be enforced in production to allow for better security and uptime.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Method
      </th>
      <th style={{ textAlign: "left" }}>
        Endpoint
      </th>
      <th style={{ textAlign: "left" }}>
        Limit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        GET
      </td>
      <td style={{ textAlign: "left" }}>
        `/users/{userID}/kyc-status`
      </td>
      <td style={{ textAlign: "left" }}>
        10 per second\
        Burst: 10
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        GET
      </td>
      <td style={{ textAlign: "left" }}>
        `/users/{userID}`
      </td>
      <td style={{ textAlign: "left" }}>
        100 per second\
        Burst: 100
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        PATCH
      </td>
      <td style={{ textAlign: "left" }}>
        `/users/{userID}`
      </td>
      <td style={{ textAlign: "left" }}>
        100 per second\
        Burst: 100
      </td>
    </tr>
  </tbody>
</Table>

Exceeding the rate limits will provide an error - "429 - Too many requests".

Please note there will be additional rate limits implemented over the next few weeks as we continue to improve our platform.

See [Rate Limits](https://developer.drivewealth.com/reference/limits) for additional information on Sandbox and Production limits