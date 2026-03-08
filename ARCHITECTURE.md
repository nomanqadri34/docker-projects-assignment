# Project Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Compose Network                   │
│                        (app-network)                         │
│                                                              │
│  ┌──────────────────────┐      ┌──────────────────────┐   │
│  │   Frontend Container │      │  Backend Container    │   │
│  │   (Express/Node.js)  │      │      (Flask)          │   │
│  │                      │      │                       │   │
│  │  Port: 3000          │◄────►│  Port: 5000          │   │
│  │  Image: frontend     │      │  Image: backend       │   │
│  └──────────────────────┘      └──────────────────────┘   │
│           │                              │                  │
└───────────┼──────────────────────────────┼──────────────────┘
            │                              │
            │                              │
    localhost:3000                 localhost:5000
            │                              │
            ▼                              ▼
      ┌──────────┐                  ┌──────────┐
      │  Browser │                  │ REST API │
      └──────────┘                  └──────────┘
```

## Component Details

### Frontend (Express.js)
- **Technology**: Node.js 18, Express, EJS
- **Port**: 3000
- **Responsibilities**:
  - Serve HTML forms
  - Handle user input
  - Make HTTP requests to backend
  - Display responses

### Backend (Flask)
- **Technology**: Python 3.9, Flask, Flask-CORS
- **Port**: 5000
- **Responsibilities**:
  - REST API endpoints
  - Form data validation
  - Data storage (in-memory)
  - CORS handling

## Data Flow

```
1. User fills form in browser
   └─► http://localhost:3000

2. Frontend receives form data
   └─► POST /submit

3. Frontend sends to backend
   └─► POST http://backend:5000/api/submit

4. Backend validates and stores data
   └─► Returns JSON response

5. Frontend displays success page
   └─► User sees confirmation
```

## API Endpoints

### Backend (Flask)
| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| POST   | /api/submit       | Submit form data         |
| GET    | /api/submissions  | Get all submissions      |
| GET    | /api/health       | Health check             |

### Frontend (Express)
| Method | Endpoint      | Description              |
|--------|---------------|--------------------------|
| GET    | /             | Main form page           |
| POST   | /submit       | Handle form submission   |
| GET    | /submissions  | View all submissions     |

## Docker Network

- **Network Name**: app-network
- **Driver**: bridge
- **Purpose**: Allows containers to communicate using service names
- **Example**: Frontend connects to `http://backend:5000` instead of `http://localhost:5000`

## Environment Variables

### Frontend
```
BACKEND_URL=http://backend:5000
NODE_ENV=production
```

### Backend
```
FLASK_ENV=production
PYTHONUNBUFFERED=1
```

## Health Checks

Both services include health checks:
- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3
- **Start Period**: 40 seconds

## Volume Mounts

Development volumes for hot-reload:
```yaml
frontend:
  volumes:
    - ./frontend:/app
    - /app/node_modules  # Prevent overwriting

backend:
  volumes:
    - ./backend:/app
```

## Dependencies

Frontend depends on backend being healthy:
```yaml
depends_on:
  backend:
    condition: service_healthy
```

## Docker Hub Images

After building and pushing:
- `YOUR_USERNAME/form-submission-backend:latest`
- `YOUR_USERNAME/form-submission-frontend:latest`

## Security Features

1. **CORS**: Enabled on backend for cross-origin requests
2. **Input Validation**: Both frontend and backend validate data
3. **Error Handling**: Comprehensive error messages
4. **Health Checks**: Automatic container health monitoring
