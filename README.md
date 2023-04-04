# Containerized QR Generator Web App using Flask and AWS

This is a simple web app that generates QR codes using Flask and AWS. The app is containerized using Docker and deployed on AWS.

## Requirements

To run this project, you will need:
- An AWS account
- A centOS instance 
- Ansible installed on your local machine

## Dockerfile

### Variables
You need to swap these variables with the ones from your AWS account inside the Dockerfile:
- `ENV AWS_ACCESS_KEY_ID=<your-access-key-id>`
- `ENV AWS_SECRET_ACCESS_KEY=<your-secret-access-key>`
- `ENV S3_BUCKET_NAME=<your-bucket-name>`

## Ansible Playbook
This playbook contains the following tasks:
- Install Docker
- Build Docker image
- Run Docker container
- Configure HAproxy

### Variables
You need to swap these variables with the ones form your project:

On roles/deploy-app/var/main.yml:

- app_port_1: 
- app_port_2: 
- app_port_3: 
- docker_image: 


