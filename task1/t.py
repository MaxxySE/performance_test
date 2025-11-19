# from threading import Thread
#
# list1 = []
#
# res1 = ""
#
# n = int(input("n = "))
# m = int(input("m = "))
#
# for i in range(1,n+1):
#     list1.append(i)
#
# k = 0
# for j in list1:
#     res1 += str(list1[k])
#     k += m-1
#     if k >= len(list1):
#         list1 += list1
#     if list1[k] == 1:
#         break
#
# print(res1)

import time
from threading import Thread

def sleepMe(i):
    print("Поток %i засыпает на 5 секунд.\n" % i)
    time.sleep(5)
    print("Поток %i сейчас проснулся.\n" % i)
for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()