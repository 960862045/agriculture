
from .base import BaseModel
from peewee import (
    CharField,
    FixedCharField
)


"""用户相关类"""


class User(BaseModel):
    """用户类"""
    name = CharField()
    password = CharField()
    mobile = FixedCharField(11)

    class Meta:
        table_name = "user"




