import strategy.lessVolumeAndDown as lvad
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