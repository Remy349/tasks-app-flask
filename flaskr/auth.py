from flaskr import app
from flask import request, render_template, redirect, url_for

from .models import Users

@app.route("/signin", methods=["GET", "POST"])
def signin():
    """ Funcion para manejar el inicio de sesion """
    if request.method == "GET":
        return redirect(url_for("index"))
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

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

        return redirect(url_for("index"))
