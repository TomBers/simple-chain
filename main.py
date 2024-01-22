import time
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from packages.stream_chain.stream import chain
from fastapi.staticfiles import StaticFiles

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <p id='messages'>
        </p>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                
                var content = document.createTextNode(event.data)
                messages.appendChild(content)
                
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

app.mount("/gui", StaticFiles(directory="static", html=True), name="app")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    content = """
        <div hx-swap-oob="beforeend:#content">
        <p>{time}: {message}</p>
        </div>
    """
    while True:
        data = await websocket.receive_json()
        # await websocket.send_text(content.format(time=time.time(), message=data["chat_message"]))
        for chunk in chain.stream({"text": data["chat_message"]}):
            await websocket.send_text(content.format(time=time.time(), message=chunk))
