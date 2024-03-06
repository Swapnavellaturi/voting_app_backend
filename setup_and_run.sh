#!/bin/bash

# Ensure script is executed from the root of the cloned repository
if [ ! -f "voting_backend.py" ]; then
    echo "voting_backend.py not found! Please run this script from the root of the Flask application directory."
    exit 1
fi

# Update and install Python 3 and pip
sudo apt update
sudo apt install -y python3 python3-pip

# Install virtualenv
pip3 install virtualenv

# Create and activate a virtual environment
virtualenv -p python3 venv
source venv/bin/activate

# Install Flask, psycopg2-binary, and Flask-CORS within the virtual environment
pip install Flask psycopg2-binary flask-cors

# Run the Flask application
export FLASK_APP=voting_backend.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
