# -*- coding: utf-8 -*- 
from flask import Blueprint
from flask_restx import Api, Resource, reqparse
from random import randint
import logging
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
        try:
            impar = 0
            while (impar % 2) == 0:
                impar = randint(0, 99)
            
            logging.warning("Numero impar requisitado -> {0}".format(impar))
            return impar
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)

@api.route('/par', doc={"description": "Gera numero par aletorio entre 0 e 99"})
class Par(Resource):
    def get(self):
        try:
            par = 1
            while (par % 2) != 0:
                par = randint(0, 99)
            
            logging.warning("Numero par requisitado ->  {0}".format(par))
            return par
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)

@api.route('/getvalorgeral', doc={"description": "Retorna valor geral de todos os users"})
class GetValorGeral(Resource):
    def get(self):
        try:
            dados=database.getData()
            logging.warning("Numero geral requisitado -> {0}".format(dados))
            return dados
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)

@api.route('/putvalorgeral', doc={"description": "Incrementa valor de determinado user"})
class PutValorGeral(Resource):
    @api.doc(params={'user': 'Nome do usuario para registro', 'increment': 'Valor a ser incrementado'})
    def put(self):
        user=parser.parse_args().get('user')
        increment=parser.parse_args().get('increment')
        database.updateData(user, increment)
        logging.warning("Numero geral incrementado por {0} -> {1}".format(user,increment))
        return database.getData()[user]
        
@api.route('/registro', doc={"description": "Caso GET, retorna os users cadastrados e caso PUT registra um user novo"})
class Registra(Resource):
    def get(self):
        try:
            return list(database.getData().keys())
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)
    @api.doc(params={'user': 'Nome do usuário para registro'})
    def put(self):
        try:
            user=parser.parse_args().get('user')
            database.addData(user)
            logging.warning("Usuário {0} registrado".format(user))
            return 0
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)