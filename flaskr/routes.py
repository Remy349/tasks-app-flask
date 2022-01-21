from flaskr import app
from flask import render_template, request, redirect, url_for, jsonify, session
from helpers import login_required

from .models import Tasks, Users

tasks_list = []

@app.route("/", methods=["GET"])
def index():
    """ Funcion para mostrar la vista principal de la app """
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
@login_required
def tasks():
    """ Funcion para mostrar formulario de creacion de nuevas tareas """
    if request.method == "GET":
        user_id = session["user_id"]
        user = Users.query.get(user_id)
        username = user.username
        print(tasks_list, user)
        return render_template("routes/tasks.html", username=username, tasks=tasks_list)

@app.route("/tasks_get", methods=["GET"])
def tasks_get():
    """ 
        El cliente realizara una llamada a esta ruta del servidor para 
        obtener los datos de manera ascincrona sin recargar la pagina
    """
    return jsonify(tasks_list)

@app.route("/tasks", methods=["POST"])
def tasks_post():
    """ Procesar los datos del formulario para guardar en la db """
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        task = {
            "title": title,
            "description": description
        }
        tasks_list.append(task)
        print(tasks_list)
        return redirect(url_for("tasks"))
