@echo off
REM Build and Push Docker Images to Docker Hub

echo ========================================
echo Docker Build and Push Script
echo ========================================
echo.

REM Prompt for Docker Hub username
set /p DOCKER_USERNAME="Enter your Docker Hub username: "

if "%DOCKER_USERNAME%"=="" (
    echo Error: Docker Hub username cannot be empty!
    exit /b 1
)

echo.
echo Building Docker images...
docker-compose build

if errorlevel 1 (
    echo Build failed!
    exit /b 1
)

echo.
echo ✓ Images built successfully!
echo.

REM Tag images for Docker Hub
echo Tagging images for Docker Hub...
docker tag docker-projects-assignment-backend:latest %DOCKER_USERNAME%/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest %DOCKER_USERNAME%/form-submission-frontend:latest

if errorlevel 1 (
    echo Tagging failed!
    exit /b 1
)

echo ✓ Images tagged successfully!
echo.

echo Logging into Docker Hub...
docker login

if errorlevel 1 (
    echo Docker login failed!
    exit /b 1
)

echo.
echo Pushing backend image to Docker Hub...
docker push %DOCKER_USERNAME%/form-submission-backend:latest

if errorlevel 1 (
    echo Backend push failed!
    exit /b 1
)

echo ✓ Backend image pushed!
echo.

echo Pushing frontend image to Docker Hub...
docker push %DOCKER_USERNAME%/form-submission-frontend:latest

if errorlevel 1 (
    echo Frontend push failed!
    exit /b 1
)

echo.
echo ========================================
echo ✓ All images pushed successfully!
echo ========================================
echo.
echo Your Docker Hub images:
echo   Backend:  %DOCKER_USERNAME%/form-submission-backend:latest
echo   Frontend: %DOCKER_USERNAME%/form-submission-frontend:latest
echo.
echo You can now pull these images using:
echo   docker pull %DOCKER_USERNAME%/form-submission-backend:latest
echo   docker pull %DOCKER_USERNAME%/form-submission-frontend:latest
echo.
pause
