# Twitter API

A production-ready REST API built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and role-based authorization.

## Live Demo

API Documentation:

https://twitter-api-931t.onrender.com/docs

---

## Features

### Authentication
- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Authentication
- Protected Routes using OAuth2

### Authorization
- Posts belong to individual users
- Only the owner of a post can update it
- Only the owner of a post can delete it

### Posts
- Create a Post
- Get All Posts
- Get a Single Post
- Update a Post
- Delete a Post

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy ORM
- Render PostgreSQL
- JWT Authentication
- OAuth2 Password Flow
- Passlib + bcrypt
- Uvicorn
- Render

---

## Project Structure

```text
twitter_api/
│
├── main.py              # API routes
├── models.py            # Database models
├── schemas.py           # Pydantic schemas
├── database.py          # Database connection and session management
├── oauth2.py            # JWT creation and verification
├── utils.py             # Password hashing and verification
├── requirements.txt
├── Procfile
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shivamhota724/twitter_api.git
```

Move into the project directory:

```bash
cd twitter_api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users` | Register a new user |
| POST | `/login` | Login and receive JWT token |

---

### Posts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/posts` | Get all posts |
| GET | `/posts/{post_id}` | Get a single post |
| POST | `/posts` | Create a new post |
| PUT | `/posts/{post_id}` | Update a post |
| DELETE | `/posts/{post_id}` | Delete a post |

---

## Authentication Flow

### Register

```text
POST /users
```

User password is hashed before storing in the database.

---

### Login

```text
POST /login
```

Returns:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

### Access Protected Routes

Click **Authorize** in Swagger UI and enter:

```text
username = your email
password = your password
```

FastAPI automatically attaches the JWT token to future requests.

---

## Database Schema

### Users

| Column | Type |
|--------|------|
| id | Integer |
| email | String |
| password | String |

---

### Posts

| Column | Type |
|--------|------|
| id | Integer |
| content | String |
| owner_id | Integer |

---

## Future Improvements

- Database migrations using Alembic
- Refresh Tokens
- User profile endpoints
- Pagination
- Docker support
- CI/CD pipeline

---

## Author

**Shivam Hota**

GitHub:

https://github.com/shivamhota724
