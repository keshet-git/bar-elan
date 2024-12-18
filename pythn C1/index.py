age=int(input("Enter your age (integer): "))
if age<=3:
    print("Get a babysitter")
elif age>=4 and age<=9:
    print("you can watch G level movies")
elif 12<=age<15:
    print("G or PG movies are ok")
elif age==16 or age==17:
    print("R might be ok")
else:
    print("R is OK")    