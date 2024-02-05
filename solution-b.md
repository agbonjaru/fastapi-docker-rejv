## GitHub Repository Structure:
Create a new GitHub Repository:

Create a new repository on GitHub (https://github.com/agbonjaru/fastapi-docker-rejv).

Clone the Repository:

Clone the repository to your local machine:

```
git clone https://github.com/agbonjaru/fastapi-docker-rejv.git
cd fastapi-docker-rejv
```

**Project Structure:**

Organize your project files.

```
/fastapi-docker-rejv
├── app
│   ├── main.py
│   └── ...
├── locust
│   ├── locustfile.py
│   └── ...
├── docker-compose.yaml
├── nginx.conf
├── Dockerfile
├── requirements.txt
├── .github
│   └── workflows
│       └── deploy_to_production.yml
└── README.md
```
**GitHub Actions CI/CD Pipeline:**
Create GitHub Actions Workflow:

Inside the .github/workflows directory, create a file named deploy_to_production.yml (this can be any name- but its best to make it descriptive as possible):


**Docker Hub Credentials:**
Set Docker Hub Credentials as Secrets:
Go to your GitHub repository on the web.
Navigate to "Settings" -> "Secrets".
Add the following secrets:
DOCKER_USERNAME: Your Docker Hub/GCR/ECR username.
DOCKER_PASSWORD: Your Docker Hub/GCR/ECR password or access token.
Commit and Push:
Commit your changes and push them to GitHub:

```
git add .
git commit -m "Add CI/CD pipeline"
git push origin main
```

**Verify:**
Verify the CI/CD Pipeline:
Go to the "Actions" tab on your GitHub repository to see the CI/CD workflow in action.
Check the workflow logs for any errors or issues.