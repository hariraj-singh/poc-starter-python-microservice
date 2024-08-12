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

## pending

- cockroach db
- kafka consumer.producer
- docker compose for dev
- docker for app
- add config for db, kafka etc.

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
