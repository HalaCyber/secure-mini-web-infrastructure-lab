from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
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

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


server = HTTPServer(("127.0.0.1", 8000), SimpleWebHandler)

print("Web server running on http://127.0.0.1:8000")

server.serve_forever()
