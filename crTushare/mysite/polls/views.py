# from django.shortcuts import render
import gevent
from django.http import HttpResponse,Http404
from polls.models import stock_basic,stock_daily,stock_ban
import tushare as ts
import datetime,time
import json,re,sys
from .service.mail import mailcode
from ratelimit.decorators import ratelimit
from dateutil.relativedelta import relativedelta
from .spider.github_trend import GitHubTrend
from .spider.toutiao import Toutiao
from .spider.hacker_news import HackerNews
from .spider.segmentfault import SegmentFault
from .spider.jobbole import Jobbole


import gevent
def test1(stock_code,stock_date):
    print(stock_code)
    gevent.sleep(1)
    # print("10")
    # gevent.sleep(0)
    # print("11")
    # gevent.sleep(0)

def test2():
    print("20")
    # gevent.sleep(0)
    print("21")
    # gevent.sleep(0)

def test3():
    print("30")
    # gevent.sleep(0)
    print("31")
    # gevent.sleep(0)

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

def GetDataByDayFromgevent(stock,daytime):
    try:
        code1 =stock.code
        name1 = stock.name
        df = ts.get_hist_data(code1,start=daytime,end=daytime)
        print("df:")
        print(df)
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

def GetDataByDay(request,daytime):
    #访问的时候不用加''
    updatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("CR:"+daytime)
    basic_info  = stock_basic.objects.all()
    for stock in basic_info:
        try:
            code1 =stock.code
            name1 = stock.name
            df = ts.get_hist_data(code1,start=daytime,end=daytime)
            print("df:")
            print(df)
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
                    close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1,updatetime=updatetime)
                    q.save()
                except Exception as err:
                    print(code1)
        except Exception as err:
            print(stock.code)
    return HttpResponse("day sync data Finish!")

def not_open_judge_by_volume(df,judge_list):
    count = 0
    for code in judge_list:
        volume_in_db = stock_daily.objects.filter(code=code)[:1].values()[0]["volume"]
        volume_in_df = df[df.code==code]["volume"].values[0]*0.01
        if(volume_in_db == volume_in_df):
            count = count+1
    if(count == 2):
        return True
    return False

@ratelimit(key='ip',rate='1/5s',block=True)
def daily(request):
    judge_list=["000001","600521"]
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    updatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        df = ts.get_today_all()
    except Exception as err:
        print("sync daily data err:{}".format(err))
        mailcode("async daily Date","Fail to Get Daily Data From Tushare")
        return HttpResponse("Async Data From Tushare fail")
    if (not_open_judge_by_volume(df,judge_list)):
        print("cr aysnc data fail")
        return HttpResponse("Today has No data!") 
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
                close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1,updatetime=updatetime)      
            else:    
                q = stock_daily(date=date_today, code=code1, name=name1, open=open1,
                close=close1, low=low1, high=high1, volume= volume1,changepercent= changepercent1,updatetime=updatetime)
                q.save()
        except Exception as err:
            continue
    return HttpResponse("Daily Async Done")

# @ratelimit(key='ip',rate='1/5s',block=False)
def banshare(request,year,month):
    #       code    name        date         count  ratio
    # 0    002032   苏泊尔     2019-08-30      8.29   0.01
    # today = datetime.date.today()
    # year = today.strftime("%Y")
    # month = today.strftime("%m")
    month_total = stock_ban.objects.filter(month=month).count()
    if month_total==0:
        df = ts.xsg_data(year=year,month=month)
        id_list = df.index.tolist()
        for id in id_list:
            code1 = df.loc[id, 'code']
            name1 = df.loc[id,'name']
            date1 = df.loc[id,'date']
            count1 = df.loc[id,'count']
            ratio1 = df.loc[id,'ratio']
            sb = stock_ban(code=code1, name=name1, date=date1, count=count1,ratio=ratio1,month=month)
            sb.save()
            return HttpResponse("{} banshare Done".format(month))
    else:
        return HttpResponse("{} have synced".format(month))
    # print(month_total)
    # next_month = today+relativedelta(months=1)
    # next_year = next_month.strftime("%Y")
    # next_month = next_month.strftime("%m")
   

def volumndowngreen(request):
    '''阴跌缩量'''
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    #code_list = [{'code':'300584'},{'code':'002681'},{'code':'002897'},{'code':'300731'}]
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
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
    '''突然缩量一半 绿柱'''
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
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
            #data_list[0]['date'] != date_today or 
            if(volume_today==0 or data_list[0]['changepercent']>8.0 or data_list[0]['changepercent']<-8.0):
                continue
            if(close_today<=open_today and volume_today<=0.4*volume_pre):
                stock_list.append(code1)
        except Exception as err:
            print("error:"+str(err))
            continue
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).values()
    result_list = list(result_pd)
    result = []
    for result_data in result_list:
        result.append(result_data['code'])
    print(result)
    return HttpResponse('volumnhalf:'+",".join(result))

