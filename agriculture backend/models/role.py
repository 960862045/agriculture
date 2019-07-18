
from .base import BaseModel
from peewee import(
    IntegerField,
    CharField
)


class Role(BaseModel):
    """角色类"""

    # 主键：id
    id = IntegerField(primary_key=True)
    # 角色名称
    name = CharField()

    class Meta:
        table_name = "role"
