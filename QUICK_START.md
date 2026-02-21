# Quick Start Guide

Get the application running in 3 simple steps!

## Prerequisites

- ✅ Docker & Docker Compose installed
- ✅ Git installed

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/nomanqadri34/docker-projects-assignment.git
cd docker-projects-assignment
```

### 2. Build and Run
```bash
docker-compose up --build
```

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## What Happens?

Docker Compose will:
1. Build backend image from `backend/Dockerfile` (Flask)
2. Build frontend image from `frontend/Dockerfile` (Express)
3. Create a network connecting both services
4. Start both containers with health checks
5. Frontend will be accessible at port 3000
6. Backend API will be accessible at port 5000

## Try It Out

1. Open http://localhost:3000 in your browser
2. Fill out the form (Name, Email, Message)
3. Click "Submit Form"
4. See your submission on the success page
5. View all submissions at http://localhost:3000/submissions

## Stop the Application
```bash
docker-compose down
```

## Remove All Data and Start Fresh
```bash
docker-compose down -v
docker-compose up --build
```

## Troubleshooting

If something goes wrong, check:

1. **Is Docker running?**
   ```bash
   docker ps
   ```

2. **Are containers running?**
   ```bash
   docker-compose ps
   ```

3. **Check logs:**
   ```bash
   docker-compose logs
   # or specific service
   docker-compose logs backend
   docker-compose logs frontend
   ```

4. **Port conflicts?**
   - Backend uses port 5000
   - Frontend uses port 3000
   - If in use, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for more detailed help.

## Project Structure

```
docker-projects-assignment/
├── backend/               # Flask REST API
│   ├── app.py            # Main application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile        # Container configuration
├── frontend/             # Express.js web server
│   ├── server.js         # Main server file
│   ├── package.json      # Node dependencies
│   ├── views/            # HTML templates
│   ├── public/           # CSS and static files
│   └── Dockerfile        # Container configuration
├── docker-compose.yml    # Service orchestration
├── .gitignore           # Git ignore rules
├── README.md            # Full documentation
├── DOCKER_SETUP.md      # Docker build/push guide
└── QUICK_START.md       # This file
```

## Environment

The frontend can access the backend via: `http://backend:5000`

This is automatically configured in `docker-compose.yml` via:
- Network: `app-network`
- Environment variable: `BACKEND_URL=http://backend:5000`

## Next Steps

1. **Customize the form** - Edit [frontend/views/index.ejs](frontend/views/index.ejs)
2. **Add validation** - Enhance [backend/app.py](backend/app.py)
3. **Add database** - Replace in-memory storage with persistent database
4. **Push to Docker Hub** - See [DOCKER_SETUP.md](DOCKER_SETUP.md)

## Development Mode

For development with auto-reload:

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## API Reference

### Submit Form
```bash
curl -X POST http://localhost:5000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","message":"Hello"}'
```

### Get All Submissions
```bash
curl http://localhost:5000/api/submissions
```

### Health Check
```bash
curl http://localhost:5000/api/health
```

---

**Have fun building! 🚀**
