
from .base import BaseModel
from .category import Category

from peewee import (
    CharField,
    ForeignKeyField,
)




@attrs
class Agricultural_Product(BaseModel):
    """农产品类"""
    name = CharField()
    memo = CharField()
    category_id = ForeignKeyField(Category)

    class Meta:
        table_name = 'agricultural_product'















