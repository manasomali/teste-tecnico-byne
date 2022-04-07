from app import Application
from utils import LoggingModifier, RequestsManager
from apis import blueprint as api

if __name__ == "__main__":
    # app = Application(base_url = "https://teste-tecnico-byne.herokuapp.com", testing = False, debuging = False)
    app = Application(testing=True, debuging=True)
    app.register_blueprint(api, prefix="/api")
    log_mod = LoggingModifier(file_name="logs.log")
    # req_man = RequestsManager(base_url = "https://teste-tecnico-byne.herokuapp.com")
    req_man = RequestsManager()
    app.setup_routes(log_mod, req_man)
    app.run()