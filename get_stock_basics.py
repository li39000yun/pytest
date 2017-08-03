import tushare as ts
df = ts.get_stock_basics();
df.to_json('D:/java/python/PycharmProjects/pytest/day/stock_basics.json', orient='index');