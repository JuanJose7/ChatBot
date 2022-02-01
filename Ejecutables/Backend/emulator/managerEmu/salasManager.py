from configurationEmu.salasConfig import salas
from configurationEmu.salasConfig import sensores

class SalasManager():

    def  __init__ (self):
        self.salas = salas
        for index in range(0, len(self.salas) - 1):
            sala = self.salas[index]
            sala.sensor = self.sensore[index]
            
    def detectarMovimiento (self, idSala):
        salaAux = self.salas[idSala]
        salaAux.ocupacion = salaAux.ocupacion + 1

    def printStatus(self):
        for salaAux in self.salas:
            print(salaAux)
