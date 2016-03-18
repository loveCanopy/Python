__author__ = 'Sherlock'
from multiprocessing import Process
from multiprocessing import Lock
import time,os
def sayhi(i):
    print("hello",i)
    time.sleep(10)
if __name__ == '__main__':
    for i in range(100):
        p=Process(target=sayhi,args=(i,))
        p.start()