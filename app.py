from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from db.database import SessionLocal, engine
from db import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()

@app.get("/")
async def root():
    return {"message": "Hello World-dev"}


@app.post("/offers/", response_model=schemas.Offer)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = crud.get_offer_by_title(db, offer_title=offer.title)
    if db_offer:
        raise HTTPException(status_code=400, detail="Offer with same name already exists")
    return crud.create_offer(db=db, offer=offer)

@app.get("/offers/{offer_id}", response_model=schemas.Offer)
def get_offer(offer_id: int, db: Session = Depends(get_db)):
    offer = crud.get_offer(db, offer_id)
    return offer

@app.get("/offers/", response_model=List[schemas.Offer])
def get_offers(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    offers = crud.get_offers(db, skip, limit)
    return offers

@app.post("/knowmore/")
def know_more(email: str, db: Session = Depends(get_db)):
    email = crud.know_more(db, email)
    return email