def volumerisered(request):
    '''放小量上涨'''
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
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
    print(stock_list)
    # result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).values()
    # result_list = list(result_pd)
    # result = []
      #获取近期解禁股票
    ban_stock = stock_ban.objects.filter(date__gt=date_today).values("code")
    ban_list = list(ban_stock)
    ban_code_list = []
    for ban_share in ban_list:
        ban_code_list.append(ban_share['code'])
    #找市盈率>0的
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).filter(pe__lt=20).values()
    result_list = list(result_pd)
    result = ""
    for result_data in result_list:
        result_single = []
        code = result_data['code']
        if code in ban_code_list:
            continue
        result_single.append(code)
        result_single.append(result_data['name'])
        result_single.append(result_data['industry'])
        result_single.append(result_data['area'])
        result +=json.dumps(result_single,ensure_ascii=False)
        result+="\n"
    mailcode("放小量上涨",result)
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    print("end volumerisered")
    return HttpResponse("volumerisered Done!")

@ratelimit(key='ip',rate='1/5s',block=True)
def volRiseOnBottom(request):
    '''底部放量'''
    print("start volRiseOnBottom")
    stock_changepercent = {}
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    # code_list = [{'code':'300584'},{'code':'002681'},{'code':'002897'},{'code':'300731'}]
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    for code_dic in code_list:
        code1 = code_dic['code']
        code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:3].values()
        data_list = list(code1_daily_datas)
        if(len(data_list) < 3 or data_list[0]['volume'] == 0):
            continue
        #beforeyesterday
        beforeyesterday_close = code1_daily_datas[2]['close']
        beforeyesterday_vol = code1_daily_datas[2]['volume']
        #yesterday
        yesterday_close = code1_daily_datas[1]['close']
        yesterday_low = code1_daily_datas[1]['low']
        yesterday_vol = code1_daily_datas[1]['volume']
        #today
        today_vol = code1_daily_datas[0]['volume']
        today_low = code1_daily_datas[0]['low']
        # today_close = code1_daily_datas[2]['close']
        if(yesterday_close<beforeyesterday_close and 
        yesterday_vol<beforeyesterday_vol and 
        today_vol>beforeyesterday_vol and 
        today_low>yesterday_low):
            stock_list.append(code1)
            stock_changepercent[code1]=code1_daily_datas[0]['changepercent']
    #获取近期解禁股票
    ban_stock = stock_ban.objects.filter(date__gt=date_today).values("code")
    ban_list = list(ban_stock)
    ban_code_list = []
    for ban_share in ban_list:
        ban_code_list.append(ban_share['code'])
    #找市盈率>0的
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).filter(pe__lt=20).values()
    result_list = list(result_pd)
    result = ""
    for result_data in result_list:
        result_single = []
        code = result_data['code']
        if code in ban_code_list:
            continue
        result_single.append(code)
        result_single.append(result_data['name'])
        result_single.append(result_data['industry'])
        result_single.append(result_data['area'])
        result_single.append(stock_changepercent[code])
        result +=json.dumps(result_single,ensure_ascii=False)
        result+="\n"
    mailcode("basin",result)
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    print("end volRiseOnBottom")
    return HttpResponse("volRiseOnBottom Done!")

@ratelimit(key='ip',rate='1/5s',block=True)
def volRiseAndDownRecentFourDay(request):
    '''底部放量再缩量'''
    print("start volRiseOnBottom")
    stock_changepercent = {}
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    # code_list = [{'code':'300584'},{'code':'002681'},{'code':'002897'},{'code':'300731'}]
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    for code_dic in code_list:
        code1 = code_dic['code']
        code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:4].values()
        data_list = list(code1_daily_datas)
        if(len(data_list) < 4 or data_list[0]['volume'] == 0):
            continue
        #befobefoyesterday
        befobefoyesterday_close = code1_daily_datas[3]['close']
        befobefoyesterday_vol = code1_daily_datas[3]['volume']
        befobefoyesterday_open = code1_daily_datas[3]['open']
        #beforeyesterday
        beforeyesterday_close = code1_daily_datas[2]['close']
        beforeyesterday_vol = code1_daily_datas[2]['volume']
        #yesterday
        yesterday_close = code1_daily_datas[1]['close']
        yesterday_open = code1_daily_datas[1]['open']
        yesterday_low = code1_daily_datas[1]['low']
        yesterday_vol = code1_daily_datas[1]['volume']
        #today
        today_close = code1_daily_datas[0]['close']
        today_open = code1_daily_datas[0]['open']
        today_vol = code1_daily_datas[0]['volume']
        today_low = code1_daily_datas[0]['low']
        # today_close = code1_daily_datas[2]['close']
        if(today_vol<0.7*yesterday_vol and 
        yesterday_vol>beforeyesterday_vol and 
        beforeyesterday_vol<befobefoyesterday_vol and 
        yesterday_open<yesterday_close and 
        today_open>today_close):
            stock_list.append(code1)
            stock_changepercent[code1]=code1_daily_datas[0]['changepercent']
    #获取近期解禁股票
    ban_stock = stock_ban.objects.filter(date__gt=date_today).values("code")
    ban_list = list(ban_stock)
    ban_code_list = []
    for ban_share in ban_list:
        ban_code_list.append(ban_share['code'])
    #找市盈率>0的
    result_pd = stock_basic.objects.filter(code__in=stock_list).filter(pe__gt=0).filter(pe__lt=20).values()
    result_list = list(result_pd)
    result = ""
    for result_data in result_list:
        result_single = []
        code = result_data['code']
        if code in ban_code_list:
            continue
        result_single.append(code)
        result_single.append(result_data['name'])
        result_single.append(result_data['industry'])
        result_single.append(result_data['area'])
        result_single.append(stock_changepercent[code])
        result +=json.dumps(result_single,ensure_ascii=False)
        result+="\n"
    mailcode("basin",result)
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    print("end volRiseOnBottom")
    return HttpResponse("volRiseOnBottom Done!")

