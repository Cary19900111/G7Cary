import requests
import time
def daily():
    try:
        requests.get("http://127.0.0.1:8000/polls/daily")
    except:
        time.sleep(600)
        requests.get("http://127.0.0.1:8000/polls/daily")

def VolumnFang():
    try:
        requests.get("http://127.0.0.1:8000/polls/volumerisered")
    except:
        time.sleep(600)
        requests.get("http://127.0.0.1:8000/polls/volumerisered")
if __name__=='__main__':
    test()