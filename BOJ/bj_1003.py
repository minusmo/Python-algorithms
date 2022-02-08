N = int(input())

def get_zeros_and_ones_fibonacci(n):
    if n == 0:
        return (1,0)
    elif n == 1:
        return (0,1)
    else:
        series = [-1] * (n+1)
        series[0] = (1,0)
        series[1] = (0,1)
        for i in range(2,n+1):
            series[i] = (series[i-1][0]+series[i-2][0], series[i-1][1]+series[i-2][1])
        return series[n]
    
order_of_terms = []
for _ in range(N):
    n = int(input())
    order_of_terms.append(n)

zeros_and_ones_of_terms = [get_zeros_and_ones_fibonacci(n) for n in order_of_terms]

for zeros, ones in zeros_and_ones_of_terms:
    print(f"{zeros} {ones}")