from math import sqrt
n = int(input())

def find_sqrts(n, sols):
    sol = []
    for i in range(int(sqrt(n)),0,-1):
        if n-i**2>0:
            if sols < 4:
                sol.append(i)
                sols -= 1
                sol.extend(find_sqrts(n-i**2, sols))
            else:
                sol.extend(find_sqrts())
        else:
            sol.append(i)
            return sol
    return sol

print(len(find_sqrts(n)))