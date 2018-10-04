print(49//13)

file_name="E:/demo/Python/project77/engineer_management/engineer.txt"
engforfile=open(file_name, 'r')
print(engforfile.readlines())
engforfile.seek(0)
print(len(engforfile.readlines())//13)
engforfile.seek(0)
for ls in engforfile.readlines():
    print(ls.strip("\n"))
