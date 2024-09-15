import http.server
import json
import os
import socketserver
import uuid
from http.cookies import SimpleCookie

PORT = int(os.getenv("MOCK_PORT", 8000))
DIRECTORY_TO_SERVE = "pages"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY_TO_SERVE, **kwargs)

    def do_GET(self):

        # xd
        if self.path.startswith("/login"):
            cookies = SimpleCookie()
            [x, y, z] = uuid.uuid1().__str__().split("-", 2)
            cookies["DZIENNIKSID"] = x + "-" + y
            cookies["SDZIENNIKSID"] = z
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            for cookie in cookies.values():
                self.send_header("Set-Cookie", cookie.OutputString())
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "goTo": "/"}).encode())

        elif self.path.startswith("/messages.html/") and len(self.path) > len(
            "/messages.html/"
        ):
            new_path = "/messages/" + self.path[len("/messages.html/") :]
            self.send_response(301)  # Redirect status code
            self.send_header("Location", new_path)
            self.end_headers()
        else:
            super().do_GET()

    def do_POST(self):
        self.do_GET()


with socketserver.TCPServer(("", PORT), Handler, bind_and_activate=False) as httpd:
    httpd.allow_reuse_address = True
    print("Serving at port", PORT)
    try:
        httpd.server_bind()
        httpd.server_activate()
        httpd.serve_forever()
    except:
        httpd.server_close()
        print("Closed.")
        raise
