sum_odd=0
summ_even=0
for i in range(5):
    num=int(input("Enter a number: "))
    if num%2==0:
        sum_even=+num
        print("Even")
    else:
        print("Odd")
        sum_odd=+num
print("Sum of the even number :", sum_even)
print("Sum of the odd number :", sum_odd)