# -*- coding: UTF-8 -*-

# import controller.ShareController as Share
# import strategy.regressionTree as regressionTree
import os
import numpy as np 
import pandas as pd
import tushare as ts
import pymysql
from datetime import datetime
import time
# 151  je520


def init_dataframe():
    ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
    )
    return ridership_df



def test():
    code_list = [1,2,3,4,5,6,7,8]
    for code_dic in code_list:
        try:
            print(code_dic)
            if(code_dic%2==0):
                continue
            if(code_dic%3 == 0):
                a = code_dic/0
        except Exception as err:
            continue

class people(object):
    def __init__(self,a,**kw):
        self.a = a
class student(object):
    def __init__(self,a,**kw):
        self.a = a
        for k,v in kw.items():
            setattr(k,v)
        people(a=3,)

def quoteint( ):
    a+=1

def quotelist(l):
    l.append(3)

def min_key():
    c = [-0.5,-0.1,2,2,3,4,5]
    a = min(c,key = lambda x :abs(x))
    print(a)

class desc:
    def __init__(self,name="desc"):
        self.name = name
    # def __set__(self,instance,name):
    #     print("set")
    #     self.name = name
    def __get__(self,instance,cls):
        print("get")
        return self.name+"get come on "

class Base:
    desc=desc()
    def __init__(self,desc):
        #self.desc = desc
        self.name = desc

def asyncDaily():
    import os,requests,asyncio
    pid=os.popen("lsof -i -n -P|grep 8000|awk '{print $2}'").read()
    if(pid):
        text = os.popen('kill -9 {0}'.format(int(pid)))
        print(text)
    os.system("mysql.server start")
    # f = os.popen("lsof -i:8000")
    # out = f.read()
    # print(out)
    os.system("python3 /Users/cary/Documents/python/g7/G7Cary/mysite/manage.py runserver &")
    time.sleep(3)
    # r = requests.get("http://127.0.0.1:8000/polls/learn")
    r_daily = requests.get("http://127.0.0.1:8000/polls/daily")
    # print(r.text)

def province_total():
    import requests
    from bs4 import BeautifulSoup
    r = requests.get("http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201902061009.html")
    soup = BeautifulSoup(r.text)
    tag2 = soup.find_all('tr',{'height':"19"})
    print(len(tag2))

def jsonVsPack():

    import json,msgpack,sys,time

    a = {'name':'yzy','age':26,'gender':'male','location':'Shenzhen'}

    begin_json = time.clock()
    for i in range(10000):
        in_json = json.dumps(a)
        un_json = json.loads(in_json)
    end_json = time.clock()
    print('Json serialization time: %.05f seconds' %(end_json-begin_json))
    print (type(in_json),'content:  ',in_json,'size: ',sys.getsizeof(in_json))
    print (type(un_json),'content:  ',un_json,'size: ',sys.getsizeof(un_json))
    print(un_json['name'])

    begin_msg = time.clock()
    for i in range(10000):
        in_msg = msgpack.packb(a)
        un_msg = msgpack.unpackb(in_msg)
    """
    # alias for compatibility to simplejson/marshal/pickle.
    load = unpack
    loads = unpackb

    dump = pack
    dumps = packb
    """
    # in_msg1 = msgpack.dumps(a)
    # un_msg1 = msgpack.loads(in_msg)
    end_msg = time.clock()
    print('Msgpack serialization time: %.05f seconds' %(end_msg-begin_msg))

    print(type(in_msg),'content:  ',in_msg,'size: ',sys.getsizeof(in_msg))
    print(type(un_msg),'content:  ',un_msg,'size: ',sys.getsizeof(un_msg))
    print(un_msg['name'])
if __name__ == '__main__':
    jsonVsPack()
    # asyncDaily()
    # b = Base("Base")
    # print(b.__dict__)
    # print(b.desc)
    # bc = Base
    # df = ts.xsg_data(year=2020)
    # print(df)

    # c = datetime.now().strftime('%Y-%m-%d')
    # print(type(c))
    #df = ts.get_stock_basics()
    #code_list = df.index.tolist()
    # df = ts.get_hist_data("603040")
    # print(df)

    # list = [column for column in df]
    # print(list)
    #print(df.columns.values.tolist())
    #print(df)
    # print(df.columns.values.tolist())
    # print(type(df.loc[code1, 'name']))#str
    # print(type(df.loc[code1, 'industry']))#str
    # print(type(df.loc[code1, 'area']))#str
    # print(type(df.loc[code1, 'pe']))#float64
    # print(type(df.loc[code1, 'outstanding']))#float64
    # print(type(df.loc[code1, 'totals']))#float64
    # print(type(df.loc[code1, 'totalAssets']))#float64
    # print(type(df.loc[code1, 'liquidAssets']))#float64
    # print(type(df.loc[code1, 'fixedAssets']))#float64
    # print(type(df.loc[code1, 'reserved']))#float64
    # print(type(df.loc[code1, 'reservedPerShare']))#float64
    # print(type(df.loc[code1, 'esp']))#floate
    # print(type(df.loc[code1, 'bvps']))#float
    # print(type(df.loc[code1, 'pb']))#float
    #            name,名称
    #            industry,细分行业
    #            area,地区
    #            pe,市盈率
    #            outstanding,流通股本
    #            totals,总股本(万)
    #            totalAssets,总资产(万)
    #            liquidAssets,流动资产
    #            fixedAssets,固定资产
    #            reserved,公积金
    #            reservedPerShare,每股公积金
    #            eps,每股收益
    #            bvps,每股净资
    #            pb,市净率
    #            timeToMarket,上市日期
    #DataFrame.columns.values.tolist()
    #ts.get_stock_basics
    #print(df.iloc[1:3])
    # print(df.loc["601162"])
    #Share.get_less_volume_with_down()
    # a = ts.get_cpi()
    # print(a)
    # data = init_person()
    # tree = regressionTree.Tree()
    #['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change', 'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20']