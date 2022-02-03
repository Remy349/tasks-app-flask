from flaskr import app, db
from flask import render_template, request, redirect, url_for, jsonify, session
from helpers import login_required

from .models import Tasks, Users

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
        # Llamar a todas las tareas del usuario que este en la sesion
        tasks = user.tasks.all()
        return render_template("routes/tasks.html", username=username, tasks=tasks)

@app.route("/tasks_get", methods=["GET"])
def tasks_get():
    """
        El cliente realizara una llamada a esta ruta del servidor para 
        obtener los datos de manera ascincrona sin recargar la pagina
    """
    user_id = session["user_id"]
    user = Users.query.get(user_id)
    tasks = user.tasks.all()
    tasks_list = []

    for t in tasks:
        task = {
            "title": t.title,
            "description": t.description,
            "timestamp": t.timestamp,
        }
        tasks_list.append(task)

    return jsonify(tasks_list)

@app.route("/tasks", methods=["POST"])
def tasks_post():
    """ Procesar los datos del formulario para guardar en la db """
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        user_id = session["user_id"]
        user = Users.query.get(user_id)

        new_task = Tasks(title=title, description=description, author=user)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("tasks"))
