import requests
import json
import time
def test():
    s = requests.session()
    method = 'get'
    url = "http://www.baidu.com"
    resp = s.request(method,url)
    print(resp.text)
def CalZhonghanglianhanghao(card):
    s = requests.session()
    method = 'get'
    headers = {"AccessKey":"7566fc05-3287-4b3f-abe3-73823163bd70-48ec92eb-0e84-459b-ad87-b01608bc9ea6"}
    url = "http://service-cashdesk-truck-broker.test.g7pay.net/cashdesk-truck-broker/v0/bank/cardBin/{}".format(card)
    resp = s.request(method,url,headers=headers)
    if resp.status_code == 200:
        bank_uni_list = (json.loads(resp.text))
        return bank_uni_list["bankName"]
    return "404"
    # print(len(bank_uni_list))#1448
def main():
    wrong = []
    abort_list = get_abort_list()
    with open("20180910/bin.txt",'r') as f_bin:
            with open("20180910/name.txt",'r') as f_name:
                bin_datas = f_bin.read().splitlines()
                name_datas = f_name.read().splitlines()
                for i in range(len(bin_datas)):
                    bank_name_file =name_datas[2*i][1:]
                    if bank_name_file in abort_list:
                        continue
                    try:
                        bank_name_sw = CalZhonghanglianhanghao(bin_datas[i])
                    except Exception as err:
                        wrong.append(bin_datas[i]+" Neterror")
                    time.sleep(0.1)
                    if(bank_name_sw=="404"):
                        wrong.append(bin_datas[i]+":"+bank_name_file+"404")
                        continue
                    if(cmp_bank_name(bank_name_file,bank_name_sw)):
                        continue
                    else:
                        wrong.append(bin_datas[i]+":"+bank_name_file+":"+bank_name_sw)
    with open("result.txt",'w') as f:
        f.write("\n".join(wrong))
def cmp_bank_name(bank_name_file,bank_name_sw):
    if (bank_name_file in bank_name_sw) or (bank_name_sw in bank_name_file):
        return True
    return False
def str_to_list():
    abort_list = []
    with open("20180910/data.txt",'r') as f:
        data = f.read()
        data_dict =json.loads(data)
    for (k,vs) in  data_dict.items():
        for v in vs:
            if(v['BankCode']==-1 or v['BankCode']==0):
                if(v['SwiftBankName']==''):
                    bankname = v['BankName']
                else:
                    bankname=v['SwiftBankName']
                if bankname not in abort_list:
                    abort_list.append(v['BankName'])
    with open("abort.txt",'w') as f:
        f.write("\n".join(abort_list))
def get_abort_list():
    abort_list = []
    with open("20180910/abort.txt",'r') as f:
        datas = f.read().splitlines()
        for data in datas:
            abort_list.append(data)
    return abort_list
if __name__=="__main__":
    main()   
