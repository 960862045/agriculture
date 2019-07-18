
import json
from .base import BaseHandler
from models.test_item import TestItem
from models.sample import Sample
from models.agricultural_product import Agricultural_Product
from  models.category import Category
from cattr import  unstructure

"""查询数据业务"""





class FindByEleHandler(BaseHandler):
    """根据成分查询数据"""
    def get(self):
        pass


    def post(self):
        pass


class FindByOriHandler(BaseHandler):
    """根据产地查询数据"""
    def get(self):
        # 获取要查询的产地名称
        origin = self.get_argument("origin", "")
        if not origin:
            return self.write("产地名称为空")
        try:
            items = Sample.select().where(Sample.origin == origin)
        except Exception:
            items = Sample()

        list = []
        # 遍历查询到的对象，转换为字典并添加进列表
        for item in items:
            dir = item.to_dir()
            list.append(dir)
            print(item.no)
        # 转化为json数据
        json1 = json.dumps(list)

        self.write(json1)


    def post(self):
        pass


class FindByCatHandler(BaseHandler):
    """根据农产品类别查询数据"""
    def get(self):
        pass

    def post(self):
        pass


class FindByProHandler(BaseHandler):
    """根据农产品查询数据"""

    def get(self):
        id = self.get_argument("id", "")
        if not id:
            return self.write("农产品id为空")
        try:
            product = Agricultural_Product.select().where(Agricultural_Product.id == id).get()
        except:
            product = Agricultural_Product()
        print(product.name)
        category_id = product.category_id
        try:
            category = Category.get(Category.id == category_id)
        except:
            category = Category()

        print(category.name)
        self.write("ok")




    def post(self):
        pass



