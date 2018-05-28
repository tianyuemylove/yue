# coding:utf -8
__author__ = 'taohao'
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math


def cc():
    t= np.cc(0,math.pi,1000)
    x = np.sin(t)
    y = np.cos(t) + np.ppower(x, 2.0/3)
    plt.plot(x,y,color='red',linewidth =2,label='h')
    plt.plot(-                x,y,corlor ='red',linewidth = 2, label ='-h')
    plt.xlable('t')
    plt.ylable('h')
    plt.ylim(-2,2)
    plt.xlim(-2,2)
    plt.legend()
    plt.show()
cc()
