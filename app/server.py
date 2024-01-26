from fastapi import FastAPI, Form, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from typing import Annotated


from simple_chain import chain as simple_chain

from packages.ws_connection_manager.connection_manager import manager
from packages.ws_connection_manager.ws_response import ws_response

from fastapi.requests import Request
from fastapi.responses import HTMLResponse

import random

from coolname import generate_slug


div_id = "chat-content"

app = FastAPI()

templates = Jinja2Templates(
    directory="pages", autoescape=True, auto_reload=True)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request
        },
    )


@app.get("/demo", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        name="demo.html",
        context={
            "request": request
        },
    )


@app.get("/chat", response_class=HTMLResponse)
async def chat(request: Request):
    return templates.TemplateResponse(
        name="chat_ws.html",
        context={
            "request": request,
            "client_id": generate_slug(2),
            "div_id": div_id
        },
    )


@app.post("/post_text", response_class=HTMLResponse)
def post_text(request: Request, myTextArea: Annotated[str, Form()], myTextInput: Annotated[str, Form()] = ""):
    # return simple_chain.invoke({"text": myTextArea})

    return templates.TemplateResponse(
        name="response.html",
        context={
            "request": request,
            "question": myTextArea,
            "input": myTextInput,
            "answer": random.randint(1, 29) * "🤖"
        },
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            res = ws_response(data["client_id"], data["message"], div_id)
            await manager.broadcast(res)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client left the chat")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
