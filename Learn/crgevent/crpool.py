from gevent.pool import Group
import gevent
import time

def green1(str1,str2):
    while(1):
        print("{}{}".format(str1,str2))
        gevent.sleep(1)
def green2(str2):
    while(1):
        print(str2)
        gevent.sleep(1)

def green3(str3):
    while(1):
        print(str3)
        gevent.sleep(1)

# def killAll():

def Groupadd():
    group = Group()
    g1 = gevent.spawn(green1,"green1"," so green")
    g2= gevent.spawn(green2,"green2")
    g3 = gevent.spawn(green3,"green3")
    group.add(g1)
    group.add(g2)
    group.add(g3)
    group.join()

def Groupspawn():
    greenlet = Group()
    greenlet.spawn(green1,"green1"," so green")
    greenlet.spawn(green2,"green2")
    greenlet.spawn(green3,"green3")
    greenlet.join()

#     self.greenlet.spawn(self.heartbeat_worker).link_exception(callback=self.noop)
#     self.greenlet.spawn(self.client_listener).link_exception(callback=self.noop)

if __name__=="__main__":
    Groupspawn()
    