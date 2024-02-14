# 상하 좌우
N = int(input())
x,y = 1,1 # 처음 좌표
plans = input().split() #방향 계획

# L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        # 공간 벗어나는 경우 무시
    if nx <1 or ny <1 or nx > N or ny > N:
        continue
    x,y = nx,ny

print(x,y)
