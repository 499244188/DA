from matplotlib import pyplot as plt
import numpy as np

#%pylab
a = np.arange(10)
plt.plot(a,a*1.5,'r-.',a,a*2.5,'g|',a,a*3.5,'kD')
plt.plot(a,a*3,color='red',markersize=20)

#显示中文标签
'''
font.family:字体名称
font.style:风格（normal/italic）
font.size:字体大小

simhei:黑体
Kaiti：中文楷体
STSong:华文仿宋
LiSu:中文隶书
YouYuan:中文幼圆

'''
matplotlib.rcParams['font.family']='simhei'
plt.ylabel('纵轴标签')
plt.show()


a = np.arange(0.0,5.0,0.02)
plt.xlabel('横轴：时间',fontproperties='simhei',fontsize=20)
plt.ylabel('纵轴：振幅',fontproperties='simhei',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')

'''
plt.xlabel()   x轴标签
plt.ylabel()   y轴标签
plt.title()    标题
plt.text(x,y,'文本',)     任意位置文本

plt.axis([x0,x9,y0,y9])    坐标区间
plt.grid(True)             显示网格

plt.annotate('文本',xy=(x,1),xytext=(x,y),arrowprops=\
    dict(facecolor='black',shrink='0.1',width=2))



'''


'''
color:颜色
linestyle:线条风格
marker:标记风格
markerfacecolor：标记颜色
markersize:标记尺寸




'''







'''
颜色字符：
b:蓝色    m:洋红色（magenta)
g:绿色    y:黄色
r:红色    k:黑色
c:青色(cyan)     w:白色
#008000    RGB颜色     
0.8   灰度字符串

'''


'''
风格字符
-：实线
--：破折线
-.：点划线
：：虚线
空或者空格：不绘制线条
'''


'''
标记字符
.：点标记
，：像素标记（极小点）
o:实心圈
v:倒三角形
^：上三角形
>:右三角形
<:左三角形




1:下花三角
2：上花三角
3：左花三角
4：右花三角
s:实心正方形
p:实心五角星
*:星型标记


h:竖六边形
H:横六边形
+：十字标记
x:x标记
D:菱形标记
d:瘦菱形标记
|：垂直线标记
'''

#多窗口

from matplotlib import pyplot as plt
import numpy as np

plt.subplot2grid((6,6),(2,4))
plt.show()

plt.subplot2grid((4,4),(1,0),colspan=4)
'''
colspan:横向延伸
rowspan:纵向延伸
'''
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(3,3)

ax1 = plt.subplot(gs[0,:])

'''
gs[x0:x9,y0:y9]
'''





























