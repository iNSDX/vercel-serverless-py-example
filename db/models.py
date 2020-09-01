from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    creator = Column(String, index=True)
    title = Column(String)
    description = Column(String)

class KnowMoreContact(Base):
    __tablename__ = 'know_more'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
