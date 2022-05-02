from Bot.model.operation import Operation

API_TOKEN = '5260264151:AAFmQ04QpQJ-epSw22C_qOJP0Qhaf2GUAnw'
URL_NGROK = 'http://dcd1-92-189-94-207.ngrok.io'

salas = [
    'Sala Norte',
    'Sala Oeste',
    'Sala Sur',
    'Sala Sorento',
    'Sala Espacio'
]

operaciones = [
    Operation('Gente en la sala', 'sala', True, ["nombre", "capacidad", "id", "ocupacion", "contadorTotal"]),
    Operation('Ocupación Total', 'currentOcupation', False, ["currentOcupacion"]),
    Operation('Sala menos ocupación', 'lessOcupation', False, ["nombre", "capacidad", "id", "ocupacion", "contadorTotal"]),
    Operation('Sala mayor ocupación', 'maxOcupation', False, ["nombre", "capacidad", "id", "ocupacion", "contadorTotal"]),
    Operation('¿Puedo entrar a una sala?', 'canEnter', True, ["canEnterSala"]),
    Operation('Información general del gimnasio', 'info', False, ["hora-apertura", "hora-cierre", "nombre", "direccion", "mensualidad", "n-salas", "ocupacionTotal"]),
    Operation('Sala favorita de la gente', 'salaFavorita', False, ["nombre", "capacidad", "id", "ocupacion", "contadorTotal"]),
    Operation('Porcentaje de sala', 'porcentajeOcupacion', True, ["nombre", "capacidad", "id", "ocupacion", "contadorTotal"]),
    Operation('Información de TODAS las salas', 'infoTotalSalas', False, None),
]