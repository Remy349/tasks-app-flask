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
            "id": t.id,
            "title": t.title,
            "description": t.description,
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

@app.route("/tasks/edit/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_tasks(task_id):
    """ Funcion para la edicion de las tareas """
    if request.method == "GET":
        task = Tasks.query.filter_by(id=task_id).first()
        return render_template("routes/task_edit.html", task=task)
    elif request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        task = Tasks.query.filter_by(id=task_id).first()
        task.title = title
        task.description = description

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("tasks"))

@app.route("/tasks/delete/<int:task_id>", methods=["GET"])
@login_required
def delete_tasks(task_id):
    """ Funcion para manejar el borrado de tareas de la basse de datos """
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))
