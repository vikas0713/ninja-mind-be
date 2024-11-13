from fastapi import FastAPI
from rfid_ingestor.routes import router as rfid_routes

app = FastAPI()

# app.router.(rfid_routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
