import tushare as ts;
import datetime;





# 12.深深房000029 天音控股（000829） 23.深深爱（新三板挂牌公司）833378 # 24.易图资讯（新三板挂牌公司）834386
# arr = ['601318', '000002', '000829','000089','601139','000027','000037','000088','000058','000061','000019','000070','000025','000011','000029','000045','002243','000006','000090','600548','000014','002736','002238','833378','834386'];
#  港股 # 18.深圳国际0152HK # 19.深圳控股0604HK

# arr = ['000029','000829','833378','834386'];
arr = ['00152'];
# arr = ['000027'];
# arr = ['0152','0604'];

today = datetime.date.today(); #获得今天的日期
lastmonth = today - datetime.timedelta(days=31); #用今天日期减掉时间差，参数为31天，获得上月的日期
endDate = today.strftime('%Y-%m-%d');
startDate = lastmonth.strftime('%Y-%m-%d');

for code in arr :
    # df = ts.get_k_data(code,start=startDate, end=endDate);
    df = ts.get_k_data(code);
    # print(df);
    if df is not None:
        print(df);
        print("------------------")
        df.to_json('D:/java/python/PycharmProjects/pytest/day/'+code+'.json',orient='records')
        print(code+" : "+df.to_json(orient='records'))
    else:
        print(code+"对象空");
    # df.to_json('D:/java/python/PycharmProjects/pytest/day/'+date+code+'.json',orient='records');

#或者直接使用
# print(df.to_json(orient='records'))