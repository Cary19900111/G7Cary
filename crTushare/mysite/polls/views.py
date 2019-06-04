# from django.shortcuts import render
from django.http import HttpResponse
from polls.models import stock_basic,stock_daily
import tushare as ts
from datetime import datetime
import json,re


# Create your views here.
def basicElementExist(stock_code):
    try:
        obj = stock_basic.objects.get(code=stock_code)
        return True
    except Exception as err:
        print(1)
        return False

def dailyElementExist(stock_code,stock_date):
    try:
        obj = stock_daily.objects.get(code=stock_code,date=stock_date)
        return True
    except Exception as err:
        return False

def index(request):
    return HttpResponse("This is HomePage")

def basic(request):
    df = ts.get_stock_basics()
    code_list = df.index.tolist()
    for code1 in code_list:
        name1 = df.loc[code1, 'name']
        industry1 = df.loc[code1, 'industry']
        area1 = df.loc[code1, 'area']
        pe1 = df.loc[code1, 'pe']
        outstanding1 = df.loc[code1, 'outstanding']
        totals1 = df.loc[code1, 'totals']
        totalAssets1 =df.loc[code1, 'totalAssets']
        liquidAssets1 =df.loc[code1, 'liquidAssets']
        fixedAssets1 =df.loc[code1, 'fixedAssets']
        reserved1 =df.loc[code1, 'reserved']
        reservedPerShare1 =df.loc[code1, 'reservedPerShare']
        eps1 =df.loc[code1, 'esp']
        bvps1 =df.loc[code1, 'bvps']
        pb1 =df.loc[code1, 'pb']
        timeToMarket1 =df.loc[code1, 'timeToMarket']
        if basicElementExist(code1):
            stock_basic.objects.filter(code=code1).update(name=name1, industry=industry1, area=area1, pe=pe1, outstanding=outstanding1,
            totals=totals1, totalAssets=totalAssets1, liquidAssets=liquidAssets1, fixedAssets=fixedAssets1,
            reserved=reserved1, reservedPerShare=reservedPerShare1, eps=eps1, bvps=bvps1, pb=pb1,timeToMarket=timeToMarket1)      
        else:        
            q = stock_basic(code=code1, name=name1, industry=industry1, area=area1, pe=pe1, outstanding=outstanding1,
            totals=totals1, totalAssets=totalAssets1, liquidAssets=liquidAssets1, fixedAssets=fixedAssets1,
            reserved=reserved1, reservedPerShare=reservedPerShare1, eps=eps1, bvps=bvps1, pb=pb1,timeToMarket=timeToMarket1)
            q.save()
    return HttpResponse("basic information sync Done!")

def history(request):
    basic_info  = stock_basic.objects.all()
    for stock in basic_info:
        try:
            code1 = stock.code
            name1 = stock.name
            df = ts.get_hist_data(code1)
            date_list = df.index.tolist()
            for date1 in date_list:
                try:
                    open1 = df.loc[date1, 'open']
                    close1 = df.loc[date1, 'close']
                    low1 = df.loc[date1, 'low']
                    high1 = df.loc[date1, 'high']
                    volume1 =df.loc[date1, 'volume']
                    changepercent1 =df.loc[date1, 'p_change']
                    q = stock_daily(date=date1, code=code1, name=name1, open=open1,
                    close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1)
                    q.save()
                except Exception as err:
                    print(code1)
        except Exception as err:
            print(stock.code)
    return HttpResponse("history Finish!")

    # print(df)
    #  code1 = df.loc[id, 'code']
    #         name1 = df.loc[id, 'name']
    #         open1 = df.loc[id, 'open']
    #         close1 = df.loc[id, 'trade']
    #         low1 = df.loc[id, 'low']
    #         high1 = df.loc[id, 'high']
    #         volume1 = df.loc[id, 'volume']
    #         changepercent1 = df.loc[id, 'changepercent']
    #         q = stock_daily(date=date_today, code=code1, name=name1, open=open1,
    #         close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1)
    #         q.save()
    # column_list = [column for column in df]
    # print(column_list)
    # date_list = df.index.tolist()
    # for date in date_list[:5]:
    #     open = df.loc[date, 'open']
    #     close = df.loc[date, 'close']
    #     low = df.loc[date, 'low']
    #     high = df.loc[date, 'high']
    #     volume =df.loc[date, 'volume']
    #     changepercent =df.loc[date, 'p_change']
    #     print(open)

def daily(request):
    date_today = datetime.now().strftime('%Y-%m-%d')
    df = ts.get_today_all()
    id_list = df.index.tolist()
    for id in id_list:
        try:
            code1 = df.loc[id, 'code']
            name1 = df.loc[id, 'name']
            open1 = df.loc[id, 'open']
            close1 = df.loc[id, 'trade']
            low1 = df.loc[id, 'low']
            high1 = df.loc[id, 'high']
            volume1 = df.loc[id, 'volume']*0.01
            changepercent1 = df.loc[id, 'changepercent']
            if dailyElementExist(code1,date_today):
                stock_daily.objects.filter(code=code1,date=date_today).update(date=date_today, code=code1, name=name1, open=open1,
                close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1)      
            else:    
                q = stock_daily(date=date_today, code=code1, name=name1, open=open1,
                close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1)
                q.save()
        except Exception as err:
            continue
    return HttpResponse("Daily Async Done")

