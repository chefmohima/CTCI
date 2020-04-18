from collections import defaultdict
d = defaultdict(list)

d = {'A': ['B', 'C', 'D'],'B': ['A', 'D'],'C': ['A', 'E'],'D': ['B', 'A', 'E'], 'E': ['D', 'C']}
            

def dfs(adj_list, start_node):
  # initialize Stack
  s = []
  # set to track visited nodes
  visited = set()
  s.append(start_node)
  visited.add(start_node)
  while s:
    # pop element-> process->explore neighbors->push if not visited-> mark as visited
    # pop and process
    node = s.pop()
    print(node)
    for n in adj_list[node]:
      if n not in visited:
        s.append(n)
        visited.add(n)
  return
    

dfs(d, 'A')



    
        
            
