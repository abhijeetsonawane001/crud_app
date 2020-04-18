# Python official image
FROM python:3.7.4

# Copy requirments file
COPY requirments.txt requirments.txt

# Run pip install and ignore 
RUN pip install --no-cache-dir -r requirments.txt

# Copy current app to image it contains flask app package
COPY . /usr/src/app

# Set working directory to /usr/src/app

WORKDIR /usr/src/app

# Set flask_app and flask_debug environment
ENV FLASK_APP=run_app.py
ENV FLASK_DEBUG=0
ENV FLASK_ENV=production
ENV APP_CONFIG=app.config.ProductionConfig

# Expose the flask default port 5000
EXPOSE 5000

# Start gunicorn server
CMD [ "gunicorn", "--access-logfile=-", "-b", "0.0.0.0:5000", "run_app:app" ]