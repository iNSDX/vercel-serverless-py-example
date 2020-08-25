from typing import List, Optional
from pydantic import BaseModel

class OfferBase(BaseModel):
    creator: str
    title: str
    description: str

class OfferCreate(OfferBase):
    pass

class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True
