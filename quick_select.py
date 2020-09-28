def quick_select(l, k):
    p = l[0]
    a, b, m = [], [], []
    for i in l:
        if i < p:
            a.append(i)
        elif i > p:
            b.append(i)
        else:
            m.append(i)
    if len(a) > k:
        return quick_select(a, k)
    elif len(a)+len(m) < k:
        return quick_select(b, k-(len(a)+len(m)))
    else:
        return p


arr = [4, 3, 2, 1, 932, 2, 31, 43]
print(quick_select(arr, 2))
