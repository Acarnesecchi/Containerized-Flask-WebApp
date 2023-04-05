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

## Steps to run the project

1. Clone the project to your local machine `git clone https://github.com/Acarnesecchi/Containerized-Flask-WebApp.git`
2. Go to the project directory `cd Containerized-Flask-WebApp`
3. Make sure you have Ansible installed on your local machine and the next python libraries:
   - boto3
   - docker
4. Set up your AWS account:
    - Generate an SSH key pair and save the private key in your local machine
    - Create an IAM role with the necessary permissions
    - Create a security group with the necessary ports open
    - Create a public S3 bucket and add the next policy to it:
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPublicRead",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<your-bucket-name>/*"
            }
        ]
    }
    ```
5. 

### Variables
You need to swap these variables with the ones form your project:

On roles/deploy-app/var/main.yml:

- app_port_1: 
- app_port_2: 
- app_port_3: 
- docker_image: 


