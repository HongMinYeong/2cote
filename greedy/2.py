N,M = map(int,input().split())

result = 0
for i in range(N):
    data = list(map(int,input().split()))
    min_value = min(data) # 제일 작은 수 찾기
    # print('min_value는 ->',min_value)
    result = max(result,min_value) # 둘중에 더 큰 숫자 저장

print(result)