sentens=input("enter a  string: ")
list1 = sentens.split()
occ_dic = dict()
for one_word in list1:
    occ_dic[one_word]=occ_dic.get(one_word,0)+1
l2=[]
for k,v in occ_dic.items():
    l2.append((v,k))
l2.sort(reverse=True)
for v,k in l2:
    print("the word",k,"was",v,"times") 