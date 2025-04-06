# SQL Alchemy se usa en todo el proyecto y lo correcto par no repetir el código es crear un archivo db.py y no crear multiples instances de SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()