import os
import sqlite3
from flask_bcrypt import generate_password_hash
from app import create_app, init_db

app = create_app()

with app.app_context():
    # Define the paths to your instance folder and database file
    instance_path = app.instance_path
    db_path = os.path.join(instance_path, 'alfurqa_academy.db')

    # Ensure the instance directory exists
    os.makedirs(instance_path, exist_ok=True)

    # Delete old database file if it exists, though Render's FS is ephemeral
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Old database deleted.")

    # Initialize the database and create all tables
    init_db()

    # Connect to the new database
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    
    # Create the admin user with a correctly hashed password using Flask-Bcrypt
    admin_password_hash = generate_password_hash('adminpassword').decode('utf-8')
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ('admin', admin_password_hash, 'admin')
    )
    
    db.commit()
    db.close()

print("Database initialized and 'admin' user created successfully!")
