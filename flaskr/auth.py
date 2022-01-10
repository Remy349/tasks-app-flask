from flaskr import app
from flask import request, render_template, redirect, url_for

@app.route("/signin", methods=["GET", "POST"])
def signin():
    """ Funcion para manejar el inicio de sesion """
    if request.method == "GET":
        return redirect(url_for("index"))
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        return render_template("index.html")
