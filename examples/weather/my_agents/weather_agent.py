import json

from agents.model_settings import ModelSettings
from agents import Agent, FunctionTool, RunContextWrapper, function_tool
from typing_extensions import TypedDict

INSTRUCTIONS = (
    "You are an assistant who is good at checking the weather. You can check the weather at a specified time and location. If the user does not specify a time, it defaults to today"
)

class WeatherRequest(TypedDict):
    location: str
    date: str

@function_tool(name_override="fetch_weather")
async def fetch_weather(weather_request: WeatherRequest) -> str:
    """Check the weather conditions at a certain time and place

        Args:
            weather_request: request for fetching weather
        """

    data = {"data": "明天杭州的天气预报是晴天，气温约为22度，湿度为65%，风向为东南风。"}
    return json.dump(data)


weather_search_agent = Agent(
    name="Weather Assistant",
    instructions=INSTRUCTIONS,
    model="gpt-4o",
    tools=[fetch_weather],
    model_settings=ModelSettings(tool_choice="auto"),
)