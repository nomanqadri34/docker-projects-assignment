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

## Running with Docker Compose

1. **Build and start all services**:
   ```bash
   docker-compose up --build
   ```

2. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

3. **Stop services**:
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

## Docker Hub Images

Build and push images to Docker Hub:

```bash
# Build images
docker-compose build

# Tag images
docker tag docker-projects-assignment-backend:latest YOUR_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest YOUR_USERNAME/form-submission-frontend:latest

# Push to Docker Hub
docker push YOUR_USERNAME/form-submission-backend:latest
docker push YOUR_USERNAME/form-submission-frontend:latest
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
