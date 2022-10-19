import pandas as pd
import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
a = pd.read_csv('consumption_data.csv',encoding='gbk')
#归一化
min_R=min(a['R']);max_R=max(a['R']);gap_R = max_R - min_R 
min_F=min(a['F']);max_F=max(a['F']);gap_F = max_F - min_F
min_M=min(a['M']);max_M=max(a['M']);gap_M = max_M - min_M
for i in range(len(a)):
    a.loc[i,'R'] = (a.loc[i]['R']-min_R)/gap_R
    a.loc[i,'F'] = (a.loc[i]['F']-min_F)/gap_F
    a.loc[i,'M'] = (a.loc[i]['M']-min_M)/gap_M
dot_list = []
def distance(R1,F1,M1,R2,F2,M2):
    return abs(R1-R2)+abs(F1-F2)+abs(M1-M2)
class Dot():#定义一个点类
    def __init__(self,R,F,M):
        self.R = R
        self.F = F
        self.M = M
        self.cut_off = 0#局部密度
        self.distance = 0#距离
        self._class = None
for i in range(len(a)):
    R = a.loc[i,:]['R']
    F = a.loc[i,:]['F']
    M = a.loc[i,:]['M']
    dot = Dot(R,F,M)
    dot_list.append(dot)
#计算密度
dc = 0.08
for dot1 in dot_list:
    for dot2 in dot_list:
        if distance(dot1.R,dot1.F,dot1.M,dot2.R,dot2.F,dot2.M)==0:
            pass
        else:
            if distance(dot1.R,dot1.F,dot1.M,dot2.R,dot2.F,dot2.M)<dc:
                dot1.cut_off+=1

# 用以找到合适的dc值
# sum1 = 0
# for dot in dot_list:
#     sum1+=dot.cut_off
# print(sum1/940/940) #0.01490 满足百分之1到2

#计算距离
for dot1 in dot_list:
    flag = 0#是局部密度最大点
    min_distance=[]
    for dot2 in dot_list:
        if dot1.cut_off<dot2.cut_off:
            flag=1#不是局部密度最大点了
            min_distance.append(distance(dot1.R,dot1.F,dot1.M,dot2.R,dot2.F,dot2.M))
    if flag==1:
        dot1.distance=min(min_distance)
    else:#仍然是局部密度最大点
        for dot2 in dot_list:
            if distance(dot1.R,dot1.F,dot1.M,dot2.R,dot2.F,dot2.M)>dot1.distance:
                dot1.distance=distance(dot1.R,dot1.F,dot1.M,dot2.R,dot2.F,dot2.M)
dot_list.sort(key=lambda x:x.cut_off+x.distance,reverse=True)
class_num = 3
dot_list[0]._class = 1
dot_list[1]._class = 2
dot_list[2]._class = 3
for dot in dot_list[3:]:
    if distance(dot.R,dot.F,dot.M,dot_list[0].R,dot_list[0].F,dot_list[0].M) == \
        min(distance(dot.R,dot.F,dot.M,dot_list[0].R,dot_list[0].F,dot_list[0].M)\
            ,distance(dot.R,dot.F,dot.M,dot_list[1].R,dot_list[1].F,dot_list[1].M)\
                ,distance(dot.R,dot.F,dot.M,dot_list[2].R,dot_list[2].F,dot_list[2].M)):
        dot._class=1
    elif distance(dot.R,dot.F,dot.M,dot_list[1].R,dot_list[1].F,dot_list[1].M) == \
        min(distance(dot.R,dot.F,dot.M,dot_list[0].R,dot_list[0].F,dot_list[0].M)\
            ,distance(dot.R,dot.F,dot.M,dot_list[1].R,dot_list[1].F,dot_list[1].M)\
                ,distance(dot.R,dot.F,dot.M,dot_list[2].R,dot_list[2].F,dot_list[2].M)):
        dot._class=2
    else:
        dot._class=3

ax=plt.axes(projection='3d')
for dot in dot_list:
    if dot._class == 1:
        ax.scatter3D(dot.R,dot.F,dot.M,color='green')
    elif dot._class ==3:
        ax.scatter3D(dot.R,dot.F,dot.M,color='blue')
    else:
        ax.scatter3D(dot.R,dot.F,dot.M,color='red')
ax.set_xlabel('R')
ax.set_ylabel('F')
ax.set_zlabel('M')
plt.show()