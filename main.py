"""Демомодуль для курса
wait и wait_for"""

import asyncio
import aiohttp


# Полученние в задачах параллельно 10 раз обращение к google.com

async def fetch(session, url):
    return await asyncio.wait_for(session.get(url), timeout=2)


async def main():
    urls = ['https://google.com'] * 10
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]

        done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        results = [task.result() for task in done]
        print(list(map(lambda x: x.status, results)))

asyncio.run(main())
