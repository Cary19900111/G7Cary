class AttrCheckMeta(type):
    def __new__(meta, cls, parent, attr_dict):
        import types
        attrs_checking_list=['__init__', '__del__', '__call__', '__str__', '__repr__', 
                    '__getattr__', '__setattr__', '__delattr__', '__getattribute__',
                    '__getitem__', '__setitem__', '__delitem__', '__iter__', '__next__',
                    '__contains__', '__get__', '__set__', '__delete__', '__lt__', 
                    '__le__', '__gt__', '__ge__', '__eq__', '__add__', '__iadd__', 
                    '__radd__', '__sub__', '__isub__', '__rsub__', '__mul__', '__imul__',
                    '__neg__', '__pos__', '__abs__', '__floordiv__', '__ifloordiv__', 
                    '__truediv__', '__itruediv__', '__mod__', '__imod__', '__imod__', 
                    '__pow__', '__ipow__', '__concat__', '__iconcat__', '__and__', 
                    '__iand__', '__or__', '__ior__', '__xor__', '__ixor__', '__inv__', 
                    '__invert__ ', '__lshift__', '__ilshift__', '__rshift__', '__irshift__ ',
                    '__bool__', '__len__', '__nonzero__', '__enter__', '__exit__',
                    '__new__', '__index__', '__oct__', '__hex__']
        print(attr_dict)
        for attr,value in attr_dict.items():
            #处理方法名前后都包含__，但是名字写错的情况。
            if attr[:2]=='__' and attr[-2:]=='__' and isinstance(value, types.FunctionType):
                print(attr)
                print(value)
                if attr not in attrs_checking_list:
                    print('found problem function: %s' % attr)
            #处理漏写后面__的情况，此时Python会把这个方法吗当成是需要扩张的方法。
            elif attr.startswith('_'+cls+'__') and isinstance(value, types.FunctionType):
                print('maybe has problem: %s' % attr)

        return super(AttrCheckMeta, meta).__new__(meta,cls, parent, attr_dict)
    def __init__(self,cls, parent, attr_dict):
        super(AttrCheckMeta, self).__init__(cls,parent, attr_dict)
    def __call__(self, *args, **kargs):
        return super(AttrCheckMeta, self).__call__(*args, **kargs)

class A(metaclass=AttrCheckMeta):
    '''在给函数命名时，对函数的名字进行检查'''
    def __new__(cls):
        return super(A, cls).__new__(cls)
    def __add(self, va, val):
        pass
    def __innit__(self):
        super(A, self).__init__()

class usecall(object):
    def __init__(self):
        self.name  = 1
    def __call__(self):
        print(self.name)

# u = usecall()
# u()
# a=A()