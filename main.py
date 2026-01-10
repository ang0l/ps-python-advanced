"""Демомодуль для курса
Task vs Coroutine"""

import asyncio


async def save():
    print('Сохраняю')
    await asyncio.sleep(2)
    print('Сохранено')
    raise ValueError('e')
    return 1


async def job():
    print('Работаю')
    t = save()
    # t = asyncio.create_task(save())
    # await asyncio.shield(t)
    # await t
    try:
        res = await t
        print(res)
    except ValueError:
        print('Ошибка')
    await asyncio.sleep(5)
    print('Готово')


async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    # task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(task.cancelled())
        print('Задача отменена')
    await asyncio.sleep(1)


asyncio.run(main())
