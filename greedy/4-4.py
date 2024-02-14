N, M = map(int,input().split())

d = [[0] * M for _ in range(N)] # M * N 배열 만들기
x,y,direction = map(int,input().split()) #현재위치, 방향
d[x][y] = 1 # 현재 좌표 방문 처리 #방문하거나 바다는 1

array = []
for i in range(N): #N 번 맵정보 입력받기
    array.append(list(map(int,input().split())))

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)