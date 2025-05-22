Solución para el desafío [Blogging Platform API](https://roadmap.sh/projects/blogging-platform-api) de [roadmap.sh](https://roadmap.sh)  

## Blogging Platform API  
En este proyecto, necesitamos crear una API RESTful simple con operaciones CRUD básicas para una plataforma de blogs personales. CRUD significa Crear, Leer, Actualizar y Eliminar.  
Los objetivos de este desafío son ayudarnos a comprender cómo funciona la arquitectura REST (Transferencia de Estado Representacional). Permite a las aplicaciones comunicarse entre sí, generalmente a través de la web, utilizando el protocolo HTTP. En esencia, es una forma estandarizada de intercambiar datos y realizar operaciones en sistemas distribuidos.  

## Requerimientos
Los requerimientos para este desafío son crear API RESTful para una plataforma de blogging personal. La API debera permitir a los usuarios ejecutar las siguientes operaciones:  
* Crear un nuevo blog post.
* Actualizar un blog post existente.
* Eliminar un blog post existente.
* Obtener un unico blog post.
* Obtener una lista de blog posts.
* Filtrar los blog posts por termino de búsqueda(Título, Contenido).  

No es necesario implementar paginación, autenticación ni autorización para este desafío.  
Solo nos concentraremos en la funcionalidad principal de la API.  

## Tecnología utilizada en este projecto.
* Django Rest Framework.
* Administrador de Base de datos SQLite.  

## Instrucciones de uso
* Clone el repositorio.
* Instale las dependencias con el siguiente comando.
```
pip install -r requirements.txt
```
* Ejecute el servidor de desarrollo.
```
python manage.py runserver
```
La API estará disponible en http://127.0.0.1:8000/api/

## API Endpoints

### Listar todos los post
**URL**: /api/listAllPost/  
**Método**: GET  
**Descripción**: Recupera una lista de todas las publicaciones del blog.  
**Respuesta**: 200 OK. Devuelve una lista de posts.  
**Ejemplo**:

```JSON
[
    {
        "id_post": 2,
        "title": "test one",
        "content": "Content test",
        "createdAt": "22-05-2025 03:20:43",
        "updateAt": null
    },
    {
        "id_post": 3,
        "title": "test two",
        "content": "Content test",
        "createdAt": "22-05-2025 03:20:59",
        "updateAt": null
    }
]
```
### Obtenet un único post por ID.
**URL**: /api/getPost/{id_post}/  
**Método**: GET  
**Descripción**: Recupera un único post por ID.  
**Respuesta**: 200 OK. Devuelve un único posts.  
**Ejemplo**:
```JSON
{
    "id_post": 2,
    "title": "test one",
    "content": "Content test",
    "createdAt": "22-05-2025 03:20:43",
    "updateAt": null
}
```
### Obtenet una lista post por termino de búsqueda.
**URL**: /api/searchPost/{term}/  
**Método**: GET  
**Descripción**: Recupera una lista de post filtrado por termino de búsqueda.  
**Respuesta**: 200 OK. Devuelve una lista de posts.  
**Ejemplo**:
```JSON
[
    {
        "id_post": 2,
        "title": "test one",
        "content": "Content test",
        "createdAt": "22-05-2025 03:20:43",
        "updateAt": null
    },
    {
        "id_post": 3,
        "title": "test two",
        "content": "Content test",
        "createdAt": "22-05-2025 03:20:59",
        "updateAt": null
    }
]
```
### Crear un nuevo post
**URL**: /api/createPost/  
**Método**: POST  
**Descripción**: Crea un nuevo post.  
**Respuesta**: 201 Created. Crea un nuevo post.  
**Ejemplo**:
```JSON
{
   "title": "test three",
   "content": "Content test" 
}
```
### Actualizar un post existente
**URL**: /api/updatePost/{id_post}/  
**Método**: PUT  
**Descripción**: Actualiza un post existente.  
**Respuesta**: 200 OK. Actualiza un post existente.  
**Ejemplo**:
```JSON
{
    "title": "test update",
    "content": "Content test"
}
```
### Eliminar un post existente
**URL**: /api/deletePost/{id_post}/  
**Método**: DELETE  
**Descripción**: Elimina un post existente.  
**Respuesta**: 204 No Content. Elimina un post existente.

## API Documentación Endpoints
**URL**: /api/schema/swagger-ui/  
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Blogging_Platform_API/IMG/swagger-ui.png)

## Video demostración
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Blogging_Platform_API/IMG/Blogging_Platform_API.gif)
