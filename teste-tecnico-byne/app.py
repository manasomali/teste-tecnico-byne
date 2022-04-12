# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, session
from utils import LoggingModifier, RequestsManager, DataModifier
from random import randint


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
                if request.form.get("name") in req_man.get_users():
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
                if request.form.get("name") in req_man.get_users():
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

    def setup_api(
        self,
        log_mod: LoggingModifier,
        data_base: DataModifier,
    ):
        @self.app.route("/odd", methods=["GET"])
        def odd():
            if request.method == "GET":
                odd = 0
                while (odd % 2) == 0:
                    odd = randint(0, 99)

                log_mod.write_message(
                    "Odd number requisited -> {}".format(odd)
                )
                return str(odd)

        @self.app.route("/even", methods=["GET"])
        def even():
            if request.method == "GET":
                even = 1
                while (even % 2) != 0:
                    even = randint(0, 99)

                log_mod.write_message(
                    "Even number requisited ->  {}".format(even)
                )
                return str(even)

        @self.app.route("/getgeneralvalue/<user>", methods=["GET"])
        def getgeneralvalue(user):
            if request.method == "GET":
                data = data_base.get_data(user)
                log_mod.write_message(
                    "User {} request general number -> {}".format(user, data)
                )
                return str(data)

        @self.app.route(
            "/putgeneralvalue/<user>/<int:increment>", methods=["GET"]
        )
        def putgeneralvalue(user, increment):
            if request.method == "GET":
                data_base.update_data(user, increment)
                log_mod.write_message(
                    "General number incremented by {} -> {}".format(
                        user, increment
                    )
                )
                return str(data_base.get_data(user))

        @self.app.route("/getusers", methods=["GET"])
        def getusers():
            if request.method == "GET":
                users_list = [*data_base.get_all_data()]
                return str(users_list)

        @self.app.route("/registeruser/<user>", methods=["GET"])
        def registeruser(user):
            if request.method == "GET":
                data_base.add_data(user)
                log_mod.write_message(
                    "User {} registred successfully".format(user)
                )
                return "0"
