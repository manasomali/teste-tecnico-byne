# -*- coding: utf-8 -*- 
from flask import request, Blueprint
from flask_restx import Api, Resource, fields
from random import randint
from core.utils import writeLog

blueprint = Blueprint('api', __name__)
api = Api(blueprint)
DATABASE = {}
@api.route('/impar', doc={"description": "Gera numero impar aletorio entre 0 e 99"})
class Impar(Resource):
    def get(self):
        try:
            impar = 0
            while (impar % 2) == 0:
                impar = randint(0, 99)
            
            writeLog("Numero impar requisitado {0}".format(impar))
            return {'numero':impar}
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)

@api.route('/par', doc={"description": "Gera numero par aletorio entre 0 e 99"})
class Par(Resource):
    def get(self):
        try:
            par = 1
            while (par % 2) != 0:
                par = randint(0, 99)
            
            writeLog("Numero par requisitado {0}".format(par))
            return {'numero':par}
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)

@api.route('/valorgeral', doc={"description": "Caso GET, retorna valor geral de todos os users e caso PUT incrementa valor de determinado user"})
class ValorGeral(Resource):
    def get(self):
        try:
            writeLog("Numero geral requisitado -> {0}".format(DATABASE))
            return DATABASE
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)
    
    @api.doc(params={'user': 'Nome do usuário para registro', 'increment': 'Valor a ser incrementado'})
    def put(self):
        DATABASE[request.form['user']]=DATABASE[request.form['user']]+int(request.form['increment'])
        writeLog("Numero geral incrementado por {0} -> {1}".format(request.form['user'],request.form['increment']))
        return DATABASE[request.form['user']]
        

@api.route('/registro', doc={"description": "Caso GET, retorna os users cadastrados e caso PUT registra um user novo"})
class Registra(Resource):
    def get(self):
        try:
            return list(DATABASE.keys())
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)
    @api.doc(params={'user': 'Nome do usuário para registro'})
    def put(self):
        try:
            DATABASE[request.form['user']]=0
            writeLog("Usuário {0} registrado".format(request.form['user']))
            return DATABASE[request.form['user']]
        except Exception as ex:
            return "Ocorreu excecao do tipo {0}. Argumentos: {1!r}".format(type(ex).__name__, ex.args)