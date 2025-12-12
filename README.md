# FastAPI CI/CD Project

## 📌 Overview
This project is a **production-grade FastAPI microservice** showcasing **DevOps best practices**:
- REST API built with FastAPI
- Metrics and observability via Prometheus
- Automated CI/CD pipeline using GitHub Actions
- Security and quality checks integrated into the workflow
- Containerization with Docker and optional orchestration via Compose

---

## ✅ Features
- **Endpoints** for health checks, version info, statistical computations, and prime factorization
- **Prometheus metrics** exposed at `/metrics`
- **CI/CD pipeline** with linting, type checks, tests, coverage, and security scans
- **Docker image** build and push to GitHub Container Registry (GHCR) on tags
- **Smoke tests** for container validation

---

## 🏗 Architecture (Text-Based)
```
[Client] --> [FastAPI App] --> [Prometheus Metrics]
           |--> [CI/CD Pipeline: GitHub Actions]
           |--> [Docker Image Build & Push]
```

---

## 🔄 CI/CD Workflow
- **Triggers**: Push to `main`, Pull Requests, Tags (`v*`)
- **Jobs**:
  - **Quality**: Lint (ruff), Format (black), Type-check (mypy), Tests (pytest), Coverage, Security (bandit, pip-audit)
  - **Build Container**: Docker image build and push to GHCR on tags
  - **Smoke Test**: Validate container health endpoint

---

## 🔗 API Endpoints
| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| GET    | `/health`                | Health check                        |
| GET    | `/version`               | App name, version, environment      |
| POST   | `/compute/stats`         | Compute mean, median, stdev         |
| GET    | `/compute/factors/{n}`   | Prime factorization of integer      |

### Example Request
```bash
curl -X POST http://localhost:8000/compute/stats      -H "Content-Type: application/json"      -d '{"values": [1, 2, 3, 4]}'
```

### Example Response
```json
{
  "count": 4.0,
  "mean": 2.5,
  "median": 2.5,
  "stdev": 1.2909944487
}
```

---

## 🛠 How to Run This Project

### ▶️ Run Locally
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000
```
Access API at: `http://localhost:8000/docs`

Run tests:
```bash
pytest --cov=app
```

---

### 🐳 Run with Docker
```bash
docker compose up --build
# App: http://localhost:8000/docs
# Prometheus: http://localhost:9090
```

---

### 💻 Run in GitHub Codespaces
1. Open your repo → **Code** → **Open with Codespaces** → **New codespace**.
2. Wait for the environment to build using `.devcontainer/devcontainer.json`.
3. Run the app:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Access: `https://<your-codespace>.github.dev/docs`

Run tests:
```bash
pytest --cov=app
```

---

### 🧭 Run via GitHub UI (no CLI)
1. **Create a repository** on GitHub.
2. **Upload files**: Repo → *Add file* → *Upload files* → drag-drop the project ZIP contents.
3. **Enable Actions**: Go to the *Actions* tab. GitHub will detect `.github/workflows/ci.yml`. Enable if prompted.
4. **Trigger CI**: Any push/PR runs the pipeline.
5. **Publish container (optional)**: *Releases* → *Draft a new release* → tag `v1.0.0` → publish.
6. **Inspect results**: *Actions* → open the latest run → view logs, coverage artifact, and Docker build output.

---

## 📈 Metrics & Observability
- Prometheus metrics available at `/metrics`
- Ready for integration with Grafana dashboards

---

## 🔐 Security & Quality Checks
- **Static Analysis**: Bandit
- **Dependency Audit**: pip-audit
- **Type Safety**: mypy
- **Code Style**: black, ruff

---

## 🤝 How to Contribute
1. Fork the repository
2. Create a feature branch
3. Commit changes with clear messages
4. Submit a Pull Request

---

## 🏷 Badges (Add after CI runs)
```
![CI](https://github.com/<your-username>/<repo-name>/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/<your-username>/<repo-name>)
```

---

## ▶️ Open in GitHub Codespaces
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/<your-username>/<repo-name>)
