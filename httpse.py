import  Serch_img as si
# from main import q
# import change as c
import dui_lie as d
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
host = ('0.0.0.0', 8899)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header(' Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin',' *')
            self.end_headers()
            if(d.q.empty()):
                self.wfile.write('')
            data = json.dumps(d.q.get())
            # print("http:"+data)
            #调函数，或者做队列
            self.wfile.write(data.encode())
            # print('over:', time.time())
        except BaseException:
        # print("查无此人")
            mmm = 1

# if __name__ == '__main__':
def init():
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
    print(1)

# init()