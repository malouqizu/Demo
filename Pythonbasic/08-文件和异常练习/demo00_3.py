import os
import time

print(os.getcwd())
os.mkdir("newdir")
print(os.getcwd())
os.chdir("newdir")
print(os.getcwd())
os.chdir("../")
time.sleep(10)
os.rmdir("newdir")
