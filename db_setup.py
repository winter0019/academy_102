import os
from app import create_app
from app.models import db, User

# Create an application context
app = create_app()
with app.app_context():
    # Correctly format the database URL for SQLAlchemy
    db_url = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    # Create all database tables
    print("Creating all database tables...")
    db.create_all()
    print("Tables created successfully!")

    # Check for and create an admin user if it doesn't exist
    if not User.query.filter_by(username='admin').first():
        print("Creating admin user...")
        admin_user = User(username='admin', role='admin')
        admin_user.set_password('adminpassword')
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
