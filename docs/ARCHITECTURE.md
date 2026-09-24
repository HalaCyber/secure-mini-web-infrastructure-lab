# Lab Architecture

## Overview

The lab consists of a Windows host running an Ubuntu virtual machine through VMware Workstation.

The Ubuntu VM hosts the Python web server used for HTTP testing and security assessment.

## Network Architecture

```text
Windows Host
192.168.198.1
       |
       | VMware VMnet8 / NAT
       |
       v
Ubuntu VM
192.168.198.128/24
       |
       | ens33
       |
       v
Python Web Server
0.0.0.0:8000
```

## Interfaces

### Loopback

```text
127.0.0.1
```

The loopback interface allows processes on the Ubuntu VM to communicate with services on the same machine.

### Network Interface

```text
ens33
192.168.198.128/24
```

This interface connects the Ubuntu VM to the VMware virtual network.

## Routing

The Ubuntu VM uses:

```text
Default Gateway: 192.168.198.2
Network:         192.168.198.0/24
```

## Web Service

The Python application runs as a Linux process and listens on:

```text
0.0.0.0:8000
```

Binding to `0.0.0.0` makes the service listen on all IPv4 interfaces available to the VM.

## Client and Server Communication

### Local Communication

```text
Ubuntu Client
     |
     | HTTP Request
     v
127.0.0.1:8000
     |
     v
Python Web Server
     |
     | HTTP Response
     v
Ubuntu Client
```

### Host-to-VM Communication

```text
Windows Host
192.168.198.1
     |
     | HTTP Request
     v
VMware VMnet8 / NAT
     |
     v
Ubuntu VM
192.168.198.128:8000
     |
     v
Python Web Server
     |
     | HTTP Response
     v
Windows Host
```

## Security Testing Flow

```text
Client
  |
  v
Network
  |
  v
Listening Service
  |
  v
HTTP Request
  |
  v
Application Behavior
  |
  v
HTTP Response
  |
  v
Observation
  |
  v
Finding
  |
  v
Remediation
  |
  v
Retest
```

## Network Troubleshooting Lesson

During the lab, the Windows host initially could not reach the Ubuntu web server even though the service was listening and VMware networking was configured.

Testing showed that Proton VPN was active on the Windows host. After temporarily disconnecting the VPN, the host was able to reach the Ubuntu web server through VMnet8.

This demonstrated that a working application and a correct route do not always guarantee successful network connectivity. VPNs and other network filtering components can affect local virtual-network traffic.

## Security Boundary

The web server and all security tests in this project are part of a controlled educational lab.

Testing is limited to infrastructure owned or explicitly authorized for testing.
