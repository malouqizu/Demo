#encoding=UTF-8
import tushare as ts

import matplotlib.pyplot as plt
df=ts.get_hist_data('sh', start='2016-08-11')
df.to_excel('stock_sh.xlsx')
df.close.plot()
ax = plt.gca()
ax.invert_xaxis()
plt.show()

'''
1. 获取股票历史数据
ts.get_hist_data('601688')

2. 获取股票实时行情
ts.get_realtime_quotes('000002')

3. 存款利率
ts.get_deposit_rate()

4. 电影票房
ts.realtime_boxoffice()

5.
import matplotlib.pyplot as plt
df=ts.get_hist_data('sh', start='2016-01-01')
df.to_excel('stock_sh.xlsx')
df.close.plot()
ax = plt.gca()
ax.invert_xaxis()
plt.show()

6.看新闻
ts.get_latest_news()

7.看一些宏观数据，如居民消费指数：
ts.get_cpi()

8.看股票基本面：
ts.get_stock_basics()

9.获取一些分类信息，如上证50成份股：
ts.get_sz50s()
'''