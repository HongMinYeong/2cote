# 큰수의 법칙 2
n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second=data[n-2]

count = int(m/(k+1)*k) #큰수가 더해지는 횟수
count += m%(k+1) #정확이 떨어지지 않을 때

result = 0
result += count * first
result += (m-count)*second

print(result)