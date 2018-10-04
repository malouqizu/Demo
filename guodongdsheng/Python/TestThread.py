import threading
from time import sleep


def test(i):
    while 1:
        print(i)
        sleep(1)

if __name__=="__main__":
    lst = []
    for i in range(0,15):
        th = threading.Thread(target=test,args=[i])
        lst.append(th)

    for i in lst:
        i.start()
        i.join()

