"""Демомодуль для курса
gather"""

import asyncio
# import time


async def fetch():
    # time.sleep(2)  # здеь хотим получить данные
    await asyncio.sleep(2)
    return 'done'


async def main():
    tasks = [fetch() for _ in range(100)]
    results = await asyncio.gather(*tasks)
    print(results)
    # for _ in range(3):
    #     print(fetch())


asyncio.run(main())
