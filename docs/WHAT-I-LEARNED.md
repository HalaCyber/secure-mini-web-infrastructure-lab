# WHAT I LEARNED

## Lesson 1 — Client, IP, Port, and Web Server

### What I Thought

I knew what an IP address and a port were separately, but I did not have a clear picture of how a client uses them to reach a web server.

### What I Discovered

I understood that a client, such as a web browser, requests a service or resource from a web server. The client connects to the server using its IP address and the port where the service is listening, such as `192.168.198.128:8000`.

### What I Learned

An IP address identifies the target device or network interface, while a port identifies a logical endpoint where a particular service or application can accept connections. A web server receives an HTTP request and sends an HTTP response, which may contain HTML that the browser displays as a web page.

### Why It Matters

Understanding the relationship between IP addresses, ports, and services helps me understand how services are exposed on a system and what entry points may exist during an authorized security assessment.

### Connection to Pre Security

This connects to:

- Client/Server
- IP Addresses
- Ports
- HTTP
- Networking
- Basic Security Assessment

### Practical Evidence

I used my Ubuntu environment to understand that a web server could later listen on an address such as `192.168.198.128` and a port such as `8000`. I will verify this relationship practically when I build the web server.

### Key Takeaway

**The IP tells me where to connect, and the port tells me which service endpoint I am trying to reach.**

A client connects to `IP:Port`, and the web server responds using HTTP.

---

## Lesson 2 — Git, GitHub, and the Local Repository

### What I Thought

I thought that connecting Ubuntu to my GitHub repository would make my changes automatically appear on GitHub.

### What I Discovered

I learned how to clone a GitHub repository into my Ubuntu VM and create a local working copy connected to the remote repository.

Before this project, I did not know how to do this or how the local repository was connected to GitHub.

### What I Learned

Git tracks changes in the local repository, while GitHub hosts the remote repository. Changes made locally do not automatically appear on GitHub. They need to be staged, committed, and pushed.

I also learned how to verify that a local repository is connected to the correct GitHub remote using `git status` and `git remote -v`.

### Why It Matters

This gives me a practical workflow for developing, tracking, and documenting a technical project while keeping a history of my changes.

### Connection to Pre Security

This supports practical project organization, documentation, and controlled development of application code, configuration, scripts, and security testing.

### Practical Evidence

I installed Git, cloned my GitHub repository into Ubuntu, checked the repository status and remote connection, created my first commit, integrated a local/remote difference using `git pull --rebase`, and successfully pushed the commit to GitHub.

### New Practical Skill

Before this project, I did not know how to clone a GitHub repository into Ubuntu, check its status and remote connection, create a commit, integrate a local/remote difference using rebase, or push local changes to GitHub. I can now perform this workflow myself.

### Key Takeaway

I learned how to create a local working copy of a GitHub repository using Git, track local changes, create commits, handle differences between the local and remote repositories, and push my commits to GitHub.

---

# Day 1 — Learning Summary

## Main Concepts Learned

- IP address and subnet
- Ports and services
- Client/server communication
- Web server basics
- Git and GitHub
- Local and remote repositories

## Important Connections

I connected the ideas of IP addresses, ports, clients, and web servers. I also learned how local project work in Ubuntu can be tracked with Git and stored on GitHub.

## Mistakes I Learned From

I initially thought that a commit was something created directly on GitHub and that changes would automatically appear between Ubuntu and GitHub. I learned the difference between local changes, staging, commits, and pushing to the remote repository.

## New Tools / Commands I Understood

- `git clone`
- `git status`
- `git remote -v`
- `git add`
- `git commit`
- `git pull --rebase`
- `git push`

## Security Insights

I learned the importance of understanding the environment before testing it. I identified the VM network interface, IP address, subnet, and default gateway before starting the project.

## Most Important Lesson of the Day

I learned to connect networking concepts with practical system work: an IP identifies where to connect, a port identifies the service endpoint, and a client communicates with a server through that endpoint. I also learned a practical Git workflow for tracking and documenting project changes.

---

## Lesson 3 — Virtual Environments and `.gitignore`

### What I Thought

I thought that the Python environment used to run the project would also need to be uploaded to GitHub.

### What I Discovered

I learned that the virtual environment (`.venv`) is part of my local development and execution environment. It does not need to be stored in the repository.

### What I Learned

A project repository should contain the files needed to understand, develop, and reproduce the project, while local environment files such as `.venv` can remain on the machine. I also learned that `.gitignore` tells Git which local files and directories should not be tracked.

### Why It Matters

Keeping local environment files out of the repository makes the project cleaner and helps reduce the risk of accidentally committing unnecessary or sensitive files.

### Connection to Pre Security

This connects to:

- Linux file management
- Software environments
- Project organization
- Basic security practices

### Practical Evidence

I created a Python virtual environment named `.venv` inside the Ubuntu project directory and added `.venv/` to `.gitignore`. Git then showed `.gitignore` as an untracked project file instead of showing the files inside `.venv`.

### New Practical Skill

Before this project, I did not know how to exclude a local development environment from Git tracking. I can now create a `.gitignore` rule for local project files.

### Key Takeaway

**The repository contains the project; the local virtual environment stays on the machine. `.gitignore` helps Git avoid tracking files that should remain local.**

---

## Lesson 4 — Local Web Server and Loopback

### What I Thought

I did not have a clear picture of what a web server actually was or how it worked on a real system.

### What I Discovered

I built and started a simple Python web server inside my Ubuntu VM. The server runs as a program and listens for connections on `127.0.0.1:8000`.

### What I Learned

A web server is a program that listens for client requests and sends responses. In this project, the web server is implemented in Python.

`127.0.0.1` is the loopback address, which means the server is currently reachable from the same machine. The port `8000` is the endpoint where our web server is listening.

### Why It Matters

Understanding where a service is listening helps me understand which systems and interfaces can reach it. This is important when thinking about service exposure and attack surface.

### Connection to Pre Security

This connects to:

- Operating Systems
- Processes
- Client/Server
- IP Addresses
- Ports
- HTTP
- Networking

### Practical Evidence

I started the Python web server on Ubuntu and confirmed that it was listening on `127.0.0.1:8000`.

### New Practical Skill

Before this project, I did not know how to create and start a local web server in Python. I can now run a basic web server and understand the address and port where it listens.

### Key Takeaway

**A web server is a program that listens for client requests and sends responses. `127.0.0.1` means local access from the same machine, while the port identifies where the service is listening.**

---

## Lesson 5 — HTTP Request and Response

### What I Thought

I understood that a client requests something from a web server, but I had not seen the process happen in a real system.

### What I Discovered

I used `curl` as a client to send an HTTP GET request to my Python web server at `127.0.0.1:8000`. The server received the request and logged it, then returned an HTTP response.

### What I Learned

The client sends an HTTP request to the server, and the server sends an HTTP response back to the client. In this test, `curl` displayed the response while the web server terminal logged the incoming request.

### Why It Matters

Understanding the request/response flow helps me analyze how web applications communicate and where security issues can appear during authorized testing.

### Connection to Pre Security

This connects to:

- HTTP Requests and Responses
- GET Method
- HTTP Status Codes
- Client/Server
- Web Servers
- Networking

### Practical Evidence

I sent a GET request using `curl` to `http://127.0.0.1:8000` and observed a `200 OK` response containing HTML. The Python web server also logged the incoming GET request.

### New Practical Skill

Before this project, I had not used `curl` to send an HTTP request to a web server I built myself. I can now start a local web server and test it as a client using `curl`.

### Key Takeaway

**The client sends the request, the server processes it and sends a response, and the client receives the response.**
