import controller.ShareController as Share
import strategy.regressionTree as regressionTree
import os
import numpy as np 
import pandas as pd
import tushare as ts
#151  je520

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
def init_person():
    persons = pd.DataFrame(
        data=[['熊大',21,4,12000],
        ['车老二',25,5,15000],
        ['张三',23,6,20000],
        ['李四',28,8,35000]],
        columns=['name','age','grade','salary']
    )
    return persons
if __name__=='__main__':
    stock = "603398"
    df = ts.get_realtime_quotes(stock)
    print(df)
    #Share.get_less_volume_with_down()
    # a = ts.get_cpi()
    # print(a)
    # data = init_person()
    # tree = regressionTree.Tree()
    # tree.fit(data,data[0])
    
    