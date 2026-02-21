@echo off
REM Build and Push Docker Images to Docker Hub
REM Replace 'your-docker-username' with your actual Docker Hub username

set DOCKER_USERNAME=your-docker-username

echo Building Docker images...
docker-compose build

if errorlevel 1 (
    echo Build failed!
    exit /b 1
)

echo.
echo Images built successfully!
echo.

REM Tag images for Docker Hub
echo Tagging images for Docker Hub...
docker tag docker-projects-assignment-backend:latest %DOCKER_USERNAME%/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest %DOCKER_USERNAME%/form-submission-frontend:latest

echo.
echo Logging into Docker Hub...
docker login

if errorlevel 1 (
    echo Docker login failed!
    exit /b 1
)

echo.
echo Pushing backend image...
docker push %DOCKER_USERNAME%/form-submission-backend:latest

echo.
echo Pushing frontend image...
docker push %DOCKER_USERNAME%/form-submission-frontend:latest

echo.
echo All images pushed successfully!
echo.
echo Backend: %DOCKER_USERNAME%/form-submission-backend:latest
echo Frontend: %DOCKER_USERNAME%/form-submission-frontend:latest
