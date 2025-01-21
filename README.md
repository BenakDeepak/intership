# FastAPI PostgreSQL CRUD Application

## Features
- Implements RESTful CRUD operations for a User resource.
- Database: PostgreSQL (Neon Serverless Postgres recommended).
- Framework: FastAPI.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update `DATABASE_URL` in `app/database/database.py` with your PostgreSQL connection details.
3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints
- `GET /users`
- `GET /users/{id}`
- `POST /users`
- `PUT /users/{id}`
- `DELETE /users/{id}`

## Testing
Use Postman or any API testing tool to interact with the endpoints.
