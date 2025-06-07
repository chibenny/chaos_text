from dataclasses import dataclass, field
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from chaos_text import make_rage

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")


@dataclass
class Request:
    rage_input: str
    extra_rage: int = field(default=0)
    chaos_mode: int = field(default=0)


@app.get("/")
async def home():
    return FileResponse("index.html")


@app.post("/entropy")
async def make_some_chaos(payload: Request):
    return {"result": make_rage(**payload.__dict__)}
