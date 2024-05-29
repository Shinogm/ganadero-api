import random
import asyncio
async def generate_aletory_int_6():
    return random.randint(100000, 999999)

async def main():
    numbdf = await generate_aletory_int_6()
    print(numbdf)

if __name__ == '__main__':
    asyncio.run(main())
    

