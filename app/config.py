from path import APP_DIR


class BaseConfig:
    """Базовая конфигурация"""
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(APP_DIR)


class DevConfig(BaseConfig):
    """Конфигурация для разработки"""
    ENV = 'development'
    DEBUG = True
    TESTING = True


class ProdConfig(BaseConfig):
    """Конфигурация product"""
    ENV = 'production'
