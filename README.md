# POC-2

# POC-2: Jenkins, Apache, Ansible, and Python Integration

## Overview
This repo demonstrates:
- Apache/Tomcat deployment
- Jenkins integration
- Ansible automation
- Python-based web message validation

## Structure
- `check_web.py`: Validates web page message
- `Jenkinsfile`: Jenkins pipeline to automate the process
- `requirements.txt`: Python dependencies

## Usage
1. Ensure Jenkins is configured with Python and Git.
2. Add this repo in a Jenkins Pipeline Job.
3. Run the pipeline to validate the Apache/Tomcat message.
