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
            errors = "Invalid Username!"
        elif not user.check_password(password):
            errors = "Invalid Password!"
        elif not username or not password:
            errors = "Filds can not be empty!"

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
        password_again = request.form["password_again"]
        errors = None

        user = Users.query.filter_by(username=username).first()

        if user is not None:
            errors = "Username already exist!"
        elif not username or not password or not password_again:
            errors = "Filds can not be empty!"
        elif len(username) > 12 or len(username) < 3:
            errors = "Username length can not be longer than 12 or shorter than 3 characters"
        elif len(password) > 12 or len(password) < 6:
            errors = "Password length can not be longer than 12 or shorter than 6 characters"

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
