import tushare as ts

pro = ts.pro_api('59d1cf89dca91fb2439d57aa2a34d7a286a31c041da6cfe4383cf30b')
#df = pro.limit_list_d(trade_date='20221202', limit_type='U', fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
df = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20221126', end_date='20221202')


print(df)
