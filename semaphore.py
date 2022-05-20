from aiodecorators import Semaphore
import asyncio

semaphore_limit = 5

@Semaphore(semaphore_limit)
async def task(i):
    print(i)
    await asyncio.sleep(5)

async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(20)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
