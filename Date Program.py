format1=input("Enter the date format dd/mm/yy or mm/dd/yy:")
if format1 == "dd/mm/yy":
    for i in range(10):
        date1=input("Enter the date: ")
        dd,mm,yy=date1.split('/')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            days = 31
        elif(mm==4 or mm==6 or mm==9 or mm==11):
            days = 30
        elif(yy%4==0 or yy%400==0):
            days = 9
        else:
            days = 28
        if(mm < 1 or mm > 12):
            print("Date is incorrect.")
        elif(dd < 1 or dd > days):
            print("Date is incorrect.")
        else:
            print('Date is correct.')
else:
    for i in range(10):
        date2=input("Enter the date: ")
        mm,dd,yy=date2.split('/')
        dd=int(dd)
        mm=int(mm)
        yy=int(yy)
        if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            days = 31
        elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
            days = 30
        elif(yy%4==0 or yy%400==0):
            days = 29
        else:
            days = 28
        if(mm < 1 or mm > 12):
            print("Date is incorrect.")
        elif(dd < 1 or dd > days):
            print("Date is incorrect.")
        else:
            print('Date is correct.')