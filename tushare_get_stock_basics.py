import tushare as ts
df = ts.get_stock_basics();
df.to_json('E:/python/workspace/data/stock_basics.json', orient='index');