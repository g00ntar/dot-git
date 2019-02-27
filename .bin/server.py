#!/usr/bin/python

"""
HTTP server classes, with simple css js additions.

TODO: 
check if there is internet connectionto differentiate CSS and JS
hide dotfiles with css
def createRow
def createHTMLHead
def createHTMLHeader
def createCSS - or something similar
def createJS - or something similar
https://codepen.io/AngularDataGrid/embed/bqXarG?height=768&theme-id=21603&slug-hash=bqXarG&default-tab=html&user=AngularDataGrid
"""

import sys
import os
import io
import html
import urllib.parse
from jinja2 import Template

try:

    # In Python 3 the 'SimpleHTTPServer'
    # module has been merged into 'http.server'.

    import http.server as server
    import socketserver

except ImportError:

    import SimpleHTTPServer as server
    import SocketServer as socketserver

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

head_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.purple-indigo.min.css">
    <style>
        table {
            margin: 0 auto;
        }
    </style>
</head>
"""

body_template = """
<body>
    <div class="demo-layout-transparent mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header">
            <div class="mdl-layout__header-row">
                <!-- Title -->
                <h1 class="mdl-layout-title">{{ title }}</h1>
            </div>
        </header>
        <main class="mdl-layout__content">
            <div class="mdl-grid">
                <div class="mdl-cell--12-col">
                    <table class="mdl-data-table mdl-js-data-table mdl-shadow--2dp">
                        <thead>
                            <tr>
                                <th>Actions</th>
                                <th class="mdl-data-table__cell--non-numeric">Name</th>
                                <th>Size</th>
                                <th class="mdl-data-table__cell--non-numeric">Type</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for file in files %}
                                <tr>
                                    <td class="actions mdl-data-table__cell--non-numeric"></td>
                                    <td class="name mdl-data-table__cell--non-numeric"><a href="{{ file }}">{{ file }}</a></td>
                                    <td class="size"></td>
                                    <td class="filetype mdl-data-table__cell--non-numeric"></td>
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </main>
    </div>
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
    <script>
        var options = {
                valueNames: ['name', 'type', 'size']
        }
        var documentTable = new List('mdl-table', options);
    </script>
</body>
</html>
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class requestHandler(server.SimpleHTTPRequestHandler):

    # def do_GET(self):
    #     """Serve a GET request."""
    #     f = self.send_head()
    #     if f:
    #         try:
    #             self.copyfile(f, self.wfile)
    #         finally:
    #             f.close()

    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """

        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(
                404,
                "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        list = map(build_file_object)
        try:
            displaypath = urllib.parse.unquote(self.path,
                                               errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath, quote=False)
        enc = sys.getfilesystemencoding()
        title = 'Directory listing for %s' % displaypath
        response = Template(head_template+body_template).render(title=title,files=list)

        encoded = response.encode(enc, 'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f


def run(server_class=socketserver.ThreadingTCPServer, handler_class=requestHandler, port=8088):
    try:
        # Create but don't automatically bind socket
        # (the 'allow_reuse_address' option needs to be set first).
        httpd = server_class(
            ("localhost", port), handler_class, False)

        # Prevent 'cannot bind to address' errors on restart.
        # https://brokenbad.com/address-reuse-in-pythons-socketserver/
        httpd.allow_reuse_address = True

        # Manually bind socket and start the server.
        httpd.server_bind()
        httpd.server_activate()
        print("Serving content on port: ", port)
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("^C received, shutting down the web server")
        # server.socket.close()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
