def my_reverse(num):
    num_as_str=str(num)
    num_as_str=num_a_str[::-1]
    return int(num_as_str)

num=int(input("enter 3 numbers"))
num2=my_reverse(num)
print("reeversed:",num2)
print(type(num2))

'''
num=int(input("enter 3 numbers"))
x = [num]
def num_torn():
    l=x[::-1]

print(l)
'''