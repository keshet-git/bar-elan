age=int(input("Enter your age (integer): "))
if age<=3 or age>=60:
    print("pay",int(0.8*40))
elif 18<=age<=21:
    print("pay:",20)
else:
    print("pay: 40")