# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:15:00 2017

@author: Z
"""

import numpy as np

def npSum():
    a = np.array([1,2,3,4])
    b = np.array([2,3,6,3])
    
    c = a**2 + b**3
    
    return c

print(npSum())

'''
ndarray:
    实际数据
    这些数据的描述（类型，维度）
'''

a = np.array([[2,3,4,5],[2,3,4,6]],dtype=np.int64)
b = np.array(list('1234324323423'),dtype=np.int64)
'''
.ndim    ：数组的维度
.shape   :数组的形状
.size    ：元素个数（.shape(n,m)=>n*m）
.dtype   :元素类型
.itemsize:每个元素大小/字节
'''
#支持元素类型非常多

'''
np.arange(n)        0----n-1
np.ones(shape)      生成全是1的shape形状数组
np.zeros(shape)     生成全是0的shape形状数组
np.full(shape,val)  生成全是val的shape形状数组
np.eye(n)           生成方阵，对角为1
'''
'''
np.ones_like(a)     根据a的形状生成全是1的数组
np.zeros_like(a)    根据a的形状生成全是0的数组
np.full_like(a,val) 根据a的形状生成全是val的数组
       
np.linspace()       根据起止数据等间距的填充数据，形成数组
np.concatenate()    将两个或多个数组合并成一个
'''



np.arange(4,13,2)
x = np.ones(shape=(3,4),dtype = np.int32)
ff=np.full(shape=(3,4),fill_value=45.,dtype=np.float64)

l = np.linspace(3,20,6)
#是否取最后一个数
ll = np.linspace(3,20,6,endpoint=False)
#数组连接
c = np.concatenate((l,ll))


#维度改变
'''
.reshape(shape)      返回一个shape形状的数组，原数组不变
.resize(shape)       返回一个shape形状的数组，改变原数组
.swapaxes(ax1,ax2)   将数组n个维度中的两个维度调换
.flatten()           对数组进行降维，返回一维数组，原数组不变
'''

a = np.ones(shape=(2,3,4),dtype=np.int32)

a1 = a.reshape(2,12)

a.resize((4,6))

#降成一维数组
a.flatten()


a = np.ones(shape=(2,3,4),dtype = np.int)
#变换类型
a.astype(dtype=np.float64)

#转变为python中的列表
a = np.full((2,3,4),23,dtype=np.int)
ls = a.tolist()

#数组的索引和切片
a = np.array([9,8,7,6,5,3,4,5,6,0])
a[2]

a[1::2]

a = np.arange(24).reshape(2,3,4)
a
a[1,1,3]
a[0,1,1]

xx = a[:,1:2,1:3]

#数组的计算

#计算数组的平均值的商
a = np.arange(24).reshape(4,6)

a.mean()

a = a/a.mean()

#原数组不改变
'''
np.abs(x) np.fabs(x)       计算各元素绝对值
np.sqrt(x)                 计算各元素平方根
np.square(x)               计算各元素的平方
np.log(x) np.log10(x) 
np.log2(x)                 计算各元素的底数

np.ceil(x)  np.floor(x)    计算各元素的ceiling 或floor
np.ring(x)                   计算各元素四舍五入的值
np.modf(x)                 计算各元素小数和整数部分，以独立方式返回
np.cos(x),np.cosh(x)
np.sin(x),np.sinh(x)
np.tan(x),np.tanh(x)       计算三角函数

np.exp(x)                  计算各元素的指数值
np.sign(x)                 计算各元素的符号 1（+），0 ，-1（-）
'''

'''
np.maximum(x,y)np.fmax()   元素级的最大
np.minimum(x,y)np.fmin()   元素级的最小
np.mod(x,y)                元素级的模运算
np.copysign(x,y)           将y中元素的符号给x
'''





















