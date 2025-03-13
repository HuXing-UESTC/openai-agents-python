import logging
import asyncio
from weather_manager import WeatherSearch


def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

async def main():
    query = input("请输入：")
    logger = setup_logger()
    weather_search = WeatherSearch(logger=logger)
    await weather_search.run(query)

if __name__ == '__main__':
    asyncio.run(main())
