# FastAPI --- Developer Revision Notes

A practical revision guide for building, testing, securing, and
deploying FastAPI applications. Examples use modern Python type hints
and Pydantic v2. Treat snippets as patterns to adapt, not one complete
application.

## 1. What FastAPI provides

FastAPI is an ASGI web framework built on Starlette and closely
integrated with Pydantic.

-   **FastAPI:** routing, dependency injection, request validation,
    response serialization, OpenAPI docs.
-   **Starlette:** ASGI request/response handling, middleware, sessions,
    WebSockets, and other web primitives.
-   **Pydantic:** parsing and validating data against Python type
    annotations.
-   **ASGI server:** runs the app, commonly Uvicorn.
-   **Database layer:** optional; often SQLAlchemy/SQLModel plus a
    database driver.
-   **OpenAPI:** machine-readable API specification used by interactive
    documentation and client tools.

Useful URLs in development:

-   `/docs` --- Swagger UI.
-   `/redoc` --- ReDoc.
-   `/openapi.json` --- OpenAPI schema.

## 2. Project setup with `uv`

``` bash
uv init my-api
cd my-api
uv add "fastapi[standard]"
uv add --dev pytest httpx ruff
uv run fastapi dev main.py
```

For an existing project, install packages inside that project's
environment and keep `pyproject.toml` and `uv.lock` committed.

Useful commands:

``` bash
uv add sqlalchemy asyncpg          # Async PostgreSQL example
uv add alembic                     # Database migrations
uv add --dev pytest pytest-asyncio
uv run pytest
uv run ruff check .
uv run ruff format .
uv run fastapi dev main.py
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

Use development reload only during development. Pin and update
dependencies deliberately; review lockfile changes.

## 3. Minimal application and route handlers

``` python
from fastapi import FastAPI

app = FastAPI(title="Example API")


