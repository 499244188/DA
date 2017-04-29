# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
#饼图
labels = 'frogs','hogs','dogs','logs'
sizes = [15,50,10,50]
explode = (0.1,0,0,0)

plt.pie(sizes,explode = explode,labels = labels,autopct='%.1f%%',shadow=False,\
        startangle=90)
plt.axis('equal')#正圆形
plt.show()

#直方图
np.random.seed(102)
mu,sigma = 1000,20  #均值和方差
a = np.random.normal(mu,sigma,size=100)

#normed  0/1   个数和概率
plt.hist(a,40,normed=0,histtype='stepfilled',facecolor='r',alpha=0.75)
plt.title('Histogram')


plt.show()


#步阶图
x = np.linspace(0.1, 4*np.pi, 50)
markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
plt.setp(baseline, 'color', 'r', 'linewidth', 2)
plt.show()


#对象坐标系

 
N=5

theta = np.linspace(.0,2*np.pi,N,endpoint=False)
radii = 5*np.random.rand(N)
width = np.pi/2*np.random.rand(N)

ax = plt.subplot(111,projection='polar')

bars = ax.bar(theta,radii,width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
    
plt.show()

#绘制散点图
fig,ax = plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simplt Scatter')

plt.show()


