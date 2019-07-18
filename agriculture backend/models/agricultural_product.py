
from .base import BaseModel
from .category import Category

from peewee import (
    CharField,
    ForeignKeyField,
    IntegerField,

)





class Agricultural_Product(BaseModel):
    """农产品类"""
    # 主键：id
    id =  IntegerField(primary_key=True)
    # 农产品名称
    name = CharField()
    # 备注
    memo = CharField()
    # 外键：农产品类别ID
    category_id = ForeignKeyField(Category)

    class Meta:
        table_name = 'agricultural_product'















