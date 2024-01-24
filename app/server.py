from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.staticfiles import StaticFiles


from packages.tool_chain.tool_chain import agent_executor
import pdb

app = FastAPI()


@app.post("/post_text")
def post_text(myTextArea: Annotated[str, Form()]):
    print("Welcome to Tools")
    return agent_executor.invoke({"input": myTextArea}).get("output", "No Output")


app.mount("/", StaticFiles(directory="static", html=True), name="app")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
