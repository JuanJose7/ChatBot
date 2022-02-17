import http.server
import socketserver
import threading

from emulator.emulator import Emulator

from routes import routes

emulator = Emulator()

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.respond()

    def do_POST(self):
        self.respond()

    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

        print("Route ", self.path)
        print("Numero de gente", emulator.salasManager.getPeopleNumber(3))
        return bytes(routes[self.path], "UTF-8")

    def respond(self):
        content = self.handle_http(200, 'text/html')
        self.wfile.write(content)



def emulatorexecute():
    emulator.execute()

hilo = threading.Thread(target=emulatorexecute)
hilo.start()

print("Ejecutando server...")
httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
