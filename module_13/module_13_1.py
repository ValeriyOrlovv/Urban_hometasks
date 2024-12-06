import asyncio


async def start_strongman(name, power):
    ball_number = 5
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, ball_number+1):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар {ball}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())