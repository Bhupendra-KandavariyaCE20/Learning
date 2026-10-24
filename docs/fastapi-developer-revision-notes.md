# FastAPI — Developer Revision Notes

FastAPI is a Python web framework for building HTTP APIs. It uses Python type hints, Pydantic for data validation, and Starlette for core web functionality. It generates OpenAPI documentation automatically.

## 1. Install and run

Using `uv`:

```bash
uv init my-api
cd my-api
uv add "fastapi[standard]"
uv add --dev pytest httpx ruff

uv run fastapi dev main.py
uv run pytest
uv run ruff check .
```

- Development docs: `http://127.0.0.1:8000/docs`
- Alternative docs: `http://127.0.0.1:8000/redoc`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

## 2. Minimal application

```python
from fastapi import FastAPI

app = FastAPI(title="Example API")


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
```

Run with `uv run fastapi dev main.py`.

- `app = FastAPI()` creates the application.
- `@app.get(...)` registers an endpoint for GET requests.
- Type hints help FastAPI parse and validate input.
- Returned dictionaries are serialized to JSON.

## 3. HTTP methods and parameters

| Method | Typical use |
|---|---|
| `GET` | Read data |
| `POST` | Create or submit data |
| `PUT` | Replace a resource |
| `PATCH` | Partially update a resource |
| `DELETE` | Delete a resource |

Path parameter — identifies a resource:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Query parameter — filters or configures a request:

```python
@app.get("/products")
def products(category: str, limit: int = 10):
    return {"category": category, "limit": limit}
```

Example: `/products?category=books&limit=5`.

## 4. Request bodies and Pydantic

Use Pydantic models for structured request data:

```python
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


@app.post("/products")
def create_product(product: ProductCreate):
    return product
```

Pydantic validates types and declared constraints. Validation does not replace business rules, authorization, or database constraints.

## 5. Response models and status codes

```python
from pydantic import BaseModel
from fastapi import status


class UserResponse(BaseModel):
    id: int
    name: str


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice", "internal_note": "hidden"}
```

The response model defines the public response shape and filters undeclared fields by default.

Set a status code:

```python
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "Created"}
```

Common codes: `200` success, `201` created, `204` no content, `400` bad request, `401` unauthenticated, `403` forbidden, `404` not found, `409` conflict, `422` request validation error, `500` server error.

Raise intentional HTTP errors:

```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="User not found")
```

## 6. `def` vs `async def`

- Use `async def` with async-compatible I/O libraries and `await`.
- Ordinary `def` path operations run in a thread pool, useful for synchronous blocking I/O.
- Do not call blocking operations such as `time.sleep()` directly inside `async def`; use async equivalents such as `await asyncio.sleep()`.
- `async` does not make CPU-heavy work automatically faster. Use suitable workers/processes or a separate inference service for expensive work.

## 7. Dependency injection

`Depends` provides reusable logic/resources such as authentication checks, settings, and database sessions.

```python
from typing import Annotated
from fastapi import Depends


def get_current_user():
    # Demo only — not real authentication.
    return {"id": 1, "name": "Alice"}


@app.get("/profile")
def profile(
    user: Annotated[dict, Depends(get_current_user)],
):
    return user
```

In production, validate credentials and authorization. A hardcoded user is not authentication. Use `yield` dependencies when a resource needs cleanup, such as a database session.

## 8. Authentication and security

Know the difference:

- **Authentication:** Who is the caller?
- **Authorization:** What is the caller allowed to do?
- **OAuth2:** Authorization framework commonly used with access tokens.
- **JWT:** Token format; it must be validated, not merely decoded.
- **API key:** Credential often used for service-to-service access.
- **HTTPS:** Encrypts data in transit.

FastAPI provides security utilities, but you must implement/choose proper token validation, expiry checks, permissions, secret storage, and HTTPS. Never log or commit passwords, API keys, or tokens.

## 9. Database integration

FastAPI does not require a specific database. Common choices include PostgreSQL/MySQL with SQLAlchemy, SQLModel, or suitable database drivers.

