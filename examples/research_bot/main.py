import asyncio

from manager import ResearchManager


async def main() -> None:
    query = input("请输入：")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())
