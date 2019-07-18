
from .base import BaseModel
from peewee import (
    CharField,
    FixedCharField,
    IntegerField
)


"""用户相关类"""


class User(BaseModel):
    """用户类"""

    # 主键：id
    id = IntegerField(primary_key=True)
    # 用户名
    name = CharField()
    # 密码
    password = CharField()
    # 手机号
    mobile = FixedCharField(11)

    class Meta:
        table_name = "user"




