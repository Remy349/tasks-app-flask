from flaskr import app, db
from flask import render_template, redirect, url_for, request, flash, session

from .models import Users

@app.route("/signin", methods=["GET", "POST"])
def signin():
    """ Funcion para manejar el inicio de sesion """
    if request.method == "GET":
        return redirect(url_for("index"))
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        errors = None

        user = Users.query.filter_by(username=username).first()

        if user is None:
            errors = "Invalid Username"
        elif not user.check_password(password):
            errors = "Invalid Password"

        if errors is None:
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("tasks"))

        if errors:
            flash(errors)
            return redirect(url_for("index"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ Funcion para manejar el registro de nuevos usuarios """
    if request.method == "GET":
        return render_template("auth/signup.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        errors = None

        user = Users.query.filter_by(username=username).first()

        if user is not None:
            errors = "Username already exist!"

        if errors is None:
            new_user = Users(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("index"))

        if errors:
            flash(errors)
            return redirect(url_for("signup"))

@app.route("/logout", methods=["GET"])
def logout():
    """ Funcion para el cierre de sesion """
    session.clear()
    return redirect(url_for("index"))
