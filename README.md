# QuickShop Platform

Welcome to QuickShop Platform, an innovative shopping solution designed to streamline the grocery shopping experience. This project encapsulates a robust backend service built with FastAPI, utilizing Docker for containerization, Alembic for database migrations, PostgreSQL for data persistence, and Elasticsearch for enhanced searching capabilities.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your machine.
- Python 3.8 or above is available for local development.

## Installation

To set up your local development environment, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/mrmuhammadazeemrao/quickshop-platform
cd quickshop-platform
```

2. Start the services using Docker Compose:

```bash
docker-compose up --build
```

The command above will:
- Build the `web` service based on the Dockerfile instructions.
- Start the PostgreSQL database (`db` service) and Elasticsearch (`elasticsearch` service) with the necessary configurations.
- Perform database migrations with Alembic.
- Seed the database and Elasticsearch indices with initial data.

## Services

The QuickShop Platform consists of the following services:

- **Web**: The FastAPI application accessible at `localhost:8080`.
- **DB**: The PostgreSQL database service.
- **Elasticsearch**: A search engine that provides scalable search functionality.

## API Usage

Once the application is running, you can access the API at:

```
http://localhost:8080/docs
```

This will bring up the automatic interactive API documentation provided by Swagger UI.

## Configuration

- The services' ports and environment variables are configurable through the `docker-compose.yml` file.
- Database URL and Elasticsearch configuration are set as environment variables within the `web` service in `docker-compose.yml`.

## Persistent Data

Volumes are used to persist data:
- `./postgres_data` for PostgreSQL data.
- `./es_data_volume` for Elasticsearch data.
