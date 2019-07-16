
from .base import BaseModel
from peewee import CharField


class Role(BaseModel):
    """角色类"""
    name = CharField

    class Meta:
        table_name = "role"
