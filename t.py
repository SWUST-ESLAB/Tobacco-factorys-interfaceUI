
from cProfile import label
from operator import index
from sqlite3 import Row
import pandas as pd
import matplotlib.pyplot as plt
from requests import delete
import seaborn as sns
import numpy as np
import os
def jinomal(X):

    for i in range(X.shape[1]):
        max=X[:,i].max()
        min=X[:,i].min()
        if (max-min)!=0:
            X[:,i]=(X[:,i]-min)/(max-min)
        else:
            X[:,i]=0
    return X

def ShowGRAHeatMap(DataFrame,xticks,yticks):
    colormap = plt.cm.RdBu
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.figure(figsize=(10,14))
    plt.title('GRA Heatmap', y=1.05, size=15)
    ax=sns.heatmap(DataFrame.astype(float),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
    ax.set_xticks([i for i in range(DataFrame.shape[1])],xticks,rotation=80)
    ax.set_yticks([i for i in range(DataFrame.shape[0])],yticks,rotation=0)
    plt.savefig('GRA.jpg')
    plt.show()

def getdata(pathname):
    data = pd.read_excel(pathname,skiprows = 1,skipfooter=200)
    #data = pd.read_excel(pathname,skipfooter = 100)
    deletlist=['时间','烘梗加香批次号','烘梗加香批次状态','sirox增温增湿-物料流量','sirox增温增湿-物料重量','sirox增温增湿-提升机电机频率','sirox增温增湿-入口物料含水率修正值',
                    'sirox增温增湿-入口物料含水率','sirox增温增湿-蒸汽流量','梗丝加香-物料流量','梗丝加香-物料重量','梗丝加香-筒体电机频率','梗丝加香-出口物料含水率',
                    '梗丝加香-出口物料含水率修正值','梗丝加香-加香重量','梗丝加香-出口物料温度','梗丝加香-加香累计精度','梗丝加香-加香比例','梗丝加香-加香设定比例','Unnamed: 0']
    deleteheader = [3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,
                	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60,	61,	62,	63,	64,	65,	66,	67,	68,	69,	70,	71,	72,	73,	74,	
                    75,	76,	77,	78,	79,	80,	81,	82,	83,	84,	85,	86,	87,	88,	89,	90,	91,	92,	93,	94,	95,	96,	97,	98,	99,	100,	101,	102,	103,	104,	105,	
                    106,	107,	108,	109,	110,	111,	112,	113,	114,	115,	116,	117,	118,	119,	120,	121,	122,	123,	124,	
                    125,	126,	127,	128,	129,	130,	131,	132,	133,	134,	135,	136,	137,	138,	139,	140,	141,	142,	143,	
                    144,	145,	146,	147,	148,	149,	150,	151,	152,	153,	154,	155,	156,	157,	158,	159,	160,	161,	162,	
                    163,	164,	165,	166,	167,	168,	169,	170,	171,	172,	173,	174,	175,	176,	177,	178,	179,	180,	181,	
                    182,	183,	184,	185,	186,	187,	188,	189,	190,	191,	192,	193,	194,	195,	196,	197,	198,	199,	200,	
                    201,	202,	204]

                    
    data = data.drop(deletlist,axis=1)
    data = data.drop(deleteheader,axis=0)
    #data = data.drop(data.tail(100),axis=0)
    data=data.dropna(axis=0,how='any')
    d = data.pop('烘梗丝(滚筒)-出口物料含水率')
    data.insert(0,'烘梗丝(滚筒)-出口物料含水率', d)
    # 原始数据序列
    X = data.values
    #print(X)
    #X[X==0]=1e-14
    # 无量纲化处理
    #X = X / X[0,:]
    X=jinomal(X)
    return X

def getgamma(X):
    # 求差值序列
    X = abs((X - X[:, 0].reshape(len(X), 1))[:, 1:])

    M_delata = X.max()
    m_delta = X.min()

    rho = 0.5
    Xi = (m_delta + rho * M_delata) / (X + rho * M_delata)
    gamma = Xi.mean(axis=0)
    return gamma
    
def showheatmap_test():
    #X=np.array([[1,5,3,4],[2,5,7,6],[4,8,2,3]],dtype=np.float16)
    root='E:/Data/data'
    dirs = os.listdir( root )
    g=np.empty((0,9))
    c=np.empty((0,10))
    xstick=['sirox出口物料温度','烘梗丝(滚筒)-热风温度','烘梗丝(滚筒)-热风风速','烘梗丝(滚筒)-热风开度','烘梗丝(滚筒)-出料罩压力',
                '烘梗丝(滚筒)-筒壁温度','烘梗丝(滚筒)-排潮开度','烘梗丝(滚筒)-出口物料含水率修正值','烘梗丝(滚筒)-出口物料温度']
    ystick=[]
    for file in dirs:
        X=getdata(root+'/'+file)
        g = np.row_stack((g, getgamma(X)))
        c = np.row_stack((c, X))
        ystick.append(file)
    g = np.row_stack((g, getgamma(c)))
    ystick.append('total')
    ShowGRAHeatMap(g,xstick,ystick)
    return g,xstick,ystick