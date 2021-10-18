def knapsackFunction(item_list, capacity):
    total_value = 0.0
    fraction = 0.0
    
    def keyFunc(item_tuple):
        return item_tuple[1] / item_tuple[0]
    
    sorted(item_list, key=keyFunc)
    
    for weight, value in item_list:
        if capacity - weight > 0:
            capacity -= weight
            total_value += value
            print(f"무게: {weight}, 가치: {value}")
        else:
            fraction = capacity / weight
            total_value += value * fraction
            print(f"무게: {weight}, 가치: {value}, 비율: {fraction}")
            break
    
    print("총 담을 수 있는 가치: ", total_value)
    
    
item_list = [(10,10), (15,12), (20,10), (25,8), (30,5)]
knapsackFunction(item_list, 30.0)