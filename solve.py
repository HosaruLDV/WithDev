def solve (a,b):
    sum = 0
    c = b
    while c != 0:
        kk = str(a) * c
        sum += int(kk)
        c -= 1
    return sum
