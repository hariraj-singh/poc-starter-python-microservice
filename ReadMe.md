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

---

## For Developers

Following are some of the documentation taht you can follow to help in your devlopment.

### Debug your code

To setup debug in VSCode, create `.vscode\launch.json` and add the content below.
Then press `F5`, whihc would start the debug process and run the module `run`

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

### Running Endpoint-Testing

It is advisable to write tests against the end-points of your API, it shoudl include all business logic,
but shoudl mock external dependencies like databases, kafka publisher etc.

Sample tests are written under `tests\api_tests` and include tests for the POST method.

Note: Since the geters are mearly fetching data, and no validation is being done (other than at the DTO, test were skipped),
but in actual devlopment, it is advisable to include tests for simple getters also.

To run the test you can `python -m pytest .\tests\api_tests` command (for Linux use python3)

To debug tests you can use the below entry for `.vscode\launch.json`
Once done press `F5` to start the test.

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

### Run application as Local Container

- Run container with building new image: `docker compose -f .\docker-compose.yml up -d --build`

### MongoDB - Client

To connect and access data for MongoDB, you can use a client tool `MongoDB Compass`
It is a free s/w and can be downloaded from the internet.

To connect simpally add a new connection e.g. `mongodb://admin:password@host.docker.internal:27017/` ensuring all values are correct

---

# Features Implemented

Following are the features that have been incorporated in the service.

## RESTful service

This service exposes REST based end-points and uses OpenAPI specification 3.x, and follows spers first approach.

- All `controller` are under `app\controllers` folder.
- OpenAPI Specification (swagger-ui) is available under `app\controllers\spec\openapi.yaml`
- To open the specs `http://127.0.0.1:5000/ui`

**[IMPORTANT]** For Devlopers

- Ensure the specs are always upto-date.
- Always add all the correct Request and Response objects including all the Error's.
- Hint: Using the `operationId` it is able to connect to the required controller/method.

## Kafka Stream

A wrapper has been written to hide all the complication to Publish and Consume messages.

- Kafka Client - Using confluent_kafka client, tested with cluster setup, Update `kafka_server` section in `config.yaml`
- Kafka Publisher - Wrapper for kafka publisher with retries and writing to db, with configs

## Misc Features

- Sample Service
- DTO Objects - Base class, sample dto
- MongoDb - Database Wrapper
- Error Handler - Server (500), Input/Client error (400)
- Logging Config - Write to console
- API Testing - Controller to Service, with mocking (patch) DB layer.
- Algo, module - [@Dev] Create Unit Test under /tests/unit_tests
- Configuration - Configure get sstored in `config.yaml`
- Docker-Compose - Start app locally including all dependencies

## Pending Items

- kafka consumer
- docker for app - having issue running from docker
- Use production ready Server
- Clean-up readme.md
- cockroach db
