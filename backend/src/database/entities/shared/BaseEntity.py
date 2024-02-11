from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseEntity(Base):
    id = Column(Integer, primary_key=True, autoincrement="auto")