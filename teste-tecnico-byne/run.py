import argparse
import os
from dotenv import load_dotenv
from app import Application
from utils import LoggingModifier, RequestsManager
from apis import blueprint as api

load_dotenv(".env")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process test and debug.")
    parser.add_argument(
        "-t", "--testing", action="store_true", help="enable testing"
    )
    parser.add_argument(
        "-d", "--debugging", action="store_true", help="enable debug"
    )
    parser.add_argument(
        "-ho", "--host", default="127.0.0.1", help="define host"
    )
    parser.add_argument("-p", "--port", default="5000", help="define port")
    args = parser.parse_args()
    print(args)
    app = Application(
        host=args.host,
        port=args.port,
        testing=args.testing,
        debuging=args.debugging,
        secret_key=os.getenv("SECRET_KEY"),
    )
    app.register_blueprint(api, prefix="/api")
    log_mod = LoggingModifier(file_name="logs.log")
    req_man = RequestsManager(
        base_url="http://{}:{}/".format(args.host, args.port)
    )
    app.setup_routes(log_mod, req_man)
    app.run()
