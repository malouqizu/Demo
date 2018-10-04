import csv

f1=open('E:/Python/demo/csv/importData/zhengshuData.csv','r')
f2=open('E:/Python/demo/csv/importData/fudianshuData.csv','r')
f3=open('E:/Python/demo/csv/importData/zifuchuanData.csv','r')

data1=csv.reader(f1)
#print(data1)
zhengshu=[]
for mydata in data1:
    print(mydata)
    zhengshu.append(mydata)
print(zhengshu)

data2=csv.reader(f2)
#print(data2)
fudianshu=[]
for mydata in data2:
    print(mydata)
    fudianshu.append(mydata)
print(fudianshu)

data3=csv.reader(f3)
#print(data3)
zifuchuan=[]
for mydata in data3:
    print(mydata)
    zifuchuan.append(mydata)
print(zifuchuan)
