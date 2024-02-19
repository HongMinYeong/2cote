# 1이 될 떄까지
N, K = map(int,input().split())

count = 0

while True:
    target = (N//K)*K # 나눌수 있는 수
    count += (N-target) #1 빼는횟수
    N = target
    if N < K:
        break
    #k로 나누기
    count += 1
    N //= K

count += (N - 1) # 마지막으로 남은 수에 대해 1씩뺴기
print(count)