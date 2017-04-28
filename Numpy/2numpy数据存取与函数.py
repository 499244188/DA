# -*- coding: utf-8 -*-

import numpy as np

#csv文件
'''
np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='',
            footer='', comments='# ')

'''

a = np.arange(100).reshape(5,20)
np.savetxt('e:\\X\\numpy\\a.csv',a,fmt='%.2f',delimiter=',',header='aaa')






'''
np.loadtxt(fname, dtype=float, comments='#', delimiter=None,
            converters=None, skiprows=0, usecols=None, unpack=False,
            ndmin=0)

'''
np.loadtxt('e:\\X\\numpy\\a.csv',dtype=float,delimiter=',',skiprows=4)






a = np.arange(100).reshape(5,10,2)
a.tofile('e:\\X\\numpy\\b.dat',sep=',',format='%d')
a.tofile('e:\\X\\numpy\\c.dat',format='%d')

c=np.fromfile('e:\\X\\numpy\\c.dat',dtype=np.int).reshape(2,5,10)
c



#np.savez()
a = np.arange(100).reshape(2,5,10)
x=np.save('e:\\X\\numpy\\a.npy',a)
np.load('e:\\X\\numpy\\a.npy')


'''
np.random.randint(2,10,size=20).reshape(4,5)
#随机函数
rand(d0,d1,d2...dn)  根据d0-dn为维度创建随机数组，浮点数，[0,1]，均匀分布。
randn(d0,d1,d2,,,db)  ....标准正态分布

np.random.randint(2,10,size=20).reshape(4,5) 
np.random.randint(100,200,(3,4))

seed(s)   随机种子

'''
np.random.rand(2,3,4)
np.random.randn(20,2)
np.random.randint(100,200,(3,4))

'''
np.random.shuffle(a)       根据a轴的第一列随机排列，改变数组x
np.random.permutation(a)   根据数组a产生一个连续数据，不改变x
np.random.choice(,size,replace,p)  从一位数组中，以概率p抽取元素，形成新的数组，replace
                                    表示是否可以重用元素，默认False
'''

b = np.random.randint(100,200,(5,))

c = np.random.choice(b,(3,3),p = b/np.sum(b))

'''
np.random.uniform(low,high,size)            产生均匀分布数组，low为起始，high为结束，size形状
np.random.normal(loc,scale,size)            产生正态分布，loc均值，scale标准差，size形状
np.random.poisson(lam,size)                 产生泊松分布，lam随机概率，size形状
'''

'''
np.gradient(f)       梯度，连续值得变化率，即斜率
                     （当前值-前一个）/2
                     n维的数组有n个梯度值
'''












