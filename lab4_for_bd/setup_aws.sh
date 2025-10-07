#!/bin/bash

echo "Installing Python and dependencies..."
sudo apt update
sudo apt install python3 python3-pip -y

echo "Installing Python packages..."
pip3 install Flask==3.0.0 flask-sqlalchemy==3.1.1 flasgger==0.9.7.1 sqlalchemy==2.0.23 PyMySQL==1.1.0 mysql-connector-python

echo "All dependencies installed!"
echo "To run the app, use: python3 app.py"
echo "Swagger UI will be available at: http://YOUR_EC2_IP:5000/apidocs/"
