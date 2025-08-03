#!/bin/bash

# Data Analyst Agent Startup Script

echo "Starting Data Analyst Agent..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Copy environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file with your API keys before running the app"
fi

# Create logs directory
mkdir -p logs

# Run the application
echo "Starting Flask application on http://localhost:5000"
echo "Press Ctrl+C to stop the server"
python3 app.py