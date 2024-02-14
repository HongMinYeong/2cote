# 나이트 -> L 자 형태로만 이동 가능 , 정원 밖으로 나갈 수 없음
# 나이트가 이동할 수 있는 경우의 수
input = input()
x = int(ord(input[0])) - int(ord('a')) + 1 # 유니코드 환산
y = int(input[1])
count = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 나이트가 이동할 수 있는 8 가지 방향
steps = [(-2,1),(-2,-1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(-1,2)]
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count)