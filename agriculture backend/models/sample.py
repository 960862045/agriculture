from attr import attrs
from .base import BaseModel
from models.agricultural_product import Agricultural_Product
from peewee import (
    CharField,
    DateTimeField,
    ForeignKeyField,
)



class Sample(BaseModel):
    """样品类"""

    # 编号
    no = CharField(primary_key=True)
    # 产地
    origin = CharField()
    # 来源
    source = CharField()
    # 备注
    memo = CharField()
    # 外键：农产品ID
    product_id = ForeignKeyField(Agricultural_Product.id)

    class Meta:
        table_name = "sample"



    def to_dir(self):
        sample_dir = {
            "no":self.no,
            "origin":self.origin,
            "source":self.source,
            "memo":self.memo
        }
        return sample_dir
