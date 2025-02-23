str1 = input("enter a name: ")
for index, char in enumerate(str1):
    print("Current character", char, "position at", index )


s1=input("enter a name: ")
x=int(input("enter a number"))
print(s1[:x].upper()+s1[x:])
