def cc(n):
    if n>=1:
        s = n*cc(n-1)
    else:
        s = 1
    return s
v =cc(3)
print(v)
  
