"""Демомодуль для курса
async await"""

import asyncio


async def get_messate():
    return 'Привет'


async def main():
    result = await asyncio.create_task(get_messate())
    print(result)

# main()

asyncio.run(main())
