from aiohttp import web
from views import text, load_models


def setup_routes(app):
    app.add_routes([web.post('/text', text),
                    web.post('/models', load_models)])
