
def my_min(num1,num2,num3):
    if num2<num1:
        num1=num2
    if num3<num1:
        num1=num3
    return num1
def my_max (num1,num2,num3):
    if num2>num1:
        num1=num2
    if num3>num1:
        num1=num3
    return num1

def print_max_min(num1,num2,num3):
    print("the maximel number is",my_max(num1,num2,num3))
    print("the minimel number is",my_min(num1,num2,num3))

nums= input("Enter three numbers: ")
l1=nums.split()
x1,x2,x3=[int(x) for x in l1]
print_max_min(x1,x2,x3)

'''
x1,x2,x3 =nums.split()
minmal_num=my_min(x1,x2,x3)

====================================
    for x in range(y):
        temp=temp*x
    return temp

w=f1(5,3)
print(w)
print(help(f1))
'''
# param_float*1.8 +32.0
