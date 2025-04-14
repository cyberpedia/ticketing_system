from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    app.config.from_object('config')
    app.config['DEBUG'] = True

    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
