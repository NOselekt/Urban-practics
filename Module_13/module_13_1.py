import asyncio
import math


async def start_strongman(name='Zass', power=10):
    print(f'Strongman {name} has started competing')
    try:
        time_for_lifting = 10 / power
    except ZeroDivisionError:
        time_for_lifting = math.inf
        print(f'Unfortunately, the strongman {name} is too weak, he can\'t lift these balls.')
        return 1
    for i in range(1, 6):
        await asyncio.sleep(time_for_lifting)
        print(f'The strongman {name} has lifted the ball number {i}')


async def start_tournament():
    zass = asyncio.create_task(start_strongman())
    krylov = asyncio.create_task(start_strongman('krylov', 7))
    sandov = asyncio.create_task(start_strongman('sandov', 5))

    await zass
    await krylov
    await sandov


if __name__ == '__main__':
    asyncio.run(start_tournament())
