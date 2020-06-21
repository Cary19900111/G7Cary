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

def green3(group_team):
    gevent.sleep(3)
    group_team.kill(block=True)

def groupkill():
    group_team = Group()
    g1 = gevent.spawn(green1,"green1"," so green")
    g2= gevent.spawn(green2,"green2")
    g3 = gevent.spawn(green3,group_team)
    group_team.add(g1)
    group_team.add(g2)
    group_team.add(g3)
    group_team.join()

def greenkill():
    group_team = Group()
    g1 = gevent.spawn(green1,"green1"," so green")
    g3 = gevent.spawn(green3,g1)
    group_team.add(g1)
    group_team.add(g3)
    group_team.join()
    print(g1==None)
if __name__=="__main__":
        greenkill()
   
