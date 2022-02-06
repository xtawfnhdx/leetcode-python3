'''
创建者模式
创建这模式，有两个核心类，一个是指挥者，一个是创建者
创建者：创建者定义了创建产品的所有功能(有哪些功能)
指挥者：指挥者定了创建产品的步骤(功能执行的先后顺序)

使用场景：
创建产品有相对稳定的创建步骤，而每个步骤的创建又相对比较复杂
Builder隐藏了具体的组装逻辑，所以如果需要重新构建内部逻辑，则需要重新创建一个引用了Builder的构造者

'''


class Builder(object):
    '''
    创建者:创建者定义了生成产品有哪些步骤(创建一个产品的各个部分的抽象接口)
    '''
    type = ""
    
    def BuilderHead(self):
        raise NotImplementedError
    
    def BuilderPart(self):
        raise NotImplementedError
    
    def BuilderHand(self):
        raise NotImplementedError
    
    def GetResult(self):
        raise NotImplementedError


class Director(object):
    '''
    指挥者：指挥者定义了生成产品步骤的先后顺序(构造使用Builder接口的对象)
    '''
    
    def __init__(self, builder: Builder):
        '''
        初始化Builder
        :param builder:
        '''
        self.builder = builder
    
    def Constryct(self) -> Builder:
        self.builder.BuilderPart()
        self.builder.BuilderHand()
        self.builder.BuilderHead()
        self.builder.GetResult()


class Person(object):
    '''
    具体的产品，创建者和指挥者
    '''
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class ContreteBuilder(Builder):
    def __init__(self):
        self.people: Person
        self.type = "胖子"
    
    def BuilderPart(self):
        self.people = Person("张三", 16)
    
    def BuilderHand(self):
        pass
    
    def BuilderHead(self):
        pass
    
    def GetResult(self):
        print(self.people.name, self.people.age)


if __name__ == "__main__":
    fat = ContreteBuilder()
    dir = Director(fat)
    dir.Constryct()
