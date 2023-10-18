
# Book Application API using Django Rest Framework

This API is built with Django Rest Framework for managing books, authors, and categories. It offers user authentication, token-based access, error handling, and documentation with Swagger.

## Features

- CRUD operations for books, authors, and categories.
- User authentication and token-based access.
- Swagger documentation for API usage.

## Prerequisites

- Python (3.7+)
- Pipenv
- PostgreSQL (or other databases)

## Installation

1. Clone the repository.

2. Install dependencies with `pipenv`.

3. Configure your database in `settings.py`.

4. Apply migrations and create a superuser.

5. Run the development server.

## Usage

Interact with the API using tools like curl, Postman, or any HTTP client. API documentation is available at `http://localhost:8000/swagger/`.

## Authentication

Token-based authentication is used. Get an access token by registering a user or logging in.

## API Endpoints

- Books, Authors, and Categories: CRUD operations.
- Authentication: Register users and obtain access tokens.

## Error Handling

Detailed error responses with status codes and messages are provided.

## Contributing

1. Fork the repository.

2. Create a new branch for your changes.

3. Make and test your changes.

4. Create a pull request with clear descriptions.

5. Your request will be reviewed and merged if approved.

## License

This project is under the MIT License. See `LICENSE.md` for details.
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)