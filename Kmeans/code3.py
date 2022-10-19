import pandas as pd
import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
a = pd.read_csv('consumption_data.csv',encoding='gbk')

min_R=min(a['R']);max_R=max(a['R']);gap_R = max_R - min_R 
min_F=min(a['F']);max_F=max(a['F']);gap_F = max_F - min_F
min_M=min(a['M']);max_M=max(a['M']);gap_M = max_M - min_M

for i in range(len(a)):
    a.loc[i,'R'] = (a.loc[i]['R']-min_R)/gap_R
    a.loc[i,'F'] = (a.loc[i]['F']-min_F)/gap_F
    a.loc[i,'M'] = (a.loc[i]['M']-min_M)/gap_M
#至此所有数据都归一化完成，这样画图画起来就比较美观可见了
#此时的数据预览如下：
""" 
       消费间隔，  消费频率，  消费总金额，我预计把他们分成三类
   Id         R         F         M
0   1  0.223140  0.161290  0.026940
1   2  0.024793  0.129032  0.190930
2   3  0.033058  0.483871  0.102213
3   4  0.024793  0.322581  0.026965
4   5  0.115702  0.193548  0.243163
"""
dot_list = []
def distance(R1,F1,M1,R2,F2,M2):
    return abs(R1-R2)+abs(F1-F2)+abs(M1-M2)
def find_center(c): #找到第c类的中心
    R_sum = 0
    F_sum = 0
    M_sum = 0
    num = 1
    for dot in dot_list:
        if dot._class==c:
            R_sum+=dot.R
            F_sum+=dot.F
            M_sum+=dot.M
            num+=1
    R_center = R_sum/num
    F_center = F_sum/num
    M_center = M_sum/num
    return R_center,F_center,M_center
class Dot():#定义一个点类
    def __init__(self,R,F,M):
        self.R = R
        self.F = F
        self.M = M
        self._class = None
for i in range(len(a)):
    R = a.loc[i,:]['R']
    F = a.loc[i,:]['F']
    M = a.loc[i,:]['M']
    dot = Dot(R,F,M)
    dot_list.append(dot)
#第一个0-1的聚类中心
R1 = random.random() 
F1 = random.random()
M1 = random.random()
#第二个
R2 = random.random() #随机生成0-1的中心
F2 = random.random()
M2 = random.random()
#第三个
R3 = random.random() #随机生成0-1的中心
F3 = random.random()
M3 = random.random()

last_R1 = -1
last_F1 = -1
last_M1 = -1

while((last_R1!=R1)|(last_F1!=F1)|(last_M1!=M1)):
    last_R1=R1
    last_F1=F1
    last_M1=M1
    for dot in dot_list:
        distance1 = distance(dot.R,dot.F,dot.M,R1,F1,M1)
        distance2 = distance(dot.R,dot.F,dot.M,R2,F2,M2)
        distance3 = distance(dot.R,dot.F,dot.M,R3,F3,M3)
        #print('distance',distance1)
        if distance1 == min(distance1,distance2,distance3):
            
            dot._class = 1
        elif distance2 == min(distance1,distance2,distance3):
            
            dot._class = 2
        else:
            dot._class = 3
    R1,F1,M1 = find_center(1)
    R2,F2,M2 = find_center(2)
    R3,F3,M3 = find_center(3)



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