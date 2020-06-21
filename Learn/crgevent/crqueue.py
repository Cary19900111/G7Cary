import gevent
from gevent.event import Event,AsyncResult
from gevent.queue import Queue,Empty
 
tasks = Queue()

def Boss():
    for i in range(25):
        tasks.put(i)
    print("task set over.")

def Worker(name):
    try:
        while True:
            task = tasks.get(timeout=3)
            print("worker %s got task %s"%(name,task))
            gevent.sleep(1)#没有它就一个人做
    except Exception as e:
        print("Leave")
if __name__=="__main__":
    gevent.spawn(Boss).join()
    print("##########################")
    gevent.joinall([gevent.spawn(Worker,"keith"),gevent.spawn(Worker,"tony"),gevent.spawn(Worker,"Swaggie")])