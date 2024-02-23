
def dfs():
    if len(answer) == M:
        print(' '.join(map(str,answer))) #공백으로 구분
        return
    for i in range(1,N+1):
        if visited[i]:
            continue # 방문한건 빼기
        visited[i] = True
        answer.append(i)
        dfs()
        answer.pop()
        visited[i] = False


N,M = list(map(int,input().split()))
answer = []
visited = [False] * (N+1)

dfs()

#입력 ->  4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3