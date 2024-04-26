from flask import Flask

def app():
    app = Flask(__name__)
    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')
    return app