n, m = map(int, input().split())
a, b, direction = map(int, input().split())

# 전체 지도 정보 입력받기
mp = [list(map(int, input().split())) for _ in range(n)]

# 방문한 위치를 저장하기 위한 또 하나의 새로운 지도
# 미방문 위치는 0으로 초기화
d = [[0]*m for _ in range(n)]

# 방문한 위치는 1로 처리
d[a][b] = 1

# a,b +- 1에 따른 좌표 변화
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

# 왼쪽으로 방향 회전하는 함수


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시작
count = 1
turn_count = 0

while True:
    turn_left()

    # 회전한 방향으로 한 칸 전진한 위치를 na, nb에 저장
    na = a + da[direction]
    nb = b + db[direction]

    # 회전한 방향으로 한 칸 전진한 위치가 가보지 않은 칸인 경우 이동
    if d[na][nb] == 0 and mp[na][nb] == 0:
        d[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_count = 0
        continue

    # 회전한 방향으로 한 칸 전진한 위치가 가본 칸이거나 바다인 경우
    else:
        turn_count += 1

    # 네 방향 모드 갈 수 없는 경우
    if turn_count == 4:
        na = a - da[direction]
        nb = b - db[direction]

        # 뒤가 땅이라면 이동
        if mp[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_count = 0
print(count)
