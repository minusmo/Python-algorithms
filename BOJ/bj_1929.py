from math import sqrt
M, N = map(int, input().split())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)
        
# 소수를 골라내기 위한 방법은 다음과 같다. 이 방법을 이용해 소수를 어느 정도 골라낼 수 있다.

# 2와 5를 제외하면, 모든 소수의 일의 자리 수는 1, 3, 7, 9이다.
# 어떤 자연수 n이 소수임을 판정하기 위해선 sqrt {n} sqrt {n}까지의 수 중 
# 1을 제외하고 그 자연수의 약수가 있는지 확인하면 된다.
# 배수의 성질을 이용하면 쉽게 구할 수도 있다.

# 그 외에도 다양하고 복잡한 판정법이 존재하지만, 위의 세 가지는 당연하고 간단한 것들이다.