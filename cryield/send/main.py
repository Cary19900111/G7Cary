import time,random
def product():
    t = 0
    while True:
        num = yield t#send传递进来的值相当于yield的返回值，并赋值给num
        print("Product {}".format(num))
def consume():
    p = product()
    p.send(None)#第一次是发送的None，到达yield.也可以next(p)
    while True:
        time.sleep(2)
        num = random.randint(1,10)
        p.send(num)
        print("Consum {}".format(num))
if __name__=='__main__':
    c = consume()
