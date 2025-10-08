#!/bin/bash
# Setup script for EC2 server - Continuous Deployment
# Run this ONCE on your EC2 server: bash setup_ec2_cd.sh

set -e  # Exit on error

echo "🚀 Starting EC2 Continuous Deployment Setup..."

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables
REPO_URL="https://github.com/stanko07/database-lab4.git"
PROJECT_DIR="/home/admin/database-lab4/lab4_for_bd"
VENV_DIR="$PROJECT_DIR/venv"

# Step 1: Check if repository exists
echo -e "${YELLOW}Step 1: Checking repository...${NC}"
if [ -d "/home/admin/database-lab4" ]; then
    echo -e "${GREEN}✅ Repository exists${NC}"
    cd /home/admin/database-lab4
    git pull origin main
else
    echo -e "${YELLOW}📦 Cloning repository...${NC}"
    cd /home/admin
    git clone $REPO_URL
    echo -e "${GREEN}✅ Repository cloned${NC}"
fi

# Step 2: Configure Git
echo -e "${YELLOW}Step 2: Configuring Git...${NC}"
cd /home/admin/database-lab4/lab4_for_bd
git config pull.rebase false
git remote set-url origin $REPO_URL
echo -e "${GREEN}✅ Git configured${NC}"

# Step 3: Setup Python Virtual Environment
echo -e "${YELLOW}Step 3: Setting up Python virtual environment...${NC}"
cd $PROJECT_DIR

# Remove old venv if exists
if [ -d "$VENV_DIR" ]; then
    echo "Removing old virtual environment..."
    rm -rf "$VENV_DIR"
fi

# Create new venv
python3 -m venv venv
source venv/bin/activate

echo -e "${GREEN}✅ Virtual environment created${NC}"

# Step 4: Install dependencies
echo -e "${YELLOW}Step 4: Installing Python dependencies...${NC}"
pip install --upgrade pip
pip install -r app/requirements.txt

# Verify critical packages
if pip list | grep -q "waitress"; then
    echo -e "${GREEN}✅ waitress installed${NC}"
else
    echo -e "${RED}❌ waitress NOT installed${NC}"
    exit 1
fi

if pip list | grep -q "Flask"; then
    echo -e "${GREEN}✅ Flask installed${NC}"
else
    echo -e "${RED}❌ Flask NOT installed${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All dependencies installed${NC}"

# Step 5: Set environment variables
echo -e "${YELLOW}Step 5: Setting environment variables...${NC}"

# Add to .bashrc if not already present
if ! grep -q "export USE_MYSQL=true" ~/.bashrc; then
    echo "export USE_MYSQL=true" >> ~/.bashrc
    echo -e "${GREEN}✅ Added USE_MYSQL to .bashrc${NC}"
else
    echo -e "${GREEN}✅ USE_MYSQL already in .bashrc${NC}"
fi

export USE_MYSQL=true

# Step 6: Test application
echo -e "${YELLOW}Step 6: Testing application creation...${NC}"
cd $PROJECT_DIR
source venv/bin/activate
export USE_MYSQL=true

python -c "from app import create_app; app = create_app(); print('✅ App created successfully!')" || {
    echo -e "${RED}❌ Failed to create app${NC}"
    exit 1
}

echo -e "${GREEN}✅ Application test passed${NC}"

# Step 7: Kill old processes
echo -e "${YELLOW}Step 7: Cleaning up old processes...${NC}"
# Disable exit on error temporarily
set +e
pkill -9 -f "python run_production.py" || echo "No run_production.py processes found"
pkill -9 -f "python3 run_production.py" || echo "No python3 run_production.py processes found"
pkill -9 -f "python app.py" || echo "No app.py processes found"

# Вбиваємо процеси на порту 5000
PID_ON_PORT=$(ss -tlnp 2>/dev/null | grep ':5000' | grep -oP 'pid=\K[0-9]+' | head -1)
if [ -n "$PID_ON_PORT" ]; then
  echo "Found process $PID_ON_PORT on port 5000, killing..."
  kill -9 $PID_ON_PORT 2>/dev/null || true
fi

sleep 3
set -e
echo -e "${GREEN}✅ Old processes cleaned${NC}"

# Step 8: Start production server
echo -e "${YELLOW}Step 8: Starting production server...${NC}"
cd $PROJECT_DIR
source venv/bin/activate
export USE_MYSQL=true

nohup python run_production.py > flask.log 2>&1 &
NEW_PID=$!

echo -e "${GREEN}✅ Production server started with PID: $NEW_PID${NC}"

# Wait for server to start
sleep 5

# Step 9: Verify server is running
echo -e "${YELLOW}Step 9: Verifying server...${NC}"
if kill -0 $NEW_PID 2>/dev/null; then
    echo -e "${GREEN}✅ Server is running (PID: $NEW_PID)${NC}"
else
    echo -e "${RED}❌ Server failed to start${NC}"
    cat flask.log
    exit 1
fi

# Test endpoint
sleep 3
if curl -s http://localhost:5000/candidates > /dev/null; then
    echo -e "${GREEN}✅ API endpoint responding${NC}"
else
    echo -e "${YELLOW}⚠️  API endpoint not responding (might be normal if DB not ready)${NC}"
fi

# Final summary
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   ✅ EC2 Setup Complete!                   ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}📋 Next steps:${NC}"
echo "1. Verify GitHub Secrets are set:"
echo "   - AWS_EC2_HOST"
echo "   - AWS_PRIVATE_KEY"
echo ""
echo "2. Push to main branch to test CD:"
echo "   git push origin main"
echo ""
echo "3. Monitor deployment:"
echo "   https://github.com/stanko07/database-lab4/actions"
echo ""
echo -e "${YELLOW}📊 Useful commands:${NC}"
echo "   ps aux | grep python          # Check running processes"
echo "   tail -f $PROJECT_DIR/flask.log    # View logs"
echo "   curl http://localhost:5000/candidates  # Test API"
echo ""
echo -e "${GREEN}🎉 Happy deploying!${NC}"
