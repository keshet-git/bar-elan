str1 = input("enter a name: ")
str_printed=""
for ch in str1:
  if ch in str_printed:
    continue
  str_printed+=ch
  print("the character:",ch, "appears:",str1.count(ch),"times")

