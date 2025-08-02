    #!/usr/bin/env bash
    gunicorn --bind 0.0.0.0:10000 --workers 4 'app:create_app()'
    
