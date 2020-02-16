# Running Tests

## Basic command to run tests and check test coverage

From `rbc/`, run

```bash
pytest --cov=rbc --cov-report term-missing --log-level=20 -vv
```

## Exclude files from coverage

In the `.coveragerc` file, `template.py` files are excluded from test coverage.
Add other files here to exclude

```coverage
omit =
    */templates.py
    [ADD OTHER FILE NAMES HERE]
```
