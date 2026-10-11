# CI Verification Record

Repository: https://github.com/Manasa03042004/Week6_Continuous_Integration_Python

Verified workflow run: https://github.com/Manasa03042004/Week6_Continuous_Integration_Python/actions/runs/38144782869

## Verified result

The GitHub Actions run completed successfully on 11 October 2026 with the Node.js 24-compatible official action versions and the workflow configured to validate pushes to every branch.

| Matrix job | Ruff lint | pytest | Report artifact | Job result |
|---|---|---|---|---|
| Python 3.10 | Passed — `All checks passed!` | 16 passed | `test-report-python-3.10` uploaded | Success |
| Python 3.11 | Passed — `All checks passed!` | 16 passed | `test-report-python-3.11` uploaded | Success |
| Python 3.12 | Passed — `All checks passed!` | 16 passed | `test-report-python-3.12` uploaded | Success |

The workflow runs Ruff, executes pytest while generating `test-results.xml`, and uploads that XML file as an artifact. The lint and test steps do not use `continue-on-error`, so a lint error or failing test produces a failed job. Artifacts are configured to remain available for 14 days.

## How to inspect the evidence

1. Open the [verified GitHub Actions run](https://github.com/Manasa03042004/Week6_Continuous_Integration_Python/actions/runs/38144782869).
2. Expand each Python matrix job and inspect the Ruff and pytest step logs.
3. Under **Artifacts**, download the test report for each Python version and open `test-results.xml`.

The project ZIP also includes copies of the three generated XML reports in the `reports/` folder. This record reflects the results for the linked workflow run and is not a substitute for rerunning the pipeline after future code changes.
