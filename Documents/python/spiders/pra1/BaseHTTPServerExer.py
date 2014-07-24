from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import sep, curdir
import cgi

PORT = 8080
    
class myHandler(BaseHTTPRequestHandler):
            
    def do_GET(self):

        if self.path == '/':
            self.path = '\\test.html'
            
        try:
            reply = False
            if self.path.endswith('.html'):
                reply = True
                mimeType = 'text/html'
                
            if self.path.endswith('.jpg'):
                reply = True
                mimeType = 'image.jpg'
                
            if self.path.endswith('.js'):
                reply = True
                mimeType = 'application/javascript'
                
            if self.path.endswith('.txt'):
                reply = True
                mimeType = 'text/txt'
                
            
            if(reply == True):
                fp = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('content-type', mimeType)
                self.end_headers()
                self.wfile.write(fp.read())
                fp.close()
            return
        except IOError:
            self.send_error(404, 'Not Found File %s' %self.path);
        
    def do_POST(self):
        form = cgi.FieldStorage(
                                fp = self.rfile,
                                headers = self.headers,
                                environ = {
                                           'REQUEST_METHOD':'POST',
                                           'CONTENT_TYPE':self.headers.getheader('current-type')
                                           }
                                )
        
        print form
        
        

        #self.wfile.write(form['name'])

    
try:
    ser = HTTPServer(('', PORT), myHandler) 
    print '\n\nStart HTTP Server at PORT:' , PORT
    ser.serve_forever()
except KeyboardInterrupt:
    print 'Shutting down the server!!'
    ser.socket.close()
