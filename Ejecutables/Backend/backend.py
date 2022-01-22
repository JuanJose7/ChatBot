import http.server
import socketserver
from http import HTTPStatus
from routes import routes
from model.sala import Sala
from manager.salasManager import SalasManager

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
        print("Send ", routes[self.path])
        return bytes(routes[self.path], "UTF-8") 

    def respond(self):
        content = self.handle_http(200, 'text/html')
        self.wfile.write(content)


print ("Creando salas...")
salas = [
    Sala(0, "Sala 1", 4, 0),
    Sala(1, "Sala 2", 3, 0),
    Sala(2, "Sala 3", 6, 0),
    Sala(3, "Sala 4", 5, 0),
    Sala(4, "Sala 5", 4, 0),
]
managerSalas = SalasManager(salas)
managerSalas.printStatus()

print ("Ejecutando server...")
httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()