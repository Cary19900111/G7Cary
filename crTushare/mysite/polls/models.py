from django.db import models

# Create your models here.
#python manage.py startapp my_app最好用命令来创建app（app中创建migrations文件夹）
#python manage.py makemigrations
#python manage.py migrate

class stock_basic(models.Model):
        '''
        code,代码
        name,名称
        industry,细分行业
        area,地区
        pe,市盈率
        outstanding,流通股本
        totals,总股本(万)
        totalAssets,总资产(万)
        liquidAssets,流动资产
        fixedAssets,固定资产
        reserved,公积金
        reservedPerShare,每股公积金
        eps,每股收益
        bvps,每股净资
        pb,市净率
        timeToMarket,上市日期
        '''
        code = models.CharField(max_length=100,default="")
        name = models.CharField(max_length=20,default="")
        industry = models.CharField(max_length=100,default="")
        area = models.CharField(max_length=100,default="")
        pe = models.FloatField(default=None)
        outstanding = models.FloatField(default=None)
        totals = models.FloatField(default=None)
        totalAssets=models.FloatField(default=None)
        liquidAssets=models.FloatField(default=None)
        fixedAssets=models.FloatField(default=None)
        reserved=models.FloatField(default=None)
        reservedPerShare=models.FloatField(default=None)
        eps=models.FloatField(default=None)
        bvps=models.FloatField(default=None)
        pb=models.FloatField(default=None)
        timeToMarket=models.IntegerField(default=None)


class stock_daily(models.Model):
        '''
        date,日期
        code,代码
        name,名称
        open,开盘价
        close,收盘价
        low,最低价，
        high,最高价
        volume,成交量， 
        turnoverratio,换手率
        changepercent,涨跌幅
        updatetime,更新时间
        '''
        date = models.CharField(max_length=20,default="")
        code = models.CharField(max_length=100,default="")
        name = models.CharField(max_length=20,default="")
        open = models.FloatField(default=None)
        close = models.FloatField(default=None)
        low = models.FloatField(default=None)
        high = models.FloatField(default=None)
        volume = models.FloatField(default=None)
        changepercent = models.FloatField(default=None)
        updatetime = models.CharField(max_length=100,default="")
        class Meta:
                unique_together = ["date", "code"]
                index_together = ["date", "code"]
                # ordering = ['-id']

class stock_ban(models.Model):
        '''
        code:
        name:
        date:
        count(万手)
        ratio:解禁后所占比例
        '''
        code = models.CharField(max_length=100,default="")
        name = models.CharField(max_length=20,default="")
        date = models.CharField(max_length=20,default="")
        month = models.CharField(max_length=20,default="")
        count = models.FloatField(default=None)
        ratio = models.FloatField(default=None)