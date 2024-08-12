# Starter-Service

Overview of the Microservice

- [Name of the Service]
- [Few lines of description about the service]

## Checklist for the Service

    - OpenAPI upto date: [Yes/No]
    - Database: [if so specify]
    - Kafka Dependency: [if so specify]
    - End-points Tests: [if so specify]
    - Unit-Tests: [if so specify]

## Configuration Description

Find below documentation for the configuration, the file can be found under `config.yml`

    - [parameter]: [Description]
    - [parameter]: [Description]
    - [parameter]: [Description]
    - [parameter]: [Description]

# For Developers

## Debug your code

To setup debug in VSCode, create `.vscode\launch.json` and add the content below.
Then press `F5`, whihc would start the debug process and run the module `run`

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

## Running Endpoint-Testing

It is advisable to write tests against the end-points of your API, it shoudl include all business logic,
but shoudl mock external dependencies like databases, kafka publisher etc.

Sample tests are written under `tests\api_tests` and include tests for the POST method.

Note: Since the geters are mearly fetching data, and no validation is being done (other than at the DTO, test were skipped),
but in actual devlopment, it is advisable to include tests for simple getters also.

To run the test you can `python -m pytest .\tests\api_tests` command (for Linux use python3)

To debug tests you can use the below entry for `.vscode\launch.json`
Once done press `F5` to start the test.

    {
    "version": "0.2.0",
        "configurations": [
            {
                "name": "Python Debugger: Module",
                "type": "debugpy",
                "request": "launch",
                "module": "pytest",
                "args": [".\\tests\\api_tests"]
            },
        ]
    }

## Run application as Local Container

- Run container with building new image: `docker compose -f .\docker-compose.yml up -d --build`

## Connecting to MongoDB.

To connect and access data for MongoDB, you can use a client tool `MongoDB Compass`
It is a free s/w and can be downloaded from the internet.

To connect simpally add a new connection e.g. `mongodb://admin:password@host.docker.internal:27017/` ensuring all values are correct

`=========================================
IMPORTANT: This section should be removed
=========================================`

# Documentation for the Starter-Kit

## Features Implemented

- RESTful service

  - Sample Controller
    - This provides sample end-point with POST and GET examples.
  - Swagger-UI - The RESTful endpoint is controller by OpenAPI spec, the file is available under `app\controllers\spec\openapi.yaml`

    - Ensure the specs are always upto-date.
    - Always add all the correct Request and Response objects including all the Error's.
    - Hint: Using the `operationId` it is able to connect to the required controller/method.

- Sample Service
- DTO Objects - Base class, sample dto
- MongoDb - Database Wrapper
- Error Handler - Server (500), Input/Client error (400)
- Logging Config - Write to console
- API Testing - Controller to Service, with mocking (patch) DB layer.
- Algo, module - [@Dev] Create Unit Test under /tests/unit_tests
- Configuration - Configure get sstored in `config.yaml`
- Docker-Compose - Start app locally including all dependencies

## pending

- cockroach db
- kafka consumer.producer
- docker for app - having issue running from docker
- Use production ready Server
- Clean-up readme.md
