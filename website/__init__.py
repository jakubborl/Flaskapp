from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "database.db"
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ghghhghhg"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    migrate.init_app(app, db)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

 

    from .models import User, Note

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():  # Zajištění kontextu aplikace
            db.create_all()
        print("Created Database!")
