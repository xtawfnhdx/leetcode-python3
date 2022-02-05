'''
简单工厂模式

适用场景：
1：适用方不需要知道具体实现类
2：当一个类希望由他的子类实现创建的过程
3：当类将创建职责委托给多个子类中的一个

优点：
1：隐藏了子类的创建逻辑

缺点：
1：违反了开闭原则，当需要增加功能，需要增加具体功能类以及修改工厂类
'''


class BaseSeting(object):
    '''
    基类或者抽象类，抽象出具体的方法
    '''
    
    def showMsg(self):
        pass


class Red(BaseSeting):
    '''
    具体实现类，实现具体功能
    '''
    
    def showMsg(self):
        print("this is red")


class Blue(BaseSeting):
    def showMsg(self):
        print("this is blue")


class Black(BaseSeting):
    def showMsg(self):
        print("this is black")


class Factory():
    '''
    工厂类，实现创建具体类的逻辑
    '''
    
    def CreateFactory(self, msg: str) -> BaseSeting:
        if msg == "red":
            return Red()
        elif msg == "blue":
            return Blue()
        else:
            return Black()


if __name__ == "__main__":
    # 创建工厂
    factory = Factory()
    
    # 工厂中具体创建过程隐藏
    product = factory.CreateFactory("blue")
    product.showMsg()
    
    product2 = factory.CreateFactory("abc")
    product2.showMsg()
