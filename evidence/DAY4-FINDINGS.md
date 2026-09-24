# Day 4 — Security Findings

## Finding 01 — Incorrect 404 Handling

### Description

The web server returns `HTTP 200 OK` for paths that do not exist.

### Evidence

The following requests all returned `200 OK` and the same HTML page:

```text
/does-not-exist
/abc
/admin
```

### Security / Operational Impact

This behavior makes it difficult to distinguish valid resources from invalid paths. It can affect monitoring, automated testing, routing logic, and the interpretation of scan results.

### Classification

Improper error handling / soft 404 behavior.

### Evidence File

`evidence/day4-http-enumeration.txt`

---

## Finding 02 — Server Information Disclosure

### Description

The HTTP response exposes the server implementation and Python version through the `Server` header.

### Evidence

```text
Server: BaseHTTP/0.6 Python/3.14.4
```

### Security Impact

This provides technology and version information to a client. Such information can help an assessor identify the software stack and research relevant weaknesses.

### Classification

Information disclosure.

### Evidence File

`evidence/day4-http-enumeration.txt`

---

## Observation 03 — Verbose Unsupported-Method Errors

### Description

Unsupported HTTP methods such as `OPTIONS` and `POST` return `501` responses containing detailed error information.

### Evidence

```text
HTTP/1.0 501 Unsupported method ('OPTIONS')
HTTP/1.0 501 Unsupported method ('POST')
```

The response body also includes the error code, message, and explanation.

### Security Impact

Verbose error responses can expose implementation details and provide unnecessary information to clients.

### Classification

Error handling / information disclosure observation.

### Evidence File

`evidence/day4-http-enumeration.txt`

---

## Day 4 Assessment Notes

The testing was performed against the locally controlled Ubuntu web server at:

```text
192.168.198.128:8000
```

The testing confirmed that the service is reachable and that its HTTP behavior can be observed and documented.

No attempt was made to exploit the findings. The purpose of the testing was to identify and document observable security and configuration issues in the lab service.
---

## Observation 04 — Missing Common Security Response Headers

### Description

The server response contains only a small set of HTTP headers and does not currently include common browser security headers such as:

- `X-Content-Type-Options`
- `Content-Security-Policy`
- `Referrer-Policy`

### Evidence

Current response headers:

```text
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.14.4
Date: ...
Content-Type: text/htmlNo X-Content-Type-Options, Content-Security-Policy, or Referrer-Policy headers were observed.

Security Impact

These headers can provide additional browser-side security controls. Their usefulness depends on the application's content and deployment context.

Classification

Security hardening observation.

Evidence File

evidence/day4-http-enumeration.txt
---

# Day 5 — Remediation and Retest

## Finding 01 — Incorrect 404 Handling

### Remediation

The application was updated to check the requested path. The root path `/` returns the normal page, while unknown paths return `404 Not Found`.

### Retest Result

The following requests were tested:

```text
/      → 200 OK
/abc   → 404 Not Found
/admin → 404 Not Found
Status

Fixed and retested successfully.

Retest Evidence

evidence/day5-retest.txt

Finding 02 — Server Information Disclosure
Remediation

The default server identification was changed from the Python BaseHTTPServer implementation and Python version to a generic application server name.

Before
Server: BaseHTTP/0.6 Python/3.14.4
After
Server: SecureMiniWeb
Status

Improved and retested successfully.

Retest Evidence

evidence/day5-retest.txt

Observation 03 — Verbose Error Responses
Remediation

Custom error handling was added for HTTP errors so that responses no longer expose detailed implementation messages and explanations.

Before

Error responses included:

Message:
Error code explanation:
After

Error responses contain a simple status and message without the previous detailed explanation.

Status

Improved and retested successfully.

Retest Evidence

evidence/day5-retest.txt

Observation 04 — Missing Common Security Response Headers
Remediation

The application was updated to include:

X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
Referrer-Policy: no-referrer
Status

Implemented and retested successfully.

Retest Evidence

evidence/day5-retest.txt
