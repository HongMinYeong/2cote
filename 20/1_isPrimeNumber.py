#소수 판별하기 -> 제곱근까지만 확인
import math
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2,int(math.sqrt(x)) + 1):
        if x%i == 0:
            return False
    return True


print(is_prime_number(3))
print(is_prime_number(6))
