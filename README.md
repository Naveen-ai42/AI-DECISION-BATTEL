# Decision Arena

Decision Arena compares options across user priorities and category-specific factors. It includes a React/Vite frontend and a FastAPI backend for candidate scoring and rankings.

Repository: https://github.com/Naveen-ai42/AI-DECISION-BATTEL

## Features

- Decision flows for electronics, vehicles, finance, career, education, travel, shopping, and general decisions
- Category-specific factors and ranked recommendations
- Use-case leaderboards for phones and laptops, plus factor rankings for other categories
- Saved decision history and owner reviews stored in the current browser
- Demo candidate catalogs for local evaluation

> Candidate catalogs and scores are demo data. Recommendations are informational and are not professional financial, legal, or safety advice.

## Requirements

- Node.js and npm
- Python 3.10 or newer

## Run locally

Open two PowerShell terminals from the repository folder.

### Backend

```powershell
Set-Location backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run_server.py
```

The API runs at `http://127.0.0.1:8001`. Interactive API documentation is available at `http://127.0.0.1:8001/docs`.

### Frontend

```powershell
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`. If that port is busy, Vite selects another available port.

## Checks

From the repository folder:

```powershell
npm run build
npm run lint
```

Run backend tests from the `backend` folder:

```powershell
Set-Location backend
.\.venv\Scripts\python.exe -m pytest -q --ignore=test_http_live.py
```

The live HTTP test requires the backend server to be running.
