from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World-dev"}


@app.get("/offer/{offer_id}")
async def get_offer(offer_id: int):
    return {"offer_id": offer_id}