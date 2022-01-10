import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Clase para manejar de manera mas facil las configuraciones de la app """
    # Clave secreta para las sesiones del lado del cliente
    SECRET_KEY = os.getenv("SECRET_KEY")
    # URL de la base de datos o crear una dentro del proyecto
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
