from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

# Import Blueprints
from routes.auth import bp as auth_bp
from routes.rooms import bp as rooms_bp
from routes.reservations import bp as reservations_bp
from routes.schedules import bp as schedules_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(schedules_bp)
    
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        # We need to import the modules where the columns are defined
        from models import user, room, schedule, reservation, unavailable
        db.create_all()
        print("Database tables created.")
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
