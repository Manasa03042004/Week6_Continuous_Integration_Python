# Week 6 CI Documentation

## 1. Objective

The objective is to integrate a Continuous Integration (CI) pipeline into a Python project. The pipeline automatically checks code quality, executes automated tests, and publishes a test report. It is intended to make code changes easier to validate and to fail visibly when code does not meet the configured checks.

## 2. Selected CI tool

**GitHub Actions** is used because it is integrated into GitHub repositories and supports workflow definitions stored as YAML files. The workflow is located at:

```text
.github/workflows/ci.yml
```

The workflow has three triggers:

- `push` to any branch
- `pull_request` targeting `main`
- `workflow_dispatch` for manual runs from the Actions page

## 3. Project and toolchain

- **Python 3.10, 3.11, and 3.12:** CI runtime matrix.
- **Ruff:** linter and basic code-quality checker.
- **pytest:** automated test runner.
- **JUnit XML:** portable machine-readable test report.
- **GitHub Actions artifacts:** downloadable storage for test reports.
- **Git:** version control and trigger for push-based CI.

The sample Python application is a small calculator. Its simplicity helps isolate the CI concepts instead of introducing unrelated application setup.

## 4. Pipeline stages

### Stage 1 — Checkout source code

The `actions/checkout` step makes the repository source available to the runner.

### Stage 2 — Configure Python

The `actions/setup-python` step installs the Python version requested by the matrix. The workflow runs the same checks on Python 3.10, 3.11, and 3.12 to detect version-related incompatibilities.

### Stage 3 — Install dependencies

The runner updates pip and installs the packages declared in `requirements.txt`. The dependency list contains pytest and Ruff.

### Stage 4 — Lint

The command is:

```bash
python -m ruff check .
```

Ruff checks Python source and test files according to `ruff.toml`. Any lint error returns a non-zero exit code, causing the workflow job to fail.

### Stage 5 — Test and generate report

The command is:

```bash
python -m pytest --junitxml=test-results.xml
```

pytest discovers tests in the `tests` directory. It returns a non-zero exit code when tests fail and writes test results to JUnit XML when it reaches report generation.

### Stage 6 — Publish the report

The `actions/upload-artifact` step stores `test-results.xml` as an artifact named for its Python version. The step uses `if: always()` so the upload is attempted even if an earlier step failed. If tests fail before writing the XML report, GitHub displays a warning because the report file may not exist.

## 5. Why the pipeline fails on errors

GitHub Actions treats a run step that exits with a non-zero code as failed by default. The lint and test steps do not use `continue-on-error`, so a Ruff finding or a failing pytest assertion makes the matrix job fail. Test reporting is separate from the test exit code and does not turn a failed test run into a successful one.

With a three-version matrix, each Python version has an independent job. The overall workflow is successful only when the required matrix jobs are successful; a failure in a version's lint or test steps remains visible.

## 6. Replicate the environment locally

### Windows PowerShell

```powershell
git clone https://github.com/Manasa03042004/Week6_Continuous_Integration_Python.git
cd Week6_Continuous_Integration_Python
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run the sample program
python app.py

# Run linting
python -m ruff check .

# Run tests and create a local JUnit XML report
python -m pytest --junitxml=test-results.xml
```

If PowerShell blocks virtual-environment activation due to execution policy, use a permitted shell or activate the environment through the VS Code interpreter selector. Do not change the machine-wide execution policy just for this project.

### macOS / Linux

```bash
git clone https://github.com/Manasa03042004/Week6_Continuous_Integration_Python.git
cd Week6_Continuous_Integration_Python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
python -m ruff check .
python -m pytest --junitxml=test-results.xml
```

## 7. How to trigger and view a CI run

1. Make a small change, for example update a docstring in `app.py`.
2. Save the change and commit it.
3. Push the commit to any branch, or open a pull request targeting `main`.
4. Open the repository on GitHub and select **Actions**.
5. Open the latest **Python CI** run.
6. Inspect the job for each Python version. Each step can be expanded to see its logs.
7. Download the test report from the run's artifact section.

A manual run can also be started from **Actions → Python CI → Run workflow** because the workflow includes `workflow_dispatch`.

## 8. Test report details

The generated `test-results.xml` follows the JUnit XML format. It includes suite/test-case details and failure information. It can be consumed by a range of CI reporting tools and integrated into later reporting dashboards.

The repository's current test suite covers:
- Addition with positive, negative, zero, and floating-point values.
- Subtraction with different operand orders.
- Multiplication with positive, negative, and floating-point values.
- Division for integer and floating-point results.
- Expected exceptions when the denominator is zero.

## 9. Troubleshooting

| Issue | Suggested fix |
|---|---|
| `ModuleNotFoundError: pytest` or `ruff` | Activate the project's virtual environment, then run `python -m pip install -r requirements.txt`. |
| Ruff fails in CI | Open the Ruff step log, fix the reported file/line, and run `python -m ruff check .` locally. |
| A pytest test fails | Read the assertion and traceback in the pytest step; reproduce with `python -m pytest -q`. |
| No Actions run appears | Confirm workflow is committed under `.github/workflows/ci.yml`, the branch is `main`, and the event matches a workflow trigger. |
| Test report artifact is absent | Inspect the pytest step first; a runner interruption before XML creation or a missing report file may prevent an artifact. |
| Workflow fails on one Python version | Inspect that matrix job's log; fix compatibility issues and rerun after committing. |

## 10. Challenges considered

- **Dependency consistency:** both local and CI runs install from `requirements.txt`.
- **Repeatable tests:** pytest tests use fixed inputs and do not depend on network services or external credentials.
- **Version compatibility:** a matrix checks the same code across multiple supported Python versions.
- **Failure visibility:** lint and test commands retain their non-zero exit codes, so errors are not silently ignored.
- **Report availability:** the artifact step runs with `if: always()` and warns if no report was created.

These are the main setup considerations addressed by the project. Document any additional issues observed during your actual run instead of reporting hypothetical problems as if they occurred.

## 11. Verification checklist

Only tick items after you have verified them in your local environment or in GitHub Actions.

- [ ] Dependencies installed successfully.
- [ ] `python -m ruff check .` passed locally.
- [ ] `python -m pytest --junitxml=test-results.xml` passed locally.
- [ ] A commit or manual dispatch triggered GitHub Actions.
- [ ] All Python matrix jobs passed.
- [ ] The test report artifact was uploaded and downloaded.
- [ ] Logs or screenshots were saved for submission.

## 12. Conclusion

This project demonstrates how a CI pipeline improves feedback and consistency by automatically linting code, running tests, and preserving a test report. It runs on every branch push and on pull requests targeting the main branch, with an optional manual trigger. The lint and test steps can fail the build, providing a repeatable quality gate for future changes.
