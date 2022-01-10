from flaskr import app
from flask import render_template

@app.route("/", methods=["GET"])
def index():
    """ Funcion para mostrar la vista principal de la app """
    return render_template("index.html")
