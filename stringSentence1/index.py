str1 = input("enter a sentence: ")
for word in str1.split():
     if len(word)==1:
          print(word.upper(), end=" ")
     else:
          print(word[0].upper() + word[1:-1] + word[-1].upper(), end=" ")
