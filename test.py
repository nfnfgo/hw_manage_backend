import asyncio
import json

from sql import users as users


async def main():
    info = await users.get_user_list('test')
    print(info)
    # print(json.dumps(info))

# Test Part
if __name__ == '__main__':
    for i in range(1):
        asyncio.run(main())
