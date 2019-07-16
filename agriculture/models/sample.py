
from .base import BaseModel
from peewee import (
    CharField,
    DateTimeField
)



class Sample(BaseModel):
    """样品类"""
    no = CharField()
    origin = CharField()
    source = CharField()
    memo = CharField()