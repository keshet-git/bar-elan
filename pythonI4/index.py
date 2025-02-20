def contains_two(l1,res):
    for num in l1:
        if res-num in l1:
            return True
    return False

l1 =[27,45,7657,5,7,98]
res=54
print(contains_two(l1,res))
