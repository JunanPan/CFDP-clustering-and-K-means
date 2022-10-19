from matplotlib import pyplot as plt
import random
def distance(x1,y1,x2,y2): #计算两点间距离的函数 为了减少运算消耗没有加开根号的步骤
    return (x1-x2)**2+(y1-y2)**2
dot_list=[] #用于存放所有点的列表
def find_center(c): #找到第c类的中心位置的函数
    x_sum = 0
    y_sum = 0
    num = 1 #防止出现被除数为0的情况
    for dot in dot_list:
        if dot._class==c:
            x_sum+=dot.x
            y_sum+=dot.y
            num+=1
    x_center = x_sum/num
    y_center = y_sum/num
    return x_center,y_center
class Dot():#定义一个点类
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self._class = None
for i in range(500):    #随机生成500个点
    x = random.randint(1,200)
    y = random.randint(1,200)
    dot_list.append(Dot(x,y))
    # plt.plot(x,y,'d',color = 'blue')
x1=random.randint(1,200) #随机生成一开始的若干个中心
y1=random.randint(1,200)
x2=random.randint(1,200)
y2=random.randint(1,200)
x3=random.randint(1,200)
y3=random.randint(1,200)
x4=random.randint(1,200)
y4=random.randint(1,200)
x5=random.randint(1,200)
y5=random.randint(1,200)
x6=random.randint(1,200)
y6=random.randint(1,200)
last_x1 = 0 #给last_x1初始化值
last_y1 = 0
while ((last_x1!=x1)|(last_y1!=y1)): #当第一类一直再更新，只要有一个在变，则一直循环迭代
    last_x1 = x1
    last_y1 = y1
    for dot in dot_list:
        distance1=distance(dot.x,dot.y,x1,y1)
        distance2=distance(dot.x,dot.y,x2,y2)
        distance3=distance(dot.x,dot.y,x3,y3)
        distance4=distance(dot.x,dot.y,x4,y4)
        distance5=distance(dot.x,dot.y,x5,y5)
        distance6=distance(dot.x,dot.y,x6,y6)
        if distance1 == min(distance1,distance2,distance3,distance4,distance5,distance6):
            dot._class = 1
        elif distance2 == min(distance1,distance2,distance3,distance4,distance5,distance6):
            dot._class = 2
        elif distance3 == min(distance1,distance2,distance3,distance4,distance5,distance6):
            dot._class = 3
        elif distance4 == min(distance1,distance2,distance3,distance4,distance5,distance6):
            dot._class = 4
        elif distance5 == min(distance1,distance2,distance3,distance4,distance5,distance6):
            dot._class = 5
        else:
            dot._class = 6
    x1,y1 = find_center(1)
    x2,y2 = find_center(2)
    x3,y3 = find_center(3)  
    x4,y4 = find_center(4)    
    x5,y5 = find_center(5) 
    x6,y6 = find_center(6) 
plt.figure()
plt.plot(x1,y1,'o',color = 'red')
plt.plot(x2,y2,'o',color = 'red')
plt.plot(x3,y3,'o',color = 'red')
plt.plot(x4,y4,'o',color = 'red')
plt.plot(x5,y5,'o',color = 'red')
plt.plot(x6,y6,'o',color = 'red')
for dot in dot_list:
    if dot._class==1:
        plt.plot(dot.x,dot.y,'x',color = 'blue')
    elif dot._class==2:
        plt.plot(dot.x,dot.y,'d',color = 'green')
    elif dot._class==3:
        plt.plot(dot.x,dot.y,'^',color = 'black')
    elif dot._class==4:
        plt.plot(dot.x,dot.y,'^',color = 'purple')
    elif dot._class==5:
        plt.plot(dot.x,dot.y,'^',color = 'yellow')    
    else:
        plt.plot(dot.x,dot.y,'^',color = 'brown')  
plt.show()