## Technologies to be used for AWS or GCP hosting

**AWS (Amazon Web Services):**

**Compute:**

Use Amazon EC2 (Elastic Compute Cloud) instances to host your FastAPI application. Multiple instances can be launched for scalability.

Alternatively, AWS ECS (Elastic Container Service) or AWS Fargate for container orchestration can be used.


**Containerization:**

Using Docker to containerize the FastAPI application and push the Docker images to Amazon ECR (Elastic Container Registry).

AWS ECS for container orchestration or AWS Elastic Kubernetes Service (EKS) can be used if kubernetes is the preference.


**Load Balancing:**

Use AWS Elastic Load Balancing (ELB) to distribute incoming traffic across multiple instances or containers.
Application Load Balancer (ALB) supports HTTP/HTTPS and is suitable for web applications.


**Networking:**

Leverage Amazon VPC (Virtual Private Cloud) for networking isolation.
Utilize Amazon Route 53 for DNS management.

**Storage:**

Store persistent data in Amazon RDS (Relational Database Service) for databases.
Encryption at rest can be assured using AWS KMS (Key Management System)
Use Amazon S3 for static files or object storage.


**Monitoring and Logging:**

Set up Amazon CloudWatch for monitoring application performance.
Use AWS CloudTrail and AWS Config for auditing changes.



#GCP (Google Cloud Platform):

**Compute:**

Deploy the FastAPI application on Google Compute Engine instances. Scale horizontally as needed.
Alternatively, use Google Kubernetes Engine (GKE) for container orchestration.


**Containerization:**

Containerize the application and store Docker images in Google Container Registry (GCR).
Use GKE for Kubernetes-based container orchestration.


**Load Balancing:**

Utilize Google Cloud Load Balancing to distribute traffic among instances or containers.
HTTP(S) Load Balancing is suitable for web applications.


**Networking:**

Set up Google VPC for networking isolation.
Use Google Cloud DNS for managing domain names.


**Storage:**

Store persistent data in Google Cloud SQL for databases.
Google Cloud Storage (GCS) is suitable for static files.


**Monitoring and Logging:**

Use Google Cloud Monitoring for performance monitoring.
Stackdriver Logging for centralized logging.


**Common Considerations:**

**Security:**

Implement Identity and Access Management (IAM) on AWS or Cloud Identity and Access Management (Cloud IAM) on GCP to control access and permissions.

Use Security Groups on AWS or Firewall Rules on GCP for network security.
Scaling:

Implement Auto Scaling on AWS or Managed Instance Groups (MIGs) on GCP for automatic scaling based on demand.


**Serverless:**

Explore AWS Lambda or Google Cloud Functions/Cloud Run for serverless compute options.








## Common Techniques and Best Practices:

**Use a Minimal Base Image:**

Start with a minimal base image to reduce the image size and enhance security.
Example: python:3.9-slim instead of python:3.9.

**Leverage Layer Caching:**

Instructions should be ordered to make use of Docker layer caching.
Less frequently chaning instructions should be placed towards the end of the Dockerfile.

**Combine RUN Commands:**

Combine multiple RUN commands into a single line to minimize layers.
Example:
```
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    apt-get clean

```

**Use COPY Instead of ADD:**

Prefer COPY over ADD for copying files, as ADD has additional features that may not be needed.
Example:
```
COPY requirements.txt /app/
```

**Specify Versions for Dependencies:**

Explicitly specify versions for all dependencies to ensure reproducibility in the dockerfile.

Example:
```
RUN pip install --no-cache-dir -r requirements.txt
```

**Remove Unnecessary Files:**

Remove unnecessary files after installing dependencies to reduce image size.
Example:
```
RUN apt-get purge -y --auto-remove package1 && \
    rm -rf /var/lib/apt/lists/*
```

**Use Environment Variables:**

Set environment variables for configuration to make the Dockerfile more flexible.
Example:
```
ENV APP_HOME /app
```

**Clean Up in a Single Layer:**

Combine cleanup operations into a single RUN command to minimize layers.
Example:
```
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

**Health Checks:**

Include a health check instruction to help Docker determine the status of the container.
Example:
```
HEALTHCHECK CMD curl --fail http://localhost/ || exit 1
```

**USER Instruction:**

Use the USER instruction to run commands as a non-root user for enhanced security.
Example:
```
USER nonrootuser
```

## Relevance to Practical Assignment:
For the practical assignment, the following practices are particularly relevant:

**Containerization:**

Use a multi-stage build if applicable to create a smaller production image.
Example:
```
FROM python:3.9 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app /app
COPY . .
CMD ["python", "app.py"]
```

**Container Orchestration:**

Ensure that the Dockerfile is compatible with container orchestration platforms like Docker Compose, Kubernetes, or AWS ECS.


**Logging and Monitoring:**

Incorporating application code logging using agents or code instrumentation is vital to pick logs when application is running.


**Security:**

Implementing best practices for security, including minimizing the attack surface, running as a non-root user, and regularly update of base images.

