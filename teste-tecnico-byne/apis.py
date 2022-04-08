# -*- coding: utf-8 -*-
from random import randint
from flask import Blueprint
from flask_restx import Api, Resource, reqparse
from utils import DataModifier, LoggingModifier

log_mod = LoggingModifier(file_name="logs.log")
blueprint = Blueprint("api", __name__)
api = Api(blueprint)

database = DataModifier("data.json")

parser = reqparse.RequestParser()
parser.add_argument("user", type=str, help="User needed")
parser.add_argument("increment", type=int, help="Increment needed")


@api.route(
    "/odd",
    doc={"description": "Generate a randon odd number betewen 0 and 99"},
)
class Odd(Resource):
    def get(self):
        odd = 0
        while (odd % 2) == 0:
            odd = randint(0, 99)

        log_mod.write_message("Odd number requisited -> {}".format(odd))
        return odd


@api.route(
    "/even",
    doc={"description": "Generate a randon even number betewen 0 and 99"},
)
class Even(Resource):
    def get(self):
        even = 1
        while (even % 2) != 0:
            even = randint(0, 99)

        log_mod.write_message("Even number requisited ->  {}".format(even))
        return even


@api.route(
    "/getgeneralvalue",
    doc={"description": "Returns the general value of all users"},
)
class GetGeneralValue(Resource):
    def get(self):
        data = database.get_data()
        log_mod.write_message("Request general numbers -> {}".format(data))
        return data


@api.route(
    "/putgeneralvalue",
    doc={"description": "Increment general value of determined user"},
)
class PutGeneralValue(Resource):
    @api.doc(
        params={
            "user": "User name to register",
            "increment": "Value to be incremented",
        }
    )
    def put(self):
        user = parser.parse_args().get("user")
        increment = parser.parse_args().get("increment")
        database.update_data(user, increment)
        log_mod.write_message(
            "General number incremented by {} -> {}".format(user, increment)
        )
        return database.get_data()[user]


@api.route(
    "/register",
    doc={
        "description": "GET: returns registred users. PUT: register new user"
    },
)
class Register(Resource):
    def get(self):
        return list(database.get_data().keys())

    @api.doc(params={"user": "User name to register"})
    def put(self):
        user = parser.parse_args().get("user")
        database.add_data(user)
        log_mod.write_message("User {} registred successfully".format(user))
        return 0
