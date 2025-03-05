# AI Math Tutor

AI Math Tutor is a tool that solves and explains math problems using SymPy for computation and an open-source large language model for explanations. It provides an interactive UI built with Streamlit and a backend powered by FastAPI.

## Features
- **Mathematical Expression Solver:** Uses SymPy to parse and solve expressions.
- **Natural Language Explanation:** Generates step-by-step explanations using an LLM.
- **Interactive Web UI:** Built with Streamlit for easy user interaction.
- **Dockerized Deployment:** Supports easy setup and execution using Docker and Docker Compose.

## Folder Structure
```
ai-math-tutor/
│── backend/
│   ├── main.py  # FastAPI backend
│   ├── requirements.txt  # Dependencies
│   ├── Dockerfile  # Containerization
│── frontend/
│   ├── app.py  # Streamlit UI
│   ├── requirements.txt  # UI Dependencies
│   ├── Dockerfile  # Containerization
│── docker-compose.yml  # Orchestration
│── README.md  # Documentation
```

## Setup and Installation
### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- Hugging Face account (for free LLM usage, if required)

### Running with Docker
1. Clone the repository:
   ```sh
   git clone (Form UI or URL)
   cd ai-math-tutor
   ```
2. Build and start the services:
   ```sh
   docker-compose up --build
   ```
3. Access the frontend at: [http://localhost:8501](http://localhost:8501)

### Running Locally (Without Docker)
1. Install backend dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
2. Install frontend dependencies:
   ```sh
   cd ../frontend
   pip install -r requirements.txt
   streamlit run app.py
   ```

## API Endpoints
### Solve a Math Problem
**Endpoint:** `POST /solve`
- **Request Body:**
  ```json
  {
    "problem": "x**2 - 4"
  }
  ```
- **Response:**
  ```json
  {
    "problem": "x**2 - 4",
    "solution": "x^2 - 4",
    "explanation": "This is a quadratic equation..."
  }
  ```
