N = int(input())

def number_of_binary_series_with_00and1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        number_of_binary_series = [0]*(n+1)
        number_of_binary_series[1] = 1
        number_of_binary_series[2] = 2
        for i in range(3,n+1):
            number_of_binary_series[i] = ((2 * number_of_binary_series[i-1] + 2 * number_of_binary_series[i-2]) // 2)%15746
        return number_of_binary_series[n]

print(number_of_binary_series_with_00and1(N))

"""
111

100
001

00
11

n 번째:

( n-1 + 1 : 오른쪽에 1
1 + n-1: 왼쪽에 1
n-2 + 00 : 오른쪽에 00
00 + n-2 : 왼족에 00 ) / 2

점화식을 그림으로 생각하자!!
마지막에 어떤것을 더해서 달라졌는가?
메모된 어떤값에 어떻게 더해서 n번째 값을 구할 수 있는가?
"""