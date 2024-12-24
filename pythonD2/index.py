while True:
    name1=input("Enter your name1: ")
    if name1=="End":
        break
    age1 =int(input("Enter your age1: "))
    height1==int(input("Enter your heght1: "))

    name2=input("Enter your name1: ")
    age2 =int(input("Enter your age1: "))
    height2==int(input("Enter your heght1: "))
    if abs(age1-age2)<=5 and abs(height1-height2)<=5:
        print("There is a match")
    else:
        print("There is no match")