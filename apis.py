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
parser.add_argument('user', type=str, help='Informe user')
parser.add_argument('increment', type=int, help='Informe incremento')


@api.route('/impar', doc={"description": "Gera numero impar aletorio entre 0 e 99"})
class Impar(Resource):
    def get(self):
        impar = 0
        while (impar % 2) == 0:
            impar = randint(0, 99)

        logging.warning("Numero impar requisitado -> %s",impar)
        return impar

@api.route('/par', doc={"description": "Gera numero par aletorio entre 0 e 99"})
class Par(Resource):
    def get(self):
        par = 1
        while (par % 2) != 0:
            par = randint(0, 99)

        logging.warning("Numero par requisitado ->  %s",par)
        return par

@api.route('/getvalorgeral', doc={"description": "Retorna valor geral de todos os users"})
class GetValorGeral(Resource):
    def get(self):
        try:
            dados=database.getData()
            logging.warning("Numero geral requisitado -> %s",dados)
            return dados
        except:
            return None

@api.route('/putvalorgeral', doc={"description": "Incrementa valor de determinado user"})
class PutValorGeral(Resource):
    @api.doc(params={'user': 'Nome do usuario para registro', 'increment': 'Valor a ser incrementado'})
    def put(self):
        user=parser.parse_args().get('user')
        increment=parser.parse_args().get('increment')
        database.updateData(user, increment)
        logging.warning("Numero geral incrementado por %s -> %s",user,increment)
        return database.getData()[user]
        
@api.route('/registro', doc={"description": "Caso GET, retorna os users cadastrados e caso PUT registra um user novo"})
class Registra(Resource):
    def get(self):
        return list(database.getData().keys())

    @api.doc(params={'user': 'Nome do usuário para registro'})
    def put(self):
        user=parser.parse_args().get('user')
        database.addData(user)
        logging.warning("Usuário %s registrado",user)
        return 0
