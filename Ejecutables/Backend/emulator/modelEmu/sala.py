class Sala():

        # init method or constructor   
    def __init__(   self, 
                    nombre, 
                    id, 
                    capacidad, 
                    ocupacion):  
        self.nombre = nombre  
        self.id = id
        self.capacidad = capacidad
        self.ocupacion = ocupacion
        self.sensor = None;

    def aumentarOcupacion (self):
        self.ocupacion = self.ocupacion + 1

    def disminuirOcupacion (self):
        self.ocupacion = self.ocupacion - 1

    def __str__(self):
       return  self.nombre + "\n     Id: " + str(self.id) + "     Capacidad: " + str(self.capacidad) + "     Ocupacion: " + str(self.ocupacion)
