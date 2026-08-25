---
updatedAt: 2025-09-05T18:13:08.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# HMAC Authentication

```java Java
package com.modulr.api;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.SignatureException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.function.Supplier;

public class ModulrApiAuth {
    private static final String HMAC_SHA1_ALGORITHM = "HmacSHA1";
    private static final String DATE_PATTERN = "EEE, dd MMM yyyy HH:mm:ss z";
    private final String secret;
    private final String token;
    private Date date;
    private Supplier<Date> dateSupplier;

    private String lastUsedNonce;


    public ModulrApiAuth(String token, String secret) {
        this(token, secret, Date::new);
    }

    public ModulrApiAuth(String token, String secret, Supplier<Date> dateSupplier) {
        this.token = (token != null) ? token.trim() : null;
        this.secret = secret.trim();
        this.dateSupplier = dateSupplier;
    }

    public Map<String, String> generateApiAuthHeaders(String nonce) throws SignatureException {
        return buildHeaders(nonce, false);
    }

    public Map<String, String> generateRetryApiAuthHeaders() throws SignatureException {
        return buildHeaders(this.lastUsedNonce, true);
    }

    private Map<String, String> buildHeaders(String nonce, Boolean retry) throws SignatureException {
        final Map<String, String> headerParams = new HashMap<>();
        String hmac = generateHmac(nonce);

        headerParams.put("Authorization", formatAuthHeader(this.token, hmac));
        headerParams.put("Date", getFormattedDate(this.getDate()));
        headerParams.put("x-mod-nonce", nonce);
        headerParams.put("x-mod-retry", String.valueOf(retry));

        this.lastUsedNonce = nonce;

        return headerParams;
    }

    public String generateHmac(String nonce) throws SignatureException {
        validateFields();
        this.date = dateSupplier.get();
        String data = String.format("date: %s\nx-mod-nonce: %s", getFormattedDate(this.getDate()), nonce);
        return calculateHmac(data);
    }

    public Date getDate() {
        return date;
    }

    public String getSecret() {
        return secret;
    }

    public String getToken() {
        return token;
    }

    private String formatAuthHeader(String token, String signature) {
        return String.format("Signature keyId=\"%s\",algorithm=\"%s\",headers=\"date x-mod-nonce\",signature=\"%s\"", token, "hmac-sha1", signature);
    }

    private String calculateHmac(final String content) throws SignatureException {
        try {
            final SecretKeySpec signingKey = new SecretKeySpec(secret.getBytes(), HMAC_SHA1_ALGORITHM);
            Mac mac = Mac.getInstance(HMAC_SHA1_ALGORITHM);
            mac.init(signingKey);

            // compute the hmac on input data bytes
            byte[] rawHmac = mac.doFinal(content.getBytes());

            // base64-encode the hmac
            String hmac = Base64.getEncoder().encodeToString(rawHmac);
            return URLEncoder.encode(hmac, "UTF-8");
        } catch (NoSuchAlgorithmException | InvalidKeyException | UnsupportedEncodingException e) {
            throw new SignatureException("Failed to generate HMAC : " + e.getMessage(), e);
        }
    }

    private String getFormattedDate(Date date) {
        DateFormat sdf = new SimpleDateFormat(DATE_PATTERN,Locale.UK);
        sdf.setTimeZone(TimeZone.getTimeZone("GMT"));
        return sdf.format(date);
    }

    private void validateFields() {
        if (this.secret == null) {
            throw new IllegalStateException("Secret required for Modulr API Auth");
        }
        if (this.dateSupplier == null) {
            throw new IllegalStateException("A date supplier is required for Modulr API Auth");
        }
    }

}
```

```json Response Example
Authorization = Signature keyId="<YOUR API Key>",algorithm="hmac-sha1",headers="date x-mod-nonce",signature="<CALCULATED HMAC SECRET>"
Date: Mon, 25 Jul 2020 16:36:07 GMT
x-mod-nonce: bb016d2efd6c2e1d4dd04cdb2f8aef6f741aaae1
x-mod-retry = true
```

# Secure Hash Algorithms

<!-- java@16 -->

At Modulr we support:
HmacSHA1
HmacSHA256
HmacSHA384
HmacSHA512

# Date Format

<!-- java@17 -->

All Dates for HMAC Authentication should be in RFC 7231 format e.g. 
Mon, 25 Jul 2020 16:36:07 GMT

# Building your headers

<!-- java@44-56 -->

This method has everything you need for creating the necessary headers for submitting a request to the Modulr platform.

# x-mod-retry

<!-- java@51 -->

For more information on this header please refer to document - https://modulr.readme.io/docs/limits-and-errors#idempotent-requests

# Generating Hmac data

<!-- java@58-63 -->

This method is in place to generate the data needed to calculate the HMAC secret this is mainly the Date and nonce of the request.

This needs to be passed into the calculateHmac method in the format:

date: Mon, 25 Jul 2020 16:36:07 GMT
nonce: 28154b2-9c62b93cc22a-24c9e2-5536d7d

# Calculating Hmac Secret

<!-- java@81-96 -->

This method calculates the secret value.

The important thing to pay attention to is that the calculated value is first Base64 encoded then URL encoded to UTF-8