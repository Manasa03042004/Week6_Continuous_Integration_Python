# CI Verification Record

Repository: https://github.com/Manasa03042004/Week6_Continuous_Integration_Python

Verified workflow run: https://github.com/Manasa03042004/Week6_Continuous_Integration_Python/actions/runs/38145463783

## Verified result

The GitHub Actions run completed successfully on 11 October 2026. The workflow checks pushes to every branch, pull requests targeting `main`, and manual runs. Each matrix job uses Node.js 24-compatible official action releases and executes a Python compile/build check, Ruff lint, pytest, and report upload.

| Matrix job | Build/compile | Ruff lint | pytest | Report artifact | Job result |
|---|---|---|---|---|---|
| Python 3.10 | Passed | Passed — `All checks passed!` | 16 passed in 0.04s | `test-report-python-3.10` uploaded | Success |
| Python 3.11 | Passed | Passed — `All checks passed!` | 16 passed in 0.02s | `test-report-python-3.11` uploaded | Success |
| Python 3.12 | Passed | Passed — `All checks passed!` | 16 passed in 0.02s | `test-report-python-3.12` uploaded | Success |

The workflow compiles `app.py` and the `tests` directory with `python -m compileall -q app.py tests`, runs Ruff, executes pytest while generating `test-results.xml`, and uploads the XML report. The build, lint, and test steps do not use `continue-on-error`, so their failures fail the job. Reports are configured to remain available as Actions artifacts for 14 days.

## How to inspect the evidence

1. Open the [verified GitHub Actions run](https://github.com/Manasa03042004/Week6_Continuous_Integration_Python/actions/runs/38145463783).
2. Expand each Python matrix job and inspect the compile, Ruff, and pytest step logs.
3. Under **Artifacts**, download the test report for each Python version and open `test-results.xml`.

The project ZIP includes copies of the three generated XML reports in the `reports/` folder. This record reflects the results for the linked workflow run and is not a substitute for rerunning the pipeline after future code changes.
