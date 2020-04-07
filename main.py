import aiohttp_cors
from aiohttp import web
from routes import setup_routes
from config import defaults_cors

app = web.Application()
setup_routes(app)
cors = aiohttp_cors.setup(app, defaults=defaults_cors)
for route in list(app.router.routes()): cors.add(route)

if __name__ == '__main__':
    web.run_app(app)
