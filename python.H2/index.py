sentens = input("enter a sentence")
list1 = sentens.split()
occ_dic = dict()
for idx,one_word in enumerate(list1):
    if one_word in occ_dic:
        occ_dic[one_word].append(idx)
    else:
        occ_dic[one_word]=[idx]

for k,v in occ_dic.items():
    print(k,"is:",v) 