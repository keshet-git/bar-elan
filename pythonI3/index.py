def my_reverse(num):
    num_as_str=str(num)
    num_as_str= num_as_str[::-1]
    return int(num_as_str)

def num_is_polygrom(num1):
    if num1==my_reverse(num1):
        print("Pallindrome")
    else:
        print("Pallindrome")
num=int(input("enter 3 numbers"))
print(num_is_polygrom(num))

