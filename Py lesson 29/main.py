# I

# import asyncio
#
#
# async def delay_1():
#     print("Started (task 1)")
#     await asyncio.sleep(2)
#     print("Finished (task 1)")
#
#
# async def delay_2():
#     print("Started (task 2)")
#     await asyncio.sleep(5)
#     print("Finished (task 2)")
#
#
# async def main():
#     await asyncio.gather(delay_1(), delay_2())
#
# asyncio.run(main())


# II

import asyncio
import random


async def random_number():
    rand_numb = random.randint(1, 10)
    print(f"{rand_numb} seconds delay")
    i = 1
    while i <= 10:
        print(i)
        await asyncio.sleep(rand_numb)
        i += 1

asyncio.run(random_number())
