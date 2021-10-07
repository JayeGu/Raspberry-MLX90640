from ctypes import *
import numpy as np
mlx90640 = cdll.LoadLibrary('./libmlx90640.so')
import matplotlib.pyplot as plt
import time
import smbus
bus=smbus.SMBus(1)
data = bus.read_word_data(0x33,0x800D)
bus.write_word_data(0x33,0x800D,data|0x0380)  #设置高帧率模式
# 
# mlx90640 will output 32*24 temperature array with chess mode
#
temp=(c_float*768)()
ptemp=pointer(temp)
mlx90640.get_mlx90640_temp(ptemp)
time.sleep(1)
mlx90640.get_mlx90640_temp(ptemp)
plt.figure(1)
while True:
    mlx90640.get_mlx90640_temp(ptemp)
    img = (temp-np.min(temp))/(np.max(temp)-np.min(temp))*255  #归一化
    img.resize(24,32)   #将一维数组转化为二维数组，便于转化为图片
    #img = img.astype(np.uint8)  #opencv处理的话就要
    plt.clf()
    plt.imshow(img,cmap='jet')  # jet/hsv/ranbow/gunplot等颜色模式可以选择，具体见网址https://blog.csdn.net/lly1122334/article/details/88535217
    plt.text(16,12,str(round(temp[383],2))+'°C')  #显示图像中心的物体温度
    plt.pause(0.001)