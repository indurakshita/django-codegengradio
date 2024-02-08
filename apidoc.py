def generate_api_documents(api_parameter,id=None):
    documentation = f"""
Sample API Documentation
========================

Introduction
------------

This document provides details about the API endpoints and their usage.

Endpoints
---------

- GET /{api_parameter}: Retrieve all users
- GET /{api_parameter}/{id}: Retrieve a user by ID
- POST /{api_parameter}: Create a new user
- PUT /{api_parameter}/{id}: Update a user by ID
- DELETE /{api_parameter}/{id}: Delete a user by ID

Parameters
----------

- id: The ID of the user

Response
--------

- GET /{api_parameter}: Returns a list of users
- GET /{api_parameter}/{id}: Returns the user with the specified ID
- POST /{api_parameter}: Returns the created user
- PUT /{api_parameter}/{id}: Returns the updated user
- DELETE /{api_parameter}/{id}: Returns a success message
"""
    return documentation
# # Generate API documentation
# api_documentation = generate_api_documents()

# # Save to a file
# with open("api_documentation.txt", "w") as f:
#     f.write(api_documentation)


# import requests

# def generate_api_documents(api_parameter):
#     # Make a GET request to the API endpoint
#     api_url = f"https://example.com/generate_api_document?api_parameter={api_parameter}"  # Replace with your API endpoint
#     response = requests.get(api_url)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return f"Error: Failed to generate API document. Status code: {response.status_code}"