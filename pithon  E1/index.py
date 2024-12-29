my_sum=0
for i in range(10):
    number=int(input("Enter a number: "))
    if number==-1:
        break
    if i==0:
        my_minimal=number
        my_maximal=number
    else:
        my_minimal=min(my_minimal,number)
        my_maximal=max(my_maximal,number)
    my_sum+=number
    
    
if i ==0:
    print("the sum is:0 the average is:0")   
if number==-1:
    print("the sum is",my_sum,"the average is",my_sum(i+1))
else:
    print("the minimal is",my_minimal,"the maximal is",my_maximal)
    