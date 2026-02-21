# Docker Build and Push Instructions

## Prerequisites

1. **Docker Desktop installed and running**
   - Windows: Download from https://www.docker.com/products/docker-desktop
   - Mac: Download from https://www.docker.com/products/docker-desktop
   - Linux: Follow instructions at https://docs.docker.com/engine/install/

2. **Docker Hub Account**
   - Sign up at https://hub.docker.com

3. **Git installed** (already done for GitHub)

## Steps to Build and Push Images

### Step 1: Prepare Your Docker Hub Username

Replace `your-docker-username` in the scripts with your actual Docker Hub username.

### Step 2: Build Docker Images

**Windows (PowerShell):**
```powershell
cd d:\docker\docker-projects-assignment
docker-compose build
```

**Windows (Command Prompt):**
```cmd
cd d:\docker\docker-projects-assignment
docker-compose build
```

**Linux/Mac:**
```bash
cd docker-projects-assignment
docker-compose build
```

### Step 3: Tag Images

**Windows (PowerShell):**
```powershell
$DOCKER_USERNAME = "your-docker-username"

docker tag docker-projects-assignment-backend:latest ${DOCKER_USERNAME}/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest ${DOCKER_USERNAME}/form-submission-frontend:latest
```

**Windows (Command Prompt):**
```cmd
set DOCKER_USERNAME=your-docker-username

docker tag docker-projects-assignment-backend:latest %DOCKER_USERNAME%/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest %DOCKER_USERNAME%/form-submission-frontend:latest
```

**Linux/Mac:**
```bash
DOCKER_USERNAME="your-docker-username"

docker tag docker-projects-assignment-backend:latest $DOCKER_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest $DOCKER_USERNAME/form-submission-frontend:latest
```

### Step 4: Login to Docker Hub

```bash
docker login
```

Enter your Docker Hub credentials when prompted.

### Step 5: Push Images to Docker Hub

**Backend:**
```bash
docker push your-docker-username/form-submission-backend:latest
```

**Frontend:**
```bash
docker push your-docker-username/form-submission-frontend:latest
```

### Automated Scripts

You can also use the provided scripts:

**Windows:**
```powershell
.\build-and-push.bat
```

**Linux/Mac:**
```bash
chmod +x build-and-push.sh
./build-and-push.sh
```

## Verify Images on Docker Hub

1. Visit https://hub.docker.com
2. Go to your profile
3. Look for:
   - `form-submission-backend`
   - `form-submission-frontend`

## Pull and Run from Docker Hub

Once images are pushed, anyone can run them:

```bash
docker-compose -f docker-compose.production.yml up
```

Where `docker-compose.production.yml` uses your Docker Hub images:

```yaml
version: '3.8'

services:
  backend:
    image: your-docker-username/form-submission-backend:latest
    ports:
      - "5000:5000"
    networks:
      - app-network

  frontend:
    image: your-docker-username/form-submission-frontend:latest
    ports:
      - "3000:3000"
    environment:
      - BACKEND_URL=http://backend:5000
    networks:
      - app-network
    depends_on:
      - backend

networks:
  app-network:
    driver: bridge
```

## Troubleshooting

**Docker daemon not running:**
- Make sure Docker Desktop is running
- On Linux, run: `sudo systemctl start docker`

**Docker Hub login failed:**
- Verify credentials are correct
- Check internet connection

**Image build fails:**
- Check error messages
- Ensure all files are in correct locations
- Verify Dockerfile syntax

**Push fails:**
- Ensure you're logged in: `docker login`
- Verify image name matches your Docker Hub username
- Check internet connection
