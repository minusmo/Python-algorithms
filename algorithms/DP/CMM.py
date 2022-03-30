import sys
'''
CMM(Chained Matrix Multiplication)은, 
연속된 행렬의 결과를 구하는 식에서,
어떤 순서로 계산을 하는 것이 가장 작은 계산량을 가지는 지,
그 때의 계산량은 얼마인지를 구하는 문제이다.

행렬의 곱의 결과는 n x m 의 행렬이 되고, 
이로 미루어 보아 행렬 곱은 두가지 변수로 대표되는, 2차원 배열에 계산 결과를 저장할 수 있음을 알 수 있다.
이 때 2차원 배열의 인덱스는, 행렬의 곱셈에서, 모든 곱셈을 마치면 중간 행렬은 사라지고,
처음 행렬의 행 x 마지막 행렬의 열의 결과로 귀결된다는 점에서 
[처음 행렬의 행][마지막 행렬의 열]
과 같이 사용할 수 있음을 알 수 있다.

임의의 개수의 행렬 곱을 계산하는 과정을 직접 손으로 해보면,
규칙을 찾을 수 있는데, 
이 때 중요한 점은 가장 쉬운(작은) 문제를 푸는 것 부터 시작해야 한다는 것이다.
그래야 DP의 과정을 경험적으로 이해하기 쉽고,
이를 linear recurrence equation으로 표현하기 쉬워진다. 

경험적으로 찾은 CMM의 recurrence equation은 다음과 같다.
M[i,j] = min(M[i,k] + M[k+1, j] + C(i-1)*C(k)*C(j) for i <= k <= j-1)
M[i,i] = 0

이러한 과정은 DP의 solution steps
0. check examples(guessing)
1. find recursive property => recurrence in mathmatical expression
2. save and reuse
중 

0, 1 번째 스텝에 해당한다.

save and reuse 기법을 사용하지만, 연산량이 많은 경우에는,
running time에서의 시간 최적화를 위해 code optimization이 필요하다.
'''

class DP_CMM:
    def __init__(self, matricies_sequence, dimension_row_col):
        self.lookup_table = [[0 for _ in range(len(matricies_sequence))] for _ in range(len(matricies_sequence))]
        self.calculate_min_cmm(matricies_sequence, dimension_row_col)
    
    def calculate_min_cmm(self, matricies_sequence, dimension_row_col):
        for i in range(len(matricies_sequence)):
            for j in range(len(matricies_sequence)):
                if i == j:
                    self.lookup_table[i][j] = 0
                else:
                    minimum_calculation = sys.maxsize
                    for k in range(i, j-1):
                        calculation = self.lookup_table[i,k] + self.lookup_table[k+1,j] + dimension_row_col[i-1].col * dimension_row_col[k].col * dimension_row_col[j].col
                        if calculation < minimum_calculation:
                            minimum_calculation = calculation
                    self.lookup_table[i][j] = minimum_calculation
        return self.lookup_table[0][len(matricies_sequence)]