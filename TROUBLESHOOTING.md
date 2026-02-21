# Troubleshooting Guide

## Common Issues and Solutions

### Docker Issues

#### Docker daemon is not running
**Error:** `failed to connect to the docker API`

**Solution:**
1. Ensure Docker Desktop is running
2. Windows: Check system tray for Docker Desktop icon
3. Linux: Run `sudo systemctl start docker`
4. Mac: Start Docker from Applications

#### Cannot connect to Docker daemon
**Error:** `Cannot connect to the Docker daemon`

**Solution:**
```bash
# On Linux, add your user to docker group
sudo usermod -aG docker $USER
# Log out and log back in for group changes to take effect
```

### Application Issues

#### Frontend cannot reach backend
**Error:** Connection refused when submitting form

**Solution:**
1. Verify backend is running: `docker-compose logs backend`
2. Check backend URL in frontend environment variable
3. Ensure services are on same network: `docker network ls`

#### Port already in use
**Error:** `bind: address already in use`

**Solution:**
1. Check what's using the port:
   ```bash
   # Windows
   netstat -ano | findstr :3000
   netstat -ano | findstr :5000
   
   # Linux/Mac
   lsof -i :3000
   lsof -i :5000
   ```
2. Kill the process or use different ports in docker-compose.yml

#### Form submission fails
**Error:** Error submitting form

**Solution:**
1. Check browser console for errors
2. Verify backend is running: `docker-compose ps`
3. Check backend logs: `docker-compose logs backend`
4. Verify CORS is enabled in Flask app

### Database Issues (if applicable)

#### Data not persisting
**Issue:** Submissions lost when container restarts

**Solution:**
Add a database volume to docker-compose.yml (currently using in-memory storage)

### Git Issues

#### Cannot push to GitHub
**Error:** Authentication failed

**Solution:**
1. Use personal access token instead of password
2. Generate token at https://github.com/settings/tokens
3. Use token as password when pushed

#### Merge conflicts
**Error:** Merge conflict when pulling

**Solution:**
```bash
git status
# Resolve conflicts in files
git add .
git commit -m "Resolve merge conflicts"
git push
```

### Node.js/NPM Issues

#### npm install fails
**Error:** Module not found or installation errors

**Solution:**
1. Delete node_modules and package-lock.json
2. Clear npm cache: `npm cache clean --force`
3. Reinstall: `npm install`
4. Rebuild images: `docker-compose build --no-cache`

### Python/Flask Issues

#### Module import errors
**Error:** ModuleNotFoundError or ImportError

**Solution:**
1. Verify requirements.txt has all dependencies
2. Rebuild backend image: `docker-compose build --no-cache backend`
3. Check Python version compatibility

#### CORS errors
**Error:** CORS policy blocking requests

**Solution:**
Ensure Flask-CORS is properly configured in app.py:
```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

### Docker Compose Issues

#### Service fails to start
**Error:** Container exits immediately

**Solution:**
1. Check logs: `docker-compose logs service-name`
2. Verify Dockerfile syntax
3. Check environment variables
4. Verify ports aren't already in use

#### Health check failing
**Error:** Unhealthy status

**Solution:**
1. Check what the health check command is doing
2. Verify service is actually running
3. Check port availability
4. Review logs for startup errors

### Performance Issues

#### Slow response times
**Issue:** Application is very slow

**Solution:**
1. Check container resources: `docker stats`
2. Verify disk space: `docker system df`
3. Check network: `docker network inspect app-network`
4. Review application logs for errors

#### High memory usage
**Issue:** Container using excessive memory

**Solution:**
1. Check what's consuming memory
2. Optimize application code
3. Add memory limits to docker-compose.yml:
   ```yaml
   services:
     backend:
       mem_limit: 512m
       memswap_limit: 512m
   ```

### Cleanup and Reset

#### Remove all containers and start fresh
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

#### View logs for debugging
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs backend
docker-compose logs frontend

# Follow logs in real-time
docker-compose logs -f backend
```

#### Check what's running
```bash
docker-compose ps
docker images
docker network ls
```

### Still Having Issues?

1. Check Docker logs: `docker logs container-name`
2. Check application logs: `docker-compose logs`
3. Verify all files are in correct locations
4. Check file permissions
5. Try rebuilding: `docker-compose build --no-cache`
6. Search GitHub issues for similar problems

## Getting Help

- Docker Documentation: https://docs.docker.com/
- Flask Documentation: https://flask.palletsprojects.com/
- Express.js Documentation: https://expressjs.com/
- Docker Compose: https://docs.docker.com/compose/
