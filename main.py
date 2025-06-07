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

    def __post_init__(self):
        # Don't try to rage text War and Peace
        self.rage_input = self.rage_input[:5000]


@app.get("/")
async def home():
    return FileResponse("index.html")


@app.post("/entropy")
async def make_some_chaos(payload: Request):
    return {"result": make_rage(**payload.__dict__)}
