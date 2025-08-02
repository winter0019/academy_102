#!/usr/bin/env bash
# Create the instance directory if it doesn't exist
mkdir -p instance

# Run the database initialization script
python init_db_and_user.py

# Start the Gunicorn server
gunicorn --bind 0.0.0.0:10000 --workers 4 'app:create_app()'
