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

* Client/Server
* IP Addresses
* Ports
* HTTP
* Networking
* Basic Security Assessment

### Practical Evidence

I used my Ubuntu environment to understand that a web server could later listen on an address such as `192.168.198.128` and a port such as `8000`. I will verify this relationship practically when I build the web server.

### Key Takeaway

**The IP tells me where to connect, and the port tells me which service endpoint I am trying to reach.**

A client connects to `IP:Port`, and the web server responds using HTTP.
