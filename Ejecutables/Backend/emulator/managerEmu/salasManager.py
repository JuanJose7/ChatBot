import sys

from Backend.configurationBackend.configurationBackend import infoConfig
from Backend.emulator.configurationEmu.salasConfig import salas, sensores


class SalasManager:

    def __init__(self, salasfield):
        self.salas = salasfield
        for index in range(0, len(self.salas) - 1):
            sala = self.salas[index]
            sala.sensor = sensores[index]


    def detectarMovimiento(self, idSala):
        salaAux = self.salas[idSala]
        salaAux.ocupacion = salaAux.ocupacion + 1


    def getPeopleNumber(self, idSala):
        return self.salas[idSala].ocupacion


    def infoSalaJson (self, idSala):
        return str(self.salas[idSala].toJson())


    def canEnter (self, idSala):
        return str("{\"canEnterSala\": " + str(not self.salas[idSala].isFull()) + "}")


    def currentOcupacionJson (self):
        ocupacion = 0
        for salaAux in self.salas:
            ocupacion = ocupacion + salaAux.ocupacion
        return str("{\"currentOcupacion\": " + str(ocupacion) + "}")


    def lessOcupacionJson(self):
        ocupacion = sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.ocupacion < ocupacion:
                ocupacion = salaAux.ocupacion
                sala = salaAux
        return str(sala.toJson())

    def maxOcupacionJson(self):
        ocupacion = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.ocupacion > ocupacion:
                ocupacion = salaAux.ocupacion
                sala = salaAux
        return str(sala.toJson())

    def favoritaSalaJson(self):
        total = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.contadorTotal > total:
                total = salaAux.contadorTotal
                sala = salaAux
        return str(sala.toJson())

    def salaPorcentajeOcupacionJson(self, porcentaje):
        sala = None
        for salaAux in self.salas:
            if (((salaAux.ocupacion / salaAux.capacidad) * 100) < porcentaje) :
                sala = salaAux
        return str(sala.toJson())

    def info(self):
        return str(infoConfig)

    def printStatus(self):
        for salaAux in self.salas:
            print(salaAux)