@app.get("/")
async def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
```

-   `@app.get(...)`, `@app.post(...)`, etc. register path operations.
-   The function is the path operation handler.
-   FastAPI infers many parameter sources from the path, type hints, and
    Pydantic models.
-   Return dictionaries/lists/models for JSON responses.
-   Use `response_model=` to document, validate, and filter output.

## 4. HTTP methods, paths, and parameters

  Method     Typical purpose
  ---------- -------------------------------------------------
  `GET`      Read a resource; should not change server state
  `POST`     Create a resource or perform an operation
  `PUT`      Replace a resource
  `PATCH`    Partially update a resource
  `DELETE`   Delete a resource

``` python
from fastapi import Query

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/products")
def list_products(
    category: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return {"category": category, "limit": limit, "offset": offset}
```

-   **Path parameter:** part of the route, e.g. `/users/10`.
-   **Query parameter:** after `?`, e.g. `/products?limit=10`.
-   **Request body:** commonly JSON sent with POST/PUT/PATCH.
-   **Header/cookie parameters:** use `Header` and `Cookie`.
-   Use explicit `Path`, `Query`, `Body`, `Header`, and `Cookie`
    declarations when they improve clarity or add constraints.
-   Avoid ambiguous route ordering: a route such as `/users/me` should
    be declared before `/users/{user_id}` if the dynamic route could
    capture it.

## 5. Pydantic request and response models

``` python
from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    # Demo only: a real app would persist this and return its generated ID.
    return {"id": 1, **product.model_dump()}
```

Key concepts:

-   `BaseModel` defines a validated data structure.
-   `Field()` adds constraints, defaults, descriptions, and metadata.
-   `model_dump()` returns a Python dictionary; `model_dump_json()`
    returns JSON text.
-   `model_validate()` validates Python data; `model_validate_json()`
    validates JSON input.
-   `str | None` means a value may be a string or `None`; it does not by
    itself make the field optional in input. Give it a default such as
    `= None` if omission is allowed.
-   `response_model` defines the public output contract and normally
    excludes undeclared fields.
-   Use separate create, update, and response schemas; do not expose
    internal fields or password hashes.
-   `ConfigDict(from_attributes=True)` lets a schema validate from
    object attributes, useful for ORM objects.
-   Validation catches shape/type/constraint errors, not all business
    rules or authorization checks.
-   Pydantic may coerce compatible inputs by default. Use strict
    types/configuration where strict rejection is required.

For partial updates:

``` python
changes = update_schema.model_dump(exclude_unset=True)
```

`exclude_unset=True` includes only fields supplied by the client. Decide
deliberately how explicit `null` should behave.

## 6. Status codes and errors

Common status codes:

-   `200 OK` --- successful request.
-   `201 Created` --- resource created.
-   `202 Accepted` --- accepted for processing, not necessarily
    completed.
-   `204 No Content` --- success with no response body.
-   `400 Bad Request` --- invalid request.
-   `401 Unauthorized` --- authentication is missing/invalid.
-   `403 Forbidden` --- caller is not permitted.
-   `404 Not Found` --- resource not found.
-   `409 Conflict` --- conflict with current state, e.g. duplicate
    unique value.
-   `422 Unprocessable Entity` --- FastAPI request validation error by
    default.
-   `429 Too Many Requests` --- rate limit exceeded.
-   `500 Internal Server Error` --- unexpected server-side failure.

``` python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Product not found")
```

Raise `HTTPException`; do not return it as an ordinary object. Do not
send stack traces, SQL errors, secrets, or raw internal exceptions to
clients.

For application-wide error formats, register exception handlers. Log
unexpected failures server-side with a request/correlation ID.

## 7. `def`, `async def`, and concurrency

-   FastAPI runs ordinary `def` path operations and dependencies in a
    thread pool.
-   `async def` runs on the event loop; use `await` with
    async-compatible I/O libraries.
-   Do not call blocking I/O such as `time.sleep()` directly inside
    `async def`; use `await asyncio.sleep()` or an appropriate async
    library.
-   `async` does not automatically make CPU-heavy work faster.
-   Use an async database driver/session with async endpoints; do not
    assume a synchronous database client becomes asynchronous just
    because the route is `async def`.
-   For CPU-heavy inference or long-running jobs, consider separate
    worker processes/services or a task queue.

``` python
import asyncio

@app.get("/wait")
async def wait():
    await asyncio.sleep(1)
    return {"done": True}
```

## 8. Dependency injection

`Depends` provides reusable values and behavior: authentication,
configuration, database sessions, pagination, and shared checks.

``` python
from typing import Annotated
from fastapi import Depends, HTTPException


def get_current_user():
    # Demo only; replace with real credential verification.
    user = None
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


CurrentUser = Annotated[dict, Depends(get_current_user)]


@app.get("/profile")
def profile(user: CurrentUser):
    return user
```

-   Dependencies can depend on other dependencies.
-   FastAPI normally caches a dependency's result within one request;
    `use_cache=False` disables that for a dependency declaration.
-   `app.dependency_overrides` is useful in tests.
-   Use `yield` dependencies for resources requiring cleanup, such as
    database sessions.
-   Keep dependencies focused; avoid hiding large amounts of business
    logic inside them.

## 9. Application lifespan and startup/shutdown

Use a lifespan context manager for resources that should be initialized
once per application process and cleaned up at shutdown.

``` python
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize shared resources here.
    yield
    # Close/release shared resources here.


app = FastAPI(lifespan=lifespan)
```

Examples include connection pools and clients. Do not open a new
connection pool on every request. Each worker process generally has its
own application lifespan and its own in-process resources.

## 10. Routers and project organization

Use `APIRouter` to group related endpoints:

``` python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Register it:

``` python
from fastapi import FastAPI
from routers import users

app = FastAPI()
app.include_router(users.router, prefix="/api/v1")
```

A growing project might use:

``` text
app/
├── main.py
├── api/             # Routers / endpoints
├── schemas/         # Pydantic request and response models
├── models/          # ORM/database models
├── services/        # Business rules/use cases
├── repositories/    # Data-access operations (if useful)
├── db/              # Engine, sessions, migrations
├── core/            # Settings, security, logging
└── dependencies.py
tests/
```

Start simple and introduce layers when they clarify responsibilities.
Avoid circular imports and avoid placing all code in `main.py`.

## 11. Settings and environment variables

Keep environment-specific configuration outside source code. Use
environment variables or a secret manager; `.env` is convenient for
local development.

``` python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    session_secret: str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
```

Install `pydantic-settings` if using this pattern. Never commit real
`.env` secrets. Add `.env` to `.gitignore`, and use different secrets
for development and production. Validate required settings early at
startup.

## 12. Database integration: SQLAlchemy async example

FastAPI does not mandate a database. For async PostgreSQL, one common
stack is SQLAlchemy's async API plus `asyncpg`.

``` python
import os
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine,
)

engine = create_async_engine(os.environ["DATABASE_URL"], echo=False)
SessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
```

Use it through dependency injection:

``` python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

DbSession = Annotated[AsyncSession, Depends(get_db)]
```

Important points:

-   `engine` manages connectivity and a connection pool; it does not
    necessarily connect immediately.
-   `SessionLocal` is a session factory, not a session itself.
-   `yield` gives the session to the endpoint and allows cleanup after
    the request's dependency scope finishes.
-   `async with SessionLocal()` closes the session; the underlying
    connection is normally returned to the pool.
-   Use `await` for async database operations, such as
    `await db.execute(...)`, `await db.commit()`, and
    `await db.refresh(obj)`.
-   Use transactions deliberately. On failure, roll back when continuing
    to use a session; closing a session also releases its resources.
-   Do not share one `AsyncSession` concurrently across independent
    tasks.
-   Create tables through migrations in real projects;
    `Base.metadata.create_all()` is useful for simple learning examples,
    not a replacement for migrations.
-   Use Alembic for schema migrations.
-   Use ORM query APIs or parameterized SQL; never concatenate untrusted
    input into SQL.
-   Consider pool size, timeouts, indexes, unique constraints, and
    database-level constraints.
-   Keep SQLAlchemy ORM models distinct from Pydantic API schemas.

Typical flow:
`request → validation → authorization → service/business logic → database transaction → response`.

## 13. Authentication and authorization

-   **Authentication:** establish who the caller is.
-   **Authorization:** determine what the caller can do.
-   **OAuth 2.0:** authorization framework commonly used for delegated
    access and token-based APIs.
-   **OpenID Connect (OIDC):** identity layer built on OAuth 2.0.
-   **JWT:** token format; verify signature, issuer, audience, expiry,
    and relevant claims. Decoding alone is not validation.
-   **Session cookie:** identifies a server-side or signed client
    session; configure cookie security carefully.
-   **API key:** often useful for service access, but needs secure
    storage, rotation, and scope/rate controls.

Security essentials:

-   Use a maintained password-hashing algorithm for passwords; never
    store plaintext passwords.
-   Validate OAuth state/nonce and tokens correctly; use established
    libraries.
-   Set token/session expiry and provide logout/revocation behavior
    appropriate to the design.
-   Use HTTPS in production.
-   For cookies, review `Secure`, `HttpOnly`, and `SameSite`; consider
    CSRF protections for cookie-authenticated state-changing requests.
-   Apply authorization checks to individual resources, not only routes.
-   Keep secrets out of source control, logs, URLs, and error messages.
-   Use least-privilege database/service accounts.

FastAPI provides security building blocks, not a complete production
authentication system by itself.

## 14. Middleware, CORS, cookies, and sessions

Middleware can wrap request/response handling for request IDs, timing,
CORS, and other cross-cutting concerns.

-   CORS controls which browser origins may read cross-origin responses.
-   CORS is **not authentication** and does not prevent non-browser
    clients from calling an API.
-   Configure explicit trusted origins when possible; credentialed
    requests should not use wildcard origins.
-   Session middleware must be configured with a strong secret and
    suitable cookie settings.
-   Behind a reverse proxy, configure trusted proxy headers only for
    known proxies.
-   Trusted-host protections can help prevent unexpected Host headers.

## 15. Files, forms, and large request bodies

-   Use `UploadFile` for uploaded files; it uses a spooled file and is
    generally preferable to loading large files fully into memory.
-   Use `File` and `Form` for multipart form requests.
-   Validate size, file type/content, filename handling, and storage
    location; client-provided MIME types alone are not trustworthy.
-   Do not trust user filenames as filesystem paths.
-   Stream or process large files where possible; set request-size
    limits at the proxy/server layer.
-   Store large or durable files in appropriate object storage rather
    than assuming local container storage is permanent.

## 16. Background work and scheduled jobs

-   `BackgroundTasks` is suitable for small, best-effort work after a
    response.
-   It is not a durable queue and may be lost if the process stops.
-   Use a task queue/worker system for long-running, retryable,
    scheduled, or resource-intensive jobs.
-   Design jobs to be idempotent where possible, record status, handle
    retries, and prevent duplicate side effects.
-   Do not run expensive model training or lengthy AI workflows in a
    normal request handler unless the architecture and timeouts
    explicitly support it.

## 17. Testing

Install:

``` bash
uv add --dev pytest httpx
```

Basic test:

``` python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
```

Run `uv run pytest`.

Test:

-   Success and invalid-input cases.
-   Status codes and response schemas.
-   Authentication and authorization, including access to another user's
    resources.
-   Database success, rollback, constraints, and missing records.
-   External-service errors, timeouts, and retry behavior.
-   Boundary conditions and pagination.

Testing notes:

-   Override dependencies with `app.dependency_overrides` and clear
    overrides after tests.
-   Use a test database or isolated test schema; never accidentally run
    destructive tests against production.
-   For async tests, use an async test setup compatible with your
    pytest/AnyIO configuration and async HTTP client.
-   Avoid tests that depend on execution order or external services
    being available.
-   Test lifespan behavior where startup/shutdown resources matter.

## 18. API design essentials

-   Use consistent resource naming and status codes.
-   Add pagination to endpoints that may return many records; set a
    maximum page size.
-   Validate sorting/filter fields against an allowlist.
-   Define stable response schemas and consistent error formats.
-   Use versioning when clients need incompatible API changes,
    e.g. `/api/v1`.
-   Make retries safe where possible; consider idempotency keys for
    operations that must not be duplicated.
-   Avoid returning database internals or fields the caller should not
    see.
-   Set request timeouts, limits, and sensible defaults.
-   Document authentication, errors, pagination, and examples in OpenAPI
    metadata.
-   Consider caching, conditional requests, and ETags where useful.

## 19. WebSockets and streaming

-   WebSockets support bidirectional communication; they are useful for
    live updates, chat, and interactive interfaces.
-   Streaming responses can deliver data incrementally instead of
    buffering a complete response.
-   Both need explicit connection lifecycle, authentication, limits,
    error handling, and deployment/proxy support.
-   Do not assume ordinary HTTP request/response behavior applies
    unchanged to long-lived connections.

## 20. Logging, observability, and reliability

-   Use Python's `logging` module instead of relying on `print()` in
    production.
-   Log useful context such as request ID, route, duration, and outcome.
-   Never log passwords, tokens, session cookies, or sensitive request
    bodies.
-   Track latency, error rate, throughput, resource use, and dependency
    health.
-   Distinguish liveness (process is running) from readiness (service
    can safely accept traffic).
-   Set timeouts for outbound HTTP/database operations and handle
    failures explicitly.
-   Retry only transient failures and avoid retry storms; use backoff
    and limits.
-   Gracefully close clients, pools, and other resources during
    shutdown.

## 21. AI/ML API patterns

Common endpoints include `POST /predict`, `POST /chat`,
`POST /documents`, and `POST /search`.

-   Load models once per worker/process, not once per request.
-   Validate expected input shape, data types, ranges, and payload
    sizes.
-   Measure latency, memory, throughput, and concurrency.
-   Account for model memory multiplied by the number of worker
    processes.
-   Use separate workers/services for expensive CPU/GPU inference where
    appropriate.
-   Set upstream timeouts and handle provider errors/rate limits.
-   Protect costly endpoints with authentication, quotas, and rate
    limits.
-   Treat uploaded documents and retrieved content as untrusted input;
    do not allow them to override system instructions or trigger
    unauthorized actions.
-   Avoid logging private prompts, credentials, or sensitive document
    contents.

## 22. Docker and deployment

A simple container deployment often includes the API, database, and
possibly a reverse proxy or worker. Keep service credentials in
environment configuration or secrets, not in the image.

Production checklist:

-   Use a supported Python version and reproducible dependency lock.
-   Run behind an appropriate ASGI server/platform and configure worker
    count intentionally.
-   Bind to the interface required by the deployment platform; use
    `0.0.0.0` inside a container when external container access is
    needed.
-   Use HTTPS at the platform/reverse proxy and configure trusted proxy
    headers correctly.
-   Keep debug/reload mode off in production.
-   Run migrations as a controlled deployment step, not concurrently
    from every worker.
-   Use persistent database storage and tested backup/restore
    procedures.
-   Configure secrets, least privilege, network restrictions, and
    database access rules.
-   Add health/readiness checks, structured logs, metrics, and alerting.
-   Set resource limits, timeouts, request/body limits, and rate limits.
-   Handle graceful shutdown and connection cleanup.
-   Understand that each worker may have its own connection pool and
    loaded model.
-   Do not rely on a container's writable filesystem for durable uploads
    or database data.

Example server command (adapt to the hosting platform):

``` bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## 23. Common mistakes to avoid

-   Returning `HTTPException` instead of raising it.
-   Using `async def` with blocking I/O.
-   Creating an engine/pool on every request.
-   Sharing an `AsyncSession` concurrently across tasks.
-   Forgetting to close resources or roll back failed transactions.
-   Treating Pydantic validation as authorization or business
    validation.
-   Returning ORM/internal fields unintentionally.
-   Committing `.env`, tokens, or credentials.
-   Using CORS as a security boundary.
-   Trusting uploaded filenames, MIME types, or client-supplied IDs.
-   Using in-process background tasks for durable work.
-   Creating database schema with `create_all()` as a production
    migration strategy.
-   Running destructive tests against a real database.
-   Returning raw exception details to clients.
-   Assuming more workers always improve performance.
-   Forgetting pagination, timeouts, rate limits, monitoring, and
    backups.

## 24. Quick reference commands

``` bash
uv add "fastapi[standard]"
uv add --dev pytest httpx ruff
uv run fastapi dev main.py
uv run pytest
uv run ruff check .
uv run ruff format .
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Official documentation

-   FastAPI: https://fastapi.tiangolo.com/
-   FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
-   Async/await: https://fastapi.tiangolo.com/async/
-   Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
-   Testing: https://fastapi.tiangolo.com/tutorial/testing/
-   Lifespan: https://fastapi.tiangolo.com/advanced/events/
-   Security: https://fastapi.tiangolo.com/tutorial/security/
-   Pydantic: https://docs.pydantic.dev/latest/
-   SQLAlchemy asyncio:
    https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
-   Alembic: https://alembic.sqlalchemy.org/
-   Uvicorn: https://www.uvicorn.org/
