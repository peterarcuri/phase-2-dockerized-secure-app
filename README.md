# Phase 2 — Dockerized Secure App

A secure, containerized Python application built as part of my DevSecOps Engineering portfolio.

This project focuses on Docker containerization, minimal image design, non-root execution, runtime hardening, vulnerability scanning, and CI/CD security automation.

---

## Objectives

- Package a Python web application using Docker
- Reduce container attack surface with a minimal base image
- Run the application as a non-root user
- Apply Docker runtime hardening controls
- Add automated tests
- Build a CI/CD security pipeline with GitHub Actions
- Scan the image for vulnerabilities using Docker Scout

---

## Tech Stack

- Python
- Flask
- Gunicorn
- Docker
- Docker Compose
- GitHub Actions
- Docker Scout
- Pytest

---

## Security Features

- Minimal Python slim base image
- Non-root container user
- Dropped Linux capabilities
- Read-only container filesystem
- No-new-privileges security option
- Healthcheck endpoint
- Automated test workflow
- Container vulnerability scanning

---

## Project Structure

```text
phase-2-dockerized-secure-app/
├── app/
├── tests/
├── docs/
├── config/
├── scripts/
├── screenshots/
├── sample-output/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md