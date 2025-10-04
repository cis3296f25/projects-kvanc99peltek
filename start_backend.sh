#!/bin/bash

# OwlNotes AI Backend Startup Script
echo "🦉 Starting OwlNotes AI Backend..."

# Navigate to backend directory
cd poc/backend

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install fastapi uvicorn pydantic

# Start the server
echo "🚀 Starting FastAPI server..."
echo "   API will be available at: http://localhost:8000"
echo "   Interactive docs at: http://localhost:8000/docs"
echo "   Press Ctrl+C to stop the server"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
