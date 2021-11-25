from math import sqrt
n = int(input())

def find_sqrts(n):
    sol = []
    for i in range(int(sqrt(n)),0,-1):
        if n-i**2>0:
            if len(sol) < 4:
                sol.append(i)
                sol.extend(find_sqrts(n-i))
            else:
                
        elif n-i**2==0:
            sol.append(i)
            return sol
    return sol

print(len(find_sqrts(n)))