import queue
class task(object):
    tid = 0
    def __init__(self,target):
        task.tid = task.tid+1
        self.id = task.tid
        self.target = target
        self.sendval = None
    def run(self):
        return self.target.send(self.sendval)

class schedule(object):
    def __init__(self):
        self.task_map = {}
        self.ready = queue.Queue()
    def new(self,target):
        task_sc = task(target)
        self.task_map[task_sc.id]=task_sc
        self.ready.put(task_sc)
    def exit(self,id):
        del self.task_map[id]
    def main_loop(self):
        while True:
            print("crlen:"+str(self.ready.qsize()))
            task = self.ready.get(block=False)
            try:
                task.run()
            except Exception as err:
                self.exit(task.id)
                continue
            self.ready.put(task,block=False)
def Laundry():
    for i in range(5):
        yield i
        print('I am doing the laundry')
def Cook():
    for i in range(10):
        yield
        print('I am cooking')


if __name__ == "__main__":
    s = schedule()
    s.new(Cook())
    s.new(Laundry())
    s.main_loop()
