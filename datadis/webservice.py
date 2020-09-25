# -*- coding: utf-8 -*-
import requests
import logging
import json
from os import path
from datadis.validators import validar_contrato
from datadis.adaptors import adaptar_datos_contrato

BASE_URL = "https://apihsdistribuidoras.asemeservicios.com"
HEADER={"Accept": "text/plain", "Content-Type": "application/json"}
logger = logging.getLogger('Datadis Webservice')

class DatadisWebserviceController(object):

    def __init__(self):
        self.token = ""

    @property
    def templates(self):
        return path.join(path.dirname(path.realpath(__file__)), 'templates/')

    @property
    def token(self):
        return 'Bearer ' + self.token

    @token.setter
    def token(self, value):
        self.token = value

    @token.deleter
    def token(self):
        del self.token

    @property
    def url_autenticar(self):
        return BASE_URL + '/autenticar'

    @property
    def url_contrato(self):
        return BASE_URL + '/contrato'

    @property
    def url_eliminar_contrato(self):
        return BASE_URL + '/contrato/{nif}/{cups}'

    def url_bloquear_consumidor(self):
        return BASE_URL + '/consumidor/bloquear'

    @property
    def url_maximas_potencia(self):
        return BASE_URL + '/maximaspotencia'

    @property
    def url_estado(self):
        return BASE_URL + '/estado/{timestamp}/{guid}'

    def autenticar(self, user, password):
        user = str(user).zfill(4)
        r = requests.post(self.url_autenticar, headers=HEADER, json={'usuario': user, 'contraseña': password})
        if r.status_code == 200:
            resp_data = r.json()
            api_token = resp_data.get('token', '')
            username = resp_data.get('usuario', '')
            logger.info('User {} is now connected'.format(username))
            self.token = api_token
            self.user = username
            HEADER['Authorization'] = self.token
            return resp_data
        else:
            raise Exception(r.status_code)

    def contrato(self, data, method='POST'):
        if method.upper() == 'POST':
            data = adaptar_datos_contrato(data)
            validar_contrato(data)
            if isinstance(data['modoControlPotencia'], str):
                control_potencia = 1 if 'max' in data['modoControlPotencia'] else 2
                data.update({'modoControlPotencia': control_potencia})
            with open(self.templates + 'contrato.json') as json_template:
                template = json.load(json_template)
            for key in data.keys():
                if key in template['contrato']:
                    template['contrato'].update({key: data[key]})
                if key in template['puntoSuministro']:
                    template['puntoSuministro'].update({key: data[key]})
                if key in template['titular']:
                    template['titular'].update({key: data[key]})
            r = requests.post(self.url_contrato, headers=HEADER, json=template)
            return r.json()
        if method.upper() == 'DELETE':
            return self.eliminar_contrato(data)

    def eliminar_contrato(self, data):
        if 'nif' in data and 'cups' in data:
            r = requests.delete(self.url_eliminar_contrato.format(**data), headers=HEADER)
            return r.json()
        else:
            raise KeyError("nif y/o cups no especificados")

    def maximas_potencia(self, data):
        # todo: get datetime from any measure and separe fecha y hora
        with open(self.templates + 'maximaspotencia.json') as json_template:
            template = json.load(json_template)
        r = requests.post(self.url_maximas_potencia, headers=HEADER, json=json.dumps(data))
        return r.json()

    def bloquear_consumidor(self, nif):
        data = {'nif': nif, 'bloqueado': 'true'}
        r = requests.post(self.url_bloquear_consumidor(), headers=HEADER, json=json.dumps(data))
        return r.json()

