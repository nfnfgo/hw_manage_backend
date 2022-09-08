import asyncio

import aiomysql

from . import config
from .pool import SQLPool


async def check(apikey=None) -> bool | str:
    '''Check if an APIKEY valid. If Valid, return true, else, return Err Msg'''
    # if key is empty
    if (apikey is None) or apikey == '':
        return 'Bad Request: Empty key not allowed'
    # estabilish sql conn
    try:
        pool = await SQLPool()
        async with pool.acquire() as conn:
            conn: aiomysql.Connection
            async with conn.cursor() as cursor:
                cursor: aiomysql.Cursor
                await cursor.execute('''SELECT user FROM apikey WHERE apikey=%s AND status=%s''', (apikey,1))
                af_rows = cursor.rowcount
    except Exception as e:
        print(e)
        return 'Internal Error: Failed to check APIKEY. Failed to connect to SQL server'
    # Check if it has valid apikey
    if af_rows == 0:
        return 'Bad Request: APIKEY not valid'
    else:
        return True
