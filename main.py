"""Демомодуль для курса
shield"""

import asyncio


async def save():
    print('Сохраняю')
    await asyncio.sleep(2)
    print('Сохранено')


async def job():
    print('Работаю')
    t = asyncio.create_task(save())
    # await t
    await asyncio.shield(t)
    await asyncio.sleep(5)
    print('Готово')


async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(task.cancelled())
        print('Задача отменена')
    await asyncio.sleep(1)


asyncio.run(main())
