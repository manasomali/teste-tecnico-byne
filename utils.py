from datetime import datetime
import requests
URLBASE="https://teste-tecnico-byne.herokuapp.com"

def writeLog(messege):
        f = open("log.txt", "a")
        f.write('{0} -> {1}\n'.format(datetime.now(),messege))
        f.close()


def getKeys():
    return requests.get(URLBASE+'/api/registro').json()

def registraUser(user):
    return requests.put(URLBASE+'/api/registro', data = {'user':user}).text
