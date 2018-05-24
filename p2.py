def v(n):
    if n>=1:
        s = n*v(n-1)
    else:
        s = 1
    return s
cc = v(4)
print(cc)
