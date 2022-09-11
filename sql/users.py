'''SQL Functions About users'''

import asyncio

import aiomysql

from .pool import SQLPool


# Get User List of ALL Users.
async def get_user_list() -> list | str:
    '''(Asynchronous) Get A List of Dict Object that contain every single user's info

    Return:
    List.
    e.g. [{'id':10001, 'name':'xxx',....}, {...}, {...}]

    If failed. return string type err msg'''
    # Get a conn pool
    try:
        pool = await SQLPool()
        async with pool.acquire() as conn:
            conn: aiomysql.Connection
            async with conn.cursor() as cursor:
                await conn.commit()
                cursor: aiomysql.Cursor
                await cursor.execute('''SELECT * FROM users ORDER by point DESC''')
                res = await cursor.fetchall()
    except:
        return 'Internal Error: Cannot connected to SQL Server'
    # If data got succesfully, start to format the info
    user_list = []
    # NEED REWRITE
    # use specified mark but NOT Sequence
    for single_user in res:
        single_user_dict = {}
        single_user_dict['id'] = single_user[0]
        single_user_dict['name'] = single_user[1]
        single_user_dict['status'] = single_user[2]
        single_user_dict['point'] = single_user[3]
        user_list.append(single_user_dict)
    return user_list


async def change_user_point() -> dict | str:
    '''(Asynchronous) Change the user point
    
    Params:
    user_id: Unique ID of user
    d_point: Means delta_point.

    Returns:
    dict_info: Dict type.
    '''
    # Get a conn pool
    try:
        pool = await SQLPool()
        async with pool.acquire() as conn:
            conn: aiomysql.Connection
            async with conn.cursor() as cursor:
                await conn.commit()
                cursor: aiomysql.Cursor
                await cursor.execute('''SELECT * FROM users ORDER by point DESC''')
                res = await cursor.fetchall()
    except:
        return 'Internal Error: Cannot connected to SQL Server'
    # If data got succesfully, start to format the info
    user_list = []
    for single_user in res:
        single_user_dict = {}
        single_user_dict['id'] = single_user[0]
        single_user_dict['name'] = single_user[1]
        single_user_dict['status'] = single_user[2]
        single_user_dict['point'] = single_user[3]
        user_list.append(single_user_dict)
    return user_list
