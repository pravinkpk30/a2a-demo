import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agent_executor import GreetingAgentExecutor


def main():
    # Define the agent's skill - this represents what the agent can do
    skill = AgentSkill(
        id="hello_world",
        name="Greet",
        description="Return a greeting",
        tags=["greeting", "hello", "world"],
        examples=["Hey", "Hello", "Hi"],
    )

    # Create an agent card that describes the agent's capabilities and metadata
    agent_card = AgentCard(
        name="Greeting Agent",
        description="A simple agent that returns a greeting",
        url="http://localhost:9999/",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        skills=[skill],
        version="1.0.0",
        capabilities=AgentCapabilities(),
    )

    # Set up the request handler with an in-memory task store
    # This handles incoming requests and manages task state
    request_handler = DefaultRequestHandler(
        agent_executor=GreetingAgentExecutor(),  # The actual implementation of the agent's logic
        task_store=InMemoryTaskStore(),          # Stores task state in memory (not persistent)
    )

    # Create the A2A application with our request handler and agent card
    server = A2AStarletteApplication(
        http_handler=request_handler,  # Handles HTTP requests
        agent_card=agent_card,         # Provides agent metadata
    )

    # Start the server using uvicorn
    # - host="0.0.0.0" makes the server available on all network interfaces
    # - port=9999 specifies the port to listen on
    uvicorn.run(server.build(), host="0.0.0.0", port=9999)


if __name__ == "__main__":
    main()  # Entry point of the application