import gevent
import time
def test1():
    n = 0
    while(1):
        if n<5:
            print(1111)
            n +=1
            time.sleep(1)
        else:
            break

if __name__=="__main__":
    greenlet = gevent.spawn(test1)
    greenlet.join()
    print("end")