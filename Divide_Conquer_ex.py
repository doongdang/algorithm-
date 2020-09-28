# O(n)
def p1(a, n):
    if n == 1:
        return a

    if n == 0:
        return 1
    if n % 2 == 0:
        return p1(a, n//2)*p1(a, n//2)
    else:
        return p1(a, n//2)*p1(a, n//2)*a

# O(log(n))


def p2(a, n):
    if n == 0:
        return 1
    x = p2(a, n//2)
    if n % 2 == 0:
        return x*x
    else:
        return x*x*a


a = 2
n = 10
print(p1(a, n))
print(p2(a, n))
