# Importancion de Flask
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base de datos en memoria (se pierde cuando se apaga el servidor)
usuarios = [
    {"id": 1, 
     "nombre": "Juan Pérez", 
     "edad": 25, 
     "ciudad": "Ciudad de México"},
    {"id": 2, 
     "nombre": "Ana Gómez", 
     "edad": 30, 
     "ciudad": "Buenos Aires"},
    {"id": 3, 
     "nombre": "Carlos López", 
     "edad": 22, 
     "ciudad": "Madrid"}
]

# METODOS HTTP
# POST => Insertar
# PUT PATCH => Editar
# DELETE  => Eliminar
# GET => Obtener

# Para crear un endpoint usaremos el @
@app.route("/api/usuarios", methods=["GET"])
def obtener_usuarios():
   return jsonify(usuarios)

if __name__ == "__main__":
   app.run(debug=True)