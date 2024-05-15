import http.server
import socketserver
import os

PORT = int(os.getenv("MOCK_PORT", 8000))
DIRECTORY_TO_SERVE = "pages"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY_TO_SERVE, **kwargs)

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
