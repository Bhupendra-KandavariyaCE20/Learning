# Python Developer Tutorial: `unittest`, `pytest`, `argparse`, and `logging`

A practical guide to four useful Python tools:

- `unittest`: built-in testing framework.
- `pytest`: popular third-party testing framework.
- `argparse`: built-in command-line argument parser.
- `logging`: built-in application logging system.

Examples work with Python 3.10+ unless stated otherwise.

## 1. `unittest`: Test your code

`unittest` is included in Python. It helps you check that functions behave as expected.

`calculator.py`:

```python
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Create `test_calculator.py`:

```python
import unittest
from calculator import add, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
```

Run tests:

```bash
python -m unittest -v
```

Important assertions:

- `self.assertEqual(a, b)`: values should be equal.
- `self.assertTrue(condition)` / `self.assertFalse(condition)`: check a Boolean condition.
- `self.assertIsNone(value)`: check for `None`.
- `self.assertRaises(Error)`: check that code raises an expected exception.

Test discovery normally looks for files named `test*.py`. Keep tests in discoverable locations and use test names beginning with `test`.

## 2. `pytest`: Write concise tests

`pytest` is a third-party testing framework with simple assertions, fixtures, parameterized tests, and support for many `unittest` tests.

Install it in a `uv` project:

```bash
uv add --dev pytest
```

Or with pip inside the intended virtual environment:

```bash
python -m pip install pytest
```

Using the same `calculator.py`, write `test_calculator.py`:

```python
import pytest
from calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Run:

```bash
pytest
# In a uv-managed project:
uv run pytest
```

### Parameterized tests

Use one test function with multiple sets of inputs:

```python
import pytest
from calculator import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, 5, 3),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Fixtures

A fixture provides reusable setup or test data:

```python
import pytest


@pytest.fixture
def sample_numbers():
    return [10, 20, 30]


def test_sum(sample_numbers):
    assert sum(sample_numbers) == 60
```

Pytest supplies the fixture to a test when the test requests it by name.

### Useful pytest commands

```bash
pytest                  # Run discovered tests
pytest -v               # Verbose output
pytest tests/           # Run tests in a directory
pytest -k "divide"      # Run tests whose names match an expression
pytest --maxfail=1      # Stop after the first failure
```

### `unittest` vs `pytest`

| | `unittest` | `pytest` |
|---|---|---|
| Included with Python | Yes | No |
| Typical style | Classes and `TestCase` | Plain test functions |
| Assertions | `self.assertEqual(...)` | `assert ...` |
| Parameterization | `subTest` or other patterns | `pytest.mark.parametrize` |
| Fixtures | `setUp` / `tearDown` | Fixture system |

**Guideline:** Know both; pytest is a convenient default for many new projects.

## 3. `argparse`: Accept command-line arguments

`argparse` lets users pass input and options from the terminal instead of hardcoding values.

Create `greet.py`:

```python
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Greet someone from the command line"
    )
    parser.add_argument("name", help="Person's name")
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of greetings (default: 1)",
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count must be at least 1")

    for _ in range(args.count):
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
```

Run:

```bash
python greet.py Alice
python greet.py Alice --count 3
python greet.py --help
```

- `ArgumentParser(...)`: defines the CLI parser and help description.
- `add_argument("name")`: required positional argument.
- `add_argument("--count", ...)`: optional flag.
- `type=int`: converts the input to an integer.
- `default=1`: value used if the option is omitted.
- `parse_args()`: parses the command line.
- `parser.error(...)`: displays a CLI error and exits.

### Common argument patterns

Boolean flag:

```python
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output",
)
```

Restrict allowed values:

```python
parser.add_argument(
    "--format",
    choices=["json", "csv"],
    default="json",
)
```

Make an optional flag mandatory:

```python
parser.add_argument("--token", required=True)
```

Avoid putting secrets such as API tokens directly on the command line when they may be saved in shell history or exposed in process listings. Prefer environment variables or a secret manager for sensitive values.

## 4. `logging`: Record application events

`logging` is built into Python. Compared with `print()`, it supports severity levels, timestamps, log destinations, and exception tracebacks.

### Logging levels

From lowest to highest severity:

1. `DEBUG`: detailed diagnostic information.
2. `INFO`: normal application events.
3. `WARNING`: something unexpected, but the program can continue.
4. `ERROR`: an operation failed.
5. `CRITICAL`: a severe failure.

### Basic example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Detailed diagnostic information")
logging.info("Application started")
logging.warning("Retrying request")
logging.error("Could not process file")
logging.critical("Service cannot continue")
```

At `INFO` level, `DEBUG` messages are hidden.

### Use a named logger and write to a file

```python
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def read_file(filename: str) -> str | None:
    logger.info("Reading file: %s", filename)

    try:
        content = Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.exception("File not found: %s", filename)
        return None

    logger.info("File read successfully")
    return content


if __name__ == "__main__":
    content = read_file("data.txt")
    if content is not None:
        print(content)
```

This sends logs to both the terminal and `app.log`.

- `logging.basicConfig(...)`: configures the root logging system; usually configure once near the application entry point.
- `level`: minimum severity to emit.
- `format`: controls the log message format.
- `FileHandler`: writes logs to a file.
- `StreamHandler`: writes logs to a stream, usually the terminal.
- `logging.getLogger(__name__)`: creates a logger named after the current module.
- `logger.exception(...)`: logs the message and current exception traceback; call it inside an exception handler.

Use lazy formatting:

```python
logger.info("Processed %s records", count)
```

Avoid logging passwords, API keys, tokens, or sensitive personal data. Libraries should generally use named loggers and leave global logging configuration to the application.

## 5. Combine them in a small CLI

This example uses `argparse` for input and `logging` for progress/errors. The calculation function is easy to test with pytest or unittest.

`calculator_cli.py`:

```python
import argparse
import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    return a + b


def main():
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show informational logs",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    logger.info("Adding numbers")
    print(add(args.a, args.b))


if __name__ == "__main__":
    main()
```

Run:

```bash
python calculator_cli.py 10 5
python calculator_cli.py 10 5 --verbose
```

`test_calculator_cli.py`:

```python
from calculator_cli import add


def test_add():
    assert add(10, 5) == 15


def test_add_negative():
    assert add(-2, 5) == 3
```

Run tests with:

```bash
pytest
```

Or, if using `uv`:

```bash
uv add --dev pytest ruff
uv run pytest
uv run ruff check .
```

## 6. Recommended project layout

```text
my-project/
├── pyproject.toml
├── calculator_cli.py
├── calculator.py
└── tests/
    └── test_calculator.py
```

For a `uv` project, install development tools with:

```bash
uv add --dev pytest ruff
```

`argparse`, `logging`, and `unittest` are included in Python; they don't need installing.

## 7. Best practices checklist

- Write tests for normal cases, edge cases, and expected errors.
- Keep tests independent and deterministic.
- Use pytest fixtures for reusable setup and parameterization for multiple inputs.
- Use `argparse` rather than manually parsing `sys.argv`.
- Provide helpful argument descriptions and validate values.
- Use logging levels appropriately and include useful context.
- Configure logging once in the application entry point.
- Never log secrets.
- Keep business logic in functions so it is easy to test separately from CLI code.

## Official documentation

- `unittest`: <https://docs.python.org/3/library/unittest.html>
- `pytest`: <https://docs.pytest.org/>
- `argparse`: <https://docs.python.org/3/library/argparse.html>
- `logging`: <https://docs.python.org/3/library/logging.html>
