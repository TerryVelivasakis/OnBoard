from flask import Flask
from flask_cors import CORS
from config import Config
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Register blueprints for routes
    register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
