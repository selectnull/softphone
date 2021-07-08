from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import httpx

from pathlib import Path
import logging
import json

from .config import get_var

LOG_FILE = Path.home() / 'logs' / 'phone.logit.net.log'
logging.basicConfig(
    filename=LOG_FILE,
    encoding='utf-8', level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

app = FastAPI()


class VoiceStart(BaseModel):
    connect: str


class Call(BaseModel):
    from_number: str
    to_number: str
    voice_start: str
    api_username: str
    api_password: str


@app.get('/api/status')
async def status():
    return {'status': 'ok', 'version': 1}


@app.post('/api/forward')
async def forward(call: Call):
    auth = (call.api_username, call.api_password)
    data = {
        'from': call.from_number,
        'to': call.to_number,
        'voice_start': call.voice_start
    }

    to_number = json.loads(data['voice_start'])['connect']
    log_msg = f'Outgoing call from {call.from_number} to {to_number}'
    logging.info(log_msg)

    async with httpx.AsyncClient() as client:
        response = await client.post('https://api.46elks.com/a1/calls', auth=auth, data=data)
    return response.json()


@app.post('/api/receive-call/{connect_to_phone}')
async def receive_call(
    connect_to_phone: int,
    direction: str = Form(...),
    callid: str=Form(...),
    from_number: str=Form(..., alias='from'),
    to_number: str=Form(..., alias='to')
):
    log_msg = f'Incoming call from {from_number} to {to_number}'
    logging.info(log_msg)
    return {
        'connect': f'+{connect_to_phone}'
    }


if get_var('call_serve_frontend') == 'yes':
    app.mount('/', StaticFiles(directory='frontend', html=True), name='frontend')
