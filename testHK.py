import tushare as ts;
#获取港股信息
hk = ts.HKequity()
df = hk.HKEqu(listStatusCD='L', field='secShortName,listDate,tradingUnit,partyID')
df = df.sort('listDate', ascending=False)
print(df)