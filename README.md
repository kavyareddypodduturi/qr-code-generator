# QR Code Generator (Dockerized)

This project demonstrates how to containerize a Python application using Docker.

## Features
- Generates a QR code from a provided URL
- Runs inside a Docker container
- Automated Docker build using GitHub Actions
- Docker image published to DockerHub

## DockerHub Image
https://hub.docker.com/r/kavyareddypodduturi/qr-code-generator-app

## GitHub Repository
https://github.com/kavyareddypodduturi/qr-code-generator

## How to Run

Build the Docker image:

docker build -t qr-code-generator-app .

Run the container:

docker run -d --name qr-generator qr-code-generator-app

Check container logs:

docker logs qr-generator
