def crurllib3():
    import urllib3
    http = urllib3.PoolManager()
    r = http.request("get","http://www.baidu.com")
    print(type(r))

def crhttplib():
    import http.client as httplib
    conn=httplib.HTTPConnection(host='http://www.baidu.com', port=80, strict=False, timeout=120)
    conn.request(method='GET',url='/', body=None, headers=None)
    a = conn.getresponse().read()
    print(a)
if __name__=="__main__":
    crurllib3() 