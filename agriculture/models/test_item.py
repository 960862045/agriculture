

from .base import BaseModel
from peewee import (
    CharField,

)

class TestItem(BaseModel):
    """检测指标类"""
    name = CharField()