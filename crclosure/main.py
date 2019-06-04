def add_step1(number1):
    '''内部函数能引用外部变量，那么内部函数就被认为是闭包'''
    def add_step2(number2):
        result = number1+number2
        return result
    return add_step2


if __name__ == '__main__':
    step2 = add_step1(100)
    print(step2(900))
