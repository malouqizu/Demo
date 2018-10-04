import serial

t = serial.Serial('com12',115200)
n = t.write('you are my world')

print(t.portstr)
print(n)
str = t.read(n)
print(str)