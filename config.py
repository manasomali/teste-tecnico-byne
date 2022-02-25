class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\xd91t\xfd_\xbb\xfc\x0b\xc2\xea\xcclg\x9f\xadu\xd1\xf6\xd9\xc5\x85f5\x17'

class ProductionConfig(Config):
    ENV="production"
    BASE_URL="https://teste-tecnico-byne.herokuapp.com/login"
    pass

class DevelopmentConfig(Config):
    ENV="development"
    BASE_URL="http://127.0.0.1:5000"
    DEBUG = True

class TestingConfig(Config):
    ENV="testing"
    BASE_URL="http://127.0.0.1:5000"
    TESTING = True
