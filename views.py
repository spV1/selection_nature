from aiohttp import web
from app import process_text
import json

async def text(request):
    try:
        data = await request.json()
        # print(data['text'])

        text_process = await process_text(data['text'])

        return web.json_response(text=json.dumps(text_process), status=200)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}

        return web.json_response(text=json.dumps(response_obj), status=500)

