import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
x = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
y = [50, 45, 65, 76, 75, 85, 55, 78, 86, 89, 94, 90]
plt.plot(x, y, color = 'r', linestyle = 'solid', linewidth = 2)
plt.title(label = '销售额趋势图',fontdict = {'family' : 'KaiTi', 'color' : 'k', 'size' : 30}, loc = 'center')
plt.xlabel('月份', fontdict = {'family' : 'SimSun', 'color' : 'k', 'size' : 20}, labelpad = 20)
plt.ylabel('销售额(万元)', fontdict = {'family' : 'SimSun', 'color' : 'k', 'size' : 20}, labelpad = 20)
plt.grid(b = True, color = 'r', linestyle = 'dotted', linewidth = 1)
plt.show()
plt.grid(b = True, axis = 'y', color = 'r', linestyle = 'dotted', linewidth = 1)
plt.show()
plt.subplot(2,2,1)#subplot()第一个参数表示整张画布分成几行，第二个参数表示整张画布分成几列，第三个参数表示在从左到右第个位置放置图表
plt.pie(y,labels = x,labeldistance = 1.1,startangle=90,counterclock=False)
plt.subplot(2,2,2)
plt.bar(x,y,width=0.5,color='r')
