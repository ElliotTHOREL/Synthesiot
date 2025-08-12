import asyncio

def function_a() :
    asyncio.run(function_b())

async def function_b() :
    function_c()

def function_c():
    asyncio.run(une_fonction_async_toute_bête())

async def une_fonction_async_toute_bête():
    print("une_fonction_async_toute_bête")


if __name__ == "__main__":
    function_a()