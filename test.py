import asyncio
import json

from sql import users as users
from sql import key_checker


async def main():
    info = await key_checker.check('123')
    print(info)
    # print(json.dumps(info))

# Test Part
if __name__ == '__main__':
    asyncio.run(main())
