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
            if i%2 == 0:
                pass
            else:
                number_of_binary_series[i] = (number_of_binary_series[i-1])*2 - 1
                
                
                
"""
111

100
001

00
11

"""