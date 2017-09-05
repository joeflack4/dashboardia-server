"""Config."""
from os import path, environ

CONFIG_DIR = path.dirname(__file__)
TEMPLATE_DIR = path.join(CONFIG_DIR, '../../client/routes')


class Config(object):
    """Base config class."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']


class ProductionConfig(Config):
    """Production config."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development config."""
    DEVELOPMENT = True
    DEBUG = True


class StagingConfig(DevelopmentConfig):
    """Staging config."""
    pass


class TestConfig(DevelopmentConfig):
    """Test config."""
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'test': TestConfig,
    'default': ProductionConfig
}
