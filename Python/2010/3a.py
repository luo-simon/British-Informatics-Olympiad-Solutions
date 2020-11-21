
inp = input('> ').split(' ')

number_of_jugs = int(inp[0])
target = int(inp[1])

inp2 = input('> ').split(' ')
capacity = tuple([int(x) for x in inp2])

origin_node = (tuple([0 for _ in range(number_of_jugs)]))

def get_children(parent):
	children = []
	#Fill
	for jug in range(len(parent)):
		if parent[jug] != capacity[jug]:
			new_child = list(parent)
			new_child[jug] = capacity[jug]
			children.append(tuple(new_child))
		if parent[jug] != 0:
			new_child = list(parent)
			new_child[jug] = 0
			children.append(tuple(new_child))
			for jug_to in range(len(parent)):
				if jug != jug_to:
					new_child = list(parent)
					amount = parent[jug] + parent[jug_to]
					if amount > capacity[jug_to]:
						new_child[jug] = parent[jug] - (capacity[jug_to] - parent[jug_to])
						new_child[jug_to] = capacity[jug_to]
					else:
						new_child[jug] = 0
						new_child[jug_to] = amount
					children.append(tuple(new_child))
	return children

def bfs():
	layer = [origin_node]
	seen = set(layer)

	distance = 0

	if target in origin_node:
		return 0

	while True:
		next_layer = []
		for parent in layer:
			for child in get_children(parent):
				if child in seen:
					continue
				if target in child:
					return distance + 1

				next_layer.append(child)
				seen.add(child)
		layer = next_layer
		distance += 1

print(bfs())
