from agents.model_settings import ModelSettings
from agents import Agent, FunctionTool, RunContextWrapper, function_tool
from typing_extensions import TypedDict

INSTRUCTIONS = (
    "你是一个通知助理，你可以将指定的DING消息发送给用户"
)

class WeatherRequest(TypedDict):
    msg: str
    receiver: str

@function_tool(name_override="发送DING消息")
async def send_ding_msg(weather_request: WeatherRequest) -> bool:
    """发送指定的DING消息给指定用户

        Args:
            msg: DING消息的内容
            receiver: 接收人
        """

    return True


ding_send_agent = Agent(
    name="DING消息通知助理",
    instructions=INSTRUCTIONS,
    model="gpt-4o",
    tools=[send_ding_msg],
    model_settings=ModelSettings(tool_choice="required"),
)