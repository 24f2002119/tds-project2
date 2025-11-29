# TDS Sep 2025 – LLM Analysis Quiz Solver

## Project Structure
tds-llm-analysis-quiz/
│
├── app/
│   ├── main.py
│   ├── solver.py
│   ├── browser.py
│   ├── submit.py
│   └── utils/
│       ├── parser.py
│       ├── analysis.py
│       └── viz.py
│
├── tests/
│   ├── test_endpoint.py
│   └── test_solver.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE

This repo contains a FastAPI-based server that:
- Verifies email + secret
- Loads quiz pages with JavaScript (Playwright)
- Parses instructions and files
- Performs data extraction, PDF/CSV parsing, analysis, visualization
- Submits answer to the provided endpoint
- Follows the 3-minute window requirement
- Supports chained quizzes

## Run locally
pip install -r requirements.txt
playwright install
uvicorn app.main:app --reload

## Environment
export TDS_SECRET="your-secret-here"

## Endpoint
POST http://localhost:8000/
