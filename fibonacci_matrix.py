# Divide_Conquer의 p2함수, 즉 log(n)의 수행시간의 연산을 통해 log(n)시간을 갖는 피보나치 알고리즘 짜기
def recursive_matrix_squared(arr, number):
    if number == 0:
        return [[1, 0], [0, 1]]
    x = recursive_matrix_squared(arr, number//2)
    x2 = [[x[0][0]*x[0][0]+x[0][1]*x[1][0], x[0][0]*x[0][1]+x[0][1]*x[1][1]],
          [x[1][0]*x[0][0]+x[1][1]*x[1][0], x[1][0]*x[0][1]+x[1][1]*x[1][1]]]
    print(x2)
    if number % 2 == 0:
        return x2
    else:
        return [[x2[0][0]*arr[0][0]+x2[0][1]*arr[1][0], x2[0][0]*arr[0][1]+x2[0][1]*arr[1][1]],
                [x2[1][0]*arr[0][0]+x2[1][1]*arr[1][0], x2[1][0]*arr[0][1]+x2[1][1]*arr[1][1]]]


start = [1, 0]
base = [[1, 1], [1, 0]]
n = int(input())
ans = recursive_matrix_squared(base, n-1)
ans = [ans[0][0]*start[0]+ans[0][1]*start[1],
       ans[1][0]*start[0]+ans[1][1]*start[1]]
print(ans)
