import math
# 어떤 수가 입력되면 그 수가 소수인지 판단하시오
# 소수 -> Primt
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return "not prime"

    return "prime"
x = int(input())
print(is_prime_number(x))