@ratelimit(key='ip',rate='1/5s',block=True)
def shrinkStopFall(request):
    '''获取最近两天数据，第一天绿柱放量，第二天绿柱缩量，第二天最低价>第一天最低价'''
    print("start shrinkStopFall")
    stock_changepercent = {}
    stock_list = []
    code_list = stock_daily.objects.values("code").distinct()
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    for code_dic in code_list:
        code1 = code_dic['code']
        code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:3].values()
        data_list = list(code1_daily_datas)
        if(len(data_list) < 3 or data_list[0]['volume'] == 0):
            continue
        #beforeyesterday
        beforeyesterday_vol = code1_daily_datas[2]['volume']
        #yesterday
        yesterday_open = code1_daily_datas[1]['open']
        yesterday_close = code1_daily_datas[1]['close']
        yesterday_low = code1_daily_datas[1]['low']
        yesterday_vol = code1_daily_datas[1]['volume']
        yesterday_hign = code1_daily_datas[1]['high']
        #today
        today_open = code1_daily_datas[0]['open']
        today_close = code1_daily_datas[0]['close']
        today_low = code1_daily_datas[0]['low']
        today_vol = code1_daily_datas[0]['volume']
        today_hign = code1_daily_datas[0]['high']

        # today_close = code1_daily_datas[2]['close']
        if(yesterday_vol>beforeyesterday_vol and #昨天交易量>前天
        yesterday_close<yesterday_open and #昨天收盘价<开盘价
        today_close<today_open and #今日收盘价<开盘价
        today_low>yesterday_low and
        today_hign<yesterday_hign):#今日最低价>昨日最低价
            stock_list.append(code1)
            stock_changepercent[code1]=code1_daily_datas[0]['changepercent']
    #找市盈率>0的
    result_pd = stock_basic.objects.filter(code__in=stock_list).values()
    result_list = list(result_pd)
    result = ""
    for result_data in result_list:
        result_single = []
        code = result_data['code']
        # if code in ban_code_list:
        #     continue
        result_single.append(code)
        result_single.append(result_data['name'])
        result_single.append(result_data['industry'])
        result_single.append(result_data['area'])
        result_single.append(stock_changepercent[code])
        result +=json.dumps(result_single,ensure_ascii=False)
        result+="\n"
    print(result)
    mailcode("稳住跌势",result)
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    print("end shrinkStopFall")
    return HttpResponse("shrinkStopFall")

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


@ratelimit(key='ip',rate='1/5s',block=True)
def learn(request):
    c = mailcode("11","11")
    print(c)
    return HttpResponse("fjlsf")
    #pip3 install django-ratelimit
    # id = request.GET.get("id")
    # df_index = ts.get_index()
    # print(df_index)
    # resp = {"code":"2803004019","detail":"in uni"}
    # return HttpResponse(json.dumps(resp))
    # ts.get_hist_data('600123')
    # date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    # ban_stock = stock_ban.objects.filter(date__gt=date_today).values("code")
    # print("CR:learn")
    # return HttpResponse("learn")
    # ip = request.META.get("HTTP_X_FORWARD_FOR",0)
    # ip2 = request.META.get('REMOTE_ADDR')
    # request_time = request.session.get('request_time',0)
    # # id  = GetId(request)
    # name = GetName(request)
    # return HttpResponse("获得数据 %s:%s"%(request_time,ip2))


def GetId(request):
    code1= "600123"
    code1_daily_datas = stock_daily.objects.filter(code=code1).order_by("date").reverse()[:2].values()
    data_list = list(code1_daily_datas)
    volume_today = data_list[0]['volume']
    return volume_today

def GetName(request):
    return HttpResponse("GetName")


def get_github_trend(request):
    if request.method=="POST":
        gh_trend = GitHubTrend()
        gh_trend_list = gh_trend.get_trend_list()
        result = {"message":"OK","data":gh_trend_list}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    else:
        raise Http404

def get_toutiao_posts(request):
    if request.method=="POST":
        toutiao = Toutiao()
        post_list = toutiao.get_posts()
        result = {"message":"OK","data":post_list}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    else:
        raise Http404

def get_hacker_news(request):
    if request.method=="POST":
        hacker = HackerNews()
        news_list = hacker.get_news()
        result = {"message":"OK","data":news_list}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    else:
        raise Http404

def get_segmentfault_blogs(request):
    if request.method=="POST":
        sf = SegmentFault()
        blogs = sf.get_blogs()
        result = {"message":"OK","data":blogs}
        return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    else:
        raise Http404