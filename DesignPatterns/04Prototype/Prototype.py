'''
原型模式：拷贝原有实体类，用原有实体类对象创建一个新的类的对象
'''
import copy


class Product(object):
    '''
    产品类，基于原型模式拷贝操作的具体实体类
    '''
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Prototype(object):
    '''
    原型实体类(虚拟类)
    '''
    
    def __init__(self):
        self.pro: Product = None
    
    def Clone(self) -> Product:
        '''
        原型方法的核心逻辑，拷贝逻辑，深拷贝或者浅拷贝，输出副本
        :return:
        '''
        obj = copy.deepcopy(self.pro)
        return obj


class ConcretePrototypeA(Prototype):
    '''
    继承原型模式，实现拷贝操作
    '''
    
    def __init__(self, pro: Product):
        self.pro = pro


class ConcretePrototypeB(Prototype):
    def __init__(self, pro: Product):
        self.pro = pro


if __name__ == "__main__":
    ca = ConcretePrototypeA(Product("张三", 16))
    print(ca.pro.name, ca.pro.age)
    # 创建产品的副本，但是不影响产品本身
    cb = ca.Clone()
    cb.age = 18
    print(ca.pro.name, ca.pro.age)
    print(cb.name, cb.age)
