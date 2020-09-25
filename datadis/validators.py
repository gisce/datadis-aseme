# -*- coding: utf-8 -*-
CODIGOS_TARIFA = ['30', '31', '62', '63', '64', '65', '21', '2A', '6A']
CODIGOS_TENSION = ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6']
CODIGOS_DH = ['G0', 'E3', 'E2', 'E1']

def validar_contrato(data):
    if not isinstance(data, dict):
        raise Exception("El formato de datos debe ser un diccionario")

    validar_provincia()
    validar_municipio()
    validar_cups(data['cups'])
    validar_tension(data['tensionConexion'])
    validar_tarifa(data['tarifaAcceso'])
    validar_dh(data['discriminacionHoraria'])
    validar_tipo_punto(data['tipoPunto'])
    validar_control_potencia(data['tipoPunto'])
    validar_nif(data['nif'])

def validar_municipio(municipio):
    pass

def validar_provincia(poblacion):
    pass

def validar_cups(cups):
    if len(data['cups']) != 22:
        raise Exception('El cups debe tener 22 caracteres')

def validar_tension(tension):
    if not isinstance(tension, str):
        raise TypeError("Tension {} incorrecta".format(tension))
    if tension.upper() not in CODIGOS_TENSION:
        raise Exception("Codigo tension {} no catalogada en las tablas de tension".format(tension))

def validar_tarifa(tarifa):
    if not isinstance(tarifa, str):
        raise TypeError("Tarifa {} incorrecta".format(tarifa))
    if tarifa.upper() not in CODIGOS_TARIFA:
        raise Exception("Codigo tarifa {} no catalogada en las tablas de tarifa".format(tarifa))

def validar_dh(dh):
    if not isinstance(dh, str):
        raise TypeError("Discriminacion horaria {} incorrecta".format(dh))
    if dh.upper() not in CODIGOS_DH:
        raise Exception("Codigo discriminacion horaria {} no catalogada en las tablas de discriminacion horaria -> {}".format(dh, CODIGOS_DH))

def validar_tipo_punto(tipo_punto):
    if int(tipo_punto) > 5 or int(tipo_punto) < 1:
        raise Exception("Codito tipo de punto {} incorrecto -> 1, 2, 3, 4, 5".format(tipo_punto))

def validar_control_potencia():
    pass

def validar_nif():
    pass
