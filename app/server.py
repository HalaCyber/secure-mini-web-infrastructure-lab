from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleWebHandler(BaseHTTPRequestHandler):
    server_version = "SecureMiniWeb"
    sys_version = ""

    def _send_security_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'")
        self.send_header("Referrer-Policy", "no-referrer")

    def do_GET(self):
        if self.path == "/":
            body = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Mini Web Infrastructure Lab</title>
</head>
<body>
    <h1>Hello from the Web Server</h1>
    <p>My first Python web server is running.</p>
</body>
</html>
"""

            body_bytes = body.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self._send_security_headers()
            self.send_header("Content-Length", str(len(body_bytes)))
            self.end_headers()
            self.wfile.write(body_bytes)

        else:
            self.send_error(404)

    def send_error(self, code, message=None, explain=None):
        phrase = self.responses.get(code, ("Error",))[0]

        body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Error {code}</title>
</head>
<body>
    <h1>Error {code}</h1>
    <p>{phrase}</p>
</body>
</html>
"""

        body_bytes = body.encode("utf-8")

        self.send_response(code, phrase)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self._send_security_headers()
        self.send_header("Content-Length", str(len(body_bytes)))
        self.end_headers()

        if self.command != "HEAD":
            self.wfile.write(body_bytes)

        self.close_connection = True


server = HTTPServer(("0.0.0.0", 8000), SimpleWebHandler)

print("Web server listening on port 8000 on all IPv4 interfaces")

server.serve_forever()
