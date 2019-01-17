import pandas as pd
import numpy as np
import tushare as ts
def init_price():
    data = ts.get_hist_data()
    data = pd.DataFrame(
        data=[
            [379.45,64.44,102.43],
            [383.54,60.39,100.4],
            [394.32,58.38,97.45],
        ],
        index=[
            '2011-09-01','2011-09-02','2011-09-03'
        ],
        columns=['gzb','mcst','zgsy']
    )
    return data

if __name__=='__main__':
    data = init_data()
    print(data)
    