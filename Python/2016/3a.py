highest, p, q = (int(x) for x in input().split()) 

origin_node = p
target_node = q

def primes_up_to(num):
    primes = [True for i in range(num+1)]
    primes[0] = primes[1] = False
    for i, is_prime in enumerate(primes):
        if is_prime:
            for x in range(i*i, num+1, i):
                primes[x] = False
    return primes

def get_children(parent):
    global primes
    children = []
    power_of_two_index = 0
    while powers_of_two[power_of_two_index] <= max((highest - parent), (parent)):
        if parent + powers_of_two[power_of_two_index] <= highest:
            if primes[parent + powers_of_two[power_of_two_index]]:
                children.append(parent+powers_of_two[power_of_two_index])
        if highest >= parent - powers_of_two[power_of_two_index] > 0:
             if primes[parent - powers_of_two[power_of_two_index]]:
                children.append(parent-powers_of_two[power_of_two_index])
        power_of_two_index += 1
    return children
    
primes = primes_up_to(highest)
powers_of_two = [2**x for x in range(0, 25)]

def bfs():
    layer = [origin_node]
    seen = set(layer)
    distance = 1
    while True:
        next_layer = []
        for parent in layer:
            for child in get_children(parent):
                if child not in seen:
                    seen.add(child)
                    next_layer.append(child)
        if target_node in next_layer:
            return distance + 1
        layer = next_layer
        distance += 1

print(bfs())
