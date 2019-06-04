import os,time,datetime
import numpy as np 
import pandas as pd
import tushare as ts
def less_volume_and_down(stock_code):
    try:
        obj = ts.get_hist_data(code=stock_code,retry_count=1).head(4)
        if share_stop(obj):
            return None
        volume_list = obj["volume"]
        volume_pre = 0
        volume_current = 0
        open_list = obj["open"]
        close_list = obj["close"]
        for volume in volume_list:
            volume_later,volume_current = volume_current,volume
            if(volume_later>volume_current):
                return None
        for index in range(len(open_list)):
            if(open_list[index]<close_list[index]):
                return None
        return stock_code
    except Exception:
        pass
        print(stock_code)

def less_volume_and_down_today_half(stock_code):
    #todo
    try:
        obj = ts.get_today_all(code=stock_code,retry_count=1).head(4)
        if share_stop(obj):
            return None
        volume_list = obj["volume"]
        volume_pre = 0
        volume_current = 0
        open_list = obj["open"]
        close_list = obj["close"]
        for volume in volume_list:
            volume_later,volume_current = volume_current,volume
            if(volume_later>volume_current):
                return None
        for index in range(len(open_list)):
            if(open_list[index]<close_list[index]):
                return None
        return stock_code
    except Exception:
        print(stock_code)

def rise_volume_greater_down_volume(stock_code):
    try:
        obj = ts.get_hist_data(code=stock_code,retry_count=1).head(6)
        merge = 0
        volume_list = obj["volume"]
        open_list = obj["open"]
        close_list = obj["close"]
        
        for index in range(len(open_list)):
            merge  = merge+volume_list[index]*(close_list[index]-open_list[index])
        if merge>0:
            return stock_code
        else:
            return None
    except Exception as err:
        print(err)
        print(stock_code)
        return None

def get_code_list():
    share_list = ts.get_stock_basics().index.tolist()
    return share_list

def share_stop(share_data):
    obj = share_data[0:1]#data.irow(0)
    date = obj.index.tolist()[0]#date str '2018-01-18'
    today = get_today_str()
    dayOfWeek = datetime.datetime.now().weekday()
    if(date==today or dayOfWeek>4):
        return False
    else:
        return True

def get_today_str():
    day_str = time.strftime('%Y-%m-%d',time.localtime())
    return day_str

def run():
    result_list=[]
    code_list = get_code_list()
    for code in code_list:
        result = rise_volume_greater_down_volume(code)
        if result!=None:
            result_list.append(result)
    print(result_list)

def query_single_share():
    obj = ts.get_hist_data(code="002053",retry_count=1).head(4)
    print(obj)

def pb_code():
    data = ts.get_today_all()
    
    print(data)
if __name__=="__main__":
    pb_code()
    #query_single_share()

 