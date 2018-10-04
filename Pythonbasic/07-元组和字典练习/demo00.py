#课中举例练习
months=('January','February','March','April','May','June','July','August','September','Octaober','November','December')
print(months)

tup=(4,2,9,1)
print(tup)

tup_mix=(2,30,'Python',5.8,'Program')
print(tup_mix)

nested_tuple=("python",[1,4,2],["john",3.9])
print(nested_tuple)

tup1=4.9,6,'home'
print(tup1)

tup2=("home")
print(tup2)
print(type(tup2))

tup3=("home",)
print(tup3)
print(type(tup3))

tup4="home",
print(tup4)
print(type(tup4))

tup5=("Physics","chemistry","mathematics")
tup6=(10,20,30,40,50)
print(tup5[1])
print(tup6[4])
print(tup6[0])
print(tup6[-1])
print(tup6[::-1])
print(tup6[1:4])
print(tup6[:1])
print(tup6[:2])

tup7=(12,15,"python",2.3)
print(tup7)

anil=("221","anil","rahul","delhi",1971,"jaipur gwalior")
print(anil)
(id,fst_name,lst_name,city,year_of_birth,birth_palce)=anil
print(id,fst_name," ",lst_name," ",city," ",year_of_birth," ",birth_palce)

x=3
y=4
y,x=x,y
print(x," ",y)

def div_mod(a,b):
    quotient=a//b
    remainder=a%b
    return quotient,remainder

x=10
y=3
t=div_mod(x,y)
print(t)
print(type(t))

def traverse(*t):
    print(t)
    print(type(t))
    for item in t:
        print(item)

traverse(1,2,3,4,5)
m=(1,2,3,4,5)
n=('a','b','c')
traverse(m,n)

addr='hello@python.org'
usrname,domain=addr.split('@')
print(usrname)
print(domain)

t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
print(t1)
print(t2)
print(t3)

t3=('ok',)
t4=t3*5
print(t4)

t5=(10,20,30,40,50)
if 10 in t5:
    print("10 in t5")
else:
    print("10 not in t5")

if 3 in t5:
    print("3 in t5")
else:
    print("3 not in t5")

for item in t5:
    print(item)

tup5=("Physics","chemistry","mathematics")
tup6=(10,20,30,40,50)
for item in zip(tup5,tup6):
    print(item)

print(min(tup5))
print(min(tup6))
print(max(tup5))
print(max(tup6))

list6=[10,20,30,40,50]
print(tuple(list6))
print(len(tup5))

print(tup5+tup6)

dict1={}
print(dict1)

dict2={1:'red',2:'yellow',3:'green'}
print(dict2)

dict3={'name':'jinnie',3:['hello',2,3],'age':27}
print(dict3)

d1=dict({1:'red',2:'yellow',3:'green'})
d2=dict([(1,'red'),(2,'yellow'),(3,'green')])
d3=dict(one=1,two=2,three=3)
print(d1)
print(d2)
print(d3)

d4={'name':'john','age':27}
d4['age']=30
print(d4)
d4['address']='beijing'
print(d4)
print(d4['address'])
print(d4.get('address',0))

dict_cubes={1:1,2:8,3:9,4:64,5:125,6:216}
print(dict_cubes.pop(3))
print(dict_cubes)
print(dict_cubes.popitem())
print(dict_cubes.popitem())
print(dict_cubes)
del dict_cubes[2]
print(dict_cubes)
dict_cubes.clear()
print(dict_cubes)
del dict_cubes


dict_cubes={0:1,2:8,3:9,4:64,5:125,6:216,1:1}
print(all(dict_cubes))
print(any(dict_cubes))
print(len(dict_cubes))
print(sorted(dict_cubes))
print(str(dict_cubes))

d5=dict_cubes.copy()
print(d5)
if d5 is dict_cubes:
    print("d5 is dict_cubes")
else:
    print("d5 is not dict_cubes")

seq=[1,2,3]
d6=dict.fromkeys(seq,'hello')
print(d6)

seq2=(1,2,3)
d7=dict.fromkeys(seq2,'hello')
print(d7)

dict_cubes={0:1,2:8,3:9,4:64,5:125,6:216,1:1}
print(dict_cubes.items())
for m,n in dict_cubes.items():
    print(m,n)

print(dict_cubes.keys())
print(dict_cubes.values())
dict_cubes.setdefault(10,1000)
print(dict_cubes)

dict_cubes={0:1,2:8,3:9,4:64,5:125,6:216,1:1}
d8={'name':'john','age':27}
dict_cubes.update(d8)
print(dict_cubes)

