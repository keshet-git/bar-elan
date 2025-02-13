def merge_func(l1,l2):
    l3=[]
    l1_idx=0
    l2_idx=0
        
    while(l1_idx<len(l1) and l2_idx<len(l2)):
        if l1[l1_idx]<=l2[l2_idx]:
            l3.append(l1[l1_idx])
            l1_idx+=1
        else:
            l3.append(l2[l2_idx])
            l2_idx+=1
    if l1_idx>=len(l1):
        l3.extend(l2[l2_idx:])
    else:
        l3.extend(l1[l1_idx:])
    return(l3)

s1 = input("Please enter numbers (in ascending order): ")
s2 = input("Please enter numbers (in ascending order): ")
l1=[int(x) for x in s1.split()]
l2=[int(x) for x in s2.split()]

print(merge_func(l1,l2))
'''
    while(l1_idx<len(l1) and l2_idx<len(l2)):
        if l1[l1_idx]<=l2[l2_idx]:
            l3.append(l1[l1_idx])
            l1_idx+=1
        else:
            l3.append(l2[l2_idx])
            l2_idx+=1
    if l1_idx>=len(l1):
        l3.extend(l2[l2_idx:])
    else:
        l3.extend(l1[l1_idx:])
    return(l3)

s1 = input("Please enter numbers (in ascending order): ")
s2 = input("Please enter numbers (in ascending order): ")
l1=[int(x) for x in s1.split()]
l2=[int(x) for x in s2.split()]

print(merge_func(l1,l2))
    
    for k,v in d.items():
        print('the kee is', k,'the value is',v)
        
dict1={}
dict1['moshe']=100
dict1['Divid']=60
dict1['dana']=99
f1(dict1) 
'''