'''
输入一个0-100整数分数，根据分数，转换成对应的等级
使用if-elif-else完成
'''

score=input("请输入考试成绩(0-100):")
score=int(score)

if 90<=score<=100:
    print("成绩等级为A，优秀！")
elif 80<=score<90:
    print("成绩等级为B，良好！")
elif 70<=score<80:
    print("成绩等级为C，中等！")
elif 60<=score<70:
    print("成绩等级为D，及格！")
elif 0<=score<60:
    print("成绩等级为E，不及格！")
else:
    print("成绩非法！")
