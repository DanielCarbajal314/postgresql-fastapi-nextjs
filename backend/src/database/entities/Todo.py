from sqlalchemy import Column, String, DateTime
from .shared.IntegerIdEntity import IntegerIdEntity
from .shared.base import Base


class Todo(Base, IntegerIdEntity):
    __tablename__ = "todos"
    description = Column(String)
    name = Column(String)
    date = Column(DateTime)
