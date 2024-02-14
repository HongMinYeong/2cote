# 시각
# 00시 00분 00초 ~ N시 59분 59초
# 3 이 하나라도 포함되는 모든 경우의 수
N = int(input())
count = 0
# 데이터 갯수가 100 만개 이하일때 완전탐색
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)
