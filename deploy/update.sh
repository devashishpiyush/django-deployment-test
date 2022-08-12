#!/usr/bin/env bash

echo "Starting Update"

# Config to show error
set -e

# Project file configurations
PROJECT_NAME='django_api'
PROJECT_BASE_PATH='/usr/local/workspace/apps'
VIRTUALENV_BASE_PATH='/usr/local/workspace/env'

# Change to project dir
cd $PROJECT_BASE_PATH/$PROJECT_NAME

# Pull the update from github
git pull

$VIRTUALENV_BASE_PATH/$PROJECT_NAME/bin/python manage.py makemigrations
$VIRTUALENV_BASE_PATH/$PROJECT_NAME/bin/python manage.py migrate
$VIRTUALENV_BASE_PATH/$PROJECT_NAME/bin/python manage.py collectstatic --noinput

supervisorctl restart $PROJECT_NAME

echo "Update completed"