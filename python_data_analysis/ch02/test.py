import  json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
##使用pylab进行调试
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
#无格式的数据转换成json格式
records = [json.loads(line) for  line in  open(path)]
#将json格式的数据转换成表格的形式
frame = DataFrame(records)
#表格中缺失项自动填充Missing
clean_tz = frame['tz'].fillna('Missing')
#表格中空白项自动填充Unknown
clean_tz[clean_tz == ''] = 'Unknown'
#重新统计
tz_counts = clean_tz.value_counts()
#表格输出前十项
tz_counts[:10].plot(kind='barh', rot=0)
#单独切出表格中的user-agent项
results = Series([x.split()[0] for x in frame.a.dropna()])
#查看user-agent和地区的关系
#移除无useragent的项
cframe = frame[frame.a.notnull()]
#将useragent中的Windows和Not Windows分开
operating_system = np.where(
    cframe['a'].str.contains('Windows'),
    'Windows','Not Windows'
)
#对新得到的表进行分组
by_tz_os = cframe.groupby(['tz',operating_system])
#对分组进行计数统计
agg_count = by_tz_os.size().unstack().fillna(0)
#对统计进行排序
indexer = agg_count.sum(1).argsort()
count_subset = agg_count.take(indexer)[-10:]
count_subset.plot(kind='barh', stacked=True)
#对统计使用相对比例的方式输出
normed_submet = count_subset.div(count_subset.sum(1), axis=0)
normed_submet.plot(kind='barh', stacked=True)