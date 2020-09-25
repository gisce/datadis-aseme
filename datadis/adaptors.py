# -*- coding: utf-8 -*-
REQUIRED_CONTRATO_KEYS = [
    'comercialitzadora', 'tensionConexion', 'tarifaAcceso', 'discriminacionHoraria', 'tipoPunto', 'modoControlPotencia', 
    'fechaInicioContrato', 'nif', 'nombre', 'cups', 'distribuidora', 'codigoPostal', 'provincia', 'municipio'
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
    return data
