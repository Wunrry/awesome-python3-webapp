import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(reuqest):
    return web.Response(body=b'<h1>INDEX</h1>',content_type='text/html')

app = web.Application()
app.add_routes(routes)
web.run_app(app,host='localhost',port=8000) 