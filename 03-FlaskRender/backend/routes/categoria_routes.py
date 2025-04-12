# Aqui vamos a crear las rutas de mi API
# Y señalaremos como deben actuar estas rutas

from flask_restful import Resource
from flask import request
from models.categorias import CategoriaModel
from db import db


class CategoriaListResource(Resource):
    def post(self):
        # Aqui vamos a crear una categoria
        # Nosotros vamos a recibir un json con el nombre de la categoria
        # {
        #    "nombre": "Salud"
        # }
        # Si o si debes tener from flask import request
        data = request.get_json()

        # Vamos a insertar la categoria en la base de datos
        # Debes tener importado el modelo a donde insertaras
        nueva_categoria = CategoriaModel(nombre=data['nombre'])

        # Vamos a guardarlo en la bd => SQLAlchemy
        db.session.add(nueva_categoria)
        db.session.commit()

        # Siempre se devuelve una respuesta

        return {
            'id': nueva_categoria.id,
            'nombre': nueva_categoria.nombre
        }, 201  # 201 Significa CREACION EXITOSA

    def get(self):
      #   SELECT * FROM categorias;
        categorias = CategoriaModel.query.all()
        categoriaLista = []

        for categoria in categorias:
            categoriaLista.append({
                'id': categoria.id,
                'nombre': categoria.nombre
            })
        return categoriaLista, 200
