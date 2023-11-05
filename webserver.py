#import RPi.GPIO as GPIO
from http.server import HTTPServer, BaseHTTPRequestHandler

host_name='192.168.1.1'
host_port=1234
'''
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT) #red
    GPIO.setup(23, GPIO.OUT) #yellow
    GPIO.setup(24, GPIO.OUT) #green
'''
class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        
        self.do_HEAD()

        html = '''
           <html>
           <body style="width:960px; margin: 20px auto;">
           <h1>Traffic Light Control</h1>
           <form action="/" method="POST">
               <input type="submit" name="submit" value="Red">
               <input type="submit" name="submit" value="Yellow">
               <input type="submit" name="submit" value="Green">
           </form>
           </body>
           </html>
        '''
        self.wfile.write(html.encode())
        

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]
        '''
        setupGPIO()
        
        if post_data == 'red':
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(18,GPIO.HIGH)

        if post_data == 'yellow':
            GPIO.output(18,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)

        if post_data == 'green':
            GPIO.output(23,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
        '''
        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()