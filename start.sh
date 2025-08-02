#!/usr/bin/env bash
# This script will set up the database and start the server.

# 1. Create the 'instance' directory for the database.
mkdir -p instance

# 2. Use a python one-liner to initialize the database and create the admin user.
# This ensures the database is ready for the app to use.
python -c "
import os
import sqlite3
from flask_bcrypt import generate_password_hash

# Set up paths
instance_path = './instance'
db_path = os.path.join(instance_path, 'alfurqa_academy.db')
schema_path = './app/schema.sql'

# Connect to the new, empty database
db = sqlite3.connect(db_path)
cursor = db.cursor()

# Run the schema script to create all tables
with open(schema_path, 'r') as f:
    cursor.executescript(f.read())
db.commit()

# Create the admin user with a correctly hashed password
admin_password_hash = generate_password_hash('adminpassword').decode('utf-8')
cursor.execute(
    'INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
    ('admin', admin_password_hash, 'admin')
)
db.commit()
db.close()
"

# 3. Start the Gunicorn server.
gunicorn --bind 0.0.0.0:10000 --workers 4 'app:create_app()'
