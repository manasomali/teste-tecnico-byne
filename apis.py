# -*- coding: utf-8 -*- 
import logging
from random import randint
from flask import Blueprint
from flask_restx import Api, Resource, reqparse
from utils import DataModifier

logging.basicConfig(format='%(asctime)s -> %(message)s', filename='logs.log', level=logging.WARNING)

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

database = DataModifier('data.json')

parser = reqparse.RequestParser()
parser.add_argument('user', type=str, help='User needed')
parser.add_argument('increment', type=int, help='Increment needed')


@api.route('/odd', doc={"description": "Generate a randon odd number betewen 0 and 99"})
class Odd(Resource):
    def get(self):
        odd = 0
        while (odd % 2) == 0:
            odd = randint(0, 99)

        logging.warning("Odd number requisited -> %s", odd)
        return odd

@api.route('/even', doc={"description": "Generate a randon even number betewen 0 and 99"})
class Even(Resource):
    def get(self):
        even = 1
        while (even % 2) != 0:
            even = randint(0, 99)

        logging.warning("Even number requisited ->  %s", even)
        return even

@api.route('/getgeneralvalue', doc={"description": "Returns the general value of all users"})
class GetGeneralValue(Resource):
    def get(self):
        try:
            dados=database.getData()
            logging.warning("Request general numbers -> %s",dados)
            return dados
        except:
            return None

@api.route('/putgeneralvalue', doc={"description": "Increment general value of determined user"})
class PutGeneralValue(Resource):
    @api.doc(params={'user': 'User name to register', 'increment': 'Value to be incremented'})
    def put(self):
        user=parser.parse_args().get('user')
        increment=parser.parse_args().get('increment')
        database.updateData(user, increment)
        logging.warning("General number incremented by %s -> %s",user,increment)
        return database.getData()[user]
        
@api.route('/register', doc={"description": "Case GET, returns registred users and case PUT register a new user"})
class Registra(Resource):
    def get(self):
        return list(database.getData().keys())

    @api.doc(params={'user': 'User name to register'})
    def put(self):
        user=parser.parse_args().get('user')
        database.addData(user)
        logging.warning("User %s registred successfully",user)
        return 0
