# Giving a graph input in form of dictionary
# where Keys are vertices and values are edges.
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

# BFS is Implemented using queue, where queue is FIF0-> First In First Out
queue = []

# Getting all the vertices from the graph
vertices = list(graph.keys())
print(vertices)

# Add an initial vertex or the vertex where you need to start from
queue.append(vertices[2])

# Mark the visited vertex
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


'''
1. Select a vertex
2. Go to all adjacent edges of the vertices.
3. Check if the vetrices is marked[Visited]
	if the vertex is not visited
		add vertex to the queue and marked list
4. Pop the first inserted element in thr queue

'''
