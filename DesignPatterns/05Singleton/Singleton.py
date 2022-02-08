'''
单例模式
'''


# region 函数装饰器方式

def Single(cls):
    _include = {}
    
    def inner():
        if cls not in _include:
            _include[cls] = cls()
        return _include[cls]
    
    return inner


@Single
class TestA(object):
    def __init__(self):
        pass


@Single
class TestB(object):
    def __init__(self):
        pass


# endregion

# regino 类装饰器

class SingleClass(object):
    def __init__(self, cls):
        self._cls = cls
        self._inspect = {}
    
    def __call__(self):
        if self._cls not in self._inspect:
            self._inspect[self._cls] = self._cls()
        return self._inspect[self._cls]


@SingleClass
class TestCA():
    def __init__(self):
        pass


# endregion

# region new方法实现单例

class TestSingle(object):
    _inspect = None
    
    def __new__(cls, *args, **kwargs):
        if cls._inspect is None:
            cls._inspect = object.__new__(cls, *args, **kwargs)
        return cls._inspect
    
    def __init__(self):
        pass


# endregion
if __name__ == "__main__":
    ta1 = TestA()
    ta2 = TestA()
    print(id(ta1), id(ta2))
    
    tb1 = TestB()
    tb2 = TestB()
    print(id(tb1), id(tb2))
    
    tca1 = TestCA()
    tca2 = TestCA()
    
    tca3 = SingleClass(TestCA)
    tca4 = tca3()
    tca5 = tca3()
    print(id(tca1), id(tca2))
    print(id(tca4), id(tca5))
    
    tg1 = TestSingle()
    tg2 = TestSingle()
    print(id(tg2), id(tg2))
