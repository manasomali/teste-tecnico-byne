import json
import requests
from typing import Dict


class DataModifier:
    def __init__(self, filename):
        self.filename: str = filename

    def getData(self) -> Dict[str, int]:
        with open(self.filename, "r") as read_file:
            data: Dict[str, int] = json.load(read_file)

        return data

    def addData(self, user: str) -> None:
        data: Dict[str, int] = self.getData()
        data[user] = 0
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)

    def updateData(self, user: str, increment: int) -> None:
        data: Dict[str, int] = self.getData()
        data[user] = data[user] + increment
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)


def getKeys(app):
    return requests.get(app.config["BASE_URL"] + "/api/register").json()


def registerUser(app, user: str):
    return requests.put(
        app.config["BASE_URL"] + "/api/register", data={"user": user}
    ).text
