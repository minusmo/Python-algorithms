N: int = int(input())

def minimum_of_costs(n) -> int:
    minimum_costs: int = [0] * (n+1)
    used_colors: int = [-1] * (n+1)
    for i in range(1, n+1):
        costs = get_costs_of_colors()
        smaller_cost, color = get_smaller_cost_and_color(costs, used_colors[i-1])
        minimum_cost_before_a_step = minimum_costs[i-1]
        minimum_costs[i] = minimum_cost_before_a_step + smaller_cost
        used_colors[i] = color
    return minimum_costs[n]

def get_costs_of_colors() -> list:
    return [int(cost) for cost in input().split()]

def get_smaller_cost_and_color(costs, used_color) -> int:
    costs[used_color] = 1001
    smaller_cost: int = min(costs)
    smaller_color: int = costs.index(smaller_cost)
    return (smaller_cost, smaller_color)


print(minimum_of_costs(N))