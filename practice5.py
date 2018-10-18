#题目：输入三个整数x,y,z，请把这三个数由小到大输出

print("Please input numbers:")
number_array=[]
for i in range(3):
    x=int(input())
    number_array.append(x)
number_array.sort()
print(number_array)