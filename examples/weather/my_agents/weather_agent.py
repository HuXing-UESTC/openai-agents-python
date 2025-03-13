from agents.model_settings import ModelSettings
from agents import Agent, FunctionTool, RunContextWrapper, function_tool
from typing_extensions import TypedDict

INSTRUCTIONS = (
    "你是一个擅长查询天气的助理，可以查询指定时间、指定地点的天气， 如果用户没有指明时间，那么默认是今天"
)

class WeatherRequest(TypedDict):
    location: str
    date: str

@function_tool(name_override="查询天气")
async def fetch_weather(weather_request: WeatherRequest) -> str:
    """查询某个时间某个地点的天气情况

        Args:
            location: 查询的地点、城市名
            date: 查询的日期
        """

    return "明天杭州的天气预报是晴天，气温约为22度，湿度为65%，风向为东南风。"

@function_tool(name_override="上报天气")
async def upload_weather(data: str) -> bool:
    """将天气信息上报到表单

        Args:
            data: 天气信息
        """

    return True

weather_search_agent = Agent(
    name="天气助理",
    instructions=INSTRUCTIONS,
    model="gpt-4o",
    tools=[fetch_weather, upload_weather],
    model_settings=ModelSettings(tool_choice="required"),
)