def create_number_dict(num):
    d={}
    for i in range(1, num+1):
        d[i]=i**2
    return d
d2 = create_number_dict(5)
print(d2)
    