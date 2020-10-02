# -*- coding: utf-8 -*-
REQUIRED_CONTRATO_KEYS = [
    'comercialitzadora', 'tensionConexion', 'tarifaAcceso', 'discriminacionHoraria', 'tipoPunto', 'modoControlPotencia', 
    'fechaInicioContrato', 'nif', 'nombre', 'cups', 'distribuidora', 'codigoPostal', 'provincia', 'municipio'
]
REQUIRED_MAXIMAS_POTENCIA_KEYS = [
    'cups', 'medida', 'fecha'
]

def adaptar_datos_contrato(data):
    for key in REQUIRED_CONTRATO_KEYS:
        if key not in data:
            raise KeyError("Clave requerida {} no encontrada!".format(key))

    data.update({
        'comercialitzadora': str(data['comercialitzadora'].zfill(4)),
        'distribuidora': str(data['distribuidora'].zfill(4)),
        'tarifaAcceso': str(data['tarifaAcceso'].upper()),
        'tensionConexion': str(data['tensionConexion'].upper()),
        'discriminacionHoraria': str(data['discriminacionHoraria'].upper()),
        'municipio': str(data['municipio']).zfill(3),
        'provincia': str(data['provincia']).zfill(2),
        'codigoPostal': str(data['codigoPostal']).zfill(5),
        'tipoPunto': int(data['tipoPunto']),
        'nif': str(data['nif']).replace('ES', '')
    })
    if isinstance(data['modoControlPotencia'], str):
        control_potencia = 1 if 'max' in data['modoControlPotencia'] else 2
        data.update({'modoControlPotencia': control_potencia})

    return data

def adaptar_maximas_potencia(data):
    for key in REQUIRED_MAXIMAS_POTENCIA_KEYS:
        if key not in data:
            raise KeyError("Clave requerida {} no encontrada!".format(key))

    hour_mask = "%H:%M"
    date_mask = "%Y-%m-%d"
    try:
        ts = datetime.strptime(data['fecha'], date_mask + ' ' + hour_mask)
    except ValueError, TypeError:
        try:
            ts = datetime.strptime(data['fecha'], date_mask)
        except:
            raise Exception("Formato {} fecha incorrecto -> AAAA/mm/dd o AAAA/mm/dd HH:MM".format(data['fecha']))
    fecha = ts.strftime(date_mask)
    hora = ts.strftime(hour_mask)
    medida = "%.3f" % round(data['medida'], 3)
    data.update({'medida': medida, 'fecha': fecha, 'hora': hora})
    return data

def adaptar_estado(data):
    if isinstance(data['timestamp'], str):
        data['timestamp'] = int(data['timestamp'])
