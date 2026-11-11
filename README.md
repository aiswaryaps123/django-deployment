# 🐍 Django Web Application Deployment on Rocky Linux

### 🚀 Developing, Deploying & Hosting a Python Web Application Using Gunicorn and Nginx

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-4.2.30-green?logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/Rocky_Linux-9.7-10B981?logo=rockylinux&logoColor=white">
  <img src="https://img.shields.io/badge/Gunicorn-23.0.0-499848">
  <img src="https://img.shields.io/badge/Nginx-Reverse_Proxy-009639?logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/Deployment-Successful-brightgreen">
</p>

---

## 🌟 Project Overview

This project demonstrates the development and deployment of a Python-based web application using the Django framework on a Rocky Linux 9.7 server.

The application is served using Gunicorn as the WSGI application server, with Nginx configured as a reverse proxy to handle incoming HTTP requests.

The project focuses on practical Linux server administration, Python application deployment, service management, networking, and security configuration.

## 🏗️ Deployment Architecture

```text
             CLIENT / WEB BROWSER
                      |
                      | HTTP - Port 80
                      v
                +-------------+
                |    NGINX    |
                | Web Server  |
                +-------------+
                      |
                      | Reverse Proxy
                      v
                +-------------+
                |  GUNICORN   |
                | WSGI Server |
                +-------------+
                      |
                      v
                +-------------+
                |   DJANGO    |
                | Application |
                +-------------+
                      |
                      v
                +-------------+
                |   SQLITE    |
                |  DATABASE   |
                +-------------+
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.9 | Programming language |
| Django 4.2.30 | Web application framework |
| SQLite | Database |
| Gunicorn 23.0.0 | WSGI application server |
| Nginx | Web server and reverse proxy |
| Rocky Linux 9.7 | Deployment operating system |
| systemd | Service management |
| firewalld | Firewall management |
| SELinux | Security enforcement |
| Git & GitHub | Version control |

## ✨ Application Features

- Custom Django homepage.
- Python virtual environment for dependency isolation.
- Django views and URL routing.
- SQLite database integration.
- Gunicorn application server.
- Gunicorn managed through systemd.
- Nginx reverse proxy configuration.
- Firewall configuration for HTTP access.
- SELinux network connection configuration.
- Automatic service startup after system reboot.

## 📂 Project Structure

```text
django-deployment/
│
├── home/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── mydjangoapp/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Implementation & Deployment

### 1. Linux Server Preparation

- Connected to Rocky Linux using PuTTY.
- Verified Python installation.
- Installed pip.
- Created a dedicated project directory.

### 2. Python Virtual Environment

Created and activated a virtual environment to isolate project dependencies.

```bash
python3 -m venv django-env
source django-env/bin/activate
```

Installed Django:

```bash
pip install django==4.2.30
```

### 3. Django Project Development

Created the Django project and application.

```bash
django-admin startproject mydjangoapp .
python manage.py startapp home
```

Configured the application in `INSTALLED_APPS`, developed a homepage using Django views, and configured URL routing.

### 4. Database Configuration

Used Django's default SQLite database and applied database migrations.

```bash
python manage.py migrate
```

### 5. Gunicorn Configuration

Installed Gunicorn to serve the Django application.

```bash
pip install gunicorn==23.0.0
```

Configured Gunicorn as a systemd service to run in the background and start automatically during system boot.

### 6. Nginx Configuration

Installed and configured Nginx as a reverse proxy.

- Configured Nginx to listen on port 80.
- Forwarded incoming requests to Gunicorn.
- Configured proxy headers.
- Verified Nginx configuration.

### 7. Firewall & SELinux Configuration

- Configured firewalld to allow HTTP traffic.
- Verified SELinux enforcement.
- Enabled `httpd_can_network_connect` to allow Nginx to communicate with Gunicorn.

### 8. Deployment Verification

Verified Gunicorn and Nginx services using systemd and tested the deployed application through a web browser.

## 🚀 Deployment Configuration

| Component | Configuration |
|---|---|
| Operating System | Rocky Linux 9.7 |
| Application Directory | `/opt/django-deployment` |
| Python Version | 3.9 |
| Django Version | 4.2.30 |
| Gunicorn Version | 23.0.0 |
| Gunicorn Binding | `127.0.0.1:8000` |
| Nginx HTTP Port | 80 |
| Database | SQLite |
| Service Manager | systemd |

### Application Access

```text
http://<SERVER-IP>/
```

## 📸 Application Preview

The deployed Django application displays:

**Welcome to My First Django Application!**

**Successfully Deployed on Linux Server**

Powered by Python and Django.

<!-- Add deployment screenshot here -->

## 📚 Key Learning Outcomes

Through this project, I gained hands-on experience in:

- Python and Django application development.
- Python package and virtual environment management.
- Django project structure and URL routing.
- Gunicorn application server configuration.
- Linux service management using systemd.
- Nginx reverse proxy configuration.
- Firewall management using firewalld.
- SELinux security configuration.
- Linux server troubleshooting.
- Python web application deployment.

## 👩‍💻 Author

**Aiswarya PS**

B.Tech Computer Science and Engineering

Interested in Linux Administration, Cloud Computing, DevOps, and Infrastructure Management.

---

<p align="center">
  ⭐ Thank you for visiting this project!
</p>
