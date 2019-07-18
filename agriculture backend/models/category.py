
from .base import BaseModel
from peewee import (
    CharField,
    IntegerField,
)


class Category(BaseModel):
    """农产品类别类"""

    # 主键：id
    id = IntegerField(primary_key=True)
    # 类别名称
    name = CharField()
    # 父类别id
    parent_id = IntegerField()

    class Meta:
        table_name = "category"