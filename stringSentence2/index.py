#without splitting
str1 = input("enter a sentence: ")
s=str1[0].upper()
for idx in range(1,len(str1)-1):
     if str1[idx]==" ":
          s=s[:-1]+s[-1].upper()+" "
     elif str1[idx-1]==" " and str1[idx]!=" ":
          s=s+str1[idx].upper()
     else:
          s=s+str1[idx]
if len(s)>1:
     s=s+str1[-1].upper()
print(s)

