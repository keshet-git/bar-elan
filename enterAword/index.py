st1=input("Enter a word: ")
st2=input("Enter a word: ")
st3=input("Enter a word: ")
st4=input("Enter a word: ")
if st1 in st2 or st1 in st3 or st1 in st4:
    print(st1)
if st2 in st1 or st2 in st3 or st2 in st4:
    print(st2)
if st3 in st1 or st3 in st2 or st3 in st4:
    print(st3)
if st4 in st1 or st4 in st2 or st4 in st3:
    print(st4)
