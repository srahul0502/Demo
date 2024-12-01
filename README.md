# Flask App with Docker and Jenkins Pipeline

This repository demonstrates the process of building and deploying a simple Flask application using Docker and automating it with a Jenkins pipeline. It is beginner-friendly and provides a practical introduction to CI/CD concepts.

## Overview

### What You'll Learn:
- **Flask Application Development**: Create a basic web application in Python using Flask.
- **Dockerization**: Containerize the application to ensure portability and ease of deployment.
- **Jenkins Pipeline**: Automate the build and deployment process with a Jenkins declarative pipeline.

### Jenkins Pipeline Stages:
1. **Clone the Code**: Pull the Flask application code from the repository.
2. **Build Docker Image**: Use the Dockerfile to create an image of the application.
3. **Run the Container**: Deploy the containerized app and verify it's running.

## Getting Started

### Prerequisites:
- **AWS EC2 Instance**: An Ubuntu instance with proper network configuration (Ports 22, 8080, 5000 allowed).
- **Docker**: Installed and configured on the EC2 instance.
- **Jenkins**: Installed and set up with Docker access.

### Steps:

1. **Set Up AWS EC2**: Launch an Ubuntu instance, configure inbound rules, and SSH into the instance.
   
2. **Clone the Repository**:
    ```bash
    git clone https://github.com/srahul0502/Demo.git
    cd Demo
    ```

3. **Build and Test Locally**:
    - **Build the Docker image**:
    ```bash
    docker build -t flask-app .
    ```
    - **Run the Docker container**:
    ```bash
    docker run -d -p 5000:5000 flask-app
    ```
    - Test the app by visiting `http://<your-ec2-ip>:5000`.

4. **Set Up Jenkins Pipeline**:
    - Create a new pipeline job in Jenkins.
    - Use the provided pipeline script to automate the process.

## Verifying the Setup

- Monitor pipeline progress in Jenkins.
- Once complete, access the application at `http://<your-jenkins-server-ip>:5000`.

### Application Output:
```
Hello, This is my first pipeline..!
```

## Wrapping Up

With this setup, you've implemented a complete CI/CD pipeline for a Flask application. You can now expand it to include automated testing, deploy to production, or integrate with cloud platforms.

**Happy Coding! 🚀**
