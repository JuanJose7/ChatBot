from Backend.emulator.configurationEmu.emulatorConfig import ConfigEmu


class Sala:

    # init method or constructor
    def __init__(self,
                 nombre,
                 id,
                 capacidad,
                 ocupacion):
        self.nombre = nombre
        self.id = id
        self.capacidad = capacidad
        self.ocupacion = ocupacion
        self.sensor = None

    def aumentarOcupacion(self):
        self.ocupacion = self.ocupacion + 1

    def disminuirOcupacion(self):
        self.ocupacion = self.ocupacion - 1

    def __str__(self):
        return self.nombre + "\n     Id: " + str(self.id) + "     Capacidad: " + str(
            self.capacidad) + "     Ocupacion: " + str(self.ocupacion)

    def canDoAccion(self, accion):
        if accion == ConfigEmu.ENTER:
            if self.ocupacion < self.capacidad:
                return True
            else:
                return False
        else:
            if self.ocupacion == 0:
                return False
            else:
                return True

    def executeAccion(self, accion):
        if (accion == ConfigEmu.ENTER):
            self.aumentarOcupacion()
        else:
            self.disminuirOcupacion()
