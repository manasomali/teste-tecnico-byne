import logging
import requests


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
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_users(self):
        return list(
            (requests.get(self.base_url + "/getusers").text)
            .strip("][")
            .replace("'", "")
            .split(", ")
        )

    def register_user(self, user: str):
        return requests.put(self.base_url + "/registeruser/" + user).text
