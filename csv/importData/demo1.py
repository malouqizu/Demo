import csv

list1_zhengshu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2_zhengshu=[10,20,30,40,50,60,70,80,90,100]
res_zhengshuRight=[10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
res_zhengshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zhengshu = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [10,20,30,40,50,60,70,80,90,100],
            [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

list1_fudianshu=[0.1,  1.1,  2.1,  3.1,  4.1,  5.1,  6.1,  7.1,  8.1,  9.1]
list2_fudianshu=[10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1]
res_fudianshuRight=[10.2, 21.2, 32.2, 43.2, 54.2, 65.2, 76.2, 87.2, 98.2, 109.2]
res_fudianshu=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

fudianshu = [[0.1,  1.1,  2.1,  3.1,  4.1,  5.1,  6.1,  7.1,  8.1,  9.1],
             [10.1, 20.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1, 100.1],
             [10.2, 21.2, 32.2, 43.2, 54.2, 65.2, 76.2, 87.2, 98.2, 109.2],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

list1_zifuchaun=["张三learn:", "李四learn:", "王五learn:", "小红study:", "小明study:"]
list2_zifuchaun=["Java!",        "C++!",        "Python!",    "Perl!",      "Shell!"]
res_zifuchaunRight=["张三learn:Java!", "李四learn:C++!", "王五learn:Python!",
                  "小红study:Perl!", "小明study:Shell!"]
res_zifuchaun=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zifuchaun = [["张三learn:", "李四learn:", "王五learn:", "小红study:", "小明study:"],
             ["Java!",        "C++!",        "Python!",    "Perl!",      "Shell!"],
             ["张三learn:Java!", "李四learn:C++!", "王五learn:Python!","小红study:Perl!", "小明study:Shell!"],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

zhengshuDataFile=open('E:/Python/demo/csv/importData/zhengshuData.csv','a+',newline = "")
fudianshuDataFile=open('E:/Python/demo/csv/importData/fudianshuData.csv','a+',newline = "")
zifuchuanDataFile=open('E:/Python/demo/csv/importData/zifuchuanData.csv','a+',newline = "")

csv_writer = csv.writer(zhengshuDataFile, dialect = "excel")
'''
csv_writer.writerow(list1_zhengshu)
csv_writer.writerow(list2_zhengshu)
csv_writer.writerow(res_zhengshuRight)
csv_writer.writerow(res_zhengshu)
'''
for row in zhengshu:
    csv_writer.writerow(row)


'''
csv_writer.writerow(list1_fudianshu)
csv_writer.writerow(list2_fudianshu)
csv_writer.writerow(res_fudianshuRight)
csv_writer.writerow(res_fudianshu)
'''
csv_writer = csv.writer(fudianshuDataFile, dialect = "excel")
for row in fudianshu:
    csv_writer.writerow(row)

'''
csv_writer.writerow(list1_zifuchaun)
csv_writer.writerow(list2_zifuchaun)
csv_writer.writerow(res_zifuchaunRight)
csv_writer.writerow(res_zifuchaun)
'''
csv_writer = csv.writer(zifuchuanDataFile, dialect = "excel")
for row in zifuchaun:
    csv_writer.writerow(row)

