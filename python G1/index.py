#l1= [7,2,14,5]
#l1.sort(revers=True)
#print(l1)

s1="this is a test"
l1 = s1.split()
count=0
for index,one_word in enumerate(l1):
    l1[index]=one_word[::-1]
    
s1="#".join(l1)
print(s1)