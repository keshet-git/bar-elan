def revers_dict(d):
    d1 ={}
    for k,v in d.items():
        d1[v]=k
    return d1

tmp_d={"a": 1,"b": 2,"c":3}
ret_d=reverse_dict(tmp_d)
print(tmp_d)
print(ret_d) 
