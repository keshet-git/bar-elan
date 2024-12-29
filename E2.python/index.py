prev1=0
prev2=1
i=int(input("enter a number: "))
for num in range(i):
    if num==i-1:
        print(prev2,end="")
    else:
        print(prev2,end=",")
    prev1,prev2=prev2,prev1+prev2
print()