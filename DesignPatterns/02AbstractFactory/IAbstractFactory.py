'''
抽象工厂模式
抽象工厂定义了所有产品的抽象实现，客户端只需要调用不同的具体工厂，就可以使用相同的方式创建不同的产品
需要将产品抽象，需要将工厂抽象
客户端通过抽象工厂操作实例，产品的具体类名也被具体的工厂实现分离，不会出现在客户端代码中

简单来说就是
工厂方法：创建某一种产品
抽象工厂：创建某一类产品
'''


# region 抽象产品接口

class IAbstractProductA(object):
    '''
    抽象产品A
    '''
    
    def __init__(self):
        self.Name = ""
    
    def ShowMsg(self):
        raise NotImplementedError


class IAbstractProductB(object):
    '''
    抽象产品B
    '''
    Name = ""
    
    def ShowMsg(self):
        raise NotImplementedError


# endregion

# region 抽象工厂接口

class IAbstractFactory(object):
    '''
    抽象工厂，包含了所有产品的抽象创建方法
    '''
    
    def CreateProductA(self) -> IAbstractProductA:
        raise NotImplementedError
    
    def CreateProductB(self) -> IAbstractProductB:
        raise NotImplementedError


# endregion

# region 具体工厂创建类

class ContreteFactoryA(IAbstractFactory):
    '''
    具体工厂类，实现了具体产品的创建
    '''
    
    def CreateProductA(self) -> IAbstractProductA:
        return ProductA1()
    
    def CreateProductB(self) -> IAbstractProductB:
        return ProductB1()


class ContreteFactoryB(IAbstractFactory):
    def CreateProductA(self) -> IAbstractProductA:
        return ProductA2()
    
    def CreateProductB(self) -> IAbstractProductB:
        return ProductB2()


# endregion

# region 具体产品创建类
class ProductA1(IAbstractProductA):
    def __init__(self):
        self.Name = "ProductA1"
    
    def ShowMsg(self):
        print(self.Name)


class ProductA2(IAbstractProductA):
    def __init__(self):
        self.Name = "ProductA2"
    
    def ShowMsg(self):
        print(self.Name)


class ProductB1(IAbstractProductB):
    def __init__(self):
        self.Name = "ProductB1"
    
    def ShowMsg(self):
        print(self.Name)


class ProductB2(IAbstractProductB):
    def __init__(self):
        self.Name = "ProductB2"
    
    def ShowMsg(self):
        print(self.Name)


# endregion

if __name__ == "__main__":
    f = ContreteFactoryA()
    pa = f.CreateProductA()
    pb = f.CreateProductB()
    pa.ShowMsg()
    pb.ShowMsg()
    
    f = ContreteFactoryB()
    pa = f.CreateProductA()
    pb = f.CreateProductB()
    pa.ShowMsg()
    pb.ShowMsg()
