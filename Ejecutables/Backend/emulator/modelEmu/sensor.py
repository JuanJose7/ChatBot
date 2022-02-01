class Sensor():

    # init method or constructor   
    def __init__(   self,
                    id, 
                    nombre, 
                    sala):  
        self.id = id  
        self.nombre = nombre
        self.sala = sala

    def __str__(self):
       return  self.nombre + "\n     Id: " + str(self.id) +  "     Sala asociada: " + str(self.sala)

    def entradaPersona(self):
        self.sala.aumentarOcupacion()

    def salidaPersona(self):
        self.sala.disminuirOcupacion()

    def salidaPersona(self):
        self.sala

