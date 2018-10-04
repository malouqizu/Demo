#编写一个程序，转换一个矩阵
a=[[4,8],
   [3,19],
   [15,6]]

trans=[[0,0,0],
       [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        trans[j][i]=a[i][j]

for i in trans:
    print(i)