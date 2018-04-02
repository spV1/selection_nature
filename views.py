from aiohttp import web
from app import process_text
import json
import spacy

app_model = web.Application()


async def load_models(request):
    try:
        data = await request.json()
        app_model['model'] = spacy.load(data['model'])

        response_obj = {'status': 'loaded'}
        return web.json_response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.json_response(text=json.dumps(response_obj), status=500)


async def text(request):
    try:
        data = await request.json()
        text_process = await process_text(data['text'], app_model['model'])

        return web.json_response(text=json.dumps(text_process), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}

        return web.json_response(text=json.dumps(response_obj), status=500)
