from fastapi import FastAPI, Form, Response, WebSocket
from typing import Annotated
from fastapi.staticfiles import StaticFiles

from simple_chain import chain as simple_chain
from packages.stream_chain.stream import chain as stream_chain
import random
import time


app = FastAPI()


# @app.post("/post_text")
# async def post_text(myTextArea: Annotated[str, Form()]):
#     async def generate():
#         async for part in stream_chain.stream({"text": myTextArea}):
#             print(part)
#             yield part
#     return Response(generate(), media_type="text/plain")


app.mount("/", StaticFiles(directory="static", html=True), name="app")


@app.websocket("/chatroom")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
