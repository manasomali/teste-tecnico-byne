import json
from typing import Dict
import logging
import requests

class DataModifier:
    def __init__(self, filename):
        self.filename: str = filename

    def get_data(self) -> Dict[str, int]:
        with open(self.filename, "r") as read_file:
            data: Dict[str, int] = json.load(read_file)

        return data

    def add_data(self, user: str) -> None:
        data: Dict[str, int] = self.get_data()
        data[user] = 0
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)

    def update_data(self, user: str, increment: int) -> None:
        data: Dict[str, int] = self.get_data()
        data[user] = data[user] + increment
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)


class LoggingModifier:
    def __init__(self, file_name, disable_werkzeug=True) -> None:
        logging.basicConfig(
            format="%(asctime)s -> %(message)s",
            filename=file_name,
            level=logging.WARNING,
        )
        logging.getLogger("werkzeug").disabled = disable_werkzeug

    def write_message(self, message) -> None:
        logging.warning(message)


class RequestsManager:
    def __init__(self, base_url="http://localhost:8000/") -> None:
        self.base_url = base_url

    def get_users_keys(self):
        return requests.get(self.base_url + "/api/register").json()

    def register_user(self, user: str):
        return requests.put(
            self.base_url + "/api/register", data={"user": user}
        ).text
