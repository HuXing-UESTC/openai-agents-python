from agents import Agent, InputGuardrail,GuardrailFunctionOutput, Runner
from .weather_agent import weather_search_agent
from .ding_agent import ding_send_agent

my_main_agent = Agent(
    name="My Assistant",
    instructions="You are good at distributing tasks and selecting specific assistants to complete tasks based on user questions",
    model="gpt-4o",
    handoffs=[weather_search_agent, ding_send_agent]
)
