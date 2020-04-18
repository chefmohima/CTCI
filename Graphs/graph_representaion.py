class Node:
    # node of a graph has info of
    # data and its connected nodes/neighbors
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        
    def add_neighbor(self, node):
        self.neighbors.append(node)
        
class Graph:
    # has collection of all nodes
    # connection info maintained by each node
    def __init__(self):
        self.node_list = []
    
    def add_node(self, node):
        self.node_list.append(node)
        
    def add_edge(self, source_node, dest_node):
        if source_node not in self.node_list or \
           dest_node not in self.node_list:
               return
        source_node.add_neighbor(dest_node)
        
    def construct_adjacency_list(self):
        al = {}
        for node in self.node_list:
            al[node] = node.neighbors
        return al
        
# create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# initialize graph
g = Graph()
g.node_list.append(node1)
g.node_list.append(node2)
g.node_list.append(node3)
g.node_list.append(node4)

g.add_edge(node1, node2)
g.add_edge(node1, node3)
g.add_edge(node2, node3)

l = g.construct_adjacency_list()
print("Adjacency List")
for k in l:
    print(k.data, ":", end="")
    for v in l[k]:
        print(v.data, ", ",end="")
    print("\n")    
    
