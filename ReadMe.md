# Starter-Service

## Overview

**Service Name**: [Name of the Service]

**Description**:  
[Few lines of description about the service]

## Service Checklist

- **OpenAPI Up-to-date**: [Yes/No]
- **Database**: [Specify if applicable]
- **Kafka Dependency**: [Specify if applicable]
- **End-point Tests**: [Specify if applicable]
- **Unit Tests**: [Specify if applicable]

## Configuration Description

Below is the documentation for the configuration file, which can be found under `config.yml`:

- **[parameter]**: [Description]
- **[parameter]**: [Description]
- **[parameter]**: [Description]
- **[parameter]**: [Description]

---

## For Developers

The following documentation is intended to assist in development.

### Debugging Your Code

To set up debugging in VSCode, create a `.vscode\launch.json` file and add the content below. Then press `F5`, which will start the debugging process and run the module `run`.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Module",
      "type": "debugpy",
      "request": "launch",
      "module": "run"
    }
  ]
}
```

### Running Endpoint Tests

It is advisable to write tests against the end-points of your API. These tests should include all business logic and mock external dependencies like databases and Kafka publishers.

Sample tests are written under `tests\api_tests` and include tests for the POST method.

**Note**: Since the getters are merely fetching data, and no validation is being done (other than at the DTO), tests were skipped. However, in actual development, it is advisable to include tests for simple getters as well.

To run the tests, use the command `python -m pytest .\tests\api_tests` (for Linux, use `python3`).

To debug tests, you can use the following entry in `.vscode\launch.json`. Once done, press `F5` to start the test.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Module",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "args": [".\\tests\\api_tests"]
    }
  ]
}
```

### Running the Application as a Local Container

- To run the container with a new image build, use: `docker compose -f .\docker-compose.yml up -d --build`

### MongoDB Client

To connect and access data in MongoDB, you can use the client tool **MongoDB Compass**. It is a free software and can be downloaded from the internet.

To connect, simply add a new connection with the string `mongodb://admin:password@host.docker.internal:27017/`, ensuring all values are correct.

---

# Features Implemented

The following features have been incorporated into the service.

## RESTful Service

This service exposes REST-based endpoints, uses OpenAPI Specification 3.x, and follows a specification-first approach.

- All `controllers` are located in the `app\controllers` folder.
- The OpenAPI Specification (swagger-ui) is available under `app\controllers\spec\openapi.yaml`.
- To view the specifications, visit `http://127.0.0.1:5000/ui`.
- It also has a service, so it demonstrate using a servcie layer `app\services\voting_service.py`

  - It has connectivity to Database Store, Kafka Stream etc.
  - Note the servcie layer is not only to be used by API service but can be used by anyone.

- We also have a DTO built, there can be found in `app\dto` folder

  - It has a base class that provides basic function on DTo and object manupilation

**Important for Developers**

- Ensure the specifications are always up-to-date.
- Always include the correct Request and Response objects, including all Errors.
- **Hint**: Using the `operationId`, it is possible to connect to the required controller/method.

## Service Layer and DTO

A service layer has been inp-lementes, the idea is all Busineess Logic, DB operation all core logic would reside in here.
All services are found under `app\services\` folder.

The layer is complemented with DTO object that are simple objects. The DTO inherits from `base_dto` and it has basic common
functionality. All DTO are found under `app\dto` folder.

## Helper Class

- app\helpers\config_wrapper.py - Provides wrapper to read `config.yaml` file and provide a centralise way to consume the configurations.
- app\helpers\database_wrapper.py - Wrapper for MongoDB
- app\helpers\decorators.py - All decorators are present in here.
- app\helpers\exception_handler.py - Basic exception handlers 50x and 40x
- app\helpers\kafka_wrapper.py - Wrapper to consume Kafka Streams

## Kafka Stream

A wrapper has been developed to simplify publishing and consuming messages.

- **Kafka Client**: Uses the `confluent_kafka` client and has been tested with a cluster setup. Update the `kafka_server` section in `config.yaml`.
- **Kafka Publisher**: Wrapper for the Kafka publisher with retries and database writing configurations.

## Miscellaneous Features

- Logging Configuration: Writes logs to console
- API Testing: Controller to service with mocking (patch) DB layer
- Test Algorithm Module: [@Dev] Create unit tests under `/tests/unit_tests`
- Docker-Compose: Starts app locally, including all dependencies

## Pending Items

- Kafka consumer
- Docker for app -> Issues running from Docker
- Use production-ready server
- Clean-up `README.md`
- CockroachDB integration
