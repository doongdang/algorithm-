def cnt(a, s, m, e):
    i = s
    j = m+1
    while(i <= m and j <= e):
        check1 = False
        check2 = False
        for x in case:
            if a[i] == x[0]:
                check1 = True
                x[1] += 1
            if a[j] == x[0]:
                check2 = True
                x[1] += 1
        if check1 == False:
            case.append([a[i], 1])
        if check2 == False:
            case.append([a[j], 1])
        i += 1
        j += 1


def search(a, start, end):
    if end-start >= 1:
        mid = int(start+((end-start)/2))
        search(a, start, mid)
        search(a, mid+1, end)
        cnt(a, start, mid, end)


n = int(input())
arr = list(map(int, input().split()))
case = [[arr[0], 0]]
search(arr, 0, n-1)
print(case)
