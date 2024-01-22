from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.staticfiles import StaticFiles

from simple_chain import chain as simple_chain
import random
import time


app = FastAPI()


@app.post("/post_text")
def post_text(myTextArea: Annotated[str, Form()]):
    return simple_chain.invoke({"text": myTextArea})


app.mount("/", StaticFiles(directory="static", html=True), name="app")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
