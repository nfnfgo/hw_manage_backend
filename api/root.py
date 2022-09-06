
import asyncio

from aiohttp import web
import api.config

root_route = web.RouteTableDef()

# Receive Post request


@root_route.post(api.config.api_url_suffix + '/')
async def hello(request: web.Request):
    print(await request.json())
    return web.Response(content_type='application/json', text='''{"msg": "Hello, world"}''')
