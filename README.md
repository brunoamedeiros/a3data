# A3Data Technical Challenge for Software Engineer - Backend Focus

## Project Description

This project is a technical challenge for the position of Software Engineer with a backend focus. The objective is to develop a backend system for handling and managing patient data. While data from Synthea is suggested, candidates are free to use any similar data sets.

The project structure and organization were inspired by the project generation tool provided by [FastAPI](https://fastapi.tiangolo.com/project-generation/).

GitHub Repository: [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template)

### Features Implemented:

- Patient and user CRUD endpoints.
- Initial load of 100 patients when Docker starts.
- Creation of a superuser with the specified environment variables.
- Automatic database migrations when building the containers.
- pgAdmin accessible at [http://localhost:8081/](http://localhost:8081/) with email `admin@admin.com` and password `admin`.
- Swagger documentation accessible at [http://localhost:8000/docs](http://localhost:8000/docs).

### Additional Implementations:

- Attempted integration of Kubernetes, Elasticsearch with Kibana.
- Used the Synthea database for patient data.

## Architecture

The project is organized using the Clean Architecture methodology with the following layers:

- **Entities Layer**: Represents domain models and is implemented in the `domain` folder.
  - **Value Object**: Represents a value that doesn’t have identity and is immutable.
- **Use Cases Layer**: Contains business logic and is implemented in the `interactor` folder.
  - **Data Transfer Object (DTO)**: Used to transfer data between layers without business logic.
- **Interface Adapters Layer**: Interfaces to external systems and is implemented in the `app` and `infra` folders.
  - **Controller**: Takes user input and converts it into the input DTO.
  - **Presenter**: Converts the output DTO to a format appropriate for the user.

The project uses the following technologies:

- [**FastAPI**](https://fastapi.tiangolo.com): Web framework for building APIs.
- [**SQLAlchemy**](https://www.sqlalchemy.org/) for the Python SQL database interactions (ORM).
- [**Pydantic**](https://docs.pydantic.dev): Data validation and settings management.
- [**PostgreSQL**](https://www.postgresql.org): SQL database.
- [**Poetry**](https://python-poetry.org/): Dependency management.
- [**Docker**](https://www.docker.com/): Containerization.
- [**Alembic**](https://alembic.sqlalchemy.org/en/latest/): Database migrations.
- **JWT (JSON Web Token)**: Authentication.
- [**Pytest**](https://pytest.org): Testing framework.

## Setup and Execution Instructions

### Prerequisites

- [Python](https://www.python.org/) 3.11+
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/brunoamedeiros/a3data
   cd a3data
   ```

2. **Set up environment variables**

   ```sh
   cp .env.example .env
   # Update .env with actual values if necessary
   ```

3. **Install dependencies**

   ```sh
   poetry install
   ```

4. **Build and start the application using Docker Compose**
   ```sh
   docker-compose up --build -d
   ```
   The application will automatically:

- Run Alembic migrations.
- Load the initial 100 patients.
- Create a superuser based on environment variables.

## Configuration

### Environment Variables

You can then update configs in the `.env` files to customize your configurations.

Before deploying it, make sure you change at least the values for:

- `SECRET_KEY`: Secret key for encryption.
- `FIRST_SUPERUSER`: Initial superuser email.
- `FIRST_SUPERUSER_PASSWORD`: Initial superuser password.

### Docker Compose

The `docker-compose.yml` file defines the services required by the application, including the web service and database service.

### Kubernetes

The `deployment.yaml` and `service.yaml` files define the Kubernetes deployment and service configurations.

### Alembic

Alembic is used for handling database migrations. The configuration is in the `alembic.ini` file, and migration scripts are located in the `alembic/` directory.

## Usage

### API Endpoints

The application provides the following API endpoints.

### Authentication Endpoints

- `POST /api/v1/auth/login`: Authenticate a user and return a token.

### Patient Endpoints

- `GET /api/v1/patients`: Retrieve a list of patients.
- `POST /api/v1/patients`: Create a new patient.
- `GET /api/v1/patients/{patient_id}`: Retrieve a specific patient by ID.
- `PATCH /api/v1/patients/{patient_id}`: Update a specific patient by ID.
- `DELETE /api/v1/patients/{patient_id}`: Delete a specific patient by ID.

### User Endpoints

- `GET /api/v1/users`: Retrieve a list of users.
- `POST /api/v1/users`: Create a new user.
- `GET /api/v1/users/{user_id}`: Retrieve a specific user by ID.
- `PATCH /api/v1/users/{user_id}`: Update a specific user by ID.
- `DELETE /api/v1/users/{user_id}`: Delete a specific user by ID.

### Accessing the Database using pgAdmin

To access the database using pgAdmin, use the following credentials:

- **Host name/address**: `db`
- **Username**: `admin`
- **Password**: `pass`

### Accessing the Container

To get inside the container with a bash session, start the stack with:

```sh
docker compose up -d
```

Then, exec inside the running container:

```sh
docker compose exec backend bash
```

## Testing

To test the backend, run the following command inside the container:

```sh
bash ./test.sh
```

### Additional Instructions for Alembic

1. **Creating a New Migration**

   ```sh
   poetry run alembic revision --autogenerate -m "Description of the change"
   ```

2. **Applying Migrations**

   ```sh
   poetry run alembic upgrade head
   ```

3. **Downgrading Migrations**
   ```sh
   poetry run alembic downgrade -1
   ```

## Final Considerations

If I had more time, I would have created additional entities to load more datasets, including encounters and conditions, and used foreign keys to provide more detailed information for patients. Additionally, I would have developed more endpoints, such as retrieving all patients, and implemented pagination to enhance performance. I also aimed to add more docstrings to improve code organization.

During the project, I noticed that while Elasticsearch was functioning, it was not accessible within the application. A significant portion of my time was spent configuring Docker and establishing the connection between the backend and the database, which unfortunately impacted the time available for further development and improvements.
