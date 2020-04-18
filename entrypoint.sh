#!/usr/bin/env bash
if [ "$FLASK_ENV" == "development" ]  && [ -f dev-requirments.txt ]; then
    echo "installing dev dependencies" 
    pip install --no-cache-dir -r dev-requirments.txt
fi
exec "$@"