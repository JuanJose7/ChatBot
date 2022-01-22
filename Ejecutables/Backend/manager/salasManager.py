class SalasManager():

    def  __init__ (self, salas):
        self.salas = salas

    def incrementarPersona (idSala):
        salaAux = self.salas[idSala]
        salaAux.ocupacion = salaAux.ocupacion + 1

    def printStatus():
        salaAux = self.salas[0]
        print("Sala", salaAux.nombre)
        print("Sala", salaAux.capacidad)
        print("Sala", salaAux.ocupacion)

    