from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from typing import Annotated


from simple_chain import chain as simple_chain


from fastapi.requests import Request
from fastapi.responses import HTMLResponse

import random
import time


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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
