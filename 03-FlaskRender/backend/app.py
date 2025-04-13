from flask import Flask 
from flask_restful import Api # Para crear una API RESTful
from db import db
from flask_migrate import Migrate
from models.categorias import CategoriaModel #Es mi tabla de categorias
from models.post import PostModel #Es mi tabla de post
from routes.categoria_routes import CategoriaListResource
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Creamos la instancia de flask
app = Flask(__name__)
CORS(app)
# Vamos a conectarnos con nuestra base de datos (SQLAlchemy)
# Debes de usar el config de tu instancia de Flask
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

# Configuramos la base de datos
db.init_app(app)

# Para poder ver las tablas ya dentro de la base de datos debemos ejecutar
# Una migracion
migrate = Migrate(app,db)

# Para que mi aplicacion funcione como una bd Flask_restful
api = Api(app)

# Aqui declaramos las rutas de mi API
api.add_resource(CategoriaListResource, '/categorias')

# Levantar nuestro servidor
if __name__ == '__main__':
    app.run(debug=True)