year=int(input("Enter Year"))
x=year%400
if x==0:
    print("It is a leap year")
elif year%100==0:
    print("It is not a leap year")
elif year%4==0:
    print("It is  a leap year")
else:
    print("It is not leap year")
