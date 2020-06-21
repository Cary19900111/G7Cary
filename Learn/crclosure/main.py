'''
闭包的作用：1.保存上次的运行结果。2.类似配置的作用
'''
def add_step1(number1):
    '''如果在一个内部函数里，对在外部作用域（但不是在全局作用域）
    的变量进行引用，那么内部函数就被认为是闭包(closure)'''
    def add_step2(number2):
        result = number1+number2
        return result
    return add_step2

def nonlocal_cr():
    '''不能修改外部作用域的局部变量的'''
    foo = 10
    def add(number2):
        '''python规则指定所有在赋值语句左面的变量都是局部变量，
        add()中，变量foo在"="的左面，foo被认为是局部变量，
        查找foo的赋值语句，没找到，所以报错referenced before assignment
        不报错：加上nonlocal foo,修改外层的foo
    '''
        nonlocal foo
        foo = foo+number2
        return foo
    return add

if __name__ == '__main__':
    nc = nonlocal_cr()
    print(nc(10))
    print(nc(100))

