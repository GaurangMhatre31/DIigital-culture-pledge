from app import create_app, initialize_database_with_participants

# Create the Flask app
app = create_app()

# Initialize database with participants
with app.app_context():
    initialize_database_with_participants(app)

# For Gunicorn
application = app
