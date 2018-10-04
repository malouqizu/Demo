#编写程序，对两个矩阵相加
a=[[4,8,18],
    [3,19,12],
    [15,6,9]]

b=[[18,32,23],
   [12,1,15],
   [5,12,3]]

sum_of_mat=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        sum_of_mat[i][j]=a[i][j]+b[i][j]

for item in sum_of_mat:
    print(item)
