
import os
import numpy as np 
import pandas as pd
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

def get_index_name():
    data = init_dataframe()
    data_index = data.index.tolist()
    print(data_index)

def get_single_row():
    data = init_dataframe()
    data_index = data.iloc[0]
    print(data_index)

def index_order():
    data = init_dataframe()
    print(data)
    print("##################")
    data.sort_index(inplace=True,ascending=False)   
    print(data)

def get_specify_row():
    data = init_dataframe()
    print(data)
    print("########")
    # a=data[data.R003==1478].index.tolist()
    # print(data.loc[a])
    # print("#########")
    print(data.loc['05-07-11':'05-09-11'])
#############################################
##########
class adaptee(object):
    def foo(self):
        print('foo in adaptee')
    def bar(self):
        print('bar in adaptee')

class adapter(object):
    def __init__(self):
        self.adaptee = adaptee()

    def foo(self):
        print('foo in adapter')
        self.adaptee.foo()

    def __getattr__(self, name):
        return getattr(self.adaptee, name)

if __name__ == '__main__':
    a = adapter()
    a.foo()
    a.bar()
