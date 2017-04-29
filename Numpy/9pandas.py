# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:35:43 2017

@author: Z
"""

import pandas as pd
import numpy as np

######Series
#索引数据
a = pd.Series([3,4,2,1,5])

a1 = pd.Series([23,4,2,2],index=['a','b','c','d'])
a2 = pd.Series([23,4,23,2],['e','f','a','c'])

a3 = pd.Series(np.arange(100,200,5))
a4 = pd.Series(np.linspace(100,200,5),index = np.arange(9,4,-1))

a4.index
a4.values

a4[[9,8,7]]
a4[a4<a4.mean()]

#是否在索引中，
8 in a4

#获取，不存在返回23
a4.get(82,23)


#交集运算
a2+a1


#名字和索引名字
a4.name = 'a4数据'
a4.index.name = 'a4索引'


###########DataFrame
'''

                           column    axis = 1
         index      index ''''''''''''''''''''''''''''''
        axis = 0    index ''''''''''''''''''''''''''''''
                    index ''''''''''''''''''''''''''''''
                    index ''''''''''''''''''''''''''''''
                    index ''''''''''''''''''''''''''''''


'''

df = pd.DataFrame(np.arange(10).reshape(2,5))

dt = pd.DataFrame({'noe':pd.Series([1,2,3],index=['a','b','c']),
                    'two':pd.Series([3,4,5],index=['a','y','z'])
                    })

pd.DataFrame(dt,index=['a','b','c','z','h'],columns=['noe','bbb'])

#获取列数据
dt['noe']
#获取行数据
dt.ix['a']  



#重新索引
'''
.reindex(index=[])   重新索引,相当于重新排解数据
.reindex(columns=[])  
    fill_value       重新索引后用于填充缺失数据
    method           ffill:向前填充，bfill:向后填充
    limit            最大填充量
    copy             默认True,生成新的值，False，不相等时不复制
'''

newc = dt.columns.insert(2,'新增')

dc = dt.reindex(columns=newc,fill_value=200)


'''
.append()               连接另一个索引产生新的索引对象
.diff()                 计算差集，产生新的索引对象
.intersection()         计算交集
.union()                计算∪集
.delete(loc)            删除元素
.insert(loc,e)          插入元素

.drop()    默认删除行，axis=1可以删除列

'''

#运算标签相同的运算，不同扩维。


#数据的排序
'''
.sort_index()     根据索引排序
    axis=0,ascending=True
    
.sort_values()    根据数值排序
    .sort_values([By],axis=0,ascending=True)
    By根据指定索引排序
    axis 横或竖排序
    ascending 升序降序
    NaN统一放在末尾
'''


a=dc.describe()

b = pd.DataFrame(np.arange(20).reshape(4,5))
#累计计算
b.cumsum(axis=1)


#计算相邻
b.rolling(3,axis=1).sum()

#
#相关性分析
'''
X^--->Y^:正相关
X^--->Y_:负相关
X^----Y(随机)：不相关
'''

''''

r:0.8-1    强相关
r:0.6-0.8  相关
r:0.2-.06  弱相关

.cov
.corr()

a.corr(b)

'''























