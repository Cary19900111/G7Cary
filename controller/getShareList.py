#import strategy.lessVolumeAndDown as lvad
import tushare as ts
def get_code_list():
    share_list = ts.get_stock_basics().index.tolist()
    return share_list

def get_share_list_from_less_volume_and_down():
    result_list=[]
    code_list = get_code_list()
    for code in code_list:
        result = lvad.less_volume_and_down(code)
        if result!=None:
            result_list.append(result)
    return result_list

def get_pe_radio_top_n(n):
    stock_list = ts.get_stock_basics()
    stock_list_0 = stock_list[stock_list.pe>0].nsmallest(n,columns='pe')
    print(stock_list_0)

if __name__=='__main__':
    get_pe_radio_top_n(10)

