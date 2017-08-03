import tushare as ts;
import datetime;

# 中国平安（601318）；万科（000002）；天音控股000829
# 1.机场股份000089 # 2.深圳燃气601139 # 3.深圳能源000027 # 4.深南电000037 # 5.盐田港股份000088 # 6.赛格股份000058 # 7.农产品股份000061
# 8.深深宝000019 # 9.特发信息000070 # 10.深特力000025 # 11.深物业000011   # 13.深纺织000045 # 14.通产丽星002243 # 15.深振业000006
# 16.深天健000090 # 17.深高速600548 # 20.沙河股份000014 # 21.国信证券002736
# 22.天威视讯（深圳市广电集团为实际控制人）002238 # 建科院300675
#  深股
# 12.深深房000029 天音控股（000829） 23.深深爱（新三板挂牌公司）833378 # 24.易图资讯（新三板挂牌公司）834386
# A股上市公司代码
arr = ['300675', '601318', '000002', '000829', '000089', '601139', '000027', '000037', '000088', '000058', '000061',
       '000019', '000070', '000025', '000011', '000029', '000045', '002243', '000006', '000090', '600548', '000014',
       '002736', '002238', '833378', '834386'];
# 上证综指000001SH,tushare里是用sh   深证综指399106SZ
zzarr = ['sh', '399106'];
#  港股 # 18.深圳国际0152HK # 19.深圳控股0604HK
hkarr = ['0152', '0604'];
# B股公司代码
barr = ['200037', '200011', '200029', '200025', '200058', '200045', '200019'];
# 200037.SZ深南电B
# 200011.SZ深物业B
# 200029.SZ深深房B
# 200025.SZ特力B
# 200058.SZ深赛格B
# 200045.SZ深纺织B
# 200019.SZ深深宝B

today = datetime.date.today();  # 获得今天的日期
lastmonth = today - datetime.timedelta(days=31);  # 用今天日期减掉时间差，参数为31天，获得上月的日期
endDate = today.strftime('%Y-%m-%d');
startDate = lastmonth.strftime('%Y-%m-%d');
date = today.strftime('%Y%m%d');

# 正式环境
# filePath = 'E:/python/workspace/data/';
# 本地环境
filePath = 'D:/java/python/PycharmProjects/pytest/day/';

# 获取A股股价
for code in arr:
    df = ts.get_k_data(code, start=startDate, end=endDate);
    df.to_json(filePath + date + code + '.json', orient='records');

# 获取B股股价
for code in barr:
    df = ts.get_k_data(code, start=startDate, end=endDate);
    df.to_json(filePath + date + code + '.json', orient='records');

# 获取上证综指、深证综指股价
for code in zzarr:
    df = ts.get_k_data(code, start=startDate, end=endDate);
    df.to_json(filePath + date + code + '.json', orient='records');
