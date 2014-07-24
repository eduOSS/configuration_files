import cgi
import BaseHTTPServer,CGIHTTPServer

httpd = BaseHTTPServer.HTTPServer(('127.0.0.1',8000),CGIHTTPServer.CGIHTTPRequestHandler)
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
httpd.server_close()
