st1=input("Enter a sentence: ")
wor_to_search=input("Enter a word to search: ")
for idx,word in enumerate(st1.split()):
    if word.startswith(wor_to_search):
        print(idx)
        break
else: print("Not a prefix")
