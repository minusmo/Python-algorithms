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
            number_of_binary_series[i] = (2 * number_of_binary_series[i-1] + 2 * number_of_binary_series[i-2]) // 2
        return number_of_binary_series[n]

print(number_of_binary_series_with_00and1(N))

"""
111

100
001

00
11

n 번째:

n-1 + 1 : 오른쪽에 1
1 + n-1: 왼쪽에 1
n-2 + 00 : 오른쪽에 00
00 + n-2 : 왼족에 00 
"""