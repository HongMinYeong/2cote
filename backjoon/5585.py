#거스름돈
#1000엔 지폐 한장 냈을 떄 거스름돈 구하기
money = int(input())
change = [500,100,50,10,5,1]
coin = 1000-money
result = 0
for i in range(6):
    count = 0
    count=coin//change[i]
    coin -= count * change[i] # 남은 돈
    result += count
print(result)
