import tushare as ts;
import datetime;

# 中国平安（601318）；万科（000002）；
# 1.机场股份000089 # 2.深圳燃气601139 # 3.深圳能源000027 # 4.深南电000037 # 5.盐田港股份000088 # 6.赛格股份000058 # 7.农产品股份000061
# 8.深深宝000019 # 9.特发信息000070 # 10.深特力000025 # 11.深物业000011   # 13.深纺织000045 # 14.通产丽星002243 # 15.深振业000006
# 16.深天健000090 # 17.深高速600548 # 20.沙河股份000014 # 21.国信证券002736
# 22.天威视讯（深圳市广电集团为实际控制人）002238 #
#  深股
# 12.深深房000029 天音控股（000829） 23.深深爱（新三板挂牌公司）833378 # 24.易图资讯（新三板挂牌公司）834386
arr = ['601318', '000002', '000829','000089','601139','000027','000037','000088','000058','000061','000019','000070','000025','000011','000029','000045','002243','000006','000090','600548','000014','002736','002238','833378','834386'];
#  港股 # 18.深圳国际0152HK # 19.深圳控股0604HK
hkarr = ['0152','0604'];

today = datetime.date.today();  # 获得今天的日期
lastmonth = today - datetime.timedelta(days=31);  # 用今天日期减掉时间差，参数为31天，获得上月的日期
endDate = today.strftime('%Y-%m-%d');
startDate = lastmonth.strftime('%Y-%m-%d');
date = today.strftime('%Y%m%d');

# for code in hkarr :
#     df = ts.get_k_data(code, start=startDate, end=endDate);

for code in arr:
    df = ts.get_k_data(code, start=startDate, end=endDate);
    df.to_json('E:/python/workspace/data/' + date + code + '.json', orient='records');
