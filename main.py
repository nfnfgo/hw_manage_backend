import asyncio
import json

from aiohttp import web

import api

routes = web.RouteTableDef()


app = web.Application()
app.add_routes(api.root.root_route)
web.run_app(app, port=30000)
