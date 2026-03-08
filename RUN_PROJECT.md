# How to Run the Project

## Prerequisites
1. Install Docker Desktop from https://www.docker.com/products/docker-desktop
2. Start Docker Desktop (wait for it to fully start)
3. Create a Docker Hub account at https://hub.docker.com if you don't have one

## Step 1: Start Docker Desktop
- Open Docker Desktop application
- Wait until you see "Docker Desktop is running" in the system tray
- Verify by running: `docker --version`

## Step 2: Run the Project Locally

Open Command Prompt or PowerShell in the project directory and run:

```bash
cd docker-projects-assignment
docker-compose up --build
```

This will:
- Build both frontend and backend Docker images
- Start both containers
- Connect them on the same network

## Step 3: Access the Application

Once running, open your browser:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000/api/health

## Step 4: Test the Application

1. Go to http://localhost:3000
2. Fill out the form with:
   - Name
   - Email
   - Message
3. Click "Submit Form"
4. You should see a success page
5. Click "View All Submissions" to see all submitted forms

## Step 5: Push Images to Docker Hub

### Option A: Use the automated script (Windows)

```bash
build-and-push.bat
```

The script will:
1. Ask for your Docker Hub username
2. Build the images
3. Tag them properly
4. Login to Docker Hub
5. Push both images

### Option B: Manual commands

```bash
# Login to Docker Hub
docker login

# Build images
docker-compose build

# Tag images (replace YOUR_USERNAME with your Docker Hub username)
docker tag docker-projects-assignment-backend:latest YOUR_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest YOUR_USERNAME/form-submission-frontend:latest

# Push to Docker Hub
docker push YOUR_USERNAME/form-submission-backend:latest
docker push YOUR_USERNAME/form-submission-frontend:latest
```

## Step 6: Stop the Application

Press `Ctrl+C` in the terminal, then run:

```bash
docker-compose down
```

## Troubleshooting

### Docker Desktop not running
**Error**: "error during connect: ... pipe/dockerDesktopLinuxEngine: The system cannot find the file specified"

**Solution**: Start Docker Desktop and wait for it to fully initialize

### Port already in use
**Error**: "port is already allocated"

**Solution**: 
```bash
# Stop any running containers
docker-compose down

# Or change ports in docker-compose.yml
```

### Cannot connect to backend
**Error**: Frontend shows "Server error"

**Solution**: 
- Check if backend is running: http://localhost:5000/api/health
- Check Docker logs: `docker logs flask-backend`

## Docker Hub Images

After pushing, your images will be available at:
- `YOUR_USERNAME/form-submission-backend:latest`
- `YOUR_USERNAME/form-submission-frontend:latest`

Anyone can pull and run your images:
```bash
docker pull YOUR_USERNAME/form-submission-backend:latest
docker pull YOUR_USERNAME/form-submission-frontend:latest
```

## Project Structure

```
docker-projects-assignment/
├── frontend/           # Express.js application
│   ├── server.js      # Main server file
│   ├── views/         # EJS templates
│   ├── public/        # Static files (CSS)
│   ├── Dockerfile     # Frontend Docker config
│   └── package.json   # Node dependencies
├── backend/           # Flask application
│   ├── app.py        # Main Flask app
│   ├── Dockerfile    # Backend Docker config
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Orchestration config
└── build-and-push.bat   # Push script
```

## GitHub Repository

https://github.com/nomanqadri34/docker-projects-assignment
