#题目：输入某年某月某日，判断这一天是这一年的第几天？
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # set the days of each month

while 1:
 #input the year month and day
    print("Please input the year:")
    year_input = int(input())
    if year_input > 2100 or year_input < 1:
        print("no such year")
        exit()
    print("Please input the month:")
    month_input = int(input())
    if month_input>12 or month_input<1:
        print("no such month")
        exit()
    print("Please input the day:")
    day_input = int(input())
    if day_input>31 or day_input<1:
        print("no such day")
        exit()

#initialization
    monthCount= 1
    count_day = day_input

    while (monthCount < month_input):
#    print("monthcount and days_in_month is", monthCount,days_in_month[monthCount])
        count_day = count_day + days_in_month[monthCount]
        monthCount+=1
    if (year_input%4==0) and month_input>2 and (year_input%400!=0):
        print(year_input%4)
        count_day+=1
    print("The date", year_input, "年", month_input, "月", day_input, "日 is the ", count_day,"day of the year")
