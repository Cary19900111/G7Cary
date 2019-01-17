def producer(c):
    c.send(None)
    # c.__next__()
    t = 1
    while t < 2:
        print("product: %s" % t)
        r = c.send(t)
        print(r)
        t = t+1
    c.close()


def consume():
    r = 'gnfgfn'
    while True:
        t = yield r
        if not t:
            print("t is None")
            return
        print('[CONSUMER] Consuming %s...' % t)
        r = '200 OK'


def counter(start_at = 0):
    count = start_at
    val = 1
    while True:
        val = (yield count)
        print ('val:',val)
        if val is not None:
            count = val
        else:
            count += 1
if __name__ == "__main__":
    c = consume()
    print(next(c))
    print(c.send(20))
    #print(next(c))