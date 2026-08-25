---
updatedAt: 2025-09-05T18:45:45.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Authentication

## HMAC Signatures / Authorization header calculation

HMAC Signing is an access token method that adds another level of security by also sending a signature that identifies the request temporally to ensure that the request is from the requesting user, using a secret key that is never broadcast over the wire. HMAC signing implemented is based on the latest draft of the HMAC request signing standard.

> 📘 API Keys, API HMAC Secrets vs tokens and hmac
>
> When you onboard to Modulr/set up your sandbox account you will be given
>
> * An **API Key** - this is sometimes referred to as your **token**
> * A **Secret** - this is sometimes referred to as your **hmac**
>
> Please keep this in mind, as both terms can be used.

Sample code is available on our Github project <a href="https://github.com/Modulr-finance/modulr-hmac" target="_blank">here</a>.

We have examples for\ <a href="https://github.com/Modulr-finance/modulr-hmac#java" target="_blank">Java</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#kotlin" target="_blank">Kotlin</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#nodejs" target="_blank">Javascript/NodeJS</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#postman-pre-request-script" target="_blank">Postman</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#python" target="_blank">Python</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#ruby" target="_blank">Ruby</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#c" target="_blank">C</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#cpp" target="_blank">C++</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#c-2" target="_blank">C#</a>\ <a href="https://github.com/Modulr-finance/modulr-hmac#golang" target="_blank">Golang</a>

The required steps and a worked example are provided below, please contact us if you require any further assistance.

1. Set the HTTP “Date” header. The date format must be exactly as per the HTTP-date header specifications - RFC 7231\
   example header:\
   `Date: Mon, 25 Jul 2016 16:36:07 GMT`

2. Set a header with label x-mod-nonce to a unique value per request (see below regarding nonces)\
   example header:\
   `x-mod-nonce: 28154b2-9c62b93cc22a-24c9e2-5536d7d`

3. Create the signature string by concatenating the two headers above separated by a single newline character (note \n and not \r\n).\
   The header labels should be lowercase within the signature string.\
   `signatureString := strings.ToLower("Date") + ": " + HTTP-date + "\n"`\
   `signatureString += strings.ToLower("x-mod-nonce") + ": " + nonce`\
   example signature string:

   ```
   `date: Mon, 25 Jul 2016 16:36:07 GMT\nx-mod-nonce: 28154b2-9c62b93cc22a-24c9e2-5536d7d`
   ```

4. For a given key of `57502612d1bb2c0001000025fd53850cd9a94861507a5f7cca236882` and hmac secret of `NzAwZmIwMGQ0YTJiNDhkMzZjYzc3YjQ5OGQyYWMzOTI=` calculate the hmac-SHA1 signature of the signature string.

5. Convert the result to a url encoded base64 string. You should get a value of:\
   `hex = 58132bfd8761cac6e6888124753adfda13fb49f0`\
   url encoded base 64 = `WBMr%2FYdhysbmiIEkdTrf2hP7SfA%3D`

6. Set the Authorization header result with the below format\
   example header:\
   `Authorization: Signature keyId="57502612d1bb2c0001000025fd53850cd9a94861507a5f7cca236882",algorithm="hmac-sha1",headers="date x-mod-nonce",signature="WBMr%2FYdhysbmiIEkdTrf2hP7SfA%3D"`

## System time

The HMAC calculation above uses a date/time value and also implements the recommended clock-skew from the HMAC specification to prevent against replay attacks. It is therefore essential that the sending system has an accurate time (e.g. synchronised with NTP), any significant time error may cause the request to be rejected.

All time values are sent in GMT, so you should ensure this still continues to send the correct GMT time if your sending system is subject to changes for daylight savings.

## Nonce Value

The previous HMAC calculation uses a nonce value. This value should be set and be unique per distinct api request/operation that you send to our system (see below for limited exceptions). This is used in conjunction with the datetime to prevent replay attacks and detect duplicate messages.

A nonce should be re-used only if you wish to retry the same request in certain conditions, refer to the section on [Idempotence](https://modulr.readme.io/docs/limits-and-errors#section-idempotent-requests)  on how this works.

If the same request content is received with a new nonce, it will be treated as a separate request and may be executed again. Therefore if you wish to re-send a POST request (perhaps because the previous one errored) you need to understand the status of the previous request and that it has not been processed before doing this. Please refer to the section on error handling [Error handling](https://modulr.readme.io/docs/error-handling)  for more information.

## Common Issues

If you are having authorisation issues, please be sure to check for common issues mentioned below.

* Mismatch between date used to calculate the signature and actual date sent on the request

**Date format:**\
Commonly we see that this date isn’t in the correct format or it’s in UTC instead of GMT

* Example incorrect date format "Mon, 5 February 2019 08:54:13 GMT" instead of "Mon, 05 Feb 2019 08:54:13 GMT"

Using locale-specific month names, e.g. Sept rather than Sep for September. This is common if using Java 17 or above and passing the Locale as British - switching to the English locale will overcome this.

**Common misspellings:**\
-Items in the header\
-"algortihm"\
-"Authorization" header is spelt as "Authorisation"\
-Check headers are correctly named e.g. 'nonce' instead of 'x-mod-nonce'\
-Check for empty spaces

* The signature string should be made of two lines. i.e it needs to have \n after "date: ...." and not as one line
* Trying to base64 encode the hex representation of the signature instead of the raw bytes. Symptom: the generated signature is longer than expected
* Base URL that the call is being pointed to is not correct. Refer to [Gaining use of the API](https://modulr.readme.io/docs/gaining-use-of-the-api)
* URL encode character uses lower cases instead of upper case. Symptom: the signature may end in %3d instead of %3D