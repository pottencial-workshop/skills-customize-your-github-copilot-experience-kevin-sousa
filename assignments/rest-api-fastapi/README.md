# 📘 Assignment: REST API with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to practice creating web services, handling HTTP requests, working with JSON data, and implementing CRUD operations.

## 📝 Tasks

### 🛠️ Setup and Basic Endpoints

#### Description
Set up a FastAPI project and create basic GET endpoints to return data.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a basic FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/items` that returns a list of sample items (e.g., books, products, or tasks)
- Run the server and test the endpoints using a browser or API client


### 🛠️ Path Parameters and Query Parameters

#### Description
Enhance your API by adding endpoints that accept parameters to retrieve specific data.

#### Requirements
Completed program should:

- Create a GET endpoint `/items/{item_id}` that accepts a path parameter and returns a specific item
- Add query parameters to the `/items` endpoint to filter results (e.g., `?category=electronics&limit=5`)
- Handle cases where an item is not found and return an appropriate error message
- Use Pydantic models to validate and structure the response data


### 🛠️ POST, PUT, and DELETE Operations

#### Description
Implement create, update, and delete operations to complete the CRUD functionality of your API.

#### Requirements
Completed program should:

- Create a POST endpoint `/items` that accepts JSON data to add a new item
- Create a PUT endpoint `/items/{item_id}` to update an existing item
- Create a DELETE endpoint `/items/{item_id}` to remove an item
- Use Pydantic models to validate incoming request data
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Test all endpoints using the automatic interactive documentation at `/docs`
