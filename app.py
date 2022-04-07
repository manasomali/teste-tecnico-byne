# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, session
from utils import LoggingModifier, RequestsManager

class Application:
    def __init__(self, base_url="http://localhost:8000/", testing=False, debuging=False):
        self.application = Flask(__name__)
        self.application.config["BASE_URL"] = base_url
        self.application.config["TESTING"] = testing
        self.application.config["DEBUG"] = debuging
        self.application.config[
            "SECRET_KEY"
        ] = "\xd91t\xfd_\xbb\xfc\x0b\xc2\xea\xcclg\x9f\xadu\xd1\xf6\xd9\xc5\x85f5\x17"

    def run(self):
        self.application.run(host=self.application.config["BASE_URL"])
        

    def register_blueprint(self, api, prefix):
        self.application.register_blueprint(api, url_prefix=prefix)

    def setup_routes(self, log_mod: LoggingModifier, req_man: RequestsManager):
        @self.application.route("/", methods=["GET", "POST"])
        def index():
            if not session.get("name"):
                return redirect("/login")

            return render_template(
                "home.html",
                nome=session.get("name"),
                base_url=self.application.config["BASE_URL"],
            )

        @self.application.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                if request.form.get("name") in req_man.get_users_keys():
                    session["name"] = request.form.get("name")
                    log_mod.write_message("User {} login successfully".format(session["name"]))
                    return redirect("/")

                return redirect("/register")
            return render_template("login.html")

        @self.application.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "POST":
                if request.form.get("name") in req_man.get_users_keys():
                    return redirect("/login")

                session["name"] = request.form.get("name")
                req_man.register_user(request.form.get("name"))
                log_mod.write_message("User {} registred".format(session["name"]))
                return redirect("/")
            return render_template("register.html")

        @self.application.route("/logout", methods=["GET", "POST"])
        def logout():
            log_mod.write_message("User {} logout".format(session["name"]))
            session.clear()
            return redirect("/")
