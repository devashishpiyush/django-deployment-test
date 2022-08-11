# Project name or dir name
$PROJECT_NAME = 'django_test_api'
$PROJECT_GIT_URL = 'https://github.com/devashishpiyush/django-deployment-test.git'

# Project Base Path
$PROJECT_BASE_PATH = '/usr/local/workspace/apps'
# Virtual Environment Base Path
$VIRTUALENV_BASE_PATH = 'usr/local/workspace/env'

# Check and install updates.
sudo apt-get update
sudo apt-get upgrade

# Install dependencies / software for the project
# Python, SQLite, pip, supervisor, nginx and git
sudo apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Make dir for the project
sudo mkdir -p $PROJECT_BASE_PATH

# Clone the project from github
sudo git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/$PROJECT_NAME

# Create virtual environment
sudo mkdir -p $VIRTUALENV_BASE_PATH
sudo python3 -m venv $VIRTUALENV_BASE_PATH/$PROJECT_NAME

# Install requirement for the project from requirements.txt
sudo $VIRTUALENV_BASE_PATH/$PROJECT_NAME/bin/pip install -r $PROJECT_BASE_PATH/$PROJECT_NAME/requirements.txt

# Copy configuration files
# Setup supervisor to run our uwsgi process
sudo cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/supervisor.conf /etc/supervisor/conf.d/$PROJECT_NAME.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart $PROJECT_NAME

# Setup ngnix to make our application accessible
sudo cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/nginx.conf /etc/nginx/sites-available/$PROJECT_NAME.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/$PROJECT_NAME.conf /etc/nginx/sites-enabled/$PROJECT_NAME.conf
sudo systemctl restart nginx.service
