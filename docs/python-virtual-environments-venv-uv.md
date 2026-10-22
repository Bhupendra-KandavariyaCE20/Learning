# Python Virtual Environments: `venv` and `uv`

A practical guide to isolated Python environments, dependency management, reproducibility, and common workflows. This guide covers Python's built-in `venv` and the `uv` tool; it does not cover Conda.

## 1. Why use a virtual environment?

A virtual environment gives a project its own Python packages, separate from other projects and (usually) the system Python.

Benefits:
- Avoid dependency/version conflicts between projects.
- Keep system Python packages untouched.
- Make project setup reproducible for teammates and CI.
- Install packages without needing system-wide permissions.

Example: Project A can use Django 4 while Project B uses Django 5.

## 2. Key concepts

- **Interpreter**: the Python executable running your code.
- **Package**: installable code, usually from PyPI.
- **Dependency**: a package your project needs.
- **Environment**: an interpreter plus an isolated set of installed packages.
- **`pyproject.toml`**: modern project configuration and dependency metadata.
- **Lockfile**: records exact resolved dependency versions for repeatable installs.
- **PyPI**: the Python Package Index, a common package source.
- **Activation**: adjusts the shell's `PATH` so `python` and `pip` point to the environment. Activation is convenient, not strictly required.

## 3. Check your Python installation

```bash
python3 --version
which python3
python3 -m pip --version
```

If `pip` is unavailable on Ubuntu, install the distribution package required by your Python installation (often `python3-pip`). For `venv`, Ubuntu may require a matching `python3-venv` package:

```bash
sudo apt update
sudo apt install python3-venv python3-pip
```

Avoid replacing or deleting the system-managed Python installation.

## 4. Built-in `venv` workflow

### Create a project and environment

```bash
mkdir my-project
cd my-project
python3 -m venv .venv
```

`.venv` is a common environment directory name. It is local to the project and should not be committed to Git.

### Activate it

Linux / macOS (Bash or Zsh):

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

After activation, your shell prompt may show `(.venv)`.

### Verify the environment

```bash
which python
python --version
python -m pip --version
python -c "import sys; print(sys.executable)"
```

The executable path should point inside `.venv`.

### Install and inspect packages

```bash
python -m pip install requests
python -m pip list
python -m pip show requests
python -m pip freeze
```

Prefer `python -m pip` over bare `pip` to make clear which interpreter receives the packages.

### Save dependencies

For a simple pip-based project:

```bash
python -m pip freeze > requirements.txt
```

Install them later:

```bash
python -m pip install -r requirements.txt
```

`pip freeze` records installed packages; it is not always an ideal hand-maintained dependency specification. For applications, list direct dependencies intentionally, and use a lockfile/tooling when exact reproducibility matters.

### Deactivate

```bash
deactivate
```

This returns your shell to its previous Python selection.

## 5. `uv` overview

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager. It can manage Python versions, create environments, install dependencies, and maintain project metadata and a lockfile.

Install `uv` using the current official instructions: <https://docs.astral.sh/uv/getting-started/installation/>

Verify:

```bash
uv --version
```

## 6. Start a project with `uv`

### Create a project

```bash
uv init my-project
cd my-project
```

This creates a project structure and a `pyproject.toml`. Depending on the project type, it may also create a starter Python file.

### Choose a Python version (optional)

List available Python installations managed or discovered by `uv`:

```bash
uv python list
```

Install a version if needed:

```bash
uv python install 3.12
```

Use that version for the project when creating or syncing its environment:

```bash
uv python pin 3.12
uv sync
```

The pin is recorded in `.python-version`. Choose a Python version compatible with your project's dependencies and deployment target.

### Create/sync the environment

```bash
uv sync
```

For a project, `uv` normally creates `.venv` and installs the project dependencies. It also creates or updates `uv.lock`.

### Run code

```bash
uv run python main.py
```

`uv run` ensures the project's environment is synced before running the command. You often don't need to activate `.venv` manually.

## 7. Manage dependencies with `uv`

Add a runtime dependency:

```bash
uv add requests
```

Add a development dependency:

```bash
uv add --dev pytest ruff
```

Remove a dependency:

```bash
uv remove requests
```

Sync the environment from project metadata and lockfile:

```bash
uv sync
```

Run a tool in the project environment:

```bash
uv run pytest
uv run ruff check .
```

Inspect dependency information:

```bash
uv tree
uv lock
```

Key files:
- `pyproject.toml`: declared dependencies and project configuration.
- `uv.lock`: exact resolved dependency versions for reproducible installs.
- `.venv/`: local environment; do not commit it.
- `.python-version`: optional pinned Python version.

