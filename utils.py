from datetime import datetime
import requests

def writeLog(messege):
        f = open("log.txt", "a")
        f.write('{0} -> {1}\n'.format(datetime.now(),messege))
        f.close()


def getKeys():
    return requests.get('http://127.0.0.1:5000/api/registro').json()

def registraUser(user):
    return requests.put('http://127.0.0.1:5000/api/registro', data = {'user':user}).text
