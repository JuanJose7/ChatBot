import sys

from Backend.configurationBackend.configurationBackend import infoConfig
from Backend.emulator.configurationEmu.salasConfig import salas, sensores
from Backend.emulator.configurationEmu.emulatorConfig import ConfigEmu


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

    def infoSalaJson(self, idSala):
        if 0 <= idSala < ConfigEmu.MAX_SALAS:
            return str(self.salas[idSala].toJson())
        else:
            return str("{\"errorCode\":" + str(6) + ", \"description\": \" Id de sala no válido \"}")

    def canEnter(self, idSala):
        if 0 <= idSala < ConfigEmu.MAX_SALAS:
            return str("{\"canEnterSala\": " + str(not self.salas[idSala].isFull()) + "}")
        else:
            return str("{\"errorCode\":" + str(5) + ", \"description\": \" Id de sala no válido \"}")

    def currentOcupacionJson(self):
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

        if sala is not None:
            return str(sala.toJson())
        else:
            return str("{\"errorCode\":" + str(0) + ", \"description\": \" No existe sala con minima ocupación \"}")

    def maxOcupacionJson(self):
        ocupacion = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.ocupacion > ocupacion:
                ocupacion = salaAux.ocupacion
                sala = salaAux
        if sala is not None:
            return str(sala.toJson())
        else:
            return str("{\"errorCode\":" + str(1) + ", \"description\": \" No existe sala con maxima ocupación \"}")

    def favoritaSalaJson(self):
        total = -sys.maxsize
        sala = None
        for salaAux in self.salas:
            if salaAux.contadorTotal > total:
                total = salaAux.contadorTotal
                sala = salaAux

        if sala is not None:
            return str(sala.toJson())
        else:
            return str("{\"errorCode\":" + str(2) + ", \"description\": \" No existe sala favorita \"}")

    def salaPorcentajeOcupacionJson(self, porcentaje):
        if 0 <= porcentaje <= 100:
            sala = None
            for salaAux in self.salas:
                if ((salaAux.ocupacion / salaAux.capacidad) * 100) <= porcentaje:
                    sala = salaAux
                    break

            if sala is not None:
                return str(sala.toJson())
            else:
                return str("{\"errorCode\":" + str(3) + ", \"description\": \" No existe sala con ese porcentaje \"}")
        else:
            return str("{\"errorCode\":" + str(4) + ", \"description\": \" Porcentaje no válido \"}")

    def info(self):
        return str(infoConfig)

    def printStatus(self):
        for salaAux in self.salas:
            print(salaAux)
