from http.server import HTTPServer, CGIHTTPRequestHandler
class handler(CGIHTTPRequestHandler):
    cgi_directories=["/"]
httpd=HTTPServer(("",8000), handler)
httpd.serve_forever()
