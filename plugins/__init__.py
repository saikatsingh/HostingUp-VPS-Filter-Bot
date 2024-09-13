# Don't Remove Credit @AmRobots_Bots
# Subscribe YouTube Channel For Amazing Bot @AmRobotsTech
# Ask Doubt on telegram @Am_Robots

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
