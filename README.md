# API-Development
Lightweight FastAPI backend demonstrating user authentication, posts CRUD, voting, and migrations using SQLAlchemy and Alembic.

## Tech stack
- Python 3.14
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic Settings
- Uvicorn

## Features

- User registration and authentication (OAuth2 password flow)
- JWT access tokens
- Create/Read/Update/Delete (CRUD) posts under authentication
- Vote on posts (single upvote per user)
- Pagination and search on posts
- Database migrations managed by Alembic

## Repo layout

- app/: application package
	- main.py: FastAPI app and router registration
	- config.py: environment-backed settings
	- database.py: SQLAlchemy engine & session
	- models.py: ORM models
	- schema.py: Pydantic request/response models
	- oauth2.py: token creation & current-user dependency
	- routers/: route modules (`auth.py`, `users.py`, `post.py`, `vote.py`)
- alembic/: Alembic configuration and migration scripts
- requirements.txt

## Quick start

1. Clone the repo and enter the project folder.

2. Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
database_hostname=localhost
database_port=5432
database_username=postgres
database_password=your_db_password
database_name=your_db_name
secret_key=your_random_secret
algorithm=HS256
access_token_expire_minutes=30
```

4. Ensure PostgreSQL is running and a database matching `database_name` exists (create it if needed).

5. Run database migrations:

```bash
alembic upgrade head
```

6. Start the application:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000 and interactive docs at http://127.0.0.1:8000/docs

## Environment variables

Required variables (stored in `.env`): `database_hostname`, `database_port`, `database_username`, `database_password`, `database_name`, `secret_key`, `algorithm`, `access_token_expire_minutes`.

These are loaded by `app/config.py` via Pydantic Settings.

## Endpoints (overview)

All routes are registered in [app/main.py](app/main.py). Major endpoints:

- `GET /` — Root welcome message
- `POST /login` — Obtain JWT access token (OAuth2 password form fields: `username` and `password`)
- `POST /users/` — Create a new user
- `GET /users/{id}` — Get user profile
- `GET /posts/` — List posts (supports `limit`, `skip`, `search` query params). Requires authentication.
- `POST /posts/` — Create a post (authenticated)
- `GET /posts/{id}` — Get a single post (includes vote count)
- `PUT /posts/{id}` — Update a post (owner only)
- `DELETE /posts/{id}` — Delete a post (owner only)
- `POST /vote/` — Vote/unvote on a post (authenticated)

Authentication: include header `Authorization: Bearer <access_token>` for protected endpoints.

Learning process from https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/.
