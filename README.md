# Litestar Demo Project

[🇷🇺 Russian version](README.ru.md)

This is a demo project built using the Litestar framework. The project represents a modern web application built with best development practices in mind.

## Project Features

- 🚀 **Full Type Safety** - The project is fully typed using Python type hints
- 🔄 **Async Architecture** - Built on an asynchronous approach for maximum performance
- 🧅 **Onion Architecture** - Project structure follows clean architecture principles
- 🛠 **Development Tools**:
  - Ruff for code linting and formatting
  - mypy for static type checking
- 🐳 **Docker** - Application containerization for easy deployment

## Project Structure

```
.
├── src/       # Application source code
│   ├── apps/             # Application modules
│   │   └── users/        # Users module
│   │       ├── api/      # API layer
│   │       │   ├── controllers/  # API controllers
│   │       │   └── router.py     # API routing
│   │       ├── core/     # Business logic
│   │       │   ├── models/       # Business models
│   │       │   ├── repositories/ # Repository interfaces
│   │       │   └── services/     # Business services
│   │       └── db/       # Database operations
│   │           ├── models.py     # DB models
│   │           └── repository.py # Repository implementations
│   ├── db/               # Database configuration
│   │   ├── base_model.py # Base model class
│   │   ├── models.py     # Common DB models
│   │   └── setup.py      # DB connection setup
│   ├── app.py            # Main application file
│   ├── settings.py       # Application configuration
│   ├── requirements.txt  # Project dependencies
│   ├── pyproject.toml    # Project configuration
│   ├── ruff.toml         # Ruff configuration
│   └── mypy.ini          # mypy configuration
└── dev/                  # Development files
    ├── .env             # Environment variables
    ├── .env.example     # Environment variables example
    ├── Dockerfile       # Docker configuration
    └── docker-compose.yml # Docker Compose configuration
```

## Installation and Running

### Using Docker

1. Copy the environment variables file:
```bash
cp ./.env.example ./.env
```

2. Run the application:
```bash
docker compose up --build
```
