#题目：斐波那契数列 Fibonacci sequence

#input the amount you wantto make
import time

print("Please input the end point of the Fibonacci sequence:")
end_point=int(input())
if end_point>1000000:
   print("toooo large")
   exit()
a=0;b=1;i=0
start_time=time.time()

while i<end_point:
    tmp=a+b
    a=b
    b=tmp
    i+=1

"""    print(a, ' ', end='')
    if(i%20)==0:
        print()
"""

end_time=time.time()
print("\nstart:",start_time,"\tEnd:",end_time,"\nRun time(in seconds):",end_time-start_time,"\nend point")