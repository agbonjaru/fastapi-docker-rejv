# FastAPI Application with Nginx Load Balancing
FastAPI web application with Nginx load balancing. Dockerized for scalability, includes real-time Pi calculation, random sequences, POSIX timestamps, and load testing scripts


This repository contains a FastAPI application with Nginx load balancing for a scalable and efficient web application setup.

**Prerequisites**
Make sure you have Docker and Docker Compose installed on your machine.

Docker Installation Guide : https://docs.docker.com/engine/install/
Docker Compose Installation Guide : https://docs.docker.com/compose/install/

**Running Locally with Docker Compose**
Clone this repository:

```
git clone https://github.com/agbonjaru/fastapi-docker-rejv
cd your-repo
``` 

**Build the Docker images and start the services:**
```
docker-compose up --build
```

**Access the FastAPI application:**

Open your web browser and go to http://localhost. You should see the FastAPI application with Nginx load balancing.

**Stop the services:**

Press Ctrl + C in the terminal where docker-compose is running to stop the services.

**Configuration**
Adjusted the number of FastAPI instances and other settings in the docker-compose.yml file.
In the docker-compose.yml file, I have included the necessary configuration for Nginx, FastAPI, and any other services you have. Here's a sample section for the services in the docker-compose.yml:

```
version: '3'

services:
  fastapi-app-1:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8001:8000"

  fastapi-app-2:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8002:8000"

  nginx-proxy:
    image: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
    depends_on:
      - fastapi-app-1
      - fastapi-app-2
```

