# 피보나치 5
N = int(input())

def fibo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(N))