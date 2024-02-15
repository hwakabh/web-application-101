from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


webdb = SQLAlchemy()


def init_db(app):
    webdb.init_app(app)
    Migrate(app, webdb)
