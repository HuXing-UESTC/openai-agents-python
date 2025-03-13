from agents.model_settings import ModelSettings
from agents import Agent, FunctionTool, RunContextWrapper, function_tool
from typing_extensions import TypedDict

INSTRUCTIONS = (
    "You are a notification assistant who can send specified DING messages to users"
)

class WeatherRequest(TypedDict):
    msg: str
    receiver: str

@function_tool(name_override="Send DING Message")
async def send_ding_msg(weather_request: WeatherRequest) -> bool:
    """Send the specified DING message to the designated user

        Args:
            msg: The content of the DING message
            receiver: Recipient's name
        """

    return True


ding_send_agent = Agent(
    name="DING Message Notification Assistant",
    instructions=INSTRUCTIONS,
    model="gpt-4o",
    tools=[send_ding_msg],
    model_settings=ModelSettings(tool_choice="required"),
)