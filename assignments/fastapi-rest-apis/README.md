# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a basic REST API using FastAPI and learn how to define routes, handle request data, and return JSON responses. This assignment introduces students to API design patterns and common web service functionality.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a small FastAPI application that serves a collection of items and exposes a few API endpoints.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application.
- Define a root endpoint that returns a simple welcome message or status payload.
- Use a request body model with `pydantic` for validating incoming data.
- Run the app locally with Uvicorn or FastAPI’s development server.

### 🛠️ Build Read Endpoints

#### Description
Add endpoints that allow clients to retrieve all items and fetch a single item by ID.

#### Requirements
Completed program should:

- Create a `GET /items` route that returns a list of items in JSON format.
- Create a `GET /items/{item_id}` route that returns one matching item.
- Include meaningful data for each item, such as `id`, `name`, and `price`.
- Return a clear error response when an item ID is not found.

### 🛠️ Add Create and Update Functionality

#### Description
Extend the API so clients can create new items and update existing ones.

#### Requirements
Completed program should:

- Create a `POST /items` route that accepts item data and adds it to the collection.
- Create a `PUT /items/{item_id}` route that updates an existing item.
- Validate the data format before saving or updating results.
- Return the updated item or a confirmation response in JSON.

### 🛠️ Add API Documentation and Validation

#### Description
Use FastAPI’s built-in features to make the API easier to test and understand.

#### Requirements
Completed program should:

- Use the auto-generated docs available through the FastAPI interface.
- Add clear response models or type hints for better validation.
- Ensure endpoints behave consistently for valid and invalid requests.
- Explain in comments or documentation how the API is organized.
