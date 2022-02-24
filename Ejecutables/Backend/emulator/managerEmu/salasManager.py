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


    def printStatus(self):
        for salaAux in self.salas:
            print(salaAux)
