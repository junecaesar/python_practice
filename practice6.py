#题目：斐波那契数列 Fibonacci sequence

#input the amount of numbers you wanna make
#import time
import datetime

print("Please input the end point of the Fibonacci sequence:")
end_point=int(input())
if end_point>1000000:
   print("tooo large")
   exit()
a=0;b=1;
#start_time=time.time()
start_time=datetime.datetime.now()


for i in range(1,end_point):
#    print(' %12ld %12ld'%(a,b), end='')
#    if(i%5)==0:
 #       print()
    a=a+b
    b=a+b

#end_time=time.time()
end_time=datetime.datetime.now()

print("The start time is:%s End time is:%s Running time is:%s"%(start_time,end_time,end_time-start_time))
'''
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) # 暂停 1 秒
'''