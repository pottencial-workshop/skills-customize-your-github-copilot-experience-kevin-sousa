# REST API with FastAPI - Starter Code
# This file provides the basic structure to get you started

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI()

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float
#     category: str


# TODO: Create a sample data store (in-memory database)
# Example: items_db = []


# TODO: Task 1 - Implement basic GET endpoints
@app.get("/")
def read_root():
    """
    Welcome endpoint
    Returns a welcome message
    """
    pass


@app.get("/items")
def read_items():
    """
    Get all items
    Should support query parameters for filtering
    """
    pass


# TODO: Task 2 - Implement path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Get a specific item by ID
    Should return 404 if item not found
    """
    pass


# TODO: Task 3 - Implement POST, PUT, and DELETE operations
@app.post("/items", status_code=201)
def create_item():
    """
    Create a new item
    Should accept JSON data and validate with Pydantic
    """
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int):
    """
    Update an existing item
    Should return 404 if item not found
    """
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Delete an item
    Should return 404 if item not found
    """
    pass


# To run this application:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Open your browser to http://127.0.0.1:8000/docs for interactive API documentation
