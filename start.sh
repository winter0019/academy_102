#!/usr/bin/env bash
# This script is for starting the Gunicorn server
# It's important to use the app:create_app() syntax because your app is created with a factory function.
# The number of workers (-w) can be adjusted based on your needs.
gunicorn --bind 0.0.0.0:10000 --workers 4 'app:create_app()'
