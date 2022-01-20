from flaskr import app
from flask import render_template, request, redirect, url_for, jsonify
from helpers import login_required

from .models import Tasks

@app.route("/", methods=["GET"])
def index():
    """ Funcion para mostrar la vista principal de la app """
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
@login_required
def tasks():
    """ Funcion para mostrar formulario de creacion de nuevas tareas """
    if request.method == "GET":
        return render_template("routes/tasks.html")

@app.route("/tasks_get", methods=["GET"])
def tasks_get():
    task = {
        "title": "Test1",
        "description": "Prueba de Test1",
    }
    return jsonify(task)

@app.route("/tasks", methods=["POST"])
def tasks_post():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        print(title, description)
        return redirect(url_for("tasks"))
