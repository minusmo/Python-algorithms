'''
Binomial Coefficient
이항계수는 다음과 같은 linear equation으로 표현될 수 있다.
n개 중에서 k개를 고르는, nCk의 조합 형태를 띄므로,
nCk = (n,k)라 한다면, (n,k) = (n-1, k) + (n-1, k-1) when 0 < k < n
이 된다. 조합의 특성상, n == k, k ==0 인 경우에는 (n,k) == 1 이 된다.

이를 다음과 같은 linear recurrence equation으로 표현할 수 있다.
B[n,k] = B[n-1,k] + B[n-1, k-1] if 0 < k < n
B[n,k] = 1 if k == n, n == 0

이러한 표현의 형태는, 처음에 naive하게 접근하면 linear recurrence가 아닌
divide and conquer recurrence의 형태로 풀 수 있으나, 
잘 보면, linear recurrence의 형태를 가지고 있고, subproblem overlapping이 
심각하게 발생하므로 다른 접근 방법을 취할 필요가 있다는 것을 알 수 있다. 

바론 Dynamic Programming approach 이다. 

Dynamic programming이라고 하더라도 계산량이 많으면 
full-exhaustive enumeration(brute force)와 같은 형태가 될 수 있으나,
중복 없이 필요한 연산만을 취한다는 부분에서 큰 차이가 있다. 

DP는 필요한 subproblem의 계산 결과를 저장하고, bigger problem의 
계산에 활용하다는 점에서 Save and Reuse strategy라고도 불린다.
'''

class BinomialCoefficient:
    def __init__(self, n, k):
        self.look_up_table = [[0 for _ in range(k)] for _ in range(n)]
        self.calculate_Bnk(n, k)
    
    def calculate_Bnk(self, n, k):
        for i in range(n): # step 2
            for j in range(min(i, k)): # 전체를 반복하지 않는 것이 중요!!! 아예 계산 불가능한 부분도 있고, 계산이 불필요한 부분도 있다!!! 최적화에 있어 중요한 부분.
                if j == 0 or j == i:
                    self.look_up_table[i][j] = 1
                else:
                    self.look_up_table[i][j] = self.look_up_table[i-1][j-1] + self.look_up_table[i-1][j] # step 1
        return self.look_up_table[n][k]