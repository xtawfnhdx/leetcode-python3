'''
结构型：适配器模式
适用场景：尽量使用现有的类，将不能直接使用的类，增加一层嵌套
使接口不兼容的类，本来不能在一起工作，现在可以在一起工作
'''


class Adaptee(object):
    def GetRequest(self):
        return "这是一个最终结果"


class Target(object):
    '''
    通用业务抽象类，其他不使用适配器的具体类所抽象出来的类
    '''
    def Request(self):
        pass


class Adapter(Target):
    '''
    适配器
    '''
    _adaptee: Adaptee = None
    
    def __init__(self):
        '''
        适配器的核心，创建需要使用而不能直接用的类的实例，后续创建转换使用函数
        '''
        self._adaptee = Adaptee()
    
    def Request(self):
        '''
        创建的转换使用函数
        :return:
        '''
        return self._adaptee.GetRequest()
    
class Client(object):
    def __init__(self,target:Target):
        self._target=target
    def Res(self):
        print(self._target.Request())
        
if __name__=="__main__":
    ad=Adapter()
    cli=Client(ad)
    cli.Res()