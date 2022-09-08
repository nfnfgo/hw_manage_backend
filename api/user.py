'''Handle /user request'''


import asyncio
import json
from operator import truediv

from aiohttp import web

from . import config
from sql import users
from sql import key_checker

user_route = web.RouteTableDef()


# Receive Post request
@user_route.post(config.api_url_suffix + '/user/list')
async def user_list(request: web.Request):
    headers = {'Access-Control-Allow-Origin':'*'}
    try:
        print(await request.json())
        req = await request.json()
    except:
        return web.Response(text='Valid Json Body', status=400,headers=config.headers)
    try:
        apikey = req['apikey']
    except:
        apikey = None
    # This Method Need to check apikey
    api_check_res = await key_checker.check(apikey)
    if api_check_res != True:
        return web.Response(text=api_check_res, status=401)
    result = await users.get_user_list()
    return web.Response(content_type='application/json', text=json.dumps(result),headers=config.headers)
