# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import _thread

hostName = "localhost"
serverPort = 8080
WriteInfo = "/doRate"
GetTop10 = "/getTop10"
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if self.path==WriteInfo:
            WriteNum(self)
        elif self.path==GetTop10:
            WriteNum(self)
        else:
            python2json = {}
            python2json["1"] = "2"
            self.wfile.write(bytes(json.dumps(python2json), "utf-8"))
def WriteNum(this):
    content_length = int(this.headers['Content-Length'])
    post_data = this.rfile.read(content_length)# res bytes
    myjs = post_data.decode('utf8')
    data = json.loads(myjs) # dict
    #
    uid = data['userId']
    nid = data['novelId']
    rate = data['rating']
    # write to file 
    res = {}
    res["msg"] = "OK"
    this.wfile.write(bytes(json.dumps(res), "utf-8"))
def GetTop(this):
    content_length = int(this.headers['Content-Length'])
    post_data = this.rfile.read(content_length)# res bytes
    myjs = post_data.decode('utf8')
    data = json.loads(myjs) # dict

    # 去取top10

    #this.wfile.write(post_data)

def reflushCommend():
     while True:
        # 刷新任务
        
        #2s检查一次
        time.sleep(600)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
        _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
        print ("Error: 无法启动线程")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    13598793209