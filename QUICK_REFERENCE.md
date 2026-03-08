# Quick Reference Card

## 🚀 Start Project
```bash
cd docker-projects-assignment
docker-compose up --build
```
**Access**: http://localhost:3000

## 🛑 Stop Project
```bash
Ctrl+C
docker-compose down
```

## 📤 Push to Docker Hub
```bash
build-and-push.bat
```
Or manually:
```bash
docker login
docker-compose build
docker tag docker-projects-assignment-backend:latest YOUR_USERNAME/form-submission-backend:latest
docker tag docker-projects-assignment-frontend:latest YOUR_USERNAME/form-submission-frontend:latest
docker push YOUR_USERNAME/form-submission-backend:latest
docker push YOUR_USERNAME/form-submission-frontend:latest
```

## 🔍 Useful Commands

### Check running containers
```bash
docker ps
```

### View logs
```bash
docker logs flask-backend
docker logs express-frontend
```

### Check images
```bash
docker images
```

### Remove containers
```bash
docker-compose down -v
```

### Rebuild from scratch
```bash
docker-compose down -v
docker-compose up --build --force-recreate
```

## 🌐 URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:5000 |
| Health Check | http://localhost:5000/api/health |
| Submissions | http://localhost:3000/submissions |

## 📁 Project Structure

```
docker-projects-assignment/
├── frontend/
│   ├── server.js          # Express server
│   ├── Dockerfile         # Frontend Docker config
│   ├── package.json       # Dependencies
│   └── views/             # EJS templates
├── backend/
│   ├── app.py            # Flask API
│   ├── Dockerfile        # Backend Docker config
│   └── requirements.txt  # Dependencies
├── docker-compose.yml    # Orchestration
└── build-and-push.bat   # Push script
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Docker not found | Start Docker Desktop |
| Port in use | Change port in docker-compose.yml |
| Build fails | Check Dockerfile syntax |
| Can't connect | Check if backend is healthy |

## 📋 Submission Checklist

- [ ] Docker Desktop running
- [ ] Project runs locally (http://localhost:3000)
- [ ] Form submission works
- [ ] Images pushed to Docker Hub
- [ ] Code pushed to GitHub
- [ ] .gitignore includes node_modules and .vscode

## 🔗 Links

- **GitHub**: https://github.com/nomanqadri34/docker-projects-assignment
- **Docker Hub**: https://hub.docker.com/u/YOUR_USERNAME

## 💡 Tips

1. Always start Docker Desktop first
2. Use `docker-compose down` before rebuilding
3. Check logs if something doesn't work
4. Test locally before pushing to Docker Hub
5. Keep your Docker Hub username handy
