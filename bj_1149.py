N: int = int(input())

def minimum_of_costs(n) -> int:
    minimum_costs_r: int = [0] * (n+1)
    minimum_costs_g: int = [0] * (n+1)
    minimum_costs_b: int = [0] * (n+1)
    
    for i in range(1, n+1):
        costs = get_costs_of_colors()
        
        minimum_costs_r[i] = min(minimum_costs_g[i-1], minimum_costs_b[i-1]) + costs[0]
        minimum_costs_g[i] = min(minimum_costs_r[i-1], minimum_costs_b[i-1]) + costs[1]
        minimum_costs_b[i] = min(minimum_costs_r[i-1], minimum_costs_g[i-1]) + costs[2]
        
    return min(minimum_costs_r[n], minimum_costs_g[n], minimum_costs_b[n])

def get_costs_of_colors() -> list:
    return [int(cost) for cost in input().split()]

print(minimum_of_costs(N))