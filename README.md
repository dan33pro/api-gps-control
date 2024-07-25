# api-gps-control

Esta es la API para la prueba tecnica de GPS Control, construida don Django : [Django REST framework](http://www.django-rest-framework.org/)

## Requerimientos
- Python 3.10.12
- Django 5.0.7
- Django REST Framework

## Instalación
1. Despues de clonar el repositorio para correr la api, puedes correr los siguientes comandos en una terminal dentro del directorio:

```bash
python -m venv env
```

2. Luego bajas las dependencias:
```bash
pip install -r requirements.txt
```

3. Luego puedes configurar el gestor de base de datos de tu preferencia en el `settings.py`, realizar las migraciones y correr el proyecto como cualquier otro proyecto de django.


## Estructura
Esta es una RestFullAPI con todos los metodos HTTP de un CRUD - GET, POST, PUT, DELETE. La docuemntación del API la puedes ver con el end-point `/api/docs`.

Para esta prueba solo era necesario una entidad **Interesado**, `interested`, que puedes usar con las siguiente URLS - `api/v1/interesteds/`:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/api/v1/interesteds/` | GET | READ | Get todos los interesados
`/api/v1/interesteds/:id` | GET | READ | Get un solo interesado
`/api/v1/interesteds/`| POST | CREATE | Create un nuevo interesado
`/api/v1/interesteds/:id/` | PUT | UPDATE | Update un interesado
`/api/v1/interesteds/:id/` | PATCH | PARTIAL UPDATE | Update un interesado
`/api/v1/interesteds/:id/` | DELETE | DELETE | Delete un interesado

Curpo de la petición para POST, PUT, PATCH('el cuerpo puede estar incompleto'):
```json
{
    "brand": "DS",
    "branch": "Chapinero",
    "applicant": "Daniel Cespedes"
}
```