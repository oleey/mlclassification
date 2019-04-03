


from flask import Flask

def create_app(config_class):

    app = Flask(__name__)
    app.config.from_object(config_class)

    from .api import api_bp

    app.register_blueprint(api_bp)

    return app