**Commit** `pyproject.toml` and `uv.lock` for an application when you want teammates and CI to use the same resolved dependencies. Do not commit `.venv/`.

## 8. `uv` without a managed project

For a quick script or an existing folder, create an environment directly:

```bash
uv venv .venv
uv pip install --python .venv/bin/python requests
```

Run the script with that interpreter:

```bash
.venv/bin/python script.py
```

You can also activate it:

```bash
source .venv/bin/activate
```

On Windows, the environment's Python executable is `.venv\Scripts\python.exe`.

For a project managed by `uv`, prefer `uv add` and `uv sync` instead of manually changing the environment with `uv pip install`, so dependency metadata and the lockfile remain consistent.

## 9. `venv` vs `uv`

| Need | Built-in `venv` + `pip` | `uv` |
|---|---|---|
| Create an environment | `python -m venv .venv` | `uv venv` or `uv sync` |
| Install packages | `python -m pip install ...` | `uv add ...` for projects; `uv pip install ...` for direct environment installs |
| Declare dependencies | Often `requirements.txt` | `pyproject.toml` |
| Lock resolved versions | Additional tooling/process may be needed | `uv.lock` |
| Manage Python versions | Install Python separately | `uv python install/list` |
| Run with environment synced | Activate and run | `uv run ...` |

**Rule of thumb:** `venv` plus `pip` is built-in and straightforward. `uv` provides an integrated, fast workflow for projects, dependency resolution, lockfiles, and Python version management.

## 10. Git and `.gitignore`

Add these entries to `.gitignore`:

```gitignore
# Virtual environments
.venv/
venv/
env/

# Python cache / compiled files
__pycache__/
*.py[cod]

# Environment variables and secrets
.env
.env.*

# Test / tooling caches
.pytest_cache/
.mypy_cache/
.ruff_cache/
```

If you intentionally need to track an example environment file, use a safe template such as `.env.example` with placeholder values and adjust ignore rules accordingly. Never commit secrets.

## 11. IDE setup (VS Code)

1. Open the project folder.
2. Install or enable the Python extension.
3. Use **Python: Select Interpreter** from the Command Palette.
4. Select the interpreter inside `.venv`.
5. Open a new terminal and verify `python -c "import sys; print(sys.executable)"`.

VS Code may detect `.venv` automatically. If not, select the interpreter manually.

## 12. Common problems

### `ModuleNotFoundError`

The package may be installed into a different interpreter.

```bash
python -c "import sys; print(sys.executable)"
python -m pip show PACKAGE_NAME
```

With `uv`, try:

```bash
uv run python -c "import sys; print(sys.executable)"
uv sync
```

### `python` points to the wrong version

Check `which python` (Linux/macOS) or `where python` (Windows). Activate the intended environment or run its interpreter directly.

### Activation is blocked in PowerShell

Use the documented PowerShell activation steps for your system's execution policy, or avoid activation and call `.venv\Scripts\python.exe` directly. Do not weaken machine-wide security settings casually.

### Environment was moved or copied

Virtual environments are generally not portable because they can contain absolute paths. Recreate it in the new location:

```bash
# pip workflow
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# uv project workflow
uv sync
```

### Dependency conflicts

- Review incompatible package requirements.
- Use a supported Python version.
- Update dependency constraints deliberately.
- With `uv`, inspect `uv tree` and use `uv lock` / `uv sync` after changing dependencies.

### Ubuntu says `ensurepip` is unavailable

Install the matching `python3-venv` system package, then recreate the environment.

## 13. Best practices

- Use one environment per project.
- Prefer `.venv/` in the project root.
- Never install project dependencies into system Python.
- Pin a compatible Python version for team projects and deployment.
- Declare direct dependencies rather than relying on accidental transitive packages.
- Commit dependency definitions and the lockfile; exclude the environment directory.
- Use `uv sync` / `uv run` consistently in `uv` projects.
- Keep secrets in environment variables or a secret manager, not source control.
- Recreate environments instead of copying them between machines.
- Test setup instructions in a clean environment or CI.

## 14. Quick reference

```bash
# Built-in venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install PACKAGE
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
deactivate

# uv project
uv init my-project
cd my-project
uv add PACKAGE
uv add --dev pytest
uv sync
uv run python main.py
uv run pytest
uv tree

# uv direct environment
uv venv .venv
uv pip install --python .venv/bin/python PACKAGE
.venv/bin/python script.py
```

## Official documentation

- Python `venv`: <https://docs.python.org/3/library/venv.html>
- Python Packaging User Guide: <https://packaging.python.org/>
- `uv` documentation: <https://docs.astral.sh/uv/>
