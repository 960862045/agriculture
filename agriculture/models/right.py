

from peewee import CharField
from .base import BaseModel



class Right(BaseModel):
    """权限类"""
    name = CharField()

    class Meta:
        table_name = "right"