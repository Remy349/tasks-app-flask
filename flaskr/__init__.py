from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
# Inicializar la base de datos y migraciones
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flaskr import routes
from flaskr import auth
from flaskr import models
