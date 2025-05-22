Solution for the [Blogging Platform API](https://roadmap.sh/projects/blogging-platform-api) Challenge from [roadmap.sh](https://roadmap.sh) 

## Blogging Platform API
In this project, we need to create a simple RESTful API with basic CRUD operations for a personal blogging platform. CRUD stands for Create, Read, Update, and Delete.  
The goal of this challenge is to help us understand how REST architecture works (Representational State Transfer). It allows applications to communicate with each other, usually over the web, using the HTTP protocol.

## Requirements
The requirements for this challenge are to create a RESTful API for a personal blogging platform. The API should allow users to perform the following operations:  
* Create a new blog post.
* Update a blog post.
* Delete a blog post.
* Get a single blog post.
* Get all blog posts.
* Filter blog posts using a search term (title or content).  

It is not necessary to implement pagination, authentication, or authorization for this challenge.  
We will focus on the core functionality of the API.

## Tech Stack
* Django REST Framework.
* SQLite database.

## How to use this project
* Clone the repository
* Install dependencies
```
pip install -r requirements.txt
```
* Start the development server
```
python manage.py runserver
```

## API Endpoints

### Get all blog posts
**URL**: /api/listAllPost/  
**Method**: GET  
**Description**: Getting a list of all blog posts.  
**Response**: 200 OK. Returns a list of all blog posts.  
**Example**:

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
### Get a single blog post by ID
**URL**: /api/getPost/{id_post}/  
**Method**: GET  
**Description**: Retrieve a single blog post by its ID.  
**Response**: 200 OK. Returns the blog post with the specified ID.  
**Example**:
```JSON
{
    "id_post": 2,
    "title": "test one",
    "content": "Content test",
    "createdAt": "22-05-2025 03:20:43",
    "updateAt": null
}
```
### Search blog posts by term
**URL**: /api/searchPost/{term}/  
**Method**: GET  
**Description**: Retrieve a list of blog posts matching the search term.  
**Response**: 200 OK. Returns a list of matching blog posts.  
**Example**:
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
### Create a new blog post
**URL**: /api/createPost/  
**Method**: POST  
**Description**: Create a new blog post.  
**Response**: 201 Created. The blog post has been successfully created.  
**Example**:
```JSON
{
   "title": "test three",
   "content": "Content test" 
}
```
### Update an existing blog post
**URL**: /api/updatePost/{id_post}/  
**Method**: PUT  
**Description**: Update an existing blog post.  
**Response**: 200 OK. The blog post has been successfully updated.  
**Example**:
```JSON
{
    "title": "test update",
    "content": "Content test"
}
```
### Delete an existing blog post
**URL**: /api/deletePost/{id_post}/  
**Method**: DELETE  
**Description**:  Delete an existing blog post by ID.  
**Response**: 204 No Content. The blog post has been successfully deleted.  

## API Endpoint Documentation
**URL**: /api/schema/swagger-ui/  
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Blogging_Platform_API/IMG/swagger-ui.png)

## Demo Video
![alt text](https://github.com/LW-Homeless/ROADMAP/blob/main/backend/Blogging_Platform_API/IMG/Blogging_Platform_API.gif)
