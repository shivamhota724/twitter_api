# Twitter API

A simple REST API built using FastAPI, SQLAlchemy, and SQLite.

## Features

- Create a post
- Get all posts
- Get a single post
- Update a post
- Delete a post

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite

## Project Structure

```
twitter_api/
│
├── main.py          # API routes
├── database.py      # Database connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shivamhota724/twitter_api.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/posts` | Get all posts |
| GET | `/posts/{post_id}` | Get one post |
| POST | `/posts` | Create a post |
| PUT | `/posts/{post_id}` | Update a post |
| DELETE | `/posts/{post_id}` | Delete a post |