def banshare(request):
    year_now = datetime.now().strftime('%Y')
    month_now = datetime.now().strftime("%m")
    df = ts.xsg_data(year=year_now,month=month_now)
    print(df)
    return HttpResponse("banshare")

def volumndowngreen(request):
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    #code_list = [{'code':'300584'},{'code':'002681'},{'code':'002897'},{'code':'300731'}]
    date_today = datetime.now().strftime('%Y-%m-%d')
    for code_dic in code_list:
        code1 = code_dic['code']
        if(code1.startswith("300")):
            continue
        code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:3].values()
        data_list = list(code1_daily_datas)
        if(len(data_list) < 3 or data_list[0]['volume'] == 0):
            continue
        volume_current = 0
        for data in data_list:
            volume_pre = data['volume']
            open = data['open']
            close = data['close']
            if(volume_current > volume_pre or open < close):
                break
            volume_current = volume_pre
        else:
            stock_list.append(code1)
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).values()
    result_list = list(result_pd)
    result = []
    for result_data in result_list:
        result.append(result_data['code'])
    print(result)
    return HttpResponse('volumndowngreen:'+",".join(result))

def volumnhalf(request):
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    date_today = datetime.now().strftime('%Y-%m-%d')
    #code_list = [{'code':'600716'}]
    for code_dic in code_list:
        try:
            code1 = code_dic['code']
            if(code1.startswith("300")):
                continue
            code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:2].values()
            data_list = list(code1_daily_datas)
            volume_today = data_list[0]['volume']
            volume_pre = data_list[1]['volume']
            open_today = data_list[0]['open']
            close_today = data_list[0]['close']
            if(data_list[0]['date'] != date_today or volume_today==0 or data_list[0]['changepercent']>8.0 or data_list[0]['changepercent']<-8.0):
                continue
            if(close_today<=open_today and volume_today<=0.4*volume_pre):
                stock_list.append(code1)
        except Exception as err:
            print("error")
            continue
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).values()
    result_list = list(result_pd)
    result = []
    for result_data in result_list:
        result.append(result_data['code'])
    print(result)
    return HttpResponse('volumnhalf:'+",".join(result))

def volumerisered(request):
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    date_today = datetime.now().strftime('%Y-%m-%d')
    #code_list = [{'code':'600716'}]
    for code_dic in code_list:
        try:
            code1 = code_dic['code']
            code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:2].values()
            data_list = list(code1_daily_datas)
            volume_today = data_list[0]['volume']
            volume_pre = data_list[1]['volume']
            open_today = data_list[0]['open']
            close_today = data_list[0]['close']
            open_pre = data_list[1]['open']
            close_pre = data_list[1]['close']
            if(data_list[0]['date'] != date_today or volume_today==0 or data_list[0]['changepercent']>8.0 or data_list[0]['changepercent']<-8.0):
                continue
            if(close_today>=open_today and close_pre>=open_pre and volume_today>=volume_pre and volume_today<=1.2*volume_pre):
                stock_list.append(code1)
        except Exception as err:
            continue
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).values()
    result_list = list(result_pd)
    result = []
    for result_data in result_list:
        result.append(result_data['code'])
    print(result)
    return HttpResponse('volumerisered:'+",".join(result))

def realtime(request,code):
    code_list = code.split(',')
    index_change = ts.get_index().loc[0,"change"]
    str = "上证涨幅:%s<br/>-----------<br/>"%index_change
    code_pattern = re.compile("\d{6}$")
    for code in code_list:
        a = re.findall(code_pattern,code)
        if(len(a)!=1):
            db_data = stock_basic.objects.filter(name=code).values_list('code')[0]
            code = db_data[0]
        df = ts.get_realtime_quotes(code)
        name = df.loc[0,'name']
        pre_close = df.loc[0,'pre_close']
        open_price = df.loc[0,'open']
        price = df.loc[0,'price']
        volumn = df.loc[0,'volume']
        amount = df.loc[0,'amount']
        b1_p = df.loc[0,'b1_p']
        b1_v = df.loc[0,'b1_v']
        a1_p = df.loc[0,'a1_p']
        a1_v = df.loc[0,'a1_v']
        avg_price = float(amount)/int(volumn) 
        str += '''名字:%s  code:%s<br/>昨日收盘价:%s<br/>今日开盘价:%s<br/>当前价:%s<br/>
        成交股数:%s<br/>成交总额:%s<br/>均价:%f<br/>卖1:price:%svolumn:%s<br/>买1:price:%svolumn:%s<br/>------------------<br/>'''  % (name,code,pre_close,open_price,price,volumn,amount,avg_price,a1_p,a1_v,b1_p,b1_v)
    return HttpResponse(str)

def learn(request):
    df_index = ts.get_index()
    print(df_index)
    resp = {"code":"2803004019","detail":"in uni"}
    return HttpResponse(json.dumps(resp))