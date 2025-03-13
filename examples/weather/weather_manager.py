from __future__ import annotations

import asyncio
import logging

from agents import Runner, custom_span, gen_trace_id, trace
from my_agents.main_agent import my_main_agent

class WeatherSearch:
    def __init__(self, logger: logging.Logger = None):
        self.logger = logger

    async def run(self, query: str) -> None:
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            result = await Runner.run(my_main_agent, query)
            print(f"\n\nresult = {result}")
