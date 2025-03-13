import asyncio

from .manager import ResearchManager


async def main() -> None:
    query = input("最新的关于DeepResearch的技术进展有哪些？")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())
