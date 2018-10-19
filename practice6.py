#题目：斐波那契数列 Fibonacci sequence

#input the amount of numbers you wanna make
import time

print("Please input the end point of the Fibonacci sequence:")
end_point=int(input())
if end_point>1000000:
   print("tooo large")
   exit()
a=0;b=1;i=0
start_time=time.time()

for i in range(end_point):
    tmp=a+b
    a=b
    b=tmp

"""    print(a, ' ', end='')
    if(i%20)==0:
        print()
"""

end_time=time.time()
print("\nstart:",start_time,"\tEnd:",end_time,"\nRun time(in seconds):",end_time-start_time,"\nend point")