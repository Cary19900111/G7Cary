from contextlib import contextmanager

@contextmanager
'''
在函数test中间加一段with语句下面的程序。作为test中yied的上下文
'''
def test():
    a = 1
    c = 3
    print(a)
    yield
    print(c)

if __name__=='__main__':
    with test():
        print(4)
    print("now")