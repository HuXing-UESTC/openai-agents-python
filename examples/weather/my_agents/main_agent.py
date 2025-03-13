from agents import Agent, InputGuardrail,GuardrailFunctionOutput, Runner
from .weather_agent import weather_search_agent
from .ding_agent import ding_send_agent

my_main_agent = Agent(
    name="我的助理",
    instructions="你擅长分发任务，根据用户的问题选择具体的助理去完成任务",
    handoffs=[weather_search_agent, ding_send_agent]
)
