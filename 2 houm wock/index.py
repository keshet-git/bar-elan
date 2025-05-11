while True:
    option=input("Please enter an option")
    if option =="4":
        print("Bay")
        break
    elif option=="1":
        num=int(input("enter a number: "))
        exit_flag=True
        for candidate in range(2,num):
            if num%candidate ==0:
                print("Not prraime")
                exit_flag=False
                break
            if exit_flag==True:
                print("Prime")    
    elif option =="2":
        num = int (input("Please enter a number for 7 boom game: "))
        for i in range(1, num +1):
            if i % 7 == 0 or '7' in str(i):
                print(i,end=' ')
    elif option =="3":
        num = int(input("enter a number for a FizzBazz Game. \n"))
        for n in range(1,101):
            if (n % 3 ==0 and n % 5 ==0):
                print("FizzBazz")
            elif (n % 3 ==0 ):
                print("Fizz")
            elif (n %5 == 0):
                print("Bazz")
            else:
                print(n)
    else:
        option!="1234"
        print("wrong input")
