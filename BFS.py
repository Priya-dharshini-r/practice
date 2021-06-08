graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

queue = []
vertices = list(graph.keys())
print(vertices)
queue.append(vertices[2])
marked = [queue[0]]

while len(queue)>0:
	initial_vertex = queue[0]
	edges = graph[initial_vertex]
	for vertex in edges:
		if vertex not in marked:
			queue.append(vertex)
			marked.append(vertex)
	result = queue.pop(0)
	print(result)
