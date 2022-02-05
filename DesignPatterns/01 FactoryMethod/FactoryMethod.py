'''
工厂模式
区别：与简单工厂相比，简单工厂只有一个工厂，工厂模式有多个工厂，简单工厂的操作创建，是在同一个工厂中完成，而
工厂模式，是客户端选择调用不同的工厂
简单工厂的优势，就是工厂中封装了必要的逻辑判断，根据客户的条件动态的实例化相关的类，对客户端来说，除去了于具
体产品的依赖

工厂模式：是将本来简单工厂中的判断逻辑，挪到客户端，让业务自己选择所需要使用的工厂
'''


class FactoryBase(object):
    '''
    工厂基类
    '''
    
    def CreateFactory(self):
        '''
        创建最终的运算工厂
        :return:
        '''
        raise NotImplementedError


class AddFactory(FactoryBase):
    '''
    加法工厂
    '''
    def CreateFactory(self):
        '''
        最终返回加法类
        :return:
        '''
        return Add()


class MultiplicationFactory(FactoryBase):
    def CreateFactory(self):
        '''
        最终返回乘法类
        :return:
        '''
        return Multiplication()


class OperationBase(object):
    '''
    运算基类
    '''
    
    def __int__(self):
        '''
        自定义属性
        :return:
        '''
        self.Numbera = 0
        self.Numberb = 0
    
    def GetResult(self):
        '''
        重写运算符方法，直接调用基类报错
        :return:
        '''
        raise NotImplementedError


class Add(OperationBase):
    '''
    加法运算符
    '''
    def GetResult(self):
        return self.Numbera + self.Numberb


class Multiplication(OperationBase):
    '''
    乘法运算符
    '''
    def GetResult(self):
        return self.Numbera * self.Numberb


if __name__ == "__main__":
    # 最终工厂调用，是在业务端或者客户端
    factory = AddFactory()
    res = factory.CreateFactory()
    res.Numbera = 3
    res.Numberb = 4
    print(res.GetResult())
    
    factory = MultiplicationFactory()
    res = factory.CreateFactory()
    res.Numbera = 3
    res.Numberb = 4
    print(res.GetResult())
