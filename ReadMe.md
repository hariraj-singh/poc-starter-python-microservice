Where am i stop

## Overview

TBD

## Features implemented

- Swagger-UI
- Sample Controller
- Sample Service
- DTO Objects - Base class, sample dto
- MongoDb - Database Wrapper
- Error Handler - Server (500), Input/Client error (400)
- Logging Config - Write to console
- API Testing - Controller to Service, with mocking (patch) DB layer.
- Algo, module - [@Dev] Create Unit Test under /tests/unit_tests
- Configuration - Configure get sstored in `config.yaml`

## pending

- cockroach db
- kafka consumer.producer
- docker compose for dev
- docker for app

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
