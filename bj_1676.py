from math import factorial
N = int(input())
fact = factorial(N)
for i in range(1,len(str(fact))+1):
    if fact%pow(10,i) != 0:
        print(i-1)
        break