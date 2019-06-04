import os,time,datetime
import numpy as np 
import pandas as pd
import tushare as ts
def abruptLargeShrinkage(code):
    try:
        obj = ts.get_hist_data(code,retry_count=1).head(4)
        print(obj)
        today_change = obj["p_change"][0]
        if(today_change>11.00):
            return None
        volume_list = obj["volume"]
        today_open = obj["open"][0]
        today_close = obj["close"][0]
        today_volume = volume_list[0]
        pre_volume=volume_list[1]
        if(today_close<today_open and today_volume<0.8*pre_volume and today_change>-8.0):
            return code
        return None 
    except Exception as err:
        print(code+"has error:"+str(err))
def get_today_str():
    '''获取今天年月日的日期'''
    day_str = time.strftime('%Y-%m-%d',time.localtime())
    return day_str

def share_stop(share_data):
    '''是周末或者节假日返回False'''
    obj = share_data[0:1]#data.irow(0)
    date = obj.index.tolist()[0]#date str '2018-01-18'
    today = get_today_str()
    dayOfWeek = datetime.datetime.now().weekday()
    if(date==today or dayOfWeek>4):
        return False
    else:
        return True

def less_volume_and_down(stock_code):
    try:
        obj = ts.get_hist_data(code=stock_code,retry_count=1).head(4)
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
    except Exception as err:
        print(stock_code+"has error:"+str(err))
if __name__=="__main__":
    abruptLargeShrinkage("603398")

