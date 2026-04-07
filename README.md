🎓 Smart Campus Assistant

📌 Overview

Smart Campus Assistant is an AI-powered web application that allows students to ask questions about campus-related information such as schedules, locations, and technical services.

The system combines:

structured campus data (database)
rule-based classification
retrieval and scoring logic
AI-generated responses

The project demonstrates a full-stack system with backend, frontend, and DevOps practices.

🧠 Architecture

The system follows a client-server architecture:

Frontend → Backend (FastAPI) → Retrieval → AI → Response

🔹 Frontend
Simple UI for user interaction
Sends questions to backend API
Displays answers and system feedback

🔹 Backend (FastAPI)
Receives user questions (POST /ask)
Classifies question (schedule / general / technical / unknown)
Retrieves relevant data from database
Applies scoring logic
Uses AI to generate final answer
Includes fallback mechanism

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
Unit testing
Docker containerization
Docker Compose orchestration
🚀 Running the Project
🔹 Option 1 — Local (without Docker)
Backend
cd backend
uvicorn app.main:app --reload
Frontend
cd frontend
python -m http.server 5500
🔹 Option 2 — Docker (Recommended)

Run the entire system with one command:

docker compose up --build
🌐 Access the Application
Frontend:
http://127.0.0.1:5500
Backend Docs (Swagger):
http://127.0.0.1:8000/docs
🧪 Running Tests
cd backend
python -m pytest
🧩 Key Design Decision

A major improvement in the system:

Retrieval is not strictly dependent on classification.

If no results are found in the predicted category, the system performs a broader search across the entire dataset.

This improves:

robustness
accuracy
handling of real-world user input
🐳 Docker & DevOps

The project was containerized using Docker:

Separate Docker images for backend and frontend
Services orchestrated using Docker Compose
Entire system runs with a single command

Benefits:

consistent environment
easy setup
reproducible execution
closer to real-world deployment
📂 Project Structure
smart_campus_assistant/
│
├── backend/
│   ├── app/
│   ├── tests/
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
🎯 Future Improvements
Semantic search (embeddings)
Better scoring algorithm
React-based frontend
Deployment to cloud
Authentication
🧠 Key Takeaways
Clean separation between frontend and backend
Retrieval-first approach improves reliability
Docker simplifies environment setup
Compose enables multi-service orchestration
AI systems require fallback strategies

👨‍💻 Author
Yoav Holenberg
