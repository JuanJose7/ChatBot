from Bot.model.operation import Operation

API_TOKEN = '5260264151:AAFmQ04QpQJ-epSw22C_qOJP0Qhaf2GUAnw'
URL_NGROK = 'http://7cf5-92-189-94-207.ngrok.io'

salas = [
    'Sala Norte',
    'Sala Oeste',
    'Sala Sur',
    'Sala Sorento',
    'Sala Espacio'
]

operaciones = [
    Operation('Gente en la sala', 'sala', True),
    Operation('Ocupación Total', 'currentOcupation', False),
    Operation('Sala menos ocupación', 'lessOcupation', False),
    Operation('Sala mayor ocupación', 'maxOcupation', False),
    Operation('¿Puedo entrar a una sala?', 'canEnter', True),
    Operation('Información general del gimnasio', 'info', False),
    Operation('Sala favorita de la gente', 'salaFavorita', False),
    Operation('Porcentaje de sala', 'porcentajeOcupacion', True),
    Operation('Información de TODAS las salas', 'infoTotalSalas', False),
]