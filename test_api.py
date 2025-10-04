#!/usr/bin/env python3
"""
Test script for OwlNotes AI API
Run this to test the FastAPI endpoints
"""

import requests
import json
import time
import subprocess
import sys
import os

def test_api():
    """Test the OwlNotes AI API endpoints"""
    
    # Test data
    test_transcript = """
    Welcome to today's lecture on Data Structures and Algorithms. 
    We'll be covering binary trees, hash tables, and sorting algorithms.
    
    Binary trees are hierarchical data structures where each node has at most two children.
    They're commonly used for searching and sorting operations.
    
    Hash tables provide average O(1) lookup time by using a hash function to map keys to array indices.
    This makes them extremely efficient for many applications.
    
    Sorting algorithms like quicksort and mergesort have different time complexities.
    Quicksort has average O(n log n) but worst case O(n²).
    Mergesort guarantees O(n log n) in all cases.
    """
    
    test_slides = [
        "Introduction to Data Structures",
        "Binary Trees Overview", 
        "Hash Tables and Hashing",
        "Sorting Algorithms Comparison",
        "Time Complexity Analysis"
    ]
    
    print("🚀 Testing OwlNotes AI API")
    print("=" * 50)
    
    # Test health endpoint
    print("\n1. Testing Health Endpoint...")
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Health check passed: {health_data}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API. Make sure the server is running.")
        print("   Run: cd poc/backend && source .venv/bin/activate && uvicorn app.main:app --reload")
        return False
    
    # Test Cornell notes endpoint
    print("\n2. Testing Cornell Notes Endpoint...")
    try:
        payload = {
            "transcript": test_transcript,
            "slides": test_slides
        }
        
        response = requests.post("http://localhost:8000/notes/cornell", json=payload)
        
        if response.status_code == 200:
            notes_data = response.json()
            print("✅ Cornell notes generated successfully!")
            print(f"   📝 Cues: {len(notes_data['cues'])} items")
            print(f"   📋 Notes: {len(notes_data['notes'])} items")
            print(f"   🔑 Key concepts: {notes_data['key_concepts'][:3]}")
            print(f"   ❓ Questions: {len(notes_data['questions'])} generated")
            print(f"   📚 Citations: {len(notes_data['citations'])} references")
            
            # Show sample output
            print("\n📖 Sample Cornell Note Structure:")
            print(f"   Summary: {notes_data['summary'][:100]}...")
            if notes_data['cues']:
                print(f"   Sample Cue: {notes_data['cues'][0]}")
            if notes_data['notes']:
                print(f"   Sample Note: {notes_data['notes'][0][:80]}...")
                
        else:
            print(f"❌ Cornell notes generation failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Cornell notes: {e}")
        return False
    
    print("\n🎉 All tests passed! OwlNotes AI API is working correctly.")
    return True

if __name__ == "__main__":
    print("OwlNotes AI API Test Suite")
    print("Make sure the API server is running on http://localhost:8000")
    print("Start the server with: cd poc/backend && source .venv/bin/activate && uvicorn app.main:app --reload")
    print()
    
    success = test_api()
    sys.exit(0 if success else 1)
