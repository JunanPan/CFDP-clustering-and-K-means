import pandas as pd
import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
a = pd.read_csv('./sales_data.csv',encoding='gbk')
a['天气'] = a['天气'].map({'坏':0,'好':1})  #我把更倾向于高销量的变量置为1，因为感觉三个变量都差不多重要，所以都按同等0/1划分
a['是否周末'] = a['是否周末'].map({'否':0,'是':1}) 
a['是否有促销'] = a['是否有促销'].map({'否':0,'是':1}) 
a['销量'] = a['销量'].map({'低':0,'高':1}) 
day_list = []
def distance(x1,y1,z1,x2,y2,z2):
    return (x1-x2)**2+(y1-y2)**2+(z1-z2)**2
def find_center(c): #找到第c类的中心
    x_sum = 0
    y_sum = 0
    z_sum = 0
    num = 1
    for day in day_list:
        if day._class==c:
            x_sum+=day.weather
            y_sum+=day.weekend
            z_sum+=day.promotion
            num+=1
    x_center = x_sum/num
    y_center = y_sum/num
    z_center = z_sum/num
    return x_center,y_center,z_center
class Day(): #定义类表示每天
    def __init__(self,weather,weekend, promotion,sale):
        self.weather = weather
        self.weekend = weekend
        self.promotion = promotion
        self.sale = sale #高销量
        self._class = None
for i in range(len(a)):  #把每一行的数据逐一变成类然后存入列表
    weather = a.loc[i,:]['天气'] + random.random()/4 #因为所有的数值都是01，如果画在图上会重叠在一起，所以我给每一个点随机增加少量大小，以便让他们区分
    weekend = a.loc[i,:]['是否周末']+ random.random()/4
    promotion = a.loc[i,:]['是否有促销']+ random.random()/4
    sale = a.loc[i,:]['销量'] #虽然我读取了四个属性，但销量应该算是标签，在我分类的时候我只考虑前三个属性
    day = Day(weather,weekend,promotion,sale)
    day_list.append(day)
#因为销量就两种，所以我聚类也两种，看看根据前三个属性聚类的结果是否与销量分布类似
#随机生成第一个聚类中心
weather1 = random.randint(0,1)
weekend1 = random.randint(0,1)
promotion1 = random.randint(0,1)
#随机生成第二个聚类中心
weather2 = random.randint(0,1)
weekend2 = random.randint(0,1)
promotion2 = random.randint(0,1)

last_weather1 = -1
last_weekend1 = -1
last_promotion1 = -1
while((last_weather1!=weather1)|(last_weekend1!=weekend1)|(last_promotion1!=promotion1)):
    last_weather1 = weather1
    last_weekend1 = weekend1
    last_promotion1 = promotion1
    for day in day_list:
        #对于每一个点，都判断它和哪一个聚类中心更近
        distance1 = distance(day.weather,day.weekend,day.promotion,weather1,weekend1,promotion1)
        distance2 = distance(day.weather,day.weekend,day.promotion,weather2,weekend2,promotion2)
        if distance1 == min(distance1,distance2):
            day._class = 1
        else:
            day._class = 2
    weather1,weekend1,promotion1 = find_center(1)
    weather2,weekend2,promotion2 = find_center(2)
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
#以3D图形的形式画出按实际是否有高销量划分的结果 从而进行比较，看看聚类的效果和实际效果相差多少
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