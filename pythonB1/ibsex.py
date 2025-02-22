name1=(input("Enter a name: "))
age1=int(input("Enter the age: "))
height1=float(input("Enter your height: "))

name2=(input("Enter a name: "))
age2=int(input("Enter the age: "))
height2=float(input("Enter your height: "))

age_difference = age1-age2
height_difference = round((height1-height2)*100)
age1=age1-2024
age2=age2-2024
print("the name of the first person is:",name1,"the age of the first person is:",age1)
print("the name of the second person is:",name2,"the age of the first person is:",age2)
print("the age differenc is:" ,age_difference)
print("the height differenc is:",height_difference)
