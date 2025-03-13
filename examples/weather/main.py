import logging
import asyncio
import argparse
import os

from weather_manager import WeatherSearch


def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--api_key', dest='api_key', required=True,
        help='OpenAI API KEY'
    )
    options = parser.parse_args()
    return options

def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

async def main():
    options = define_options()
    os.environ['OPENAI_API_KEY'] = options.api_key
    query = input("请输入：")
    logger = setup_logger()
    weather_search = WeatherSearch(logger=logger)
    await weather_search.run(query)

if __name__ == '__main__':
    asyncio.run(main())
