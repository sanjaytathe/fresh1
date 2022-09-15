class Config(object):
    SECRET_KEY = 'sanjaytathe'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/wscubetech'
    SQLALCHEMY_TRACK_MODIFICATION = False


class Development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


app_config = {'development': Development}