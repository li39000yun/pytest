import tushare as ts;
import datetime;

# 中国平安（601318）；万科（000002）；天音控股（000829）
arr = ['601318','000002','000829'];

date = datetime.datetime.now().strftime('%Y%m%d');
today = datetime.date.today(); #获得今天的日期
lastmonth = today - datetime.timedelta(days=31); #用今天日期减掉时间差，参数为31天，获得上月的日期
endDate = today.strftime('%Y-%m-%d');
startDate = lastmonth.strftime('%Y-%m-%d');

for code in arr :
    df = ts.get_k_data(code,start=startDate, end=endDate);
    df.to_json('D:/java/python/PycharmProjects/pytest/day/'+date+code+'.json',orient='records');
# df = ts.get_hist_data('000875')
# df.to_json('D:/java/python/PycharmProjects/pytest/day/000875.json',orient='records')

#或者直接使用
# print(df.to_json(orient='records'))