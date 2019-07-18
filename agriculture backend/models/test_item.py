
from models.category import Category
from models.agricultural_product import Agricultural_Product
from models.sample import Sample
from .base import BaseModel

from peewee import (
    CharField,
    ManyToManyField,

)

class TestItem(BaseModel):
    """检测指标类"""

    # 主键：检测指标名称
    name = CharField(primary_key=True)

    class Meta:
        table_name = "test_item"