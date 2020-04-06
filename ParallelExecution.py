"""
    python 协程并发执行
"""

import asyncio
import time


async def a():
    print("欢迎使用 a ！")
    await asyncio.sleep(6)
    print("欢迎回到 a ！")


async def b():
    print("欢迎来到 b ！")
    await asyncio.sleep(8)
    print("欢迎回到 b ！")


async def c():
    print("欢迎来到 c ！")
    await asyncio.sleep(7)
    print("欢迎回到 c ！")


"""
    异步执行，几个任务并行执行，总耗时为= 单个任务中耗时最长的
"""


async def main():
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    task3 = asyncio.create_task(c())
    print("准备开始")

    await task2
    print("task2 结束")

    await task3
    print("task3 结束")

    await task1
    print("task1 结束")

"""
    异步执行，几个任务并行执行，总耗时为= 单个任务中耗时最长的
"""


async def main2():
    await asyncio.gather(a(), b(), c())


"""
    同步执行，耗时最长
"""


async def main3():
    await a()
    await b()
    await c()


if __name__ == "__main__":

    start = time.perf_counter()
    asyncio.run(main3())
    print('花费 {} s'.format(time.perf_counter() - start))