#!/bin/bash

# Build and Push Docker Images to Docker Hub
# Replace 'your-docker-username' with your actual Docker Hub username

DOCKER_USERNAME="your-docker-username"

echo "Building Docker images..."
docker-compose build

if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

echo ""
echo "Images built successfully!"
echo ""

# Tag images for Docker Hub
echo "Tagging images for Docker Hub..."
docker tag docker-projects-assignment-backend:latest $DOCKER_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest $DOCKER_USERNAME/form-submission-frontend:latest

echo ""
echo "Logging into Docker Hub..."
docker login

if [ $? -ne 0 ]; then
    echo "Docker login failed!"
    exit 1
fi

echo ""
echo "Pushing backend image..."
docker push $DOCKER_USERNAME/form-submission-backend:latest

echo ""
echo "Pushing frontend image..."
docker push $DOCKER_USERNAME/form-submission-frontend:latest

echo ""
echo "All images pushed successfully!"
echo ""
echo "Backend: $DOCKER_USERNAME/form-submission-backend:latest"
echo "Frontend: $DOCKER_USERNAME/form-submission-frontend:latest"
