# graph = { "a" : ["b","c"],
#          "b" : ["a", "d"],
#         "c" : ["a", "d"],
#          "d" : ["e"],
#         "e" : ["d"]
#          }

graph = {1: [2, 3],
         2: [4, 5],
         3: [6],
         4: [2],
         5: [2],
         6: [3]}

vertices = list(graph.keys())
queue = []
queue.append(vertices[0])
marked = [queue[0]]*len(graph)

while len(queue)>0:
	initial_vertex = queue[0]
	edges = graph[initial_vertex]
	for vertex in edges:
		if vertex not in marked:
			queue.append(vertex)
			marked.append(vertex)
			break
	else:
		result = queue.pop(0)
		print(result)
