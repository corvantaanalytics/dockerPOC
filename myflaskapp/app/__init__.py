from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('postgresql://postgres:postgres@flask_db:5432/postgres')
db = SQLAlchemy(app)

from app import routes, models
