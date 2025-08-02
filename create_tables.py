from app import create_app
from app.models import db, User

# Create an application context to initialize Flask-SQLAlchemy
app = create_app()

with app.app_context():
    print("Creating all database tables...")
    db.create_all()
    print("Tables created successfully!")
    
    # Check for and create an admin user
    if not User.query.filter_by(username='admin').first():
        print("Creating admin user...")
        admin_user = User(username='admin', role='admin')
        admin_user.set_password('adminpassword')
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")

