# -*- coding: utf-8 -*-
import logging
import requests
from flask import Flask, render_template, redirect, request, session
from apis import blueprint as api

app = Flask(__name__)
app.config['BASE_URL']='https://teste-tecnico-byne.herokuapp.com'
#app.config['BASE_URL']='http://127.0.0.1:5000'
app.config['TESTING'] = False
app.config['DEBUG'] = False
app.config['SECRET_KEY']='\xd91t\xfd_\xbb\xfc\x0b\xc2\xea\xcclg\x9f\xadu\xd1\xf6\xd9\xc5\x85f5\x17'

logging.basicConfig(format='%(asctime)s -> %(message)s', filename='logs.log', level=logging.WARNING)
logging.getLogger('werkzeug').disabled = True

app.register_blueprint(api, url_prefix='/api')

@app.route('/', methods=["GET", "POST"])
def index():
    if not session.get("name"):
        return redirect("/login")

    return render_template('home.html', nome=session.get("name"), base_url=app.config['BASE_URL'])

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("name") in getKeys():
            session["name"] = request.form.get("name")
            logging.warning("Usuario %s logado", session["name"])
            return redirect("/")

        return redirect("/registro")
    return render_template('login.html')

@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        if request.form.get("name") in getKeys():
            return redirect("/login")
    
        session["name"] = request.form.get("name")
        registraUser(request.form.get("name"))
        logging.warning("Usuario %s registrado", session["name"])
        return redirect("/")
    return render_template('registro.html')

@app.route('/logout', methods=["GET", "POST"])
def logout():
    logging.warning("Usuario %s logout", session["name"])
    session.clear()
    return redirect("/")

def getKeys():
    return requests.get(app.config['BASE_URL']+'/api/registro').json()

def registraUser(user: str):
    return requests.put(app.config['BASE_URL']+'/api/registro', data = {'user':user}).text

if __name__ == '__main__':
    app.run()
