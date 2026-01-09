"""Демомодуль для курса
Обработка ошибок"""

import asyncio


async def good():
    print('Начата good')
    return 1


async def bad():
    print('Начата bad')
    raise ValueError('Ошибка')
    # return 1


async def main():
    # # try:
    # #     # res = await asyncio.create_task(bad())
    # #     task = asyncio.create_task(bad())
    # #     await asyncio.sleep(2)
    # #     print('Ждем')
    # #     await task
    # #     # print(res)
    # # except ValueError as e:
    # #     print(e)
    # task = asyncio.create_task(bad())
    # task.add_done_callback(lambda t: print('Ошибочка', t.exception()))
    try:
        result = await asyncio.gather(bad(), good(), return_exceptions=True)
        print(result)
    # except ValueError as e:
    except ValueError as e:
        print(e)


asyncio.run(main())
