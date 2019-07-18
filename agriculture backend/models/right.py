

from peewee import(
    IntegerField,
    CharField,

)
from .base import BaseModel



class Right(BaseModel):
    """权限类"""


    # 主键：id
    id = IntegerField(primary_key=True)
    # 权限名称
    name = CharField()

    class Meta:
        table_name = "right"