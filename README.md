# Secure Mini Web Infrastructure Lab

## Project Overview

This project is a small, controlled web infrastructure and security testing lab built inside a VMware virtual environment.

The lab was created to connect networking, Linux, web server administration, HTTP behavior, Git/GitHub, security testing, remediation, and retesting in one practical project.

All security testing in this project was performed against infrastructure controlled by the project owner.

## Objective

The objectives of this lab were to:

* Build and operate a simple Python web server.
* Understand client/server communication.
* Understand IP addresses, ports, interfaces, and service binding.
* Test HTTP requests and responses.
* Perform basic security enumeration against the lab service.
* Identify observable security and configuration issues.
* Apply remediation and hardening.
* Retest the application and document the results.
* Maintain the project using Git and GitHub.

## Environment

### Host

* Windows host
* VMware Workstation
* VMware VMnet8 / NAT networking

### Server VM

* Ubuntu
* Python 3.14.4
* Python virtual environment: `.venv`
* Web server: Python `http.server`
* Service port: `8000`
* Network interface: `ens33`
* Server IP: `192.168.198.128`

### Network

```text
Windows Host
192.168.198.1
        |
        | VMware VMnet8 / NAT
        |
Ubuntu VM
192.168.198.128
        |
        | TCP/8000
        |
Python Web Server
0.0.0.0:8000
```

## Client and Server Model

During the project, both local and network-based communication were tested.

### Local testing

```text
Ubuntu VM
  |
  +-- Client: curl / browser
  |
  +-- Python Web Server
```

Local requests used:

```text
127.0.0.1:8000
```

### Network testing

```text
Windows Host
192.168.198.1
      |
      | VMware VMnet8
      v
Ubuntu VM
192.168.198.128
      |
      v
Python Web Server
0.0.0.0:8000
```

The Windows host successfully accessed the web server through the VM's network IP after a Proton VPN connection that was interfering with local VM connectivity was temporarily disconnected.

## Web Server

The web server is implemented in:

```text
app/server.py
```

It listens on:

```text
0.0.0.0:8000
```

The application currently serves the main page at:

```text
/
```

Unknown paths return:

```text
404 Not Found
```

## HTTP Behavior

The project used `curl` and a web browser to observe HTTP requests and responses.

Example successful response:

```text
HTTP/1.0 200 OK
Content-Type: text/html
```

The application also returns security-related response headers:

```text
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
Referrer-Policy: no-referrer
```

## Security Testing

Security testing was performed as a controlled assessment of the lab web server.

Testing included:

* Service and port verification.
* HTTP response inspection.
* Testing existing and non-existing paths.
* Testing unsupported HTTP methods.
* Inspecting HTTP response headers.
* Observing server information disclosure.
* Reviewing error handling behavior.
* Collecting repeatable evidence.

## Findings

### 1. Incorrect 404 Handling

Before remediation, unknown paths such as:

```text
/abc
/admin
/does-not-exist
```

returned:

```text
200 OK
```

The application was updated so that unknown paths return:

```text
404 Not Found
```

### 2. Server Information Disclosure

Before remediation, the response exposed:

```text
Server: BaseHTTP/0.6 Python/3.14.4
```

The application was updated to use a generic server identification:

```text
Server: SecureMiniWeb
```

### 3. Verbose Error Responses

The default error responses included detailed implementation-oriented information.

Custom error handling was added so that errors return simpler responses without the previous detailed explanations.

### 4. Security Header Hardening

The application initially returned only a small set of response headers.

The following headers were added:

```text
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
Referrer-Policy: no-referrer
```

## Remediation and Retesting

The security workflow used in this project was:

```text
Find
  |
Understand
  |
Fix
  |
Retest
  |
Document
```

The corrected application was retested after remediation.

Expected final behavior includes:

```text
/       -> 200 OK
/abc    -> 404 Not Found
/admin  -> 404 Not Found
```

Unsupported methods continue to be rejected, but the previous verbose implementation details have been reduced.

## Evidence

Raw HTTP testing evidence is stored in:

```text
evidence/day4-http-enumeration.txt
```

Security findings are documented in:

```text
evidence/DAY4-FINDINGS.md
```

Post-remediation retest evidence is stored in:

```text
evidence/day5-retest.txt
```

## Documentation

Learning notes are maintained in:

```text
docs/WHAT-I-LEARNED.md
```

The learning documentation records the practical concepts, mistakes, tools, and security insights developed throughout the project.

## Git Workflow

The project is maintained with Git and GitHub.

Typical workflow:

```bash
git status
git add <files>
git commit -m "message"
git push
```

Local development files such as the Python virtual environment and Python cache files are excluded through `.gitignore`.

## Project Structure

```text
secure-mini-web-infrastructure-lab/
├── app/
│   └── server.py
├── config/
├── docs/
│   └── WHAT-I-LEARNED.md
├── evidence/
│   ├── DAY4-FINDINGS.md
│   ├── day4-http-enumeration.txt
│   └── day5-retest.txt
├── screenshots/
├── scripts/
├── .gitignore
└── README.md
```

## Project Status

Day 1 — Lab setup and architecture: Complete

Day 2 — Web infrastructure and HTTP fundamentals: Complete

Day 3 — Network architecture and client/server testing: Complete

Day 4 — Security assessment and findings: Complete

Day 5 — Hardening, remediation, and retesting: Complete

Day 6 — Final assessment and documentation: Complete
## Key Lessons

The most important practical lessons from the project are:

1. A service can be running correctly while network connectivity to it still fails.
2. Service binding determines which network interfaces can accept connections.
3. HTTP testing involves observing both requests and responses.
4. A security assessment should reproduce and document behavior before classifying its impact.
5. Security findings should be followed by remediation and retesting.
6. Evidence and Git history make technical work reproducible and auditable.

## Scope and Safety

This project is a controlled educational lab.

Security testing should only be performed against systems and services that are owned by the tester or explicitly authorized for testing.

The techniques documented here were used only against the project's own lab infrastructure.
