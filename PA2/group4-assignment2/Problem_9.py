#
#	Programming Assignment 2
#
#	Problem 9  (10 Points)
#
#	Depth-first search algorithm (6.5) together with depth-first numbering of nodes.
#	Test your algorithm on the graph of fig. 6.38, page 226.
#

def dfs(graph):
	'Depth first search of a directed graph'
	def dfsGo(graph, node, visited):
		if node not in visited:
			visited.append(node)
			print 'Visited node:  %s (%s)' % (node, len(visited))
		for path in graph[node]:
			if path not in visited:
				dfsGo(graph, path, visited)
	visited = []
	while len(visited) < len(graph):  # Try all nodes that were missed
		for node in graph:
			if node not in visited:
				dfsGo(graph, node, visited)

graph = {
	'a' : ['b', 'd', 'f'],
	'b' : ['c', 'f'],
	'c' : ['d'],
	'd' : ['b'],
	'e' : ['d', 'f'],
	'f' : ['d']
}

dfs(graph)
