import os
from flask import Flask
from .models import db, User  # Import db and User model
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        # Correctly format the database URL for SQLAlchemy
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions with the app
    bcrypt.init_app(app)
    csrf.init_app(app)
    db.init_app(app)  # Initialize Flask-SQLAlchemy with the app

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
