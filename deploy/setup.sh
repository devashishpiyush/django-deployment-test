#!/usr/bin/env bash

echo "Starting Setup"

# Config to show errors
set -e

# Project name or dir name
PROJECT_NAME='django_api'
PROJECT_GIT_URL='https://github.com/devashishpiyush/django-deployment-test.git'

# Project Base Path
PROJECT_BASE_PATH='/usr/local/workspace/apps'
# Virtual Environment Base Path
VIRTUALENV_BASE_PATH='usr/local/workspace/env'

# Check and install updates.
apt-get update
apt-get upgrade

# Install dependencies / software for the project
# Python, SQLite, pip, supervisor, nginx and git
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Make dir for the project
mkdir -p $PROJECT_BASE_PATH

# Clone the project from github
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/$PROJECT_NAME

# Create virtual environment
mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/$PROJECT_NAME

# Install requirement for the project from requirements.txt
$VIRTUALENV_BASE_PATH/$PROJECT_NAME/bin/pip install -r $PROJECT_BASE_PATH/$PROJECT_NAME/requirements.txt

# Copy configuration files
# Setup supervisor to run our uwsgi process
cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/supervisor.conf /etc/supervisor/conf.d/$PROJECT_NAME.conf
supervisorctl reread
supervisorctl update
supervisorctl restart $PROJECT_NAME

# Setup ngnix to make our application accessible
cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/nginx.conf /etc/nginx/sites-available/$PROJECT_NAME.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/$PROJECT_NAME.conf /etc/nginx/sites-enabled/$PROJECT_NAME.conf
systemctl restart nginx.service

echo "Setup completed"