graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

stack = []
vertices = list(graph.keys())
stack.append(vertices[0])
# print(stack)
marked = [stack[-1]]
while len(stack)>0:
	top_vertex = stack[-1]
	edges = graph[top_vertex]
	for vertex in edges:
		if vertex not in marked:
			stack.append(vertex)
			marked.append(vertex)
			break
	else:
		result = stack.pop()
		print(result)
'''
