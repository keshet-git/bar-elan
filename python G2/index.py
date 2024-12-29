l1=[]
for i in range(10):
    l1.uppend(int(input("Please enter a number: ")))
avg=sum(l1)/len(l1)
l2=[str(one_val) for onn_val in l1 if one_val>avg]
print("/n".join(l2))

for one_val in l1:
    if one_val>avg:
        print(one_val)   