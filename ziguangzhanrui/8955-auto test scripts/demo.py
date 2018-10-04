import os
import time
import datetime

print(type(os.environ))
print(time.time())
stamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
print(stamp)

print(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])