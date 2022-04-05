# -*- coding: utf-8 -*-
import logging
from flask import Flask, render_template, redirect, request, session
from apis import blueprint as api
from utils import getKeys, registerUser

app = Flask(__name__)
# app.config['BASE_URL'] = 'https://teste-tecnico-byne.herokuapp.com'
app.config["BASE_URL"] = "http://127.0.0.1:5000"
app.config["TESTING"] = False
app.config["DEBUG"] = False
app.config[
    "SECRET_KEY"
] = "\xd91t\xfd_\xbb\xfc\x0b\xc2\xea\xcclg\x9f\xadu\xd1\xf6\xd9\xc5\x85f5\x17"

logging.basicConfig(
    format="%(asctime)s -> %(message)s", filename="logs.log", level=logging.WARNING
)
logging.getLogger("werkzeug").disabled = True

app.register_blueprint(api, url_prefix="/api")


@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("name"):
        return redirect("/login")

    return render_template(
        "home.html", nome=session.get("name"), base_url=app.config["BASE_URL"]
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("name") in getKeys(app):
            session["name"] = request.form.get("name")
            logging.warning("Usuario %s logado", session["name"])
            return redirect("/")

        return redirect("/register")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.form.get("name") in getKeys(app):
            return redirect("/login")

        session["name"] = request.form.get("name")
        registerUser(app, request.form.get("name"))
        logging.warning("User %s registred", session["name"])
        return redirect("/")
    return render_template("register.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logging.warning("User %s logout", session["name"])
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run()
