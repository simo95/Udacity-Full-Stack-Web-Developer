Full Stack Casting Agency API Backend
Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Motivation for project
This is the capstone project of Udacity fullstack nanodegree program, which demonstrate the skillset of using Flask, SQLAlchemy, Auth0, gunicorn and heroku to develop and deploy a RESTful API.
Getting Started
Installing Dependencies
Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

### APP is hosted at [https://udaacity-fsnd-capstone.onrender.com](https://capstone-final-nyxk.onrender.com)
### In local run it will run at http://127.0.0.1:8080

As this currently contains only backend implementation so we can access endpoints through the postman collection in this repo

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
### Models:
Movies with attributes title and release date
Actors with attributes name, age and gender
### Endpoints:
- GET /actors and /movies
- GET /actors/<id> and /movies/<id>
- DELETE /actors/<id> and /movies/<id>
- POST /actors and /movies and
- PATCH /actors/<id> and /movies/<id>

### API Reference

Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False,
    "error": 400,
    "message": "bad request"
}

  
### Roles:
#### Casting Assistant
      - Can view actors and movies
#### Casting Director
      - All permissions a Casting Assistant has and…
      - Add or delete an actor from the database
      - Modify actors or movies
#### Executive Producer
      - All permissions a Casting Director has and…
      - Add or delete a movie from the database

  #### creds for different roles:
  - Casting Assistant username:casting_assistant@abc.com    password:Udacity@123
  - Casting Director username:casting_director@abc.com    password:Udacity@123
  - Executive Producer username:executive_producer@abc.com    password:Udacity@123
