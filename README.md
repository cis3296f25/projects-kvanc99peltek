# 🦉 OwlNotes AI

> **Temple-focused note companion** that records lectures (with consent), transcribes, and organizes notes by course and topic.
> Produces Cornell note pages, Feynman teach-back explanations, and spaced repetition flashcards with citations.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## ✨ Features

### 🎯 **Core Functionality** (Implemented)
- ✅ **Cornell Note Generation** - AI-powered structured note formatting with cues, notes, and summaries
- ✅ **Key Concept Extraction** - Automatic identification of important topics and terms
- ✅ **Study Question Generation** - AI-generated questions for active learning
- ✅ **Citation Management** - Automatic slide and source referencing
- ✅ **RESTful API** - FastAPI backend with interactive documentation

### 🚀 **Planned Features** (In Development)
- 🔄 **Record & transcribe lectures** - Audio recording with automatic transcription using Whisper AI
- 🔄 **Feynman notes** - Teach-back explanation generation
- 🔄 **Flashcards & spaced repetition** - AI-generated flashcards with intelligent review scheduling
- 🔄 **Search & citation links** - Full-text search across notes with source citations
- 🔄 **Temple-course specific organization** - Course-based note organization and management

## Conceptual Design

### Backend Architecture
- **FastAPI** - High-performance Python web framework for API endpoints
- **Whisper** - OpenAI's speech recognition model for lecture transcription
- **pgvector/FAISS** - Vector database for semantic search and note retrieval
- **PostgreSQL** - Primary database for storing notes, courses, and user data

### Frontend Architecture
- **Next.js** - React framework for building the web interface
- **Tailwind CSS** - Utility-first CSS framework for responsive design
- **PDF.js** - Client-side PDF rendering for slide display

### Data Flow
1. Audio recording → Whisper transcription → Note processing
2. Note analysis → Cornell/Feynman formatting → Database storage
3. Search queries → Vector similarity → Relevant note retrieval
4. Spaced repetition → Review scheduling → Flashcard generation

*See detailed diagrams in `/docs/diagrams/` for class diagrams, use cases, and sequence diagrams.*

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (3.12 recommended)
- pip (Python package manager)

### Option 1: One-Command Setup
```bash
# Clone and start the backend server
git clone <your-repo-url>
cd owlnotes-ai
./start_backend.sh
```

### Option 2: Manual Setup
```bash
# Navigate to backend directory
cd poc/backend

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

### 🌐 Access Points
- **API Server**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 🧪 Test the API
```bash
# Run the test suite
python3 test_api.py
```

## 📡 API Endpoints

### Health Check
- **GET** `/health` 
  - Returns: `{ "status": "ok", "timestamp": "2024-01-01T12:00:00" }`
  - Purpose: Verify API server is running

### Cornell Notes Generation
- **POST** `/notes/cornell`
  - **Input**: 
    ```json
    {
      "transcript": "Lecture content here...",
      "slides": ["Slide 1", "Slide 2", "Slide 3"]
    }
    ```
  - **Output**: Structured Cornell notes with:
    - `cues`: Short prompts for active recall
    - `notes`: Detailed explanations
    - `summary`: Concise lecture summary
    - `key_concepts`: Important terms and topics
    - `questions`: Study questions for review
    - `citations`: Slide references and sources

### Example Usage
```python
import requests

# Generate Cornell notes
response = requests.post("http://localhost:8000/notes/cornell", json={
    "transcript": "Today we'll discuss machine learning algorithms...",
    "slides": ["Introduction", "Algorithms", "Applications"]
})

notes = response.json()
print(f"Generated {len(notes['cues'])} cues and {len(notes['notes'])} notes")
```

## 🛠️ Tech Stack

### Current Implementation
- **Backend**: FastAPI, Pydantic, Uvicorn
- **Language**: Python 3.12
- **API Documentation**: Swagger UI, ReDoc
- **Testing**: pytest, requests

### Planned Integration
- **AI/ML**: OpenAI Whisper, sentence-transformers, transformers
- **Database**: PostgreSQL, pgvector, Redis
- **Frontend**: Next.js, Tailwind CSS, PDF.js
- **Deployment**: Docker, AWS/GCP

## 📁 Project Structure

```
owlnotes-ai/
├── 📄 README.md                    # This file
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
├── 🚀 start_backend.sh             # Quick start script
├── 🧪 test_api.py                  # API testing suite
├── 📁 docs/diagrams/               # Architecture diagrams
│   └── 📄 README.md
├── 📁 proposal/                    # Project proposal
│   └── 📄 README.md
├── 📁 presentation/                # Presentation materials
│   └── 📄 README.md
└── 📁 poc/backend/                 # FastAPI backend
    ├── 📁 app/
    │   └── 🐍 main.py              # Main application
    └── 📄 requirements.txt         # Dependencies
```

## 🎯 Current Status

### ✅ Completed
- [x] Project structure and documentation
- [x] FastAPI backend with health endpoint
- [x] Cornell notes generation API
- [x] Key concept extraction
- [x] Study question generation
- [x] Citation management
- [x] Interactive API documentation
- [x] Comprehensive testing suite
- [x] MIT License and proper gitignore

### 🔄 In Progress
- [ ] Frontend Next.js application
- [ ] Whisper AI integration
- [ ] Database implementation
- [ ] Vector search capabilities
- [ ] User authentication
- [ ] File upload handling

### 📋 Planned
- [ ] Feynman note generation
- [ ] Spaced repetition system
- [ ] Course organization
- [ ] Mobile app
- [ ] Advanced AI features

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/owlnotes-ai/issues)
- **Documentation**: [API Docs](http://localhost:8000/docs) (when running)
- **Email**: kivanc.peltek@temple.edu

## 👥 Contributors

**Kivanc Peltek** - Lead Developer & Project Creator

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🦉 Built with ❤️ for Temple University Students**

[![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

</div>
