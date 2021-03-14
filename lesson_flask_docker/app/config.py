import os


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS',
                                                    default=False)


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    pass
