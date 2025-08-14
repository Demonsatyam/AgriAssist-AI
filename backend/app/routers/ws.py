import asyncio
from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws/live")
async def ws_live(ws: WebSocket):
    await ws.accept()
    # Minimal mock stream
    chunks = [
        "Analyzing query...",
        "Retrieving weather...",
        "Computing irrigation window...",
        "Recommendation: Delay irrigation by 24–36 hours.",
    ]
    for c in chunks:
        await ws.send_text(c)
        await asyncio.sleep(0.25)
    await ws.close()