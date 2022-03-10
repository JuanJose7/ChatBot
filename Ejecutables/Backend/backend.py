import http.server
import socketserver
import threading

from Backend.model.route import Operation
from emulator.emulator import Emulator

emulator = Emulator()

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.respond()

    def do_POST(self):
        self.respond()

    def createBody(self):
        print("Route ", self.path)

        operation = Operation(self.path)
        if operation.operation == "/sala":
            return bytes(emulator.salasManager.infoSalaJson(int(operation.id)), "UTF-8")
        elif operation.operation == "/currentOcupation":
            return bytes(emulator.salasManager.currentOcupacionJson(), "UTF-8")
        elif operation.operation == "/lessOcupation":
            return bytes(emulator.salasManager.lessOcupacionJson(), "UTF-8")
        elif operation.operation == "/maxOcupation":
            return bytes(emulator.salasManager.maxOcupacionJson(), "UTF-8")
        elif operation.operation == "/canEnter":
            return bytes(emulator.salasManager.canEnter(int(operation.id)), "UTF-8")
        elif operation.operation == "/info":
            return bytes(emulator.salasManager.info(), "UTF-8")
        elif operation.operation == "/salaFavorita":
            return bytes(emulator.salasManager.favoritaSalaJson(), "UTF-8")
        elif operation.operation == "/porcentajeOcupacion":
            return bytes(emulator.salasManager.salaPorcentajeOcupacionJson(int(operation.id)), "UTF-8")

    def respond(self):
        content = self.createBody()

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        self.wfile.write(content)


def emulatorexecute():
    emulator.execute()

hilo = threading.Thread(target = emulatorexecute)
hilo.start()

print("Ejecutando server...")
httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
