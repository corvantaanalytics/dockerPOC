# dockerPOC
Let's create a CRUD Rest API in Python, using:
Flask, SQLALchemy as an ORM , Postgres, Docker, Docker Compose and TablePlus.

>>> Required Python version 3

>>> Required TablePlus  https://tableplus.com/download

>>> Install Docker https://www.docker.com/products/docker-desktop/
    

>>> Required PIP 

# requirements.txt ---> just for reference 
>>> The requirements.txt file contains all the dependencies of the project.
Explanation of the dependencies we used in Project:

  > flask is the Python web framework we are gonna use.

  > psycopg2-binary is the driver to make the connection with the Postgres database.

  > Flask-SQLAlchemy is the ORM to make the queries to the database.


# Let's populate the Dockerfile : ---> just for reference 

> Use an official Python runtime as a parent image
  FROM python:3.8-slim

> Set the working directory to /app
  WORKDIR /app

>  Copies the requirements.txt file 
  COPY requirements.txt ./

> Installs the Python packages listed in requirements.txt inside the container.
  RUN pip install -r requirements.txt

> Copies the rest of your application code from your host machine to the /app directory inside the container.
  COPY . .

> Make port 4000 available to the world outside this container
  EXPOSE 4000

> Specifies the command to run when the container starts. It launches the Flask development server to serve your app on all available network
 interfaces (--host=0.0.0.0) and on port 4000 (--port=4000).
 CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]


## To Run the App
>>version check whether docker is connected or not 
STEP 1 ==>> docker --version

>>To run the Postgres container
STEP 2 ==>> docker compose up -d flask_db

>>To check if the container is running
STEP 3 ==>>docker compose logs

>>To show all the Existing containers
STEP 4 ==>>docker ps -a


>>Now, to test the db connection, we need to use TablePlus.
STEP 5 ==>>
> open TablePlus 

> press the add button select PostgreSQL 

> and enter 

   >>Host: localhost

   >>Port: 5432

   >>User: postgres

   >>Password: postgres

   >>Database: postgres

> Then hit "Test" (at the bottom-right).

> If you get the message "connection is OK" you are good to go.

> You can also click "Connect" and you will see an empty database. This is correct.

 
>>Build the Flask application
STEP 6 ==>>
docker compose build

>>Run the flask_app 
STEP 7 ==>>
docker compose up flask_app

>> Test the application
   Let's test our application. First of all, let's go and visit localhost:4000/test

>> You shoulds see this result:
   {"message":"test route"}

>> Now it's time to test all the endpoints using Postman.