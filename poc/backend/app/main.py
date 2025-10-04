from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import re
from datetime import datetime

app = FastAPI(
    title="OwlNotes AI API",
    description="AI-powered note-taking companion for Temple University students",
    version="1.0.0"
)

class CornellRequest(BaseModel):
    transcript: str
    slides: List[str] = []

class CornellResponse(BaseModel):
    cues: List[str]
    notes: List[str]
    summary: str
    citations: List[Dict[str, Any]]
    key_concepts: List[str]
    questions: List[str]

@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.post("/notes/cornell", response_model=CornellResponse)
def generate_cornell_notes(req: CornellRequest):
    """
    Generate Cornell-style notes from lecture transcript and slides.
    
    This endpoint processes a lecture transcript and optional slides to create
    structured Cornell notes with cues, detailed notes, summary, and citations.
    """
    try:
        # Clean and process transcript
        transcript_lines = [line.strip() for line in req.transcript.splitlines() if line.strip()]
        
        # Extract key concepts (simple keyword extraction)
        key_concepts = extract_key_concepts(req.transcript)
        
        # Generate cues and notes
        cues, notes = generate_cues_and_notes(transcript_lines)
        
        # Generate summary
        summary = generate_summary(req.transcript)
        
        # Generate study questions
        questions = generate_study_questions(req.transcript, key_concepts)
        
        # Process citations
        citations = process_citations(req.slides)
        
        return CornellResponse(
            cues=cues[:10],  # Limit to 10 cues
            notes=notes[:15],  # Limit to 15 note points
            summary=summary,
            citations=citations,
            key_concepts=key_concepts[:8],  # Limit to 8 key concepts
            questions=questions[:5]  # Limit to 5 questions
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing notes: {str(e)}")

def extract_key_concepts(transcript: str) -> List[str]:
    """Extract key concepts from transcript using simple keyword analysis"""
    # Simple keyword extraction - in production, this would use NLP libraries
    words = re.findall(r'\b[A-Z][a-z]+\b', transcript)
    word_freq = {}
    for word in words:
        if len(word) > 3:  # Filter out short words
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Return most frequent words as key concepts (just the words, not tuples)
    return [word for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]]

def generate_cues_and_notes(transcript_lines: List[str]) -> tuple[List[str], List[str]]:
    """Generate cues and detailed notes from transcript lines"""
    cues = []
    notes = []
    
    for line in transcript_lines:
        if len(line) < 50:  # Short lines become cues
            cues.append(line)
        else:  # Longer lines become detailed notes
            # Split long lines into smaller chunks
            if len(line) > 100:
                chunks = [line[i:i+100] for i in range(0, len(line), 100)]
                notes.extend(chunks)
            else:
                notes.append(line)
    
    return cues, notes

def generate_summary(transcript: str) -> str:
    """Generate a concise summary of the transcript"""
    words = transcript.split()
    if len(words) <= 50:
        return transcript
    else:
        # Take first 50 words and add ellipsis
        summary_words = words[:50]
        return " ".join(summary_words) + "..."

def generate_study_questions(transcript: str, key_concepts: List[str]) -> List[str]:
    """Generate study questions based on transcript and key concepts"""
    questions = []
    
    # Generate questions based on key concepts
    for concept in key_concepts[:3]:
        questions.append(f"What is {concept} and how does it work?")
        questions.append(f"Why is {concept} important in this context?")
    
    # Add general comprehension questions
    questions.extend([
        "What are the main points discussed in this lecture?",
        "How do the concepts relate to each other?",
        "What examples were given to illustrate the concepts?"
    ])
    
    return questions

def process_citations(slides: List[str]) -> List[Dict[str, Any]]:
    """Process slides into citation format"""
    citations = []
    for i, slide in enumerate(slides):
        citations.append({
            "type": "slide",
            "reference": slide[:100] + "..." if len(slide) > 100 else slide,
            "page": i + 1,
            "timestamp": datetime.now().isoformat()
        })
    return citations

@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to OwlNotes AI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "cornell_notes": "/notes/cornell",
            "docs": "/docs"
        }
    }
