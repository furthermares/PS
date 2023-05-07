def pow(b, e, m):
    r = 1
    if e & 1:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r
