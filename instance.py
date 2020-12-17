# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self):
        self.x=3
        self.y=4
# 建立第一個實體物件
p1=Point() #產生點的實體物件放進p1裡
print(p1.x,p1.y)
# 建立第二個實體物件
p2=Point()
print(p2.x,p2.y)
print("---------------------------------------")
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
# 建立第一個實體物件
p1=Point(3,4) #產生點的實體物件放進p1裡
print(p1.x,p1.y)
# 建立第二個實體物件
p2=Point(5,6)
print(p2.x,p2.y)
print("---------------------------------------")
# FullName 實體物件的設計: 分開紀錄姓、名資料全名
class FullName:
    def __init__(self):
        self.first="C.W."
        self.last="Peng"
name1=FullName()
print(name1.first,name1.last)
print("---------------------------------------")
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=FullName("C.W.","Peng")
print(name1.first,name1.last)
name2=FullName("T.Y.","Lin")
print(name2.first,name2.last)
print("---------------------------------------")
# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    #定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self,targetX,targetY):
        return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
p=Point(3,4)
p.show()    #呼叫實體方法/函式
result=p.distance(0,0)  #計算座標 3,4 和 座標 0,0 之間的距離
print(result)
print("---------------------------------------")
# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self, name):
        self.name=name
        self.file=None  # 尚未開啟檔案: 初期是None
    # 實體方法
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)