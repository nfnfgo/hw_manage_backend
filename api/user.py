'''Handle /user request'''


from ast import expr_context
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
    '''Deal with User List Acquaintance Request'''
    try:
        print(await request.json())
        req = await request.json()
    except:
        return web.Response(text='Invalid Json Body', status=400, headers=config.headers)
    try:
        apikey = req['apikey']
    except:
        apikey = None
    # This Method Need to check apikey
    api_check_res = await key_checker.check(apikey)
    if api_check_res != True:
        return web.Response(text=api_check_res, status=401)
    result = await users.get_user_list()
    return web.Response(content_type='application/json', text=json.dumps(result), headers=config.headers)


@user_route.post(config.api_url_suffix+'/user/point')
async def user_point(request: web.Request):
    '''Deal with requests about users point, such as changing point ans so on'''
    # if the input body can't be parsed as json, return error
    try:
        req = await request.json()
    except:
        return web.Response(text='Invalid Json Body', status=400, headers=config.headers)
    # Auth Key (opt about point is sensitive)
    try:
        apikey = req['apikey']
    except:
        apikey = None
    api_check_res = await key_checker.check(apikey)
    if api_check_res != True:
        return web.Response(text=api_check_res, status=401)

    # Start to respones with the request
    try:
        api_method = req['api_method']
    except:
        api_method = None

    # Deal with different API Method
    # Change Point Method
    if api_method == 'change_point':
        # read param
        try:
            user_id = req['user_id']
            d_point = req['d_point']
        except:
            return web.Response(text='Params Missing: user_id or d_point', status=400, headers=config.headers)
        # if params ok, start to retrive data from mySQL
        try:
            
        except:
            pass
        return web.Response(text='Request Success, but API is Developing...', status=404)

    # If no specified api_method
    return web.Response(text='No Specified api_method: change_point or ...', status=404)
