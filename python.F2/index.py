s1=input("Enter your string: ")
num=int(input("How many etters you want in upper? "))
upeer_part=s1[:num].upper()
lower_part=s1[num:]
print(upeer_part+lower_part)