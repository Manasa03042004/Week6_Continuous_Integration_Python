# Week 6 — Integrating Continuous Integration (CI) in Python Projects

A beginner-friendly Python project demonstrating how to use **GitHub Actions** to automate linting, testing, and test-report publication on every branch push and on pull requests targeting `main`.

## Project overview

This repository contains a small calculator module. The application itself is intentionally simple so the focus remains on the CI workflow and development-quality checks.

### CI capabilities

- Runs automatically on pushes to `main` and pull requests targeting `main`.
- Supports manual execution with **Actions → Python CI → Run workflow**.
- Checks code quality with Ruff.
- Runs automated tests with pytest.
- Generates a JUnit XML test report.
- Uploads the test report as a downloadable Actions artifact even when checks fail, if a report was produced.
- Executes the workflow on Python 3.10, 3.11, and 3.12.
- Fails the job if linting or tests fail.

## Repository structure

```text
Week6_Continuous_Integration_Python/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_app.py
├── .gitignore
├── app.py
├── pytest.ini
├── requirements.txt
├── ruff.toml
├── CI_DOCUMENTATION.md
├── CI_VERIFICATION.md
└── README.md
```

## Run locally (Windows PowerShell)

```powershell
git clone https://github.com/Manasa03042004/Week6_Continuous_Integration_Python.git
cd Week6_Continuous_Integration_Python

py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python app.py
python -m ruff check .
python -m pytest --junitxml=test-results.xml
```

On macOS/Linux, create and activate a virtual environment using `python3 -m venv .venv` and `source .venv/bin/activate`. The remaining pip and validation commands are the same.

## View CI runs and reports

1. Open the repository on GitHub and choose **Actions**.
2. Select **Python CI** and open a run.
3. Open the matrix job for the Python version you want to inspect.
4. Read each step's log. A failed lint or test step marks the job as failed.
5. Under the run's **Artifacts** section, download the corresponding `test-report-python-3.x` artifact and inspect `test-results.xml`.

## CI status

The workflow definition is committed at `.github/workflows/ci.yml`. Use the Actions tab to confirm the latest run's status after each push. The documentation deliberately does not hard-code a success claim; record the result shown by GitHub for the actual run.

## Learning outcomes

This project demonstrates continuous integration, automated quality checks, repeatable Python environments, test reporting, matrix testing across Python versions, and troubleshooting through CI logs.

See [CI_DOCUMENTATION.md](CI_DOCUMENTATION.md) for the full setup, workflow explanation, verification checklist, and troubleshooting guide.
