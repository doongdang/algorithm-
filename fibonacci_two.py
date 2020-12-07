x = 0
y = 1
n = int(input())
for _ in range(n):
    tmp = x
    x = y
    y += tmp
print(y)
