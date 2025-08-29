# Simple A2A Agent Demo

This document describes a simple agent and client demonstrating the Agent to Agent (A2A) SDK.

This application contains a simple agent and a test client to invoke it.

## Setup and Deployment

### Prerequisites

Before running the application locally, ensure you have the following installed:

1. **uv:** The Python package management tool used in this project. Follow the installation guide: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
2. **python 3.13** Python 3.13 is required to run a2a-sdk 

## 1. Initialize a new project (optional)

To start a new project with uv, run:

```bash
uv init <project-name>
cd <project-name>
```

## 2. Install dependencies

This will create a virtual environment in the `.venv` directory and install the required packages.

```bash
uv venv
source .venv/bin/activate
```

To add new dependencies, use:

```bash
uv add <package-name>
```

For development dependencies, use:

```bash
uv add --dev <package-name>
```

## 3. Run the Agent
Open a terminal and run the server with the dummy agent:

```bash
uv run .
```

or

```bash
uv run main.py
```

The agent will be running on `http://localhost:9999`.

## 4. Run the Test Client
Open a new terminal and run the test client:

```bash
uv run --active client.py
```
or

## In a new terminal, let's run the client with debug logging to get more details:
```bash
PYTHONUNBUFFERED=1 python -c "import asyncio; from client import main; asyncio.run(main())" --log-level=debug
```

You will see the client interact with the agent in the terminal output.

## References
- https://github.com/google/a2a-python
- https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#1

## After executing the client and you will see the client interact with the agent in the terminal output.

```bash

Fetching public agent card from: http://localhost:9999/.well-known/agent.json
Fetched public agent card
{
  "additionalInterfaces": null,
  "capabilities": {
    "extensions": null,
    "pushNotifications": null,
    "stateTransitionHistory": null,
    "streaming": null
  },
  "defaultInputModes": [
    "text"
  ],
  "defaultOutputModes": [
    "text"
  ],
  "description": "A simple agent that returns a greeting",
  "documentationUrl": null,
  "iconUrl": null,
  "name": "Greeting Agent",
  "preferredTransport": "JSONRPC",
  "protocolVersion": "0.3.0",
  "provider": null,
  "security": null,
  "securitySchemes": null,
  "signatures": null,
  "skills": [
    {
      "description": "Return a greeting",
      "examples": [
        "Hey",
        "Hello",
        "Hi"
      ],
      "id": "hello_world",
      "inputModes": null,
      "name": "Greet",
      "outputModes": null,
      "security": null,
      "tags": [
        "greeting",
        "hello",
        "world"
      ]
    }
  ],
  "supportsAuthenticatedExtendedCard": null,
  "url": "http://localhost:9999/",
  "version": "1.0.0"
}
A2AClient initialized
Sending message
Response:
{
  "id": "6465f07d-744e-42ac-8d1f-5d365e40c421",
  "jsonrpc": "2.0",
  "result": {
    "contextId": null,
    "extensions": null,
    "kind": "message",
    "messageId": "750200b7-24a7-4b68-b0e3-878b5a8aaf1d",
    "metadata": null,
    "parts": [
      {
        "kind": "text",
        "metadata": null,
        "text": "{'result': 'Hello YouTube! Make sure to like and subscribe!', 'status': 'success'}"
      }
    ],
    "referenceTaskIds": null,
    "role": "agent",
    "taskId": null
  }
}
```
