from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import httpx

from .config import get_var


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

    async with httpx.AsyncClient() as client:
        response = await client.post('https://api.46elks.com/a1/calls', auth=auth, data=data)
    return response.json()


if get_var('call_serve_frontend') == 'yes':
    app.mount('/', StaticFiles(directory='frontend', html=True), name='frontend')
