import pandas as pd
import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
a = pd.read_csv('sales_data.csv',encoding='gbk')
a['天气'] = a['天气'].map({'坏':0,'好':1})  #我把更倾向于高销量的变量置为1，因为感觉三个变量都差不多重要，所以都按同等0/1划分
a['是否周末'] = a['是否周末'].map({'否':0,'是':1}) 
a['是否有促销'] = a['是否有促销'].map({'否':0,'是':1}) 
a['销量'] = a['销量'].map({'低':0,'高':1}) 
day_list = []
def distance(x1,y1,z1,x2,y2,z2):
    return (x1-x2)**2+(y1-y2)**2+(z1-z2)**2
class Day(): #定义类表示每天
    def __init__(self,weather,weekend, promotion,sale):
        self.weather = weather
        self.weekend = weekend
        self.promotion = promotion
        self.sale = sale #高销量
        self.cut_off = 0 #邻居数，也就是局部密度
        self.distance = 0#距离
        self._class = None
for i in range(len(a)):  #把每一行的数据逐一变成类然后存入列表
    weather = a.loc[i,:]['天气'] + random.random()/4 #因为所有的数值都是01，如果画在图上会重叠在一起，所以我给每一个点随机增加少量大小，以便让他们区分
    weekend = a.loc[i,:]['是否周末']+ random.random()/4
    promotion = a.loc[i,:]['是否有促销']+ random.random()/4
    sale = a.loc[i,:]['销量'] #虽然我读取了四个属性，但销量应该算是标签，在我分类的时候我只考虑前三个属性
    day = Day(weather,weekend,promotion,sale)
    day_list.append(day)
dc=0.01
for day1 in day_list:
    for day2 in day_list:
        if distance(day1.weather,day1.weekend,day1.promotion,day2.weather,day2.weekend,day2.promotion)==0:
            pass
        else:
            if distance(day1.weather,day1.weekend,day1.promotion,day2.weather,day2.weekend,day2.promotion)-dc<0:
                day1.cut_off+=1
# for day in day_list:
#     print(day.cut_off)
# sum1 = 0
# for day in day_list:
#     sum1+=day.cut_off
# print(sum1/34/34)#共有34个数据

#计算距离
for day1 in day_list:
    flag = 0#是局部密度最大点
    min_distance=[]
    for day2 in day_list:
        if day1.cut_off<day2.cut_off:
            flag=1#不是局部密度最大点了
            min_distance.append(distance(day1.weather,day1.weekend,day1.promotion,day2.weather,day2.weekend,day2.promotion)) 
    if flag==1:
        day1.distance=min(min_distance)
    else:#仍然是局部密度最大点
        for day2 in day_list:
            if distance(day1.weather,day1.weekend,day1.promotion,day2.weather,day2.weekend,day2.promotion)>day1.distance:
                day1.distance=distance(day1.weather,day1.weekend,day1.promotion,day2.weather,day2.weekend,day2.promotion)
day_list.sort(key=lambda x:x.cut_off+x.distance,reverse=True)
# for day in day_list:
#     print(day.cut_off)
class_num = 2
day_list[0]._class = 1
day_list[1]._class = 2
for day in day_list[2:]:
    if distance(day_list[0].weather,day_list[0].weekend,day_list[0].promotion,day.weather,day.weekend,day.promotion) <\
        distance(day_list[1].weather,day_list[1].weekend,day_list[1].promotion,day.weather,day.weekend,day.promotion):
        day._class=1
    else:
        day._class=2
#以3D图形的形式画出聚类结果
ax=plt.axes(projection='3d')
for day in day_list:
    if day._class == 1:
        ax.scatter3D(day.weather,day.weekend,day.promotion,color='green')
    elif day._class ==2:
        ax.scatter3D(day.weather,day.weekend,day.promotion,color='red')
ax.set_xlabel('weahter')
ax.set_ylabel('weekend')
ax.set_zlabel('promotion')
plt.show()
#而只看标签（销量）
ax1=plt.axes(projection='3d')
for day in day_list:
    if day.sale == 1:
        ax1.scatter3D(day.weather,day.weekend,day.promotion,color='brown')
    elif day.sale ==0:
        ax1.scatter3D(day.weather,day.weekend,day.promotion,color='blue')
ax1.set_xlabel('weahter')
ax1.set_ylabel('weekend')
ax1.set_zlabel('promotion')
plt.show()