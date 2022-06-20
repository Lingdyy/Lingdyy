import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3,4,5,6,7,8]
y = [60,45,49,36,42,67,40,50]
plt.bar(x,y)
plt.show()
plt.bar(x,y,width = 0.5,color = 'r')
plt.show()
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']#设置字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False #解决负号显示为方块的问题
x = ['上海','成都','重庆','深圳','北京','长沙','南京','青岛']
y = [60,45,49,36,42,67,40,50]
plt.barh(x,y,height = 0.5,color = 'r') #参数height用于设置条形的高度
plt.show()
x = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y = [50,45,65,76,75,85,55,78,86,89,94,90]
plt.plot(x,y,color = 'r',linewidth = 2,linestyle = 'dashdot')#linewidth设置折线图的粗细，linestyle设置折线的线形
plt.show()
plt.plot(x,y,color = 'r',linewidth = 2,linestyle = 'dashdot',marker = '*',markersize = 10)#maker='*'表示设置数据标记样式为五角星，makersize=10表示设置数据标记的大小为10点。
plt.show()
plt.stackplot(x,y,color = 'r')#starckplot绘制面积图
plt.show()
data = pd.read_excel('汽车速度和刹车距离表.xlsx')
x = data['汽车速度(km/h)']
y = data['刹车距离(m)']
plt.scatter(x,y,s = 100,marker = 'o',color = 'r',edgecolor = 'k')
plt.show()
from sklearn import linear_model
data = pd.read_excel('汽车速度和刹车距离表.xlsx')
x = data['汽车速度(km/h)']
y = data['刹车距离(m)']
plt.scatter(x,y,s = 100,marker='o',color='r',edgecolor = 'k')#参数s用于设置每个点的面积，参数maker用于设置每个点的样式，color和edgecolor分别用于设置每个点的填充颜色和轮廓颜色。
model = linear_model.LinearRegression().fit(x.values.reshape(-1,1),y)#导入Scikit-Learn模块中的函数创建了一个线性回归算法模型，用于根据汽车速度预测刹车距离，第10行根据预测结果使用plot()函数绘制了一条线性趋势线
pred = model.predict(x.values.reshape(-1,1))
plt.plot(x,pred,color='k',linewidth=3,linestyle='solid')
plt.show()
x = ['上海','成都','重庆','深圳','北京','长沙','南京']
y = [10,45,25,36,45,56,78]
plt.pie(y,labels = x,labeldistance = 1.1,autopct = '%.2f%%',pctdistance = 1.5,explode = [0,0,0,0,0,0.3,0],startangle = 90,counterclock = True)
plt.show()
plt.pie(y,labels = x,labeldistance=1.1,autopct = '%.2f%%',pctdistance = 1.5,startangle = 90,counterclock = True,wedgeprops = {'width':0.3,'linewidth':2,'edgecolor':'white'})
plt.show()
