#큰 수의 법칙
# •첫째줄에N M K 의자연수가주어 지며, 각자연수는공백으로구분한다.
# •둘째줄에N개의자연수가주어진다. 각자연수는공백으로 구분한다.
#  단, 각각의 자연수는 1 이상
# 10,000이하의수로주어진다.
# 입력으로주어지는K는항상M보다작거나같다.

# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())
#N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() #입력 받은 수 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] # 두번째로 큰수

result = 0

while True:
    for i in range(k): # 3번까지 반복 가능
        if m==0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 입력 예시
# 5 8 3
# 2 4 5 4 6
# 출력 -> 46