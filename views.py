from aiohttp import web
from app import process_text
import json
import spacy

models_ = []


async def load_models(request):
    try:
        data = await request.json()
        models_.append(spacy.load(data['model']))

        response_obj = {'status': 'loaded'}
        return web.json_response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.json_response(text=json.dumps(response_obj), status=500)


async def text(request):
    try:
        data = await request.json()
        # print(models_[0])
        text_process = await process_text(data['text'], models_[0])

        return web.json_response(text=json.dumps(text_process), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}

        return web.json_response(text=json.dumps(response_obj), status=500)
