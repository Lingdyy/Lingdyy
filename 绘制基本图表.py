import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3,4,5,6,7,8]
y = [60,45,49,36,42,67,40,50]
plt.bar(x,y)
plt.show()
plt.bar(x,y,width = 0.5,color = 'r')
plt.show()
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
x = ['上海','成都','重庆','深圳','北京','长沙','南京','青岛']
y = [60,45,49,36,42,67,40,50]
plt.barh(x,y,height = 0.5,color = 'r') #参数height用于设置条形的高度
plt.show()
x = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y = [50,45,65,76,75,85,55,78,86,89,94,90]
plt.plot(x,y,color = 'r',linewidth = 2,linestyle = 'dashdot')
plt.show()
plt.plot(x,y,color = 'r',linewidth = 2,linestyle = 'dashdot',marker = '*',markersize = 10)
plt.show()
plt.stackplot(x,y,color = 'r')
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
plt.scatter(x,y,s = 100,marker='o',color='r',edgecolor = 'k')
model = linear_model.LinearRegression().fit(x.values.reshape(-1,1),y)
pred = model.predict(x.values.reshape(-1,1))
plt.plot(x,pred,color='k',linewidth=3,linestyle='solid')
plt.show()
x = ['上海','成都','重庆','深圳','北京','长沙','南京']
y = [10,45,25,36,45,56,78]
plt.pie(y,labels = x,labeldistance = 1.1,autopct = '%.2f%%',pctdistance = 1.5,explode = [0,0,0,0,0,0.3,0],startangle = 90,counterclock = True)
plt.show()
plt.pie(y,labels = x,labeldistance=1.1,autopct = '%.2f%%',pctdistance = 1.5,startangle = 90,counterclock = True,wedgeprops = {'width':0.3,'linewidth':2,'edgecolor':'white'})
plt.show()
