l1=[]
while True:
    s1=input("Enter a strung")
    if s1 =="end":
        break
    l1.append
print(l1[::-1])

insert_flag=False
for idx,one_word in enumerate(l1):
    if "Hello"<=one_word:
        l1.insert(idx,"hello")
        insert_flag=True
        break
    
    
if insert_flag==False:
    l1.append("hello")
