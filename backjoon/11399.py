N = int(input())
P = list(map(int,input().split()))

P.sort() #작은수부터 정렬 , 대기시간 줄이려고
time = 0
for i in range(1,N+1): #1부터 N까지
    time += sum(P[0:i]) #기다린 시간까지 계속 더하기

print(time)
