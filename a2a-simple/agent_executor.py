# Import necessary modules from A2A SDK and Pydantic
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message
from pydantic import BaseModel


class GreetingAgent(BaseModel):
    """
    A simple greeting agent that generates a greeting message.
    This is a Pydantic model that represents the core logic of the agent.
    """

    async def invoke(self) -> str:
        """
        Generates and returns a greeting message.
        
        Returns:
            str: A greeting message string
        """
        return "Hello YouTube! Make sure to like and subscribe!"


class GreetingAgentExecutor(AgentExecutor):
    """
    Executor class that handles the agent's execution lifecycle.
    Implements the AgentExecutor interface from A2A SDK.
    """

    def __init__(self):
        """Initialize the executor with a GreetingAgent instance."""
        self.agent = GreetingAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        """
        Execute the agent's main logic and enqueue the result as an event.
        
        Args:
            context: The request context containing metadata about the current request
            event_queue: Queue for sending events (like responses) back to the client
        """
        # result = await self.agent.invoke()
        # event_queue.enqueue_event(new_agent_text_message(result))

        try:
            # Get the result from the agent
            result = await self.agent.invoke()
            
            # Create a response with the result
            response = {
                "result": result,
                "status": "success"
            }
            
            # Enqueue the response
            await event_queue.enqueue_event(new_agent_text_message(str(response)))
        
        except Exception as e:
            # Handle any errors that occur during execution
            error_response = {
                "error": str(e),
                "status": "error"
            }
            await event_queue.enqueue_event(new_agent_text_message(str(error_response)))
            raise

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        """
        Handle cancellation of the agent's execution.
        
        Args:
            context: The request context
            event_queue: Queue for sending cancellation events
            
        Raises:
            Exception: Always raises an exception as cancellation is not supported
        """
        raise Exception("Cancel not supported")