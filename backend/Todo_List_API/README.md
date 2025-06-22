Solution to the [Todo List API](https://roadmap.sh/projects/todo-list-api) Challenge from [roadmap.sh](https://roadmap.sh)  
## Todo List API
In this project, you are required to develop a RESTful API that allows users to manage their to-do lists. This project will
help you understand how to design and implement a RESTful API with user authentication.
You'll also learn how to work with databases, handle errors, and implement security measures.  
[image]

## Goals
- User authentication
- Schema design and databases
- RESTful API design
- CRUD operations
- Error handling
- Security

## Requirements
You are required to develop a RESTful API with the following endpoints.
- User registration to create a new user
- Login endpoint to authenticate the user and generate a token
- CRUD operations for managing the to-do list
- Implement user authentication to allow only authorized users to access the to-do list
- Implement error handling and security measures
- Use a database to store the user and to-do list data (you can use any database of your choice)
- Implement proper data validation
- Implement pagination and filtering for the to-do list
- Implement filtering and sorting for the to-do list
- Implement unit tests for the API
- Implement rate limiting and throttling for the API
- Implement a refresh token mechanism for the authentication

## Tech Stack
- Programming Language: Python 3.11.3.
- Django Rest Framework (DRF).
- SQLite database.

## How to use this project
- Clone the repository
- Install dependencies
```
pip install -r requirements.txt
```
- Start the development server
```
python manage.py runserver
```
## API Endpoints
URL: /api/todo/createItem/  
Method: POST  
Description: Create a new item in the to-do list.  
Response: 201 Created. The item has been successfully created.  
Example:
```JSON
{
    "title": "Test1",
    "description": "Test1"
}
```
URL: /api/todo/updateItem/{id_item}/  
Method: PUT  
Description: Update an existing item in the to-do list.  
Response: 200 OK. The item has been successfully updated.  
Example:
```JSON
{
    "title": "test",
    "description": "test"
}
```
URL: /api/todo/deleteItem/{id_item}/  
Method: DELETE  
Description: Delete an existing item by ID.  
Response: 204 No Content. The item has been successfully deleted.  

## Get Methods 
All GET methods require two mandatory parameters:  `page` and `limit`.

URL: /api/todo/listItem/?page=1&limit=5  
Method: GET  
Description: Return a list of items with five items per page.  
Response: 200 OK.  
Example:
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
## Filtering
**You can filter by the following fields: id, title, description, createdAt, and updatedAt.**  

- URL: /api/todo/listItem/?page=1&limit=5&id=1 - Return a single item where the "id" field is equal to 1  
- URL: /api/todo/listItem/?page=1&limit=5&title=test - Returns all items that contain or match the word "test" in the title field  
- URL: /api/todo/listItem/?page=1&limit=5&description=test - Returns all items that contain or match the word "test" in the description field  
- URL: /api/todo/listItem/?page=1&limit=5&createdAt=2021-02-02 - Returns all items that match the date in the createdAt field  
- URL: /api/todo/listItem/?page=1&limit=5&updatedAt=2021-02-02 - Returns all items that match the date in the updatedAt field  

## Sorting
**You can sort by the following fields: id, title, description, createdAt, and updatedAt.**  

- URL: /api/todo/listItem/?page=1&limit=5&ordering=id - Returns all items sorted ascending by the "id" field  
- URL: /api/todo/listItem/?page=1&limit=5&ordering=-id - Returns all items sorted descending by the "id" field  
- URL: /api/todo/listItem/?page=1&limit=5&ordering=description - Returns all items sorted ascending by the "description" field  
- URL: /api/todo/listItem/?page=1&limit=5&ordering=-description - Returns all items sorted descending by the "description" field  

## Combined Filtering and Sorting
You can combine filters and sorting. For example.  
- URL: /api/todo/listItem/?page=1&limit=5&title=test&ordering=id
- URL: /api/todo/listItem/?page=1&limit=5&title=test&description=test1&ordering=id
- URL: /api/todo/listItem/?page=1&limit=5&title=test&description=test1&ordering=createdAt

Method: GET 
Description: Return a list of items based on filters and sorting options.  
Response: 200 OK.  

## Running Tests
You can run the test cases using the following command:

```
python manage.py test
```