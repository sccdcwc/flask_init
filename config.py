import os
import logging.handlers
basedir = os.path.abspath(os.path.dirname(__file__))


# 日志配置
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    'app.log', maxBytes=40 * 1024 * 1024, backupCount=5, encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(logging_format)
logger.addHandler(handler)

Flag="default"

class config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

class LocalConfig(config):
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://test:123456@localhost:3306/test"
    Debug=True

class DevConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ""

class TestConfig(config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ""

class ProdConfig(config):
    SQLALCHEMY_DATABASE_URI =""


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': LocalConfig
}