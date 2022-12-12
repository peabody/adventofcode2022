from collections import defaultdict
import heapq as heap
import sys
import pprint

def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		# go greedily by always extending the shorter cost nodes first
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts


def ce(e):
    """Convert elevation"""
    if e == 'S':
        return 'a'
    elif e == 'E':
        return 'z'
    else:
        return e


def can_reach(coor, e):
    try:
        # bounds check
        if coor[0] < 0 or coor[1] < 0:
            return False
        de = ord(ce(grid[coor[0]][coor[1]]))
        e = ord(e)
        if de > e and (de - e) > 1:
            return False
        else:
            return True
    except IndexError:
        return False


fn = "p12.txt" if len(sys.argv) < 2 else sys.argv[1]

grid = []

with open(fn) as data:
    for line in data:
        line = line.strip()
        grid.append(list(line))

# create all tuples pointing to empty dictionaries
nodes = {}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        nodes[(i,j)] = {}


# now traverse the grid again,
# only this time, add references to reachable nodes
# I think I could have done this in the first loop?
for i in range(len(grid)):
    for j in range(len(grid[0])):
        right = (i, j + 1)
        down = (i + 1, j)
        left = (i, j - 1)
        up = (i - 1, j)

        e = ce(grid[i][j])
        if can_reach(right, e):
            nodes[(i,j)][right] = 1
        if can_reach(down, e):
            nodes[(i,j)][down] = 1
        if can_reach(left, e):
            nodes[(i,j)][left] = 1
        if can_reach(up, e):
            nodes[(i,j)][up] = 1

# find starting range and ending nodes
S = []
E = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S' or grid[i][j] == 'a':
            S.append((i,j))
        elif grid[i][j] == 'E':
            E = (i,j)

path_totals = []

for each_start in S:
    parentsMap, nodeCosts = dijkstra(nodes, each_start)
    path = []
    try:
        backtrack = parentsMap[E]
    except KeyError:
        print("%s %s cannot reach E" % (grid[each_start[0]][each_start[1]], str(each_start)))
        continue
    path.insert(0, backtrack)
    while backtrack != each_start:
        backtrack = parentsMap[backtrack]
        path.insert(0, backtrack)
    path_totals.append(len(path))

path_totals.sort()
print(path_totals[0])

