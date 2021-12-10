day = int(input("Enter The Starting Date of Billing:"))
month = int(input("Enter The Month:"))
year = int(input("Enter The Year"))
if month == 1 or month == 3 or month ==5 or month ==7 or month ==8 or month == 10 or month ==12:
    max_days = 31
elif month == 4 or month == 6 or month ==9 or month ==11:
    max_days = 30
elif year%4==0 and year%100 ==0 or year%400 ==0:
    max_days = 29
else:
    max_days = 28

if month <1 or month>12:
    print("Entered date is invalid")
    print("Please enter the date again")

elif day<1 or day>max_days:
    print("Entered date is invalid")
    print("Please enter the date again")

day1 = int(input("Enter The Ending Date of Billing:"))
month1 = int(input("Enter The Month:"))
year1 = int(input("Enter The Year"))
if month1 == 1 or month1 == 3 or month1 ==5 or month1 ==7 or month1 ==8 or month1 == 10 or month1 ==12:
    max_days = 31
elif month1 == 4 or month1 == 6 or month1 ==9 or month1 ==11:
    max_days = 30
elif year1%4==0 and year1%100 ==0 or year1%400 ==0:
    max_days = 29
else:
    max_days = 28

if month1 <1 or month1>12:
    print("Entered date is invalid")
    print("Please enter the date again")

elif day1<1 or day1>max_days:
    print("Entered date is invalid")
    print("Please enter the date again")

elif month > month1:
    print("Error!.Please check the start and end month. You have entered past date")

elif year>year1:
    print("Error!.Please enter the correct Year")




