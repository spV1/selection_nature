from aiohttp import web
from views import text

def setup_routes(app):
    app.add_routes([web.post('/post', text)])

