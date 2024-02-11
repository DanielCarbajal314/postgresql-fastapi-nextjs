from sqlalchemy import Column, String, DateTime
from .shared.BaseEntity import BaseEntity

class Todo(BaseEntity):
    description = Column(String)
    date = Column(DateTime)