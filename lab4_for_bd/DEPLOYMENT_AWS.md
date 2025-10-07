# AWS Deployment Instructions

## Step 1: Install Python on AWS EC2

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip python3-venv -y

# Verify installation
python3 --version
pip3 --version
```

## Step 2: Navigate to your project

```bash
cd ~/database-lab4/lab4_for_bd
```

## Step 3: Create virtual environment (recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

## Step 4: Install system dependencies (IMPORTANT!)

```bash
# Install MySQL development libraries (required for mysql-connector)
sudo apt install -y pkg-config python3-dev default-libmysqlclient-dev build-essential
```

## Step 5: Install Python dependencies

```bash
# Install required packages one by one
pip3 install Flask==3.0.0
pip3 install flask-sqlalchemy==3.1.1
pip3 install flasgger==0.9.7.1
pip3 install sqlalchemy==2.0.23
pip3 install PyMySQL==1.1.0
pip3 install mysql-connector-python
pip3 install waitress
```

Or use this single command:

```bash
pip3 install Flask==3.0.0 flask-sqlalchemy==3.1.1 flasgger==0.9.7.1 sqlalchemy==2.0.23 PyMySQL==1.1.0 mysql-connector-python waitress
```

## Step 6: Run the application

```bash
# Run with Python 3
python3 app.py
```

The app should start and connect to your RDS database!

## Step 7: Run in background (optional)

```bash
# Install screen or tmux for background execution
sudo apt install screen -y

# Start screen session
screen -S flask_app

# Run app
python3 app.py

# Detach from screen: Press Ctrl+A, then D
# Reattach: screen -r flask_app
```

## Step 8: Configure firewall (if needed)

```bash
# Allow Flask default port (5000)
sudo ufw allow 5000
```

## Step 9: Access Swagger UI

Open in browser:
```
http://YOUR_EC2_PUBLIC_IP:5000/apidocs/
```

Or if you're using AWS security groups, make sure port 5000 is open in your EC2 instance security group.

## Alternative: Run with Waitress (Production Server)

```bash
# Install waitress
pip3 install waitress

# Create run_prod.py
cat > run_prod.py << 'EOF'
from waitress import serve
from app import create_app

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
EOF

# Run with waitress
python3 run_prod.py
```

## Troubleshooting

### If you get "ModuleNotFoundError"
Make sure all dependencies are installed:
```bash
pip3 install -r app/requirements.txt
```

### If you get database connection errors
Check your database configuration in `app/config.py`

### To check if app is running
```bash
ps aux | grep python
netstat -tulpn | grep 5000
```

### To stop the app
```bash
# Find process ID
ps aux | grep python

# Kill process
kill -9 <PID>
```

## Configuration for Production

1. Change Flask debug mode to False
2. Use environment variables for sensitive data
3. Configure proper logging
4. Use a reverse proxy (nginx) for production
5. Set up SSL/HTTPS

## Quick Start Commands Summary

```bash
# Install everything
sudo apt update
sudo apt install python3 python3-pip -y
cd ~/database-lab4/lab4_for_bd
pip3 install -r app/requirements.txt

# Run app
python3 app.py
```

Your Swagger documentation will be available at:
**http://YOUR_AWS_IP:5000/apidocs/**
