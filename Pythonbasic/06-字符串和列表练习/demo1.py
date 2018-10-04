#1、编写一个程序，找出所给字符串中重复的字符。
str="hello python!"
first_time=[]
duplicate=[]
for i in str:
    if i not in first_time:
        first_time.append(i)
    else:
        duplicate.append(i)

print(duplicate)