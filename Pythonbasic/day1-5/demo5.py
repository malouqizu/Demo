#多分支选择结构
score=input("请输入成绩：")
score=int(score)
if score>90:
    print("成绩等级A")
elif 80<score<=90:
    print("成绩等级B")
elif 70<score<=80:
    print("成绩等级C")
elif 60<score<=70:
    print("成绩等级D")
elif 0<=score<=60:
    print("不及格！")
else:
    print("非法成绩！")

