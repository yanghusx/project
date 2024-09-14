import asyncio
async def func():
     print("2")

c = func()
loop_i = asyncio.get_event_loop()
loop_i.run_until_complete(c)
