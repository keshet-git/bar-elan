number_of_rows=int(input("Enter athe number of rows: "))
for i in range(1,number_of_rows+1):
    for num_of_stars in range(i):
        print("*",end="")
    print()