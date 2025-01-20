def contains_two(num):
    for num in l1:
        if res-num in l1:
            return True
    return False

l1 =int(input("enter numbers"))
res=int(input("enter a number"))
pprint(contains_two(l1,res))