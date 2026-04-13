# 🎓 Smart Campus Assistant

## 📌 Overview
Smart Campus Assistant is an AI-powered full-stack web application that enables students to ask questions about campus-related information such as schedules, locations, and technical services.

The system combines:
- Structured campus data (database)
- Rule-based classification
- Retrieval and scoring logic
- AI-generated responses

This project demonstrates a complete end-to-end system including backend, frontend, and DevOps practices.

---

## 🧠 Architecture

The system follows a client-server architecture:

```text
Frontend → Backend (FastAPI) → Retrieval → AI → Response
🔹 Frontend
Simple UI for user interaction
Sends questions to the backend API
Displays answers and metadata
🔹 Backend (FastAPI)
Receives user questions (POST /ask)
Classifies questions (schedule, technical, general)
Retrieves relevant data from the database
Applies scoring logic
Uses AI to generate answers
Includes fallback mechanisms
Structured with router-based architecture
🔹 Database
SQLite database
Pre-seeded with campus-related data
Organized by categories
⚙️ Features
Question classification
Retrieval-based answer generation
Scoring mechanism (topic + content weighting)
AI integration
Fallback handling
Input validation with Pydantic
Structured logging
Unit and API testing with pytest
Docker containerization
Docker Compose orchestration
🚀 Running the Project
🔹 Option 1 — Local Setup
1. Clone the repository
git clone <your-repo-url>
cd smart_campus_assistant
2. Backend setup
cd backend
pip install -r requirements.txt

Create a .env file inside the backend folder:

OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1
CORS_ORIGINS=http://127.0.0.1:5500,http://localhost:5500

Run the backend:

uvicorn app.main:app --reload
3. Frontend setup
cd ../frontend
python -m http.server 5500
🌐 Access the Application
Frontend: http://127.0.0.1:5500
Backend Docs (Swagger): http://127.0.0.1:8000/docs
🧪 Running Tests
cd backend
pytest

The test suite includes:

API tests
Validation tests
Classifier tests
Fallback tests
🧩 Key Design Decisions
🔹 Retrieval is not strictly dependent on classification

If no results are found in the predicted category, the system performs a broader search across all categories.

This improves:

Robustness
Accuracy
Handling of real-world user input
🐳 Docker & DevOps

Run the entire system with Docker Compose:

docker compose up --build
Benefits
Consistent environment
Easy setup
Reproducible execution
Closer to real-world deployment
🧠 Improvements Made Based on Review Feedback
Centralized configuration using .env and config.py
Removed hardcoded frontend API URL
Added structured logging instead of print statements
Implemented input validation with Pydantic
Refactored the backend into a router-based architecture
Added broader backend and API test coverage
Improved setup and run documentation
📂 Project Structure
smart_campus_assistant/
│
├── backend/
│   ├── app/
│   │   ├── data/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── schemas.py
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── config.js
│   ├── style.css
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
🎯 Future Improvements
Semantic search using embeddings
More advanced scoring algorithm
React-based frontend
<<<<<<< HEAD

>>>>>>> abf2cf7 (Refactor backend architecture, add validation and testing, and improve frontend configuration and README)

👨‍💻 Author
Yoav Holenberg
