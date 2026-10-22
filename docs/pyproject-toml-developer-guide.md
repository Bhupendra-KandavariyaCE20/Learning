# `pyproject.toml`: Developer Quick Guide

`pyproject.toml` is a standard configuration file for Python projects. It can define project metadata, dependencies, build settings, and tool configuration.

## 1. Where it lives

Usually in the project root:

```text
my-project/
├── pyproject.toml
├── .python-version
├── uv.lock
├── .venv/
├── src/
│   └── my_project/
│       └── __init__.py
└── tests/
```

- `pyproject.toml`: project metadata, dependency declarations, and tool settings.
- `uv.lock`: exact resolved dependency versions when using `uv`.
- `.python-version`: optional preferred Python version for tools such as `uv`.
- `.venv/`: local virtual environment; don't commit it.

## 2. Minimal example

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A short project description"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.32",
]

[dependency-groups]
dev = [
    "pytest",
    "ruff",
]
```

- `name`: package/project name.
- `version`: project version.
- `description`: short summary.
- `readme`: long description file.
- `requires-python`: Python versions your project supports.
- `dependencies`: runtime packages needed by the application/package.
- `[dependency-groups].dev`: development tools such as tests and linters.

Version constraints matter. `requests>=2.32` allows versions at or above that minimum; it does not pin one exact version. With `uv`, `uv.lock` records the resolved versions.

## 3. Runtime vs development dependencies

Runtime dependency:

```bash
uv add requests
```

Development dependencies:

```bash
uv add --dev pytest ruff
```

These commands update `pyproject.toml` and, for a `uv` project, the lockfile and environment as appropriate.

Synchronize the environment:

```bash
uv sync
```

Development dependency groups are included by default unless configured otherwise.

## 4. Common `uv` workflow

```bash
uv init my-project
cd my-project

uv add requests
uv add --dev pytest ruff

uv sync
uv run python main.py
uv run pytest
uv run ruff check .
uv tree
```

If you edit dependency declarations manually, run `uv lock` to update the lockfile and `uv sync` to apply the environment changes.

## 5. Build-system configuration

If your project is packaged for building/distribution, it may include:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- `requires`: packages needed to run the build backend.
- `build-backend`: Python object that performs the build.

The exact values depend on the packaging tool you choose. This section is not always needed for a simple script-only project.

## 6. Tool configuration

Developer tools can read their settings from `pyproject.toml`.

Ruff example:

```toml
[tool.ruff]
line-length = 88
```

Pytest example:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

Each tool has its own supported keys; consult its documentation.

## 7. `pyproject.toml` vs `uv.lock`

| File | Purpose | Commit to Git? |
|---|---|---|
| `pyproject.toml` | Project metadata, dependency requirements, tool settings | Yes |
| `uv.lock` | Exact resolved dependency versions for repeatable installs | Yes, for a `uv` project |
| `.venv/` | Installed environment files | No |
| `.python-version` | Preferred Python version | Usually yes, if the team agrees |

`pyproject.toml` describes what your project needs. `uv.lock` records the concrete dependency resolution.

## 8. Developer best practices

- Keep direct runtime dependencies in `[project].dependencies`.
- Put tests and code-quality tools in the `dev` dependency group.
- Set `requires-python` to the range your project actually supports.
- Commit `pyproject.toml` and `uv.lock` for `uv` projects.
- Add `.venv/`, Python caches, and secrets to `.gitignore`.
- Avoid manually editing `uv.lock`; use `uv add`, `uv remove`, or `uv lock`.
- After changing dependencies, run `uv lock` or `uv sync` as appropriate.
- Tool-specific settings belong under `[tool.<tool-name>]`.

## 9. Quick reference

```bash
uv init my-project
uv add requests
uv add --dev pytest ruff
uv remove requests
uv lock
uv sync
uv run python main.py
uv run pytest
uv tree
```

## Official references

- Python Packaging User Guide: <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>
- `pyproject.toml` specification: <https://packaging.python.org/en/latest/specifications/pyproject-toml/>
- `uv` projects: <https://docs.astral.sh/uv/guides/projects/>
