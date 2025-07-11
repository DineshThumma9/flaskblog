from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager  # Remove imported login_manager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()  # Use consistent naming
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.Users.routes import users
    from flaskblog.Posts.routes import posts
    from flaskblog.Main.routes import main
    from  flaskblog.errors.handlers import errors

    app.register_blueprint(errors)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()


    return app