# Running Tests

## Basic command to run tests and check test coverage

From `rbc/`, run

```bash
pytest --cov=rbc --cov-report term-missing --log-level=20 -vv
```

## Exclude files from coverage

In the `.coveragerc` file, `templates.py` files are excluded from test coverage.
Add other files here to exclude them from test coverage.

```coverage
omit =
    */templates.py
    [ADD OTHER FILE NAMES HERE]
```
