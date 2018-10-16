while 1:
    print("Please input the year:")
    year_input = int(input())
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
    print(year_input, "年", month_input, "月", day_input, "日")
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    monthCount= 1

    count_day = day_input

    while (monthCount < month_input):
#    print("monthcount and days_in_month is", monthCount,days_in_month[monthCount])
        count_day = count_day + days_in_month[monthCount]
        monthCount=monthCount+1

    print("The date", year_input, "年", month_input, "月", day_input, "日 is the ", count_day,"day of the year")
