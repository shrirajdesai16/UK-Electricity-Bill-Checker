from datetime import datetime, date


year = int(input("Enter the year"))
month = int(input("month"))
day = int(input(" day"))
starting_date = date(year, month, day)
year1 = int(input("year"))
month1 = int(input("month"))
day1 = int(input("day"))
ending_date = date(year1, month1, day1)
print("Total Number of days of Billings",(ending_date - starting_date).days)
days =int((ending_date - starting_date).days)
print("Have you changed your provider recently ?")
answer = input("yes or no:")
units = float(input(" Please enter Number of Units you Consumed this month : "))
if answer == "yes":
    units_charge = float(input(" Please enter the per unit charge given by your provider : "))
    standingcharge = float(input("Please enter the standing charge: "))
    standing_charge1 = standingcharge * days
    New_Provider = units_charge * units
    Total = (New_Provider + standing_charge1)
    Energy = float(units * units_charge / 100)
    Total_final = Total / 100
    print("Period Amount is  £{:.2f}".format(Energy))
    #print("Total Amount", Total_final)
elif answer == "no":
    units_charge1 = 18.05
    standing_charge2 = 22.21 * days
    pay_amount = units_charge1 * units
    Total = (pay_amount + standing_charge2)
    Total_final = Total / 100
    Energy1 = units * 18.05 / 100
    print("Period Amount is  £{:.2f}".format(Energy1))
else:
     print("print error")
print('------------------')
print('******')
print("\nElectricity bill pay is  £{:.2f}".format(Total_final))
print('******')
print('------------------')