# -*- coding: utf-8 -*- 
from flask import Flask, render_template, redirect, request, session
from core.utils import writeLog, getKeys, registraUser
from apis import blueprint as api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.config['RESTX_VALIDATE'] = True
app.secret_key = '\xd91t\xfd_\xbb\xfc\x0b\xc2\xea\xcclg\x9f\xadu\xd1\xf6\xd9\xc5\x85f5\x17'

@app.route('/', methods=["GET", "POST"])
def index():
    if not session.get("name"):
        return redirect("/login")

    return render_template('home.html', nome = session.get("name"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("name") in getKeys():
            session["name"] = request.form.get("name")
            writeLog("Usuário {0} logado".format(session["name"]))
            return redirect("/")
        else:
            return redirect("/registro")
    return render_template('login.html')

@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        if request.form.get("name") in getKeys():
            return redirect("/login")
        else:
            session["name"] = request.form.get("name")
            registraUser(request.form.get("name"))
            writeLog("Usuário {0} registrado".format(session["name"]))
            return redirect("/")
    return render_template('registro.html')

@app.route('/logout', methods=["GET", "POST"])
def logout():
    writeLog("usuário {0} logout".format(session["name"]))
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)