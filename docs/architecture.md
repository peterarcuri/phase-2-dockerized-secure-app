# Architecture Overview

## Project Purpose

The Dockerized Secure App demonstrates secure application containerization practices commonly used in modern DevSecOps environments.

The project combines:

* Python web application development
* Docker containerization
* Container hardening
* Vulnerability scanning
* Dockerfile linting
* CI/CD automation

---

## High-Level Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions Pipeline
    ├── Pytest
    ├── Hadolint
    ├── Docker Build
    └── Trivy Scan
    │
    ▼
Docker Image
    │
    ▼
Docker Container
    │
    ▼
Flask Application
```

---

## Application Layer

The application consists of a lightweight Flask API.

Endpoints:

### Root Endpoint

```http
GET /
```

Returns application information and security features.

### Health Endpoint

```http
GET /health
```

Used for container health verification.

---

## Container Layer

The application is packaged using Docker.

Security measures include:

* Minimal Python Slim base image
* Non-root execution
* Read-only filesystem
* Dropped Linux capabilities
* No-new-privileges enforcement

---

## CI/CD Layer

GitHub Actions automatically performs:

1. Dependency installation
2. Automated testing
3. Dockerfile linting
4. Docker image creation
5. Vulnerability scanning

---

## Security Tooling

### Hadolint

Dockerfile linting and best-practice validation.

### Trivy

Container vulnerability scanning.

Scans:

* Operating system packages
* Python dependencies
* Container image layers

---

## Future Enhancements

* Multi-stage Docker builds
* SBOM generation
* Cosign image signing
* Kubernetes deployment
* Admission controller validation
* Security policy enforcement
