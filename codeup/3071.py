import math
# 시작값과 마지막값이 입력되면 그 두 수 사이의 소수를 모두 출력
# 시작값과 마지막값이 공백으로 구분되어 입력
x,y = list(map(int,input().split()))
array = [True for i in range(y+1)]
for i in range(2,int(math.sqrt(y)+1)):
    if array[i] % i == True:
        j=2
        while i*j <= y:
            array[i*j] = False
            j+=1


for i in range(x,y+1):
    if array[i]:
        print(i,end=' ')