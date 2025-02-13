s1 = input("Enter a string: ")
c1 = input("Enter one caracer: ")
exit_flag =True
for one_char in s1:
    if one_char==c1:
        print("Exist")
        exit_flag=False
        break
if exit_flag:
    print("Not exist")