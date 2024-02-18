N, K = map(int, input().split())
array = list(map(int, input().split()))

temp = sum(array[:K])
answer = [temp]

for i in range(N-K):
    temp = temp - array[i] + array[i+K]
    answer.append(temp)

print(max(answer))

#10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# 21


