Solución para el desafío [Todo List API](https://roadmap.sh/projects/todo-list-api) de [roadmap.sh](https://roadmap.sh)  
## Todo List API
En este proyecto, deberás desarrollar una API RESTful que permita a los usuarios gestionar sus listas de tareas.
Este proyecto te ayudará a comprender cómo diseñar e implementar una API RESTful con autenticación de usuarios.
También aprenderás a trabajar con bases de datos, gestionar errores e implementar medidas de seguridad.
![text alt](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Todo_List_API/todo-api.png)

## Objetivos
- Autenticación de usuario
- Diseño de esquemas y bases de datos
- Diseño de API RESTful
- Operaciones CRUD
- Manejo de errores
- Seguridad

## Requerimientos
Debes desarrollar una API RESTful con los siguientes endpoints.  

- Registro de usuario para crear un nuevo usuario
- Endpoint de inicio de sesión para autenticar al usuario y generar un token
- Operaciones CRUD para gestionar la lista de tareas
- Implementar la autenticación de usuario para que solo los usuarios autorizados puedan acceder a la lista de tareas
- Implementar la gestión de errores y medidas de seguridad
- Usar una base de datos para almacenar los datos del usuario y de la lista de tareas (puedes usar cualquier base de datos)
- Implementar una validación de datos adecuada
- Implementar la paginación y el filtrado para la lista de tareas
- Implementar el filtrado y la ordenación para la lista de tareas
- Implementar pruebas unitarias para la API
- Implementar throttling para la API
- Implementar un mecanismo de token de actualización para la autenticación

## Pila tecnológica
- Lenguaje de programación: Python 3.11.3.
- Django Rest Framework (DRF).
- Base de datos SQLite.

## Cómo usar este proyecto
- Clone el repositorio.
- Instale las dependencias.
```
pip install -r requirements.txt
```
- Ejecute el servidor de desarrollo
```
python manage.py runserver
```
## API Endpoints
URL: /api/todo/createItem/  
Método: POST  
Descripción: Crea una nueva tarea en la to-do list.  
Respuesta: 201 Created. Tarea creada exitosamente.  
Ejemplo:
```JSON
{
    "title": "Test1",
    "description": "Test1"
}
```
URL: /api/todo/updateItem/{id_item}/  
Método: PUT  
Descripción: Actualiza una tarea existente en la to-do list.  
Respuesta: 200 OK. La tarea fue actualizada exitosamente.  
Ejemplo:
```JSON
{
    "title": "test",
    "description": "test"
}
```
URL: /api/todo/deleteItem/{id_item}/  
Método: DELETE  
Descripción: Elimina una tarea existente por ID.  
Respuesta: 204 No Content. Tarea eliminada exitosamente.  

## Métodos Get
Todos los métodos Get requieren dos parámetros obligatorios:  `page` y `limit`.

URL: /api/todo/listItem/?page=1&limit=5  
Método: GET  
Descripción: Devuelve una lista de tareas con 5 elementos por página.  
Respuesta: 200 OK.  
Ejemplo:
```JSON
{
    "count": 36,
    "next": "http://127.0.0.1/api/todo/listItem/?page=2&limit=5",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Difficult share second",
            "description": "Argue feel page how laugh.",
            "createdAt": "2021-02-02T00:07:39Z",
            "updatedAt": "2021-03-15T00:07:39Z"
        },
        {
            "id": 4,
            "title": "Figure until office marriage foreign",
            "description": "Somebody themselves next a production. Ball hotel somebody goal treatment worry despite possible. Offer loss or coach hotel continue arm.",
            "createdAt": "2020-09-26T23:20:09Z",
            "updatedAt": "2020-12-11T23:20:09Z"
        },
        {
            "id": 6,
            "title": "There floor green",
            "description": "Imagine property according every do offer. Stuff born stock environment improve work treatment. Film lawyer talk form.",
            "createdAt": "2021-11-01T05:27:12Z",
            "updatedAt": "2022-04-27T05:27:12Z"
        },
        {
            "id": 7,
            "title": "Deep produce light stop for contain nice we",
            "description": "Be evidence make heart bar leave line specific. Deep knowledge popular ten. Exactly lose might loss development away civil.",
            "createdAt": "2021-06-05T09:40:16Z",
            "updatedAt": "2021-10-28T09:40:16Z"
        },
        {
            "id": 9,
            "title": "Free themselves smile",
            "description": "Part cost law against. Several increase young simply from leader purpose. make",
            "createdAt": "2023-08-09T20:56:29Z",
            "updatedAt": "2024-07-12T20:56:29Z"
        }
    ]
}
```
## Filtrado
**Puedes filtrar por los siguientes campos: id, title, description, createdAt y updatedAt.**  

- URL: /api/todo/listItem/?page=1&limit=5&id=1 - Devuelve solo una tarea donde el campo "id" sea igual a 1  
- URL: /api/todo/listItem/?page=1&limit=5&title=test - Devuelve todas las tareas que contienen o coinciden con la palabra "test" en el campo de title  
- URL: /api/todo/listItem/?page=1&limit=5&description=test - Devuelve todas las tareas que contienen o coinciden con la palabra "test" en el campo de description  
- URL: /api/todo/listItem/?page=1&limit=5&createdAt=2021-02-02 - Devuelve todas las tareas que coinciden con la fecha en el campo createdAt  
- URL: /api/todo/listItem/?page=1&limit=5&updatedAt=2021-02-02 - Devuelve todas las tareas que coinciden con la fecha en el campo updatedAt  

## Ordenamiento
**Puedes ordenar por los siguientes campos: id, title, description, createdAt y updatedAt.**  

- URL: /api/todo/listItem/?page=1&limit=5&ordering=id - Devuelve todas las tareas ordenadas descendentemente por el campo "id" 
- URL: /api/todo/listItem/?page=1&limit=5&ordering=-id - Devuelve todas las tareas ordenadas ascendentemente por el campo "id"  
- URL: /api/todo/listItem/?page=1&limit=5&ordering=description - Devuelve todas las tareas ordenadas ascendentemente por el campo "description"  
- URL: /api/todo/listItem/?page=1&limit=5&ordering=-description - Devuelve todas las tareas ordenadas descendentemente por el campo "description"  

## Filtrado y ordenamiento combinados
Puedes combinar filtros y ordenamiento. Por ejemplo:  
- URL: /api/todo/listItem/?page=1&limit=5&title=test&ordering=id
- URL: /api/todo/listItem/?page=1&limit=5&title=test&description=test1&ordering=id
- URL: /api/todo/listItem/?page=1&limit=5&title=test&description=test1&ordering=createdAt

Método: GET 
Descripción: Devuelve una lista de tareas según filtros y opciones de ordenamiento.  
Respuesta: 200 OK.  

## Ejecución de casos de prueba
Puedes ejecutar los casos de prueba utilizando el siguiente comando:
```
python manage.py test
```
