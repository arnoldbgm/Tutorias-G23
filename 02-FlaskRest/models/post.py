from db import db
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

class PostModel(db.Model):
   __tablename__ = 'posts'

   id = Column(Integer, primary_key=True)
   titulo = Column(String(250), nullable=False)
   contenido = Column(Text, nullable=False)
   fecha = Column(DateTime, nullable=False)
   categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)  