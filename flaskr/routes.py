from flaskr import app
from flask import render_template
from helpers import login_required

@app.route("/", methods=["GET"])
def index():
    """ Funcion para mostrar la vista principal de la app """
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
@login_required
def tasks():
    """ 
        Funcion para mostrar formulario de creacion de nuevas tareas y 
        lista de todas las tareas creadas
    """
    return render_template("routes/tasks.html")
