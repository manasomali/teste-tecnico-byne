# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, session
from utils import LoggingModifier, RequestsManager


class Application:
    def __init__(self, host, port, secret_key, testing=False, debuging=False):
        self.app = Flask(__name__)
        self.app.config["HOST"] = host
        self.app.config["TESTING"] = testing
        self.app.config["DEBUG"] = debuging
        self.app.config["PORT"] = port
        self.app.config["SECRET_KEY"] = secret_key

    def run(self):
        self.app.run(
            host=self.app.config["HOST"],
            port=self.app.config["PORT"],
            debug=self.app.config["DEBUG"],
        )

    def register_blueprint(self, api, prefix):
        self.app.register_blueprint(api, url_prefix=prefix)

    def setup_routes(self, log_mod: LoggingModifier, req_man: RequestsManager):
        @self.app.route("/", methods=["GET", "POST"])
        def index():
            if not session.get("name"):
                return redirect("/login")

            return render_template(
                "home.html",
                nome=session.get("name"),
                base_url="http://{}:{}/".format(
                    self.app.config["HOST"], self.app.config["PORT"]
                ),
            )

        @self.app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                if request.form.get("name") in req_man.get_users_keys():
                    session["name"] = request.form.get("name")
                    log_mod.write_message(
                        "User {} login successfully".format(session["name"])
                    )
                    return redirect("/")

                return redirect("/register")
            return render_template("login.html")

        @self.app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "POST":
                if request.form.get("name") in req_man.get_users_keys():
                    return redirect("/login")

                session["name"] = request.form.get("name")
                req_man.register_user(request.form.get("name"))
                log_mod.write_message(
                    "User {} registred".format(session["name"])
                )
                return redirect("/")
            return render_template("register.html")

        @self.app.route("/logout", methods=["GET", "POST"])
        def logout():
            log_mod.write_message("User {} logout".format(session["name"]))
            session.clear()
            return redirect("/")
