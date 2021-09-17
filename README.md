## Herramienta para facilitar la interactividad con el WebService del sistema DATADIS
- Publicación de datos de distribuidora al sistema DATADIS
- Gestión de peticiones

### Instalación
```bash
git clone https://github.com/gisce/datadis.git
cd datadis
pip install -e .
```

### Fácil de utilizar

```python
from datadis.webservice import DatadisWebServiceController
controller = DatadisWebserviceController()
controller.autenticar(usuario, password)
controller.contrato.__doc__
>>>
Publicar contrato al sistema DATADIS.
        Si el contrato ya existe en el sistema, se modificara
        Enviar un diccionario con las claves requeridas indicadas a continuacion
        data: {
            "nif": "",
            "nombre": "",
            "comercializadora": "",
            "tensionConexion": "",
            "tarifaAcceso": "",
            "discriminacionHoraria": "",
            "tipoPunto": "",
            "modoControlPotencia": "",
            "fechaInicioContrato": "",
            "cups": "",
            "distribuidora": "",
            "codigoPostal": "",
            "provincia": "",
            "municipio": ""
        }
        method: 'POST' por defecto, utilizar 'DELETE' para eliminar contrato

>>>
respuesta = controller.contrato(data)
```

### Informaciones de:

- Contrato
- Máximas potencia
- AUtoconsumo
