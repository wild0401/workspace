# 隨機模組
import random

# 隨機選取
data = random.choice ([1,5,6,10,20])
print(data)
data2 = random.sample([1,5,6,10,20],3)
print(data2)

# 隨機調換順序 (就是洗牌的概念)
data3=[1,5,8,20]
random.shuffle(data3)
print(data3)

# 隨機取得亂數
data4=random.random()   #0 ~ 1之間的隨機亂數
print(data4)
data5=random.uniform(0.0,1.0)
print(data5)

# 取得常態分配亂數
#平均數 100 標準差 10,得到的資料多數在90~110之間
data6=random.normalvariate(100,10)
print(data6)
#平均數0,標準差5,得到資料多數在 -5~5之間
data7=random.normalvariate(0,5)
print(data7)

# 統計模組
import statistics as stat
data8=stat.mean([1,2,3,4,5,8,100])    #平均數
print(data8)
data9=stat.median([1,2,3,4,5,8,100])    #中位數(會排除極端的值)
print(data9)
data10=stat.stdev([1,2,3,4,5,8,10])    #常態分配
print(data10)
#平均數,中位數，標準差，常態分配