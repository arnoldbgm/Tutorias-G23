from db import db
from sqlalchemy import Column, Integer, String

# Crearemos la tabla categorias
class CategoriaModel(db.Model):
   # __tablename__ es el nombre de la tabla en la base de datos
   __tablename__ = 'categorias'

   id = Column(Integer, primary_key=True)
   nombre = Column(String(250), nullable=False)