# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:53:41 2017

@author: Z
"""

from PIL import Image
import numpy as np
#im = np.array(Image.open('E:\\X\\numpy\背景.jpg'))

#变为灰度图
im = np.array(Image.open('E:\\X\\numpy\背景.jpg').convert('L'))
print(im.shape,im.dtype)

#对像素运算
#b=[255,255,30]-im

#灰度处理
#b=255-im

#区间变换
#b=(100/255)*im + 150

#像素平方
b=255*(im/255)**2
imz = Image.fromarray(b.astype('uint8'))
imz.save('E:\\X\\aaaa.jpg')

#####手绘效果
a = np.asarray(Image.open('').convert('L')).astype('float')

depth = 10.                     #(0-100)
grad = np.gradient(a)           #取图像的灰度梯度
grad_x,grad_y = grad            #拆分图像的灰度梯度
