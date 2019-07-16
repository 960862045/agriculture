
from .base import BaseModel
from peewee import (
    CharField,
    IntegerField,
)


class Category(BaseModel):
    """农产品类别类"""
    name = CharField()
    parent_id = IntegerField()

    class Meta:
        table_name = "category"