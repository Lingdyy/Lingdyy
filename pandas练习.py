print(len('good'))
print('good'.replace('g','G'))
print('山-水-风-雨'.split('-'))
print('好山好水好风光'.split('好'))
print('-'.join(['山','水','风','雨']))
print('和'.join(['诗','远方']))
print('good'.upper())
print('GOOD'.lower())
print('Good Bye'.swapcase()) #大小写互换
print('good'.capitalize())#首字母转换大写
print('good'.islower()) #是否全是小写
print('good'.isupper()) #是否全是大写
print('3月'.zfill(3)) #指定长度，如果长度不够，前面补零
a = [1,2,3]
print(len(a))
print(max(a))
print(a.index(1))
print(a.count(2))
for i in a : print(i)#迭代元素
print(sorted(a)) #返回一个排序的列表，但不改变原列表
print(any(a)) #是否至少有一个元素为真
print(all(a))#是否所有元素为真
a.append(4)#增加一个元素
print(a)
a.pop()#删除最后一个元素
a.extend([9,8]) #与其他列表合并
a.insert(1,'a') #在指定索引位插入元素，索引从零开始
a.remove('a') #删除第一个指定元素
a.clear() # []清空
print([i for i in range(5)])
print(['第' + str(i) for i in range(5)])
print([i for i in range(5) if i%2 == 0])
print([i.upper() for i in 'Hello world' if i != ' '])
x = (1,2,3,4,5)
a,*b = x #a占第一个，剩余的组成列表给b
print(a)
print(b)
print(a,b)
a,*b,c = x
print(a,b,c)
d = {} #定义空字典
d = dict() #定义空字典
d = {'a':1,'b':2,'c':3}
d = {'a':1,'a':1,'a':1} #{'a':1} key 不能重复，重复时取最后一个
d = {'a':1,'b':{'x':3}} #嵌套字典
d = {'a':[1,2,3],'b':[4,5,6]}
#以下均可定义如下结果
#{'name':'Tom','age':18,'height':180}
d = dict(name = 'Tom',age = 18,height = 180)
d = dict([('name','Tom'),('age',18),('height',180)])
d = dict(zip(['name','age','height'],['Tom',18,180]))
print(d['name']) #获取键的值
d['age'] = 20 #将age的值更新为20
d['Female'] = 'man' #增加属性
print(d.get('height',180)) #180
#嵌套取值
d = {'a':{'name':'Tom','age':18},'b':[4,5,6]}
print(d['b'][1])
print(d['a']['age'])
# d.pop('name') #删除指定key
# d.popitem() #随机删除某一项
# del d['name'] #删除键值对
# d.clear() #清空字典
#按类型访问，可迭代
print(d.keys()) #列出所有键
print(d.values()) #列出所有值
print(d.items()) #列出所有键值对元组(k,v)

#操作
d.setdefault('a',3) #插入一个键并给定默认值3，如不指定，则为None
d2 = {'d':[5,6,7]}
d.update(d2) #将字典dict2的键值对添加到字典dict
print(d)
# 如果键存在，则返回其对应值;如果键不在字典中，则返回默认值
d.get('math',100)
d2 = d.copy() #深拷贝，d变化不影响d2
print(d2)
d = {'a':1,'b':2,'c':3}
print(max(d)) # 'C'(最大的键)
print(min(d)) #最小的键
print(str(d)) #打印字符串形式
print(any(d)) #只要一个键为True
print(all(d)) #所有键都为True
print(sorted(d)) # ['a','b','c'] (所有键的列表排序)
s = {} #空集合
s = {'5元','10元','20元'} #定义集合
s = set() #空集合
s = set([1,2,3,4,5]) #使用列表定义
s = {1,True,'a'}
s = {1,1,1} #去重
type(s) #set (类型检测)
s = {'a','b','c'}
#判断是否有某个元素
print('a' in s) #True?
#添加元素
s.add(2)
s.update([1,3,4])
#删除和清空元素
s.remove('a') #{'b','c'} (删除不存在的会报错)
s.discard('3') #删除一个元素，无则忽略，不报错
s.clear() #清空
s1 = {1,2,3}
s2 = {2,3,4}
print(s1&s2) #交集
print(s1.intersection(s2)) #交集
print(s1.intersection_update(s2)) #交集，会覆盖s1
print(s1|s2)#并集
print(s1.union(s2)) #{1,2,3,4}(并集)
print(s1.difference(s2)) #{1}(差集)
print(s1.difference_update(s2)) #{1} (差集，会覆盖s1)
print(s1.symmetric_difference(s2)) #{1,4} (交集之外)
print(s1.isdisjoint(s2)) #False是否没有交集
print(s1.issubset(s2)) #s1是否是s2的子集
print(s1.issuperset(s2)) #s1是否是s2的超集，即s1是否包含在s2中的所有元素
