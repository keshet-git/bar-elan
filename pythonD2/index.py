while True:
    name1=input("Enter your name1: ")
    if name1=="end":
        print("bay")
        break
    age1 =int(input("Enter your age1: "))
    height1=float(input("Enter your height: "))

    name2=input("Enter your name2: ")
    age2 =int(input("Enter your age2: "))
    height2=float(input("Enter your height: "))
    if abs(age1-age2)<=5 and abs(height1-height2)<=5:
        print("There is a match")
    else:
        print("There is no match")
