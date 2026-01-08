"""Демомодуль для курса
Упражнение - Параллельные запросы"""

import asyncio
import aiohttp


# Полученние в задачах параллельно 10 раз обращение к google.com

async def main():
    urls = ['https://google.com'] * 10
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]

        result = await asyncio.gather(*tasks)
        print(list(map(lambda x: x.status, result)))

asyncio.run(main())
