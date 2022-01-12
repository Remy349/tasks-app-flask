from flask import Flask, render_template
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
# Funcion para mostrar un error(404) personalizado
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

from flaskr import routes
from flaskr import auth
from flaskr import models
