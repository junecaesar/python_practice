import time
print("Hello Python")
text="why are we here"
print(text)

total=0
print("please input:",end='')
end_num=int(input())

start_time=time.time()
for i in range(end_num):
    total=total+i

end_time=time.time()
print("\nstart:",time.strftime('%Y-%M-%D %H:%M:%S',time.localtime(start_time)),"\tEnd:",
      time.localtime(end_time),"\nRun time(in seconds):",end_time-start_time,"\nanswer is:",total)
