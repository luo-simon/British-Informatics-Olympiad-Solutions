num_digits = int(input('> '))
origin_node = input('> ')


def get_children(parent):
    children = []
    for i in range(1, num_digits-2):
        maxi = max(int(parent[i]), int(parent[i+1]))
        mini = min(int(parent[i]), int(parent[i+1]))
        if (maxi > (int(parent[i-1])) > mini) or (maxi > (int(parent[i+2])) > mini):
            child = parent[:i] + parent[i+1] + parent[i] + parent[i+2:]
            children.append(child)
    # Start and end check
    maxi = max(int(parent[0]), int(parent[1]))
    mini = min(int(parent[0]), int(parent[1]))
    if maxi > int(parent[2]) > mini:
            child = parent[1] + parent[0] + parent[2:]
            children.append(child)
    maxi = max(int(parent[num_digits-1]), int(parent[num_digits-2]))
    mini = min(int(parent[num_digits-2]), int(parent[num_digits-2]))
    if maxi > int(parent[num_digits-3]) > mini:
            child = parent[:num_digits-2] + parent[num_digits-1] + parent[num_digits-2]
            children.append(child)

    return children


def bfs():
    layer = [origin_node]
    seen = set(layer)
    
    distance = 0

    while True:
        next_layer = []
        for parent in layer:
            for child in get_children(parent):
                if child not in seen:
                    seen.add(child)
                    next_layer.append(child)
        if len(next_layer) == 0:
            return distance
        layer = next_layer
        distance += 1

print(bfs())
