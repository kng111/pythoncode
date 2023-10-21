import asyncio

async def my_async_function():
    print("1 str")
    await asyncio.sleep(2)
    print("2 str")

asyncio.run(my_async_function())