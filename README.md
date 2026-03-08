# Docker Projects Assignment - Form Submission Application

A complete Docker-based application with Express.js frontend and Flask backend, orchestrated using Docker Compose.

## Project Structure

```
docker-projects-assignment/
├── frontend/                    # Express.js Node application
│   ├── views/                   # EJS templates
│   │   ├── index.ejs           # Main form page
│   │   ├── success.ejs         # Success page
│   │   └── submissions.ejs     # Submissions list
│   ├── public/
│   │   └── style.css           # Styling
│   ├── server.js               # Express server
│   ├── package.json            # Node dependencies
│   └── Dockerfile              # Frontend Docker configuration
├── backend/                     # Flask application
│   ├── app.py                  # Flask API
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Backend Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## Features

- **Frontend**: Express.js with EJS templating engine
- **Backend**: Flask REST API with CORS support
- **Form Submission**: Full-stack form handling with validation
- **Submissions View**: Display all form submissions
- **Docker**: Containerized services with health checks
- **Docker Compose**: Orchestrated networking between services

## Prerequisites

- Docker & Docker Compose installed
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

## Quick Start

### 1. Start Docker Desktop
- Open Docker Desktop application
- Wait until it's fully running (check system tray icon)

### 2. Run the Application
```bash
cd docker-projects-assignment
docker-compose up --build
```

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000/api/health

### 4. Stop the Application
Press `Ctrl+C`, then:
```bash
docker-compose down
```

## API Endpoints

### Backend (Flask)

- **POST /api/submit** - Submit form data
  ```bash
  curl -X POST http://localhost:5000/api/submit \
    -H "Content-Type: application/json" \
    -d '{"name":"John","email":"john@example.com","message":"Hello"}'
  ```

- **GET /api/submissions** - Get all submissions
  ```bash
  curl http://localhost:5000/api/submissions
  ```

- **GET /api/health** - Health check
  ```bash
  curl http://localhost:5000/api/health
  ```

### Frontend (Express)

- **GET /** - Main form page
- **POST /submit** - Submit form and redirect
- **GET /submissions** - View all submissions

## Local Development

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Push to Docker Hub

### Option 1: Use the automated script (Windows)
```bash
build-and-push.bat
```
The script will prompt for your Docker Hub username and handle everything.

### Option 2: Manual commands
```bash
# Login to Docker Hub
docker login

# Build images
docker-compose build

# Tag images (replace YOUR_USERNAME)
docker tag docker-projects-assignment-backend:latest YOUR_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest YOUR_USERNAME/form-submission-frontend:latest

# Push to Docker Hub
docker push YOUR_USERNAME/form-submission-backend:latest
docker push YOUR_USERNAME/form-submission-frontend:latest
```

### Pull from Docker Hub
```bash
docker pull YOUR_USERNAME/form-submission-backend:latest
docker pull YOUR_USERNAME/form-submission-frontend:latest
```

## Environment Variables

- **Frontend**:
  - `BACKEND_URL` - Backend API URL (default: http://localhost:5000)
  - `NODE_ENV` - Environment (production/development)

- **Backend**:
  - `FLASK_ENV` - Flask environment
  - `PYTHONUNBUFFERED` - Unbuffered Python output

## Technologies Used

- **Frontend**: Express.js, EJS, Node.js
- **Backend**: Flask, Python, Flask-CORS
- **Containerization**: Docker, Docker Compose
- **Networking**: Docker bridge network

## Features Included

✅ Full-stack form submission  
✅ Data validation  
✅ Persistent storage (in-memory for demo)  
✅ Error handling  
✅ Responsive UI  
✅ Docker containerization  
✅ Health checks  
✅ CORS enabled  
✅ Service networking  
✅ Volume mounting for development  

## Repository

GitHub: https://github.com/nomanqadri34/docker-projects-assignment

## License

MIT

## Author

Your Name

---

For more information, visit the GitHub repository.
