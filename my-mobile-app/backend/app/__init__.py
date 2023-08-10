from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configure app settings (e.g., app.config)
    app.config["SECRET_KEY"] = "your-secret-key"

    # Import and register blueprints
    from app.routes.auth_routes import auth_routes
    app.register_blueprint(auth_routes, url_prefix="/auth")

    # More blueprints and configurations can be added here

    return app
