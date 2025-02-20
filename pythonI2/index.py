def my_reverse(num):
    num_as_str=str(num)
    num_as_str=num_as_str[::-1]
    return int(num_as_str)

num=int(input("enter 3 number: "))
print("Reeversed:",my_reverse(num))
