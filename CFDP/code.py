from matplotlib import pyplot as plt
import random

class Dot():#定义一个点类
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cut_off = 0 #邻居数，也就是局部密度
        self.distance = 0#距离
        self._class = None

def distance(x1,y1,x2,y2): #计算两点间距离的函数
    return (x1-x2)**2+(y1-y2)**2
dot_list=[] #用于存放所有点的列表
for i in range(500):    #随机生成500个点
    x = random.randint(1,200)
    y = random.randint(1,200)
    dot_list.append(Dot(x,y))
#计算密度
dc = 120
for dot1 in dot_list:
    for dot2 in dot_list:
        if distance(dot1.x,dot2.x,dot1.y,dot2.y)==0:
            pass
        else:
            if distance(dot1.x,dot2.x,dot1.y,dot2.y)<dc:
                dot1.cut_off+=1
#用以找到合适的dc值
# sum1 = 0
# for dot in dot_list:
#     sum1+=dot.cut_off
# print(sum1/500/500)

#计算距离
for dot1 in dot_list:
    flag = 0#是局部密度最大点
    min_distance=[]
    for dot2 in dot_list:
        if dot1.cut_off<dot2.cut_off:
            flag=1#不是局部密度最大点了
            min_distance.append(distance(dot1.x,dot2.x,dot1.y,dot2.y))
    if flag==1:#不是局部密度最大点，
        dot1.distance=min(min_distance)
    else:#仍然是局部密度最大点
        for dot2 in dot_list:
            if distance(dot1.x,dot2.x,dot1.y,dot2.y)>dot1.distance:
                dot1.distance=distance(dot1.x,dot2.x,dot1.y,dot2.y)
dot_list.sort(key=lambda x:x.cut_off+x.distance,reverse=True)
# for dot in dot_list:
#     print(dot.cut_off)
class_num = 3
dot_list[0]._class = 1
dot_list[1]._class = 2
dot_list[2]._class = 3
for dot in dot_list[3:]:
    if distance(dot.x,dot.y,dot_list[0].x,dot_list[0].y) == min(distance(dot.x,dot.y,dot_list[0].x,dot_list[0].y),distance(dot.x,dot.y,dot_list[1].x,dot_list[1].y),distance(dot.x,dot.y,dot_list[2].x,dot_list[2].y)):
        dot._class=1
    elif distance(dot.x,dot.y,dot_list[1].x,dot_list[1].y) == min(distance(dot.x,dot.y,dot_list[0].x,dot_list[0].y),distance(dot.x,dot.y,dot_list[1].x,dot_list[1].y),distance(dot.x,dot.y,dot_list[2].x,dot_list[2].y)):
        dot._class=2
    else:
        dot._class=3
for dot in dot_list:
    if dot._class==1:
        plt.plot(dot.x,dot.y,'x',color = 'blue')
    elif dot._class==2:
        plt.plot(dot.x,dot.y,'d',color = 'green')
    elif dot._class==3:
        plt.plot(dot.x,dot.y,'^',color = 'black')
plt.show()