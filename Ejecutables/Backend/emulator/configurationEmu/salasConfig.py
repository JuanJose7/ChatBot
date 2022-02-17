from ..modelEmu.sala import Sala
from ..modelEmu.sensor import Sensor

salas = [
    Sala("Sala 1", 0, 4, 0),
    Sala("Sala 2", 1, 3, 0),
    Sala("Sala 3", 2, 6, 0),
    Sala("Sala 4", 3, 5, 0),
    Sala("Sala 5", 4, 4, 0),
]

sensores = [
    Sensor(0, "Sala 1 - Sensor 1", salas[0]),
    Sensor(0, "Sala 2 - Sensor 2", salas[1]),
    Sensor(0, "Sala 3 - Sensor 3", salas[2]),
    Sensor(0, "Sala 4 - Sensor 4", salas[3]),
    Sensor(0, "Sala 5 - Sensor 5", salas[4]),
]