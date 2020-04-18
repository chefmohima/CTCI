from collections import defaultdict
d = defaultdict(list)

d = {'A': ['B', 'C', 'D'],'B': ['A', 'D'],'C': ['A', 'E'],'D': ['B', 'A', 'E'], 'E': ['D', 'C']}
            

def dfs_recur(adj_list, node, visited):
    print(node)
    for n in adj_list[node]:
      if n not in visited:
          visited.add(n)
          dfs_recur(adj_list, n, visited)

def dfs_helper(adj_list, start_node):
  # for every node EXCEPT the first, node is added to visited list when exploring neighbors. However first node needs to be added before this
  visited = set()
  visited.add(start_node)
  dfs_recur(adj_list, start_node, visited)
    
          
    

dfs_helper(d, 'A')



    
        
            
