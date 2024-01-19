from http.server  import HTTPServer,BaseHTTPRequestHandler
# BaseHTTPRequestHandler handles all the get requests and the posts
# post requests which the server recieves


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers() #closing the headers
        self.wfile.write(self.path[1:].encode())

        # self.wfile.write(self.path[1:].encode())

def main():
    PORT=8000
    server=HTTPServer(('',PORT),echoHandler)
    print('Server running on Port %s'% PORT)
    # print("hello world")
    server.serve_forever() 
    # THIS WILL START THE SERVER .server_forever()

if __name__=='__main__':
    main()