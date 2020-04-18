from collections import defaultdict
d = defaultdict(list)

d = {'A': ['B', 'C', 'D'],'B': ['A', 'D'],'C': ['A', 'E'],'D': ['B', 'A', 'E'], 'E': ['D', 'C']}
            

def bfs(adj_list, start_node):
    # initialise queue
    q = []
    # set for tracking visited nodes
    visited = set()
    q.append(start_node)
    visited.add(start_node)
    # dequeue->process->enqueue unvisited neighbors ->mark visited
    while q:
        # dequeue
        node = q.pop(0)
        # process
        print(node)
        for n in adj_list[node]:
            if n not in visited:
                # enqueue unvisited neighbors
                q.append(n)
                # mark as visited
                visited.add(n)
    return

bfs(d, 'A')
