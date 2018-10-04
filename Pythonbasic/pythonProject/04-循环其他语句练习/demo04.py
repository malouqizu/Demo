# continue和for
# 计算1~10之间的偶数和

# 存放累加和
sum1 = 0

for i in range(1, 11, 1):  # 使用range产生1~10序列
    # 如果i除以2，余数为0，证明是一个偶数，则进行累加
    if i % 2 == 0:
        sum1 += i
    else:  # 否则，将是一个奇数，不进行累加，也不输出显示
        continue

    print(i, sum1)
