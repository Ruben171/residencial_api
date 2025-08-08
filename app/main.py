from fastapi import FastAPI
from pydantic import BaseModel
from app.shemas import EchoIn, EchoOut
from app.utils import count_chars

# Criar a app FastAPI
app = FastAPI(
    title="Residencial API",
    version="0.1.0",
    description="API de treino para aprender backend"
)

#modelo pydantic simples para o endpoint raiz
class PingResponse(BaseModel):
    message:str

@app.get("/", response_model=PingResponse)
async def root():
    return PingResponse(message="API Online")

#endpoint helath (serve como monitorização)
@app.get("/health")
async def health():
    return {"status": "ok"}

#endpoint echo responde a pedidos post
@app.post("/echo")
async def echo(payload: EchoIn):
    length = count_chars(payload.text)
    return EchoOut(text=payload.text, length=length)

@app.get("/status/{name}")
async def status_for(name:str):
    return {"status": f"Hello, {name}. Tudo ok por aqui!"}

