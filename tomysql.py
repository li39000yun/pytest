from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://root:root@127.0.0.1/python?charset=utf8')
# engine = create_engine('sqlserver://localhost:1433;DatabaseName=pytest;')
# engine = create_engine('mssql+pymssql://test:1@127.0.0.1:1433/pytest')
#存入数据库

# df = ts.get_hist_data('000875')#读取数据，格式为DataFrame
# engine = create_engine('mysql://root:pwd@192.168.226.148/tushare?charset=utf8')#用sqlalchemy创建引擎
# df.to_sql('tick_data',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
# df1 = pd.read_sql('tick_data',engine)#从数据库中读取表存为DataFrame

df.to_sql('tick_data',engine)
df1 = pd.read_sql('tick_data',engine)#从数据库中读取表存为DataFrame