Typical request flow:

`Request → route → validation/auth → service/business logic → repository/database → response`

Developer essentials:
- Manage database sessions and connection pools correctly.
- Use transactions where needed.
- Use migrations for schema changes.
- Avoid creating a new connection pool per request.
- Use parameterized queries/ORM APIs; never concatenate untrusted input into SQL.
- Test database behavior and failure cases.

## 10. Routers and project structure

Use `APIRouter` to group related endpoints:

```python
# app/api/routes.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Register it:

```python
# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()
app.include_router(router)
```

A growing project might use:

```text
app/
├── main.py
├── api/            # Routes/endpoints
├── schemas/        # Request/response models
├── services/       # Business logic
├── repositories/   # Data access
├── db/             # Sessions and database setup
└── core/           # Settings and security
tests/
```

Start simple; add layers when they make responsibilities clearer.

## 11. Middleware and CORS

Middleware can run around requests/responses for timing, tracing, or cross-cutting behavior.

CORS controls which browser origins can make cross-origin requests. Configure explicit trusted origins where possible. Avoid wildcard origins with credentials.

**CORS is not authentication**; non-browser clients can still call the API.

## 12. Background tasks

`BackgroundTasks` can run small tasks after a response, such as a lightweight notification. It is not a durable queue.

Use a dedicated worker/queue for long-running or important jobs such as model training, large document ingestion, or lengthy AI-agent tasks. In-process tasks may be lost if the process stops.

## 13. Testing

Install test tools:

```bash
uv add --dev pytest httpx
```

Example `test_main.py`:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
```

Run `uv run pytest`.

Test success cases, invalid input, error codes, authentication/authorization, and edge cases. Override dependencies or mock external services to keep tests reliable.

## 14. AI/ML API patterns

Common endpoints:
- `POST /predict` — model inference.
- `POST /chat` — LLM request.
- `POST /documents` — ingest a document.
- `POST /search` — RAG retrieval.
- `GET /health` — health check.

For model serving:
- Load models once per worker/process, not per request.
- Validate the model's expected input shape and ranges.
- Measure latency, memory use, and throughput.
- Use separate workers/services for expensive CPU/GPU inference when needed.
- Set timeouts and handle upstream API failures.
- Protect expensive endpoints with authentication, quotas, and rate limits.

## 15. Deployment checklist

Development:

```bash
uv run fastapi dev main.py
```

ASGI server command example:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000
```

Production checklist:
- Use an appropriate production server/platform configuration.
- Configure HTTPS, trusted hosts/proxies, and network access.
- Keep secrets in environment variables or a secret manager.
- Configure structured logging, monitoring, and request tracing.
- Set timeouts, request/body limits, and rate limits as appropriate.
- Handle graceful shutdown and database cleanup.
- Apply database migrations safely.
- Understand worker count and memory usage; each worker may load its own model.
- Expose health/readiness checks appropriate to the platform.
- Do not use development mode in production.

## 16. Common mistakes

- Putting all logic in one route or one giant file.
- Using blocking I/O directly inside `async def`.
- Treating validation as authorization.
- Assuming CORS protects an API.
- Returning raw internal exceptions to clients.
- Reloading a large model on every request.
- Using in-process background tasks for durable jobs.
- Forgetting tests for error cases.
- Committing secrets or `.env` files.
- Assuming more workers always improve performance.

## 17. Quick commands

```bash
uv add "fastapi[standard]"
uv add --dev pytest httpx ruff
uv run fastapi dev main.py
uv run pytest
uv run ruff check .
uv run uvicorn main:app --host 127.0.0.1 --port 8000
```

## Official documentation

- FastAPI: <https://fastapi.tiangolo.com/>
- Tutorial: <https://fastapi.tiangolo.com/tutorial/>
- Async/await: <https://fastapi.tiangolo.com/async/>
- Testing: <https://fastapi.tiangolo.com/tutorial/testing/>
- Deployment: <https://fastapi.tiangolo.com/deployment/>
- Pydantic: <https://docs.pydantic.dev/latest/>
