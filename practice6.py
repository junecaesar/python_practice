#题目：斐波那契数列 Fibonacci sequence

#input the amount of numbers you wanna make
import time

print("Please input the end point of the Fibonacci sequence:")
end_point=int(input())
if end_point>1000000:
   print("tooo large")
   exit()
a=0;b=1;
start_time=time.time()

for i in range(1,end_point):
    print(' %12ld %12ld'%(a,b), end='')
    a=a+b
    b=a+b
    if(i%5)==0:
        print()

end_time=time.time()
print("\n\nstart:",time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(start_time)),"\tEnd:",
      time.localtime(end_time),"\nRun time(in seconds):",end_time-start_time,"\nend point")
'''
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) # 暂停 1 秒
'''