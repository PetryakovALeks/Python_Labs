with open('27-123b.txt', 'r') as file_b:
    
    N_b, K_b, V_b = map(int, file_b.readline().split())
    
    
    stations_b = []
    for _ in range(N_b):
        km, fuel = map(int, file_b.readline().split())
        stations_b.append((km, fuel))


def distance(a, b, K):
    return min(abs(a - b), K - abs(a - b))


min_cost_b = float('inf')


for i in range(N_b):
    total_cost = 0
    
    storage_km = stations_b[i][0]
    
    
    for j in range(N_b):
        km, fuel = stations_b[j]
        
        trips = (fuel + V_b - 1) // V_b
        
        dist = distance(storage_km, km, K_b)
    
        total_cost += trips * dist
    
    
    if total_cost < min_cost_b:
        min_cost_b = total_cost


print("Минимальные затраты для файла B:", min_cost